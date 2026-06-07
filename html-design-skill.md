---
name: html-design-skill
description: Skill za ustvarjanje in posodabljanje interaktivne, mobile-first HTML učne platforme za projekt anthropic-courses (Anthropic Academy kurzi). Uporabi kadar (1) dodajaš ali urejaš vsebino kurza (DATA/COURSES konstanta v index.html), (2) gradiš kartice, kvize, opombe, slike ali podsekcije, (3) delaš na mobile-first layoutu, bottom navigaciji ali multi-kurs preklopu. Vedno uporabi ta skill preden začneš kodirati ali urejati HTML.
---

# anthropic-courses — Mobile-First HTML Design Skill

Interaktivna učna platforma za Anthropic Academy kurze. **En sam HTML file** (`index.html`), brez build koraka, brez serverja. Vsebina živi v JS konstanti, render engine jo bere in gradi DOM.

> **Mobile-first je zakon.** Base CSS = mobilni telefon (~380 px). Desktop je `@media (min-width: …)` razširitev mobilnega — nikoli obratno. Vsaka nova komponenta se najprej nariše za mobilni, šele nato za širši zaslon.

---

## Projektna struktura

```
C:\Users\andre\OneDrive\Documents\GitHub\anthropic-courses\   ← edina mapa (GitHub = delovna)
├── index.html              ← master dokument
├── assets/
│   └── courses/
│       ├── cc101/          ← slike za Claude Code 101
│       └── cowork/         ← slike za Claude Cowork
├── CLAUDE.md
├── html-design-skill.md
└── README.md
```

Delovni tok v tem okolju (Claude.ai):
```
/mnt/project/index.html        ← read-only vir
/home/claude/index.html        ← delovna kopija (tu urejamo)
/mnt/user-data/outputs/index.html  ← output za uporabnika
```

---

## Design sistem — Dark mode

Font: `system-ui, -apple-system, sans-serif` (brez Google Fonts). Ikone: Tabler Icons webfont CDN. Naslovi lahko uporabljajo Georgia serif za "akademski" pridih.

### CSS spremenljivke

```css
:root {
  --bg:        #111111;   /* glavno ozadje */
  --surface:   #1c1c1c;   /* kartice, paneli, bottom nav */
  --border:    rgba(255,255,255,0.07);
  --border-md: rgba(255,255,255,0.13);
  --text:      #F0F0F0;
  --text-sec:  #A0A0A0;
  --text-ter:  #606060;
  --accent:    #FFD166;   /* zlata — akcent, aktivni elementi */
  --accent-bg: #2b2200;
  --radius:    10px;
  --radius-lg: 14px;

  /* Mobile-first dimenzije */
  --header-h:    52px;   /* sticky top header */
  --bottomnav-h: 60px;   /* bottom navigation bar */
  --content-max: 720px;  /* max širina vsebine na desktopu */
}
```

### Badge tipi

| badge_type | Barva ozadja | Barva teksta | Pomen |
|------------|-------------|-------------|-------|
| `when`     | `rgba(134,239,172,0.12)` | `#86EFAC` | Priporočeno/pogosto |
| `caution`  | `rgba(251,146,60,0.12)`  | `#FB923C` | Pazi/zavedaj se |
| `rare`     | `rgba(255,255,255,0.07)` | `#A0A0A0` | Redko |

---

## Mobile-first layout

```
┌─────────────────────────────┐
│  HEADER (sticky top, 52px)  │  ← naslov lekcije/poglavja + progress bar
├─────────────────────────────┤
│                             │
│  CONTENT (full width)       │  ← scrollable; ena lekcija = en zaslon
│  max-width 720px na desktop │
│                             │
├─────────────────────────────┤
│  BOTTOM NAV (sticky, 60px)  │  ← Kurzi · Vsebina · Kviz
└─────────────────────────────┘
```

### Bottom navigation bar (3 ikone)

Privzeti navigacijski element na vseh velikostih zaslona. Tri sekcije:

