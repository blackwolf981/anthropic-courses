# HANDOFF: Chapter Overview — header in drawer
_Datum: 2026-06-08 | Pripravil: app | Za: terminal_

## Cilj
Razširi navigacijo, da bo Chapter Overview prvorazredno mesto v hierarhiji kurz → chapter → lekcija:

1. **Lesson header** prikaži tudi v chapter overview načinu (trenutno se vidi star "ch-overview-header" namesto novega lesson headerja)
2. **Chapter dropdown** v headerju naj prikazuje "Chapter Overview" kot prvo izbiro nad lekcijami
3. **Vsebina drawer** naj ima "Chapter Overview" entry kot prvi element pod vsakim chapterjem

## Kontekst
- Trenutno klik na chapter v course dropdownu pelje uporabnika na chapter overview, ki ima star header brez dropdownov — nedosledno z lesson view
- Andrej je potrdil format "CP{N}: Chapter Overview" (npr. "CP1: Chapter Overview") — angleški "Chapter Overview", brez slovenskega prevoda
- "CP" prefix ni amber, je enak slogu kot "L{N}:" prefix v lesson headerju

---

## KORAK 1 — Header v chapter overview načinu

### Trenutno stanje
- `renderChapterOverview` (vrstica ~1095) vrne HTML, ki vključuje `<div class="ch-overview-header">` z `Poglavje N` in naslovom chapterja
- `render()` (vrstica ~1407) izriše to v `#app` brez klica `renderLessonHeader`
- Sticky lesson header se NE prikaže v chapter overview načinu

### Cilj
Lesson header (4-vrstični, z obema dropdownoma) naj se prikaže **tudi** v chapter overview načinu. Vsebina headerja:
- Vrstica 1: naslov kurza + chevron (klikabilen)
- Vrstica 2: naslov chapterja + (Ch. N) + chevron (klikabilen)
- Vrstica 3: **`CP{N}: Chapter Overview`** — "CP{N}:" v amber barvi (enak slog kot "L{N}:"), "Chapter Overview" v beli
- Vrstica 4: `Ch. X/N` (samo chapter progress, brez `Lek. Y/M`)

### Implementacija

**1.1.** Razširi `renderLessonHeader` (cca vrstica 1140) tako da deluje v obeh načinih — z `currentSectionId` (lesson) in brez njega (chapter overview).

Trenutno funkcija predpostavlja `getSection()` vrne section. Dodaj check na začetku:

```javascript
function renderLessonHeader() {
  const course = getCourse();
  const ch = getChapter();
  const sec = getSection();  // lahko je null v chapter overview načinu
  if (!ch) return;

  const chapterIdx = course.chapters.findIndex(c => c.id === currentChapterId) + 1;
  const totalChapters = course.chapters.length;

  // ... (course/chapter dropdown logika ostane)

  // Tretja vrstica — chapter overview ali lesson
  let titleRowHtml;
  let progressHtml;

  if (sec) {
    // Lesson način (kot zdaj)
    const parts = sec.title.split(':');
    const lessonName = parts.length > 1 ? parts.slice(1).join(':').trim() : sec.title.trim();
    titleRowHtml = `<div class="lh-lesson">
      <span class="l-num">L${lessonNum(sec.lesson)}:</span>${lessonName}
    </div>`;

    // Progress: globalni indeks lekcije
    let totalSections = 0, globalIdx = 0;
    for (const c of course.chapters) {
      for (const s of c.sections) {
        totalSections++;
        if (c.id === currentChapterId && s.id === currentSectionId) globalIdx = totalSections;
      }
    }
    const progressPct = totalSections ? Math.round(globalIdx / totalSections * 100) : 0;
    progressHtml = `<div class="lh-progress">
      <div class="lh-progress-bar"><div class="lh-progress-fill" style="width:${progressPct}%"></div></div>
      <span class="lh-progress-label">Ch. ${chapterIdx}/${totalChapters} &middot; Lek. ${globalIdx}/${totalSections}</span>
    </div>`;
  } else {
    // Chapter overview način
    titleRowHtml = `<div class="lh-lesson">
      <span class="l-num">CP${chapterIdx}:</span>Chapter Overview
    </div>`;

    // Progress: samo chapter
    const progressPct = Math.round(chapterIdx / totalChapters * 100);
    progressHtml = `<div class="lh-progress">
      <div class="lh-progress-bar"><div class="lh-progress-fill" style="width:${progressPct}%"></div></div>
      <span class="lh-progress-label">Ch. ${chapterIdx}/${totalChapters}</span>
    </div>`;
  }

  return `<div class="lesson-header">
    ${/* course row + course dropdown */}
    ${/* chapter row + chapter dropdown */}
    ${titleRowHtml}
    ${progressHtml}
  </div>`;
}
```

