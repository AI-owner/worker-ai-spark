#!/usr/bin/env python3
"""Validate bilingual documentation coverage, navigation, links and source hashes.

Run from any directory. Use --update-manifest only after reviewing both languages.
No network requests or third-party packages are used.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/translations.json'
FROZEN = 'benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md'
SPECIAL = {'LICENSE-CODE': 'LICENSE-CODE.en', 'LICENSE-CONTENT': 'LICENSE-CONTENT.en', 'CITATION.cff': 'CITATION.en.cff'}
LINK = re.compile(r'\[([^\]\n]*)\]\(([^\s)]+)(?:\s+"[^"]*")?\)')


def repository_files():
    result = subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT, check=True, stdout=subprocess.PIPE)
    return sorted({name for name in result.stdout.decode('utf-8').split('\0') if name and (ROOT / name).is_file()})


def pairs():
    found = {}
    for name in repository_files():
        if name.endswith('.md') and not name.endswith('.en.md') and Path(name).name != 'AGENTS.md':
            found[name] = name[:-9] + '.en.md' if name.endswith('.zh-CN.md') else name[:-3] + '.en.md'
        elif name in SPECIAL:
            found[name] = SPECIAL[name]
        elif name.startswith('.github/ISSUE_TEMPLATE/') and name.endswith('.yml') and not name.endswith('.en.yml') and Path(name).name != 'config.yml':
            found[name] = name[:-4] + '.en.yml'
    return found


def prose(text):
    return re.sub(r'^(`{3,}|~{3,}).*?^\1\s*$', '', text, flags=re.M | re.S)


def heading_slugs(text):
    result = []
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(text), flags=re.M):
        heading = LINK.sub(lambda m: m[1], heading)
        heading = re.sub(r'<[^>]*>', '', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.append(slug if n == 0 else f'{slug}-{n}')
    return result


def local_links(name):
    body = prose((ROOT / name).read_text(encoding='utf-8-sig'))
    for match in LINK.finditer(body):
        label, target = match.groups()
        parts = urlsplit(target.strip('<>'))
        if parts.scheme or parts.netloc:
            continue
        path = ((ROOT / name).parent / unquote(parts.path)).resolve() if parts.path else (ROOT / name).resolve()
        yield label, target, path, unquote(parts.fragment)


def digest(name):
    # Normalize line endings so Windows checkouts and CI share the same digest.
    return hashlib.sha256((ROOT / name).read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def update_manifest(mapping):
    records = [{'source': source, 'english': english, 'source_sha256': digest(source), 'english_sha256': digest(english)} for source, english in mapping.items()]
    MANIFEST.write_text(json.dumps({'schema_version': 1, 'hash_normalization': 'UTF-8 bytes with CRLF normalized to LF', 'pairs': records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def validate(mapping, check_manifest=True):
    errors = []
    checked_links = 0
    for source, english in mapping.items():
        if not (ROOT / english).is_file():
            errors.append(f'{source}: missing {english}')
            continue
        if source.endswith('.md') or source in ('LICENSE-CODE', 'LICENSE-CONTENT'):
            for name, counterpart in ((source, english), (english, source)):
                links = list(local_links(name))
                checked_links += len(links)
                if name != FROZEN and not any(path == (ROOT / counterpart).resolve() for _, _, path, _ in links):
                    errors.append(f'{name}: missing language link to {counterpart}')
                for label, target, path, fragment in links:
                    if not path.exists():
                        if check_manifest or path != MANIFEST.resolve():
                            errors.append(f'{name}: broken link {target}')
                    elif fragment and path.suffix == '.md' and not re.fullmatch(r'L\d+(?:-L\d+)?', fragment):
                        body = path.read_text(encoding='utf-8-sig')
                        anchors = set(heading_slugs(body)) | set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', body))
                        if fragment not in anchors:
                            errors.append(f'{name}: missing anchor {target}')
                    intentional_chinese = re.search(r'Chinese|中文', re.sub(r'\((?:currently )?in Chinese\)', '', label), re.I)
                    if name == english and not intentional_chinese:
                        try:
                            linked_source = path.relative_to(ROOT).as_posix()
                        except ValueError:
                            linked_source = ''
                        if linked_source in mapping:
                            errors.append(f'{name}: English navigation still points to Chinese: {target}')
        elif source.endswith('.yml'):
            a = (ROOT / source).read_text(encoding='utf-8')
            b = (ROOT / english).read_text(encoding='utf-8')
            for pattern, field in ((r'^\s+id:\s*(.+)$', 'form IDs'), (r'^\s+required:\s*(.+)$', 'required flags')):
                if re.findall(pattern, a, re.M) != re.findall(pattern, b, re.M):
                    errors.append(f'{english}: changed {field}')
            if Path(english).name not in a or Path(source).name not in b:
                errors.append(f'{source}: missing template language references')

    if (ROOT / FROZEN).is_file():
        package = json.loads((ROOT / FROZEN).with_name('package-manifest.json').read_text(encoding='utf-8'))
        expected = package['summary']['report']['sha256']
        actual = hashlib.sha256((ROOT / FROZEN).read_bytes()).hexdigest()
        if actual != expected:
            # Git may check out CRLF even though the frozen artifact used LF.
            if digest(FROZEN) != expected:
                errors.append('Frozen pilot report no longer matches the recorded package hash')
        directory = str(Path(FROZEN).parent).replace('\\', '/')
        for readme in (directory + '/README.md', directory + '/README.en.md'):
            paths = {path for _, _, path, _ in local_links(readme)}
            if not {(ROOT / FROZEN).resolve(), (ROOT / mapping[FROZEN]).resolve()} <= paths:
                errors.append(f'{readme}: must link both frozen report languages')

    if check_manifest:
        if not MANIFEST.exists():
            errors.append('Missing docs/translations.json')
        else:
            recorded = {row['source']: row for row in json.loads(MANIFEST.read_text(encoding='utf-8'))['pairs']}
            if set(recorded) != set(mapping):
                errors.append('Translation manifest file inventory is out of date')
            for source, english in mapping.items():
                row = recorded.get(source)
                if row and (ROOT / english).exists() and (row['english'] != english or row['source_sha256'] != digest(source) or row['english_sha256'] != digest(english)):
                    errors.append(f'{source}: review both languages, then update the translation manifest')
    return errors, checked_links


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--update-manifest', action='store_true')
    args = parser.parse_args()
    mapping = pairs()
    errors, links = validate(mapping, check_manifest=not args.update_manifest)
    if not errors and args.update_manifest:
        update_manifest(mapping)
    for error in errors:
        print('ERROR:', error)
    print(f'{len(mapping)} document/template pairs; {links} local links; {len(errors)} errors.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