| Ikona | Tabler | Sekcija | Akcija |
|-------|--------|---------|--------|
| Kurzi   | `ti-stack-2`         | preklop med kurzi | odpre course picker |
| Vsebina | `ti-list-details`    | poglavja/lekcije  | odpre content drawer / overview |
| Kviz    | `ti-circle-check`    | kviz              | odpre kviz trenutnega obsega |

```css
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  height: var(--bottomnav-h);
  background: var(--surface);
  border-top: 0.5px solid var(--border-md);
  display: flex; align-items: stretch;
  z-index: 50;
  padding-bottom: env(safe-area-inset-bottom);  /* iPhone notch */
}
.bn-item {
  flex: 1; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 3px;
  background: none; border: none; cursor: pointer;
  color: var(--text-ter); transition: color .15s;
}
.bn-item i { font-size: 22px; }
.bn-label  { font-size: 10px; letter-spacing: .02em; }
.bn-item.active { color: var(--accent); }
```

> **Touch targets:** vsak interaktivni element vsaj **44×44 px** (Apple HIG / Material). Bottom nav itemi naj zapolnijo celotno višino bara.

### Content drawer (Vsebina)

Klik na "Vsebina" odpre **drawer** (slide-up ali full-screen overlay) s hierarhijo: kurz → poglavja → lekcije. Klik na lekcijo zapre drawer in odpre lekcijo. To nadomešča stari desktop sidebar.

```css
.drawer {
  position: fixed; inset: 0;
  background: var(--bg);
  z-index: 60;
  transform: translateY(100%);
  transition: transform .25s ease;
  overflow-y: auto;
  padding-bottom: var(--bottomnav-h);
}
.drawer.open { transform: translateY(0); }
```

### Course picker (Kurzi)

Klik na "Kurzi" odpre seznam kurzov (kartice). Klik na kurz nastavi `currentCourseId`, zapre picker in pokaže overview prvega poglavja tega kurza.

### Desktop razširitev

Pri `min-width: 900px` se layout razširi: vsebina dobi `max-width: var(--content-max)` in se centrira; bottom nav lahko ostane (app feeling) ali se preseli ob stran kot navpičen rail. **Privzeto: bottom nav ostane na vseh velikostih** — konsistentna izkušnja. Drawer na desktopu postane stalni levi panel (`min-width: 1100px`), če se odločimo zanj kasneje.

```css
@media (min-width: 900px) {
  .content { max-width: var(--content-max); margin: 0 auto; }
}
```

---

## Navigacijsko stanje

```javascript
let currentCourseId   = 1;     // kateri kurz
let currentChapterId  = 1;     // katero poglavje
let currentSectionId  = null;  // null = chapter overview; number = lesson view
let selectedFeatureId = null;
let drawerOpen        = false; // content drawer
let pickerOpen        = false; // course picker
let quiz              = null;  // aktivni kviz
```

`render()` je edina vstopna točka — preriše vse glede na stanje. Vsi navigacijski klici (`goToCourse`, `goToChapter`, `goToLesson`) postavijo `quiz = null` in zaprejo drawerje.

---

## DATA shema — multi-kurs

Top-level je zdaj `COURSES`, ne `DATA`. Vsak kurz ima svoja poglavja.

```javascript
const COURSES = [
  {
    id: 1,
    slug: "cc101",
    title: "Claude Code 101",
    subtitle: "Interaktivni učni vodič",
    chapters: [ /* enako kot prej */ ]
  },
  {
    id: 2,
    slug: "cowork",
    title: "Claude Cowork",
    subtitle: "...",
    chapters: [ ... ]
  }
];
```

```
COURSES (array)
└── course { id, slug, title, subtitle, chapters[] }
    └── chapter { id, title, objectives[], reflections[], sections[] }
        └── section { id, lesson, title, features[], notes[], questions[] }
            ├── feature { id, section_id, name, icon, badge_type, badge_text,
            │             short_desc, what_it_does, when_to_use, when_not,
            │             why_it_matters, sort_order }
            ├── note    { id, section_id, note_type, content, sort_order }
            └── question{ id, q, options[4], correct (0-based), explanation }
```