**1.2.** V `render()` funkciji posodobi pogoj za `lesson-mode` body class in renderiranje headerja:

Trenutno (cca vrstica 1407):
```javascript
const inLesson = !!(currentSectionId && !quiz);
document.body.classList.toggle('lesson-mode', inLesson);
if (!inLesson) renderHeader();
```

Spremeni v:
```javascript
// Lesson header se prikaže v lesson view IN chapter overview view
const showLessonHeader = !quiz && !!currentChapterId;
document.body.classList.toggle('lesson-mode', showLessonHeader);
if (!showLessonHeader) renderHeader();
```

**1.3.** V `renderChapterOverview` **odstrani** stari `<div class="ch-overview-header">` blok, ker bo lesson header zdaj prevzel to vlogo:

```javascript
// Odstrani ta blok:
// <div class="ch-overview-header">
//   <div class="ch-label">Poglavje ${ch.id}</div>
//   <div class="ch-title">${ch.title}</div>
// </div>
```

**1.4.** V `render()` funkciji, ko se renderira chapter overview, **prepend** lesson header:

```javascript
} else {
  const ch = getChapter();
  const headerHtml = renderLessonHeader();
  const overviewHtml = renderChapterOverview(ch);
  html = headerHtml + overviewHtml;
  // ... ostale nav bar nastavitve
}
```

---

## KORAK 2 — Chapter dropdown vsebina

### Trenutno stanje
Chapter dropdown v headerju (cca vrstica 1186) prikazuje samo lekcije:
```javascript
ch.sections.map(s => {
  // ... item za lekcijo
})
```

### Cilj
Prikaži **Chapter Overview kot prvo izbiro** nad lekcijami. Aktiven, če `currentSectionId === null`.

### Implementacija

V chapter dropdown HTML, pred mapping čez `ch.sections`, dodaj overview entry:

```javascript
const chDropHtml = chapterDropdownOpen ? `<div class="lh-dropdown">
  <div class="lh-dropdown-item${!currentSectionId ? ' active' : ''}"
       onclick="goToChapterOverview(${ch.id})">
    <span class="num">CP${chapterIdx}</span>
    <span class="lh-item-title">Chapter Overview</span>
    ${!currentSectionId ? '<span class="dot"></span>' : ''}
  </div>
  ${ch.sections.map(s => {
    // ... obstoječi mapping za lekcije
  }).join('')}
</div>` : '';
```

In dodaj novo navigation funkcijo (skupaj z drugimi `goTo*` funkcijami, vrstica ~887):

```javascript
function goToChapterOverview(chId) {
  currentChapterId  = chId;
  currentSectionId  = null;
  selectedFeatureId = null;
  quiz              = null;
  closeDropdownsState();
  closeDrawer();
  render();
  window.scrollTo(0, 0);
}
```

Opomba: `goToChapter` ima podobno logiko, ampak je klican iz drugih kontekstov (course dropdown, drawer chapter toggle). Naredi ločeno funkcijo da ne pokvariš obstoječega obnašanja.

---

## KORAK 3 — Vsebina drawer

### Trenutno stanje
`renderDrawer()` (vrstica ~995) za vsak chapter prikaže `drawer-ch-btn` + listo lekcij. Klik na chapter button samo razširi/skrči lekcije (`toggleDrawerChapter`).

### Cilj
Dodaj **"Chapter Overview"** entry kot prvi element v `drawer-sections` listi vsakega chapterja. Klik nanj naj odpre chapter overview tega chapterja.

### Implementacija

V `renderDrawer()`, kjer se gradi `secsHtml`, dodaj overview entry na začetek:

```javascript
const secsHtml = ch.sections.map(s => {
  const isActiveSec = isActiveCh && s.id === currentSectionId;
  // ... obstoječ kod za lesson button
}).join('');

// Dodaj overview entry na vrh
const isActiveOverview = isActiveCh && currentSectionId === null;
const overviewBtnHtml = `<button class="drawer-sec-btn${isActiveOverview ? ' active' : ''}"
  onclick="goToChapterOverview(${ch.id})">
  <span class="drawer-sec-dot"></span>
  <span class="drawer-sec-lesson">CP${ch.id}</span>
  <span class="drawer-sec-title">Chapter Overview</span>
</button>`;

const allSecsHtml = overviewBtnHtml + secsHtml;
```

In v `drawer-sections` div uporabi `allSecsHtml` namesto `secsHtml`.

**Opomba:** Trenutno `closeDrawer` ni eksplicitno klican v `goToChapterOverview` — preveri da se drawer res zapre po kliku.

---

## KORAK 4 — Posodobi html-design-skill.md

Dodaj kratko subsekcijo "Chapter overview header" v skill datoteko, pod "Lesson header (sticky top)" sekcijo (po "Lesson number helper" subsekciji).

### Vsebina za dodajanje:

```markdown
#### Chapter overview header

Lesson header se uporablja **tudi** v chapter overview načinu (`currentSectionId === null`). Razlike:

- Tretja vrstica: `CP{chapterIdx}: Chapter Overview` namesto `L{N}: <naslov>`
- Progress label: `Ch. X/N` brez `Lek. Y/M`
- Chapter dropdown prikaže "Chapter Overview" kot prvo izbiro nad lekcijami (aktivno ko `currentSectionId === null`)
- Vsebina drawer ima "Chapter Overview" entry na vrhu sekcije vsakega chapterja

Navigacijska funkcija `goToChapterOverview(chId)` postavi `currentSectionId = null` in renderira chapter overview view.
```

---

## Kar NE smeš spremeniti
- Vsebina lekcij (COURSES data)
- Bottom navigation bar
- Quiz funkcionalnost
- Feature cards in notes rendering v lekcijah
- Obstoječe `goToCourse`, `goToChapter`, `goToLesson` (samo dodaš novo `goToChapterOverview`)
- `renderChapterOverview` ohrani vse razen ch-overview-header bloka

---

## Preverjanje po implementaciji
- [ ] V chapter overview načinu se prikaže lesson header (4 vrstice z dropdownoma)
- [ ] Tretja vrstica headerja prikazuje `CP1: Chapter Overview` (amber prefix, bel naslov)
- [ ] Progress label v chapter overview načinu prikazuje samo `Ch. X/N`
- [ ] Klik na chapter v course dropdownu pelje na chapter overview (ne na prvo lekcijo)
- [ ] Chapter dropdown ima "Chapter Overview" kot prvo izbiro, označeno z amber piko ko je aktivno
- [ ] Vsebina drawer prikazuje "Chapter Overview" entry kot prvi v vsakem chapterju
- [ ] Klikabilnost se ohrani po vseh teh navigacijah (regression check za bug 2 fix)
- [ ] Stari `ch-overview-header` z "Poglavje N" je odstranjen iz chapter overview view
- [ ] Skill posodobljen — subsekcija "Chapter overview header" dodana

---

## OPOZORILO: PROJECT_STATUS.md File registry

V prejšnji seji so bili nekateri "Zadnji sync" datumi v File registry pozabljeni (`index.html` in `PROJECT_STATUS.md` sta ostala na 2026-06-07 čeprav sta bila spremenjena).

`project-status-skill.md` je bil v tej seji posodobljen z eksplicitnim navodilom — preberi novo verzijo pred posodobitvijo statusa.

Za to sejo posodobi sync datume za vse spremenjene datoteke:
- `index.html` → današnji datum
- `html-design-skill.md` → današnji datum (ker dodajaš novo subsekcijo)
- `project-status-skill.md` → današnji datum (Andrej naloži novo verzijo v repo pred to sejo)
- `PROJECT_STATUS.md` → današnji datum
- Vsi trije datumi (na vrhu, "Zadnja seja", "Zadnji sync") se morajo ujemati
