# HANDOFF: Lesson header bug fixes
_Datum: 2026-06-07 | Pripravil: app | Za: terminal_

## Cilj
Popravi dva buga v lesson header implementaciji v `index.html`:
1. **Bug 1:** "LLekcija" double prefix v dropdown itemih in lesson title
2. **Bug 2:** Po navigaciji prek headerjevega dropdowna se klikabilnost sesuje (feature kartice, puščice naprej/nazaj ne delujejo)

## Kontekst
- Header implementacija je bila narejena v prejšnji seji — vizualno deluje
- Andrej je opazil oba buga med testiranjem na mobilni napravi
- Diagnoza je potrjena s pregledom kode v `index.html`

---

## BUG 1 — "LLekcija" double prefix

### Diagnoza
V `COURSES` data je polje `lesson` **nekonzistentno**:
- L1–L8 (Cowork Ch1+Ch2) in vse lekcije v Claude Code 101: `"lesson":"Lekcija 1"`, `"lesson":"Lekcija 2"` ... (**stringi**)
- L9–L10 (Cowork Ch3): `"lesson":9`, `"lesson":10` (**številke**)

V render kodi (vrstica ~1185 in ~1204):
```javascript
<span class="num">L${s.lesson}</span>
<span class="l-num">L${sec.lesson}:</span>
```

Pri `s.lesson = "Lekcija 1"` rezultat je `"LLekcija 1"` (double prefix). Pri `s.lesson = 10` rezultat je `"L10"` (pravilno).

### Rešitev
Najmanj invazivna pot: helper funkcija ki ekstrahira številko iz `lesson` polja ne glede na tip.

Dodaj helper funkcijo (kamor koli pred `renderLessonHeader` ali skupaj z ostalimi helperji):

```javascript
function lessonNum(lesson) {
  // Vrne čisto številko: "Lekcija 6" → 6, 10 → 10, "10" → 10
  if (typeof lesson === 'number') return lesson;
  const m = String(lesson).match(/\d+/);
  return m ? parseInt(m[0], 10) : lesson;
}
```

Nato v render kodi zamenjaj **obe pojavitvi**:

```javascript
// V chapter dropdown (cca vrstica 1185):
<span class="num">L${lessonNum(s.lesson)}</span>

// V lesson title (cca vrstica 1204):
<span class="l-num">L${lessonNum(sec.lesson)}:</span>
```

### Alternativna pot (NE priporočena za to handoff)
Normalizacija `COURSES` data tako da imajo vsi `lesson` polja številke. To je čistejše dolgoročno, ampak zahteva edit JSON-a v `index.html` — tveganje data corruption. Pusti za kasneje.

---

## BUG 2 — Klikabilnost se sesuje po dropdown navigaciji

### Diagnoza
V `toggleCourseDropdown` in `toggleChapterDropdown` (vrstice 967–977):
```javascript
document.getElementById('lh-backdrop').classList.toggle('open', courseDropdownOpen || chapterDropdownOpen);
```

Backdrop dobi CSS class `open` ko se odpre dropdown. Backdrop je element `<div id="lh-backdrop" onclick="closeLessonDropdowns()">` (vrstica 842) — prekriva celotno površino in **prestreza klike**.

V `goToCourse`, `goToChapter`, `goToLesson` (vrstice 883–915) state se resetira (`courseDropdownOpen = false; chapterDropdownOpen = false`), ampak **`lh-backdrop` element NIKOLI ne dobi odstranjen `open` class**. Backdrop ostane prekrit čez celo stran in prestreza vse klike — feature kartice, puščice naprej/nazaj, vse.

Druge navigacijske poti (kurzi picker, vsebina drawer) ne sprožijo backdropa, zato delujejo normalno. Bug je specifičen za dropdown navigacijo.

### Rešitev
V vsako od treh funkcij `goToCourse`, `goToChapter`, `goToLesson` dodaj eksplicitno odstranitev `open` class-a od backdropa **pred klicem `render()`**:

```javascript
function goToCourse(id) {
  currentCourseId      = id;
  currentChapterId     = getCourse().chapters[0].id;
  currentSectionId     = null;
  selectedFeatureId    = null;
  quiz                 = null;
  courseDropdownOpen   = false;
  chapterDropdownOpen  = false;
  document.getElementById('lh-backdrop').classList.remove('open');  // ← DODAJ
  closePicker();
  render();
}

function goToChapter(id) {
  currentChapterId     = id;
  currentSectionId     = null;
  selectedFeatureId    = null;
  quiz                 = null;
  courseDropdownOpen   = false;
  chapterDropdownOpen  = false;
  document.getElementById('lh-backdrop').classList.remove('open');  // ← DODAJ
  render();
}

function goToLesson(chId, secId) {
  currentChapterId     = chId;
  currentSectionId     = secId;
  selectedFeatureId    = null;
  quiz                 = null;
  courseDropdownOpen   = false;
  chapterDropdownOpen  = false;
  document.getElementById('lh-backdrop').classList.remove('open');  // ← DODAJ
  closeDrawer();
  render();
  window.scrollTo(0, 0);
}
```

### Boljša alternativna pot (priporočena)
Namesto da podvajaš isto vrstico v treh funkcijah, naredi helper funkcijo in jo kliči:

```javascript
function closeLessonDropdowns() {
  courseDropdownOpen  = false;
  chapterDropdownOpen = false;
  const backdrop = document.getElementById('lh-backdrop');
  if (backdrop) backdrop.classList.remove('open');
}
```

Funkcija `closeLessonDropdowns` **že obstaja** (vrstice 980–986), samo nima `render()` klica:
```javascript
function closeLessonDropdowns() {
  if (!courseDropdownOpen && !chapterDropdownOpen) return;
  courseDropdownOpen  = false;
  chapterDropdownOpen = false;
  document.getElementById('lh-backdrop').classList.toggle('open', false);
  render();
}
```

Ampak ta `if (!courseDropdownOpen && !chapterDropdownOpen) return;` na začetku je problem — ko se kliče iz `goToLesson`, sta state vrednosti že lahko `false` zaradi prejšnjega reseta. Bolje je:

**Najčistejša rešitev:**
1. V `closeLessonDropdowns` odstrani guard `if (!courseDropdownOpen && !chapterDropdownOpen) return;` ali ga premakni — ker mora vedno počistiti DOM.
2. V `goToCourse`, `goToChapter`, `goToLesson` zamenjaj inline reset z `closeLessonDropdowns()`-style cleanup, **vendar brez render() klica** (ker funkcije že naredijo render same).

**Konkretno predlagam:**

Refaktoriraj `closeLessonDropdowns` v dva dela:
```javascript
function closeDropdownsState() {
  courseDropdownOpen  = false;
  chapterDropdownOpen = false;
  const backdrop = document.getElementById('lh-backdrop');
  if (backdrop) backdrop.classList.remove('open');
}

function closeLessonDropdowns() {
  if (!courseDropdownOpen && !chapterDropdownOpen) return;
  closeDropdownsState();
  render();
}
```

Nato v `goToCourse`, `goToChapter`, `goToLesson` zamenjaj:
```javascript
courseDropdownOpen   = false;
chapterDropdownOpen  = false;
```
z:
```javascript
closeDropdownsState();
```

---

## Kar NE smeš spremeniti
- Vsebina lekcij (COURSES data) — bug fix samo v render in navigation kodi
- Bottom navigation bar
- Render engine (`render()` funkcija sama)
- Feature cards, notes, questions
- Header struktura (4 vrstice ostanejo)

---

## Preverjanje po implementaciji
- [ ] L1 v Cowork Ch1 prikazuje "L1:" (NE "LLekcija 1:") v dropdownu in v naslovu lekcije
- [ ] L6 v Cowork Ch2 prikazuje "L6:" (NE "LLekcija 6:")
- [ ] L9 in L10 v Cowork Ch3 še vedno prikazujeta "L9:" in "L10:" (regression check)
- [ ] Vse lekcije v Claude Code 101 prikazujejo "L1:", "L2:" itd.
- [ ] Po kliku na chapter v course dropdownu se klikabilnost ohrani: feature kartice se odpirajo, puščice Prej/Naprej delujejo
- [ ] Po kliku na lekcijo v chapter dropdownu se klikabilnost ohrani
- [ ] Backdrop element nima `open` class-a po navigaciji (preveri v DevTools)
- [ ] Dropdown se zapre normalno ob kliku izven (na backdrop)