**ID-ji so unikatni znotraj svojega kurza** (ne nujno globalno čez vse kurze — ker `slug` loči kurze, je dovolj da so chapter/section/feature/note/question ID-ji unikatni znotraj enega kurza). Preveri max ID v okviru kurza pred dodajanjem.

- `section.title` = `"Naslov: Podnaslov"` — razdeli pri prvem `:`
- `reflections[]` = `"vprašanje|namig"` pipe format
- `sort_order` notes: `≤ 0` = prenotes (nad karticami), `> 0` = postnotes (pod detail panelom)

### note_type vrednosti

| note_type           | Prikaz |
|---------------------|--------|
| `youtube`           | YouTube iframe embed (16:9, zaobljeni robovi, `max-width:100%`) |
| `image`             | Slika iz `assets/` (glej spodaj) |
| `desc`              | Uvodni opisni odstavek, `var(--text-sec)`, 14px |
| `tip`               | Modra opomba z `ti-info-circle` |
| `warning`           | Oranžna opomba z `ti-alert-triangle` |
| `subsection-header` | Uppercase sivi naslov z zgornjo mejo |
| `quiz`              | Mini-kviz vprašanje |

### Slike — `image` note_type

```json
{
  "id": 50,
  "section_id": 2,
  "note_type": "image",
  "content": "assets/courses/cc101/slika_01_C1_L2.png",
  "caption": "Claude Code agentic loop (vir: Anthropic Academy)",
  "sort_order": -2
}
```

- Pot relativna na `index.html`: `assets/courses/{slug}/...`
- Konvencija imen: `slika_NN_CX_LX.png` (NN = zaporedna, CX = chapter, LX = lesson)
- `caption` v angleščini, footer atribucija Anthropic kot vir
- CSS: `max-width: 100%; height: auto; border-radius: var(--radius);`
- Slike so **zunanje** (nikoli base64) — datoteke v `assets/` mapi

```css
.note-image     { margin: .75rem 0; }
.note-image img { width: 100%; height: auto; border-radius: var(--radius); border: 0.5px solid var(--border); display: block; }
.note-image figcaption { font-size: 11px; color: var(--text-ter); margin-top: .4rem; text-align: center; }
```

---

## Komponente

### Lesson header (sticky top)

Header prikazuje celoten navigacijski kontekst lekcije: kurs → poglavje → lekcija. Dva dropdowna omogočata hitro navigacijo med poglavji in lekcijami brez odpiranja Content drawerja.

```
┌─────────────────────────────────────────┐
│ [naslov kursa]              ˅           │  ← 14px/500, klik → dropdown poglavij
│ [naslov poglavja] (Ch. N)   ˅           │  ← 11px, klik → dropdown lekcij
│ L[N]: [naslov lekcije]                  │  ← 16px/500
│ ████████░░░░  Ch. X/N · Lek. Y/M        │  ← 2px progress + label
└─────────────────────────────────────────┘
```

#### CSS

