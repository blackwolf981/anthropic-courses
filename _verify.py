import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Velikost: ' + str(round(len(html)/1024)) + ' KB')
print('Placeholder ostaja: ' + str('__COURSES_PLACEHOLDER__' in html))
print('COURSES const: ' + str('const COURSES =' in html))
print('bottom-nav class: ' + str('class="bottom-nav"' in html))
print('render() fn: ' + str('function render()' in html))
print('quizEngineHTML fn: ' + str('function quizEngineHTML()' in html))
print('goToLesson fn: ' + str('function goToLesson' in html))

m = re.search(r'const COURSES = (\[.+?\]);', html, re.DOTALL)
if m:
    try:
        courses = json.loads(m.group(1))
        course = courses[0]
        all_sec  = [s['id'] for ch in course['chapters'] for s in ch['sections']]
        all_feat = [f['id'] for ch in course['chapters'] for s in ch['sections'] for f in s['features']]
        all_q    = [q['id'] for ch in course['chapters'] for s in ch['sections'] for q in s.get('questions', [])]
        print('JSON OK: ' + str(len(courses)) + ' kurz, ' + str(len(course['chapters'])) + ' poglavij, ' + str(len(all_sec)) + ' lekcij, ' + str(len(all_feat)) + ' featur, ' + str(len(all_q)) + ' vprasanj')
        print('Duplikati sec: ' + str(len(all_sec) != len(set(all_sec))))
        print('Duplikati feat: ' + str(len(all_feat) != len(set(all_feat))))
        print('Duplikati q: ' + str(len(all_q) != len(set(all_q))))
    except Exception as e:
        print('JSON FAIL: ' + str(e))
else:
    print('COURSES regex: ni najdeno')
