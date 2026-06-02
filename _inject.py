import re, json

# Preberi migrirane podatke
with open('_courses_migrated.json', 'r', encoding='utf-8') as f:
    courses_json = f.read()

# Preveri JSON veljavnost
courses = json.loads(courses_json)

# Preveri ID unikatnost
course = courses[0]
all_sec   = [s['id'] for ch in course['chapters'] for s in ch['sections']]
all_feat  = [f['id'] for ch in course['chapters'] for s in ch['sections'] for f in s['features']]
all_notes = [n['id'] for ch in course['chapters'] for s in ch['sections'] for n in s['notes']]
all_q     = [q['id'] for ch in course['chapters'] for s in ch['sections'] for q in s.get('questions', [])]

assert len(all_sec)   == len(set(all_sec)),   'DUPLICATE section IDs!'
assert len(all_feat)  == len(set(all_feat)),  'DUPLICATE feature IDs!'
assert len(all_notes) == len(set(all_notes)), 'DUPLICATE note IDs!'
assert len(all_q)     == len(set(all_q)),     'DUPLICATE question IDs!'

print('Verifikacija OK:')
print('  Poglavja:   ' + str(len(course['chapters'])))
print('  Lekcije:    ' + str(len(all_sec)))
print('  Feature:    ' + str(len(all_feat)))
print('  Notes:      ' + str(len(all_notes)))
print('  Vprasanja:  ' + str(len(all_q)))

# Vstavi v index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

compact = json.dumps(courses, ensure_ascii=False, separators=(',', ':'))

if '__COURSES_PLACEHOLDER__' not in html:
    print('ERROR: placeholder not found in index.html')
    exit(1)

html = html.replace('__COURSES_PLACEHOLDER__', compact)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html posodobljen (' + str(len(html)) + ' znakov)')
print('DONE.')