```css
.lesson-header {
  position: sticky; top: 0; z-index: 40;
  background: var(--bg);
  padding: 12px 16px 0;
  border-bottom: 0.5px solid var(--border-md);
}

.lh-course {
  font-size: 14px; font-weight: 500; color: var(--text);
  display: flex; align-items: center; gap: 6px;
  cursor: pointer; width: 100%;
  min-height: 44px;  /* touch target */
  margin-bottom: 4px;
}
.lh-course i { font-size: 14px; color: var(--accent); }

.lh-chapter {
  font-size: 11px; color: var(--text-sec);
  display: flex; align-items: center; gap: 5px;
  cursor: pointer; width: 100%;
  min-height: 32px;
  margin-bottom: 2px;
}
.lh-chapter .ch-num { color: var(--accent); }
.lh-chapter i { font-size: 12px; color: var(--accent); }

.lh-lesson {
  font-size: 16px; font-weight: 500; color: var(--text);
  margin-bottom: 10px;
}
.lh-lesson .l-num {
  color: var(--accent); font-size: 13px; font-weight: 400;
  margin-right: 4px;
}

.lh-progress {
  display: flex; align-items: center; gap: 8px;
  padding-bottom: 10px;
}
.lh-progress-bar {
  flex: 1; height: 2px;
  background: rgba(255,255,255,0.1);
  border-radius: 2px;
}
.lh-progress-fill {
  height: 100%; background: var(--accent);
  border-radius: 2px;
  transition: width .25s ease;
}
.lh-progress-label {
  font-size: 11px; color: var(--text-ter);
  white-space: nowrap;
}

/* Dropdown (poglavja in lekcije) */
.lh-dropdown {
  background: #222;
  border: 1px solid #333;
  border-radius: 12px;
  margin: 0 0 8px;
  overflow: hidden;
}
.lh-dropdown-item {
  padding: 10px 14px; font-size: 13px;
  color: var(--text-sec);
  display: flex; align-items: center; gap: 8px;
  border-bottom: 1px solid #2a2a2a;
  cursor: pointer;
  min-height: 44px;
}
.lh-dropdown-item:last-child { border-bottom: none; }
.lh-dropdown-item.active { color: var(--accent); }
.lh-dropdown-item .num {
  font-size: 10px; color: var(--text-ter); min-width: 36px;
}
.lh-dropdown-item.active .num { color: var(--accent); }
.lh-dropdown-item .check {
  margin-left: auto; font-size: 13px; color: #3B6D11;
}
.lh-dropdown-item .dot {
  margin-left: auto;
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent);
}
```

#### Behavior

