import re, json

with open('_source_cc101.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const DATA = (\[.+?\]);', html, re.DOTALL)
if not m:
    print('ERROR: DATA not found')
    exit(1)

chapters = json.loads(m.group(1))

COURSES = [{
    'id': 1,
    'slug': 'cc101',
    'title': 'Claude Code 101',
    'subtitle': 'Interaktivni ucni vodic',
    'chapters': chapters
}]

course = COURSES[0]
all_sec   = [s for ch in course['chapters'] for s in ch['sections']]
all_feat  = [f for s in all_sec for f in s['features']]
all_notes = [n for s in all_sec for n in s['notes']]
all_q     = [q for s in all_sec for q in s.get('questions', [])]

print('Poglavja: ' + str(len(course['chapters'])))
for ch in course['chapters']:
    print('  Ch ' + str(ch['id']) + ': ' + ch['title'] + ' (' + str(len(ch['sections'])) + ' lekcij)')
print('Skupaj lekcij: ' + str(len(all_sec)))
print('Skupaj featur: ' + str(len(all_feat)))
print('Skupaj notes:  ' + str(len(all_notes)))
print('Skupaj vprasanj: ' + str(len(all_q)))

courses_json = json.dumps(COURSES, ensure_ascii=False, separators=(',', ':'))
print('JSON velikost: ' + str(len(courses_json)) + ' znakov')

with open('_courses_migrated.json', 'w', encoding='utf-8') as f:
    json.dump(COURSES, f, ensure_ascii=False, separators=(',', ':'))
print('Shranjeno v _courses_migrated.json')
