# -*- coding: utf-8 -*-
import re, json

with open('_courses_migrated.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const COURSES\s*=\s*', html)
if not m:
    print('ERROR: const COURSES not found in index.html')
    exit(1)

arr_start = m.end()
if html[arr_start] != '[':
    print('ERROR: expected [ after const COURSES =, got:', repr(html[arr_start]))
    exit(1)

# Walk the string to find the matching closing bracket
depth = 0
in_string = False
escape_next = False
for i, ch in enumerate(html[arr_start:]):
    if escape_next:
        escape_next = False
        continue
    if ch == '\\' and in_string:
        escape_next = True
        continue
    if ch == '"' and not escape_next:
        in_string = not in_string
        continue
    if in_string:
        continue
    if ch == '[' or ch == '{':
        depth += 1
    elif ch == ']' or ch == '}':
        depth -= 1
        if depth == 0:
            arr_end = arr_start + i + 1
            break

old_json = html[arr_start:arr_end]
new_json = json.dumps(courses, ensure_ascii=False, separators=(',', ':'))

html = html[:arr_start] + new_json + html[arr_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('OK: index.html posodobljen (' + str(len(html)) + ' znakov)')
print('Stari JSON: ' + str(len(old_json)) + ' znakov')
print('Novi JSON:  ' + str(len(new_json)) + ' znakov')
print('DONE.')