- Samo en dropdown odprt naenkrat — odpiranje drugega zapre prejšnjega
- Klik izven dropdowna ga zapre (transparent backdrop `#lh-backdrop` z-index: 35)
- Klik na item: navigira + zapre dropdown
- Chevron ikona se obrne (`ti-chevron-down` ↔ `ti-chevron-up`) glede na stanje
- Status ikone v dropdownu poglavij:
  - Zaključeno poglavje (`ch.id < currentChapterId`): `ti-check` (zelena #3B6D11)
  - Aktivno poglavje: amber pika
  - Še neogledano: prazno
- Status ikone v dropdownu lekcij: aktivna lekcija = amber pika

#### Navigacijsko stanje (dodatki)

```javascript
let courseDropdownOpen  = false;  // dropdown za izbiro poglavja
let chapterDropdownOpen = false;  // dropdown za izbiro lekcije
```

Oba se resetirata na `false` ob `goToCourse`, `goToChapter`, `goToLesson`.

#### lesson-mode body class

```css
.lesson-mode #header { display: none; }
.lesson-mode .main   { margin-top: 0; min-height: 100vh; }
```

Ko je `currentSectionId !== null && !quiz`, `render()` doda `.lesson-mode` na `document.body`.
Sticky header na `top: 0` potem deluje brez konfliktov s fiksnim headerjem.

#### Progress label format

- `Ch. X/N` — X = index poglavja (1-based), N = skupno poglavij v kurzu
- `Lek. Y/M` — Y = globalni indeks lekcije čez vsa poglavja (1-based), M = skupno lekcij v kurzu

Primer: 3 poglavja (4+4+2 lekcij = 10). Trenutno L9 v Ch.3 → `Ch. 3/3 · Lek. 9/10`.

#### Lesson name parsing

`sec.title` je v formatu `"Lekcija N: Naslov lekcije"`. Za prikaz v headerju:
```javascript
const parts = sec.title.split(':');
const lessonName = parts.length > 1 ? parts.slice(1).join(':').trim() : sec.title.trim();
```

#### Mobile-first checklist

- [x] Touch targeti ≥ 44px za klikabilne vrstice (`.lh-course`, `.lh-dropdown-item`)
- [x] `:active` stanje za touch (opacity .7)
- [x] Deluje na ~380 px brez horizontalnega scrolla
- [x] Lesson header je IZVEN `.content-wrap` (full-width sticky, content ima max-width)

---

### Feature kartice (mobile)

Na mobilnem **ena kartica = polna širina** (ne grid). Klik razširi detail panel inline pod kartico.

```css
.feature-card {
  background: var(--surface); border: 0.5px solid var(--border);
  border-radius: var(--radius-lg); padding: 1rem 1.1rem;
  margin-bottom: 10px; cursor: pointer;
  transition: border-color .15s;
}
.feature-card:active   { border-color: var(--border-md); }  /* :active za touch */
.feature-card.selected { border: 1.5px solid var(--accent); }
.feature-card.selected .feature-name i { color: var(--accent); }

@media (min-width: 720px) {
  .feature-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
}
```

### Detail panel — mobile 1 stolpec, desktop 2×2

```css
.detail-grid { display: grid; grid-template-columns: 1fr; gap: 10px; }  /* mobile = 1 stolpec */
@media (min-width: 600px) {
  .detail-grid { grid-template-columns: 1fr 1fr; }  /* desktop = 2×2 */
}
.detail-panel { background: var(--surface); border: 1.5px solid var(--accent); border-radius: var(--radius-lg); padding: 1.1rem 1.2rem; margin-bottom: 1rem; }
.detail-cell  { padding: 10px 14px; background: var(--bg); border-radius: var(--radius); }
.detail-cell-label { font-size: 10px; text-transform: uppercase; letter-spacing: .06em; color: var(--text-ter); margin-bottom: 4px; }
.detail-cell-val   { font-size: 14px; color: var(--text); line-height: 1.6; }
```

Štiri celice: Kaj dela · Kdaj uporabiti · Kdaj NE · Zakaj to šteje. Panel dobi enako zlato obrobo kot izbrana kartica (vizualna povezava).

### Opombe

```css
.note-tip     { display:flex; align-items:flex-start; gap:.5rem; background:rgba(125,211,252,0.08); border-left:2px solid #38BDF8; padding:10px 13px; font-size:13px; border-radius:0 var(--radius) var(--radius) 0; color:#7DD3FC; margin-bottom:.75rem; }
.note-warning { display:flex; align-items:flex-start; gap:.5rem; background:rgba(251,146,60,0.08); border-left:2px solid #FB923C; padding:10px 13px; font-size:13px; border-radius:0 var(--radius) var(--radius) 0; color:#FB923C; margin-bottom:.75rem; }
.note-subsection { font-size:10px; text-transform:uppercase; letter-spacing:.07em; color:var(--text-ter); padding-top:1rem; margin:.5rem 0 .75rem; border-top:0.5px solid var(--border); }
```

### YouTube embed (responsive 16:9)

```css
.note-youtube { position: relative; width: 100%; padding-bottom: 56.25%; height: 0; margin: .75rem 0; border-radius: var(--radius); overflow: hidden; }
.note-youtube iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
```

---

## Quiz sistem — tri ravni

Vse poganja **isti engine** (`quizEngineHTML()`). Vsa vprašanja, naključni vrstni red, brez limitov.

| Raven   | Obseg | Vir vprašanj |
|---------|-------|--------------|
| `lesson`  | ena lekcija         | `section.questions` |
| `chapter` | celo poglavje       | vsa vprašanja poglavja |
| `total`   | cel kurz            | vsa vprašanja kurza |

Na mobilnem kviz teče **full-screen** (prevzame content area, bottom nav ostane). Eno vprašanje naenkrat, progress bar zgoraj, takojšen feedback (zelena `#86EFAC` / rdeča `#FB7185`), razlaga po odgovoru, final score na koncu.

```javascript
let quiz = null;
// quiz = { scope:'lesson'|'chapter'|'total', id, pool:[...], idx, correct, answered, selected }

function collectQuestions(scope, id) { /* lesson→section, chapter→chapter, total→cel kurz */ }
function startQuiz(scope, id) { /* shuffle, set quiz, render */ }
function answerQuiz(oi) { /* lock, count, re-render */ }
function nextQuiz() { /* idx++, render */ }
function quizEngineHTML() { /* skupni UI: vprašanje + opcije + progress | final score */ }
```

### question struktura

```json
{
  "id": 1,
  "q": "Vprašanje?",
  "options": ["A", "B", "C", "D"],
  "correct": 1,
  "explanation": "Razlaga po odgovoru."
}
```

- `options` = vedno 4
- `correct` = indeks (0–3)
- `id` unikaten znotraj kurza
- **Nova lekcija = nova vprašanja** (5–10 na lekcijo)

---

## Language switcher

Gumbi: SL / IT / DE / FR / PL / EN. Na mobilnem v headerju (kompaktno) ali v drawerju.

- **English** = konstanta za tehnične pojme: Claude Code, Cowork, Artifacts, Skills, MCP, Hooks, Plan Mode, Plugins… **nikoli prevedeno**
- **Lokalni jezik** = razlage, opisi — privzeto slovenščina
- Zasnovano za enostavno lokalizacijo (IT, DE, FR, PL, GR, RU, FI, SV…)

Aktivni gumb: `background: var(--accent); color: #111; font-weight: 600`.

---

## Postopek dodajanja vsebine (Python)

```python
import re, json

with open('/home/claude/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const COURSES = (\[.+?\]);', html, re.DOTALL)
courses = json.loads(m.group(1))

# Najdi pravi kurz po slug
course = next(c for c in courses if c['slug'] == 'cc101')

# Max ID-ji ZNOTRAJ kurza
all_sec  = [s['id'] for ch in course['chapters'] for s in ch['sections']]
all_feat = [f['id'] for ch in course['chapters'] for s in ch['sections'] for f in s['features']]
all_note = [n['id'] for ch in course['chapters'] for s in ch['sections'] for n in s['notes']]
all_q    = [q['id'] for ch in course['chapters'] for s in ch['sections'] for q in s.get('questions', [])]

# Modify ...

new_data = json.dumps(courses, ensure_ascii=False)
html = html.replace(m.group(0), f'const COURSES = {new_data};')

with open('/home/claude/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
```

> Vsebino vedno urejamo prek **Python skripta** — nikoli ročno. Render funkcij se ne dotikamo (samo `COURSES`).

### Deploy (v tem okolju)

```bash
cp /home/claude/index.html /mnt/user-data/outputs/index.html
```
Nato `present_files(["/mnt/user-data/outputs/index.html"])`.

> V resničnem projektu Andrej commita prek GitHub Desktop iz lokalne mape. Deploy na javni GitHub Pages šele ko je platforma ready (repo private → public + Pages, ali Netlify z geslom).

---

## Workflow (zakon)

```
Nova snov / sprememba
      ↓
Predlagaj strukturo vsebine v tabeli za odobritev
      ↓
Počakaj na "zeleno luč" / "zelena luč"
      ↓
Python skript: parse COURSES → dodaj → zapiši
      ↓
Programska verifikacija (json valid, ID-ji, render)
      ↓
cp → outputs → present_files
```

**Nikoli** ne piši/spreminjaj HTML brez Andrejeve eksplicitne odobritve. Andrej ne piše kode — Claude gradi, Andrej pregleda in odobri.

---

## Mobile-first checklist (pred vsako komponento)

- [ ] Deluje na ~380 px širine brez horizontalnega scrolla?
- [ ] Touch targeti ≥ 44×44 px?
- [ ] `:active` stanja za touch (ne samo `:hover`)?
- [ ] Slike/video `max-width: 100%`?
- [ ] Bottom nav ne prekriva vsebine (`padding-bottom: var(--bottomnav-h)`)?
- [ ] `env(safe-area-inset-bottom)` za iPhone notch?
- [ ] Desktop razširitev prek `@media (min-width: …)`, ne obratno?
