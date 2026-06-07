# HANDOFF: Lesson header redesign + skill update
_Datum: 2026-06-07 | Pripravil: app | Za: terminal_

## Cilj
1. Popravi sticky header pri prikazu lekcije v `index.html` — nov dizajn z breadcrumb navigacijo in dvema klikabnima dropdownoma.
2. Posodobi `html-design-skill.md` — dodaj sekcijo "Lesson header" za uporabo v prihodnjih učilnicah.

## Kontekst
- Trenutni header prikazuje samo "Lekcija 9" — brez konteksta kurza, poglavja ali naslova lekcije
- Nov header mora prikazati celoten kontekst v kompaktni obliki
- Odobreno s strani Andreja po vizualnem mockupu
- Skill update zagotavlja, da bo novi header pattern dostopen pri gradnji novih učilnic (npr. Zgodovina 6. razreda)

---

## KORAK 1 — Implementacija v `index.html`

### Struktura headerja (od zgoraj navzdol):
```
[1] Introduction to Claude Cowork  ˅         ← klikabilen, amber chevron
[2] Use Claude wherever you work (Ch. 3)  ˅  ← klikabilen, amber chevron
[3] L9: Claude in Chrome                      ← naslov lekcije, velik, bel
[4] ████████████░░░  Ch. 3/3 · Lek. 9/10     ← progress bar + label
```

### Vrstica [1] — naslov kursa:
- Font: 14px, weight 500, barva `var(--text)` (#F0F0F0)
- Chevron ikona desno (`ti-chevron-down` / `ti-chevron-up`), barva `var(--accent)`
- Klik odpre/zapre dropdown z vsemi poglavji kurza
- Dropdown prikazuje: `Ch. N` + naslov poglavja
  - Zaključena poglavja: checkmark ikona (`ti-check`, barva #3B6D11)
  - Aktivno poglavje: amber pika (6px) desno
  - Aktivno poglavje: tekst barva `var(--accent)`

### Vrstica [2] — naslov poglavja:
- Font: 11px, barva `var(--text-sec)` (#A0A0A0)
- Format: `[naslov poglavja] (Ch. N)` — "Ch. N" v amber barvi
- Chevron ikona desno (`ti-chevron-down` / `ti-chevron-up`), barva `var(--accent)`
- Klik odpre/zapre dropdown z vsemi lekcijami tega poglavja
- Dropdown prikazuje: `L[N]` + naslov lekcije
  - Aktivna lekcija: amber pika desno

### Vrstica [3] — naslov lekcije:
- Font: 16px, weight 500, barva `var(--text)`
- Format: `L[N]: [naslov lekcije]`
- "L[N]:" prefix: 13px, weight 400, barva `var(--accent)`, margin-right 4px

### Vrstica [4] — progress:
- Tanki progress bar (2px), barva `var(--accent)`, background #333
- Label desno: `Ch. [X]/[total] · Lek. [Y]/[total]`
- Font: 11px, barva `var(--text-ter)` (#606060)

### Dropdown styling:
- Background: #222, border: 1px solid #333, border-radius: 12px
- Padding item: 10px 14px
- Font: 13px
- Separator med itemi: 1px solid #2a2a2a
- Margin: 8px 16px 0 (znotraj headerja, nad vsebino)
- Ob kliku na item: navigacija na to poglavje/lekcijo + zapri dropdown

### Behavior:
- Samo en dropdown odprt naenkrat — odpiranje enega zapre drugega
- Klik izven dropdowna zapre dropdown
- Touch targeti za klikabilne vrstice ≥ 44px (cel row je tap target)

---

## KORAK 2 — Posodobi `html-design-skill.md`

Dodaj naslednjo sekcijo v skill datoteko. **Lokacija:** v sekciji "Komponente", takoj za `### Feature kartice (mobile)` ali pred njo — kakor je bolj logično. Lahko tudi kot nova sekcija med "Mobile-first layout" in "Navigacijsko stanje".

### Vsebina za dodajanje (copy-paste markdown):

````markdown
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
  cursor: pointer; width: fit-content;
  min-height: 44px;  /* touch target */
  margin-bottom: 4px;
}
.lh-course i { font-size: 14px; color: var(--accent); }

.lh-chapter {
  font-size: 11px; color: var(--text-sec);
  display: flex; align-items: center; gap: 5px;
  cursor: pointer; width: fit-content;
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

/* Dropdown (uporabljen tako za poglavja kot za lekcije) */
.lh-dropdown {
  background: #222;
  border: 1px solid #333;
  border-radius: 12px;
  margin: 8px 0 0;
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
  font-size: 10px; color: var(--text-ter); min-width: 32px;
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
- Klik izven dropdowna ga zapre
- Klik na item v dropdownu: navigira + zapre dropdown
- Chevron ikona se obrne (`ti-chevron-down` ↔ `ti-chevron-up`) glede na stanje
- Status ikone v dropdownu poglavij:
  - Zaključeno poglavje (vse lekcije ogledane): `ti-check` (zelena #3B6D11)
  - Aktivno poglavje: amber pika
  - Še neogledano: prazno
- Status ikone v dropdownu lekcij: aktivna lekcija = amber pika

#### Navigacijsko stanje (dodatki)

```javascript
let courseDropdownOpen  = false;  // dropdown za izbiro poglavja
let chapterDropdownOpen = false;  // dropdown za izbiro lekcije
```

Oba se resetirata na `false` ob `goToCourse`, `goToChapter`, `goToLesson`.

#### Progress label format

- `Ch. X/N` — X = trenutno poglavje (1-based), N = skupno število poglavij v kurzu
- `Lek. Y/M` — Y = globalni indeks trenutne lekcije v kurzu (1-based, čez vsa poglavja), M = skupno število lekcij v kurzu

Primer: kurz ima 3 poglavja (4+4+2 lekcij = 10 lekcij). Trenutno L9 v Ch.3 → `Ch. 3/3 · Lek. 9/10`.

#### Mobile-first checklist

- [x] Touch targeti ≥ 44px za klikabilne vrstice
- [x] `:active` stanje za touch (opacity ali border-color)
- [x] Deluje na ~380 px brez horizontalnega scrolla
- [x] Sticky top header ne prekriva vsebine (`scroll-padding-top: var(--header-h)`)
````

---

## Kar NE smeš spremeniti
- Render engine (`render()` funkcija) — samo dodaj header logiko
- Bottom navigation bar
- Vsebina lekcij (COURSES data)
- Feature cards, notes, questions — vse ostane
- Content drawer — header dropdowna NI zamenjava za drawer, je dodatek

---

## Preverjanje po implementaciji
- [ ] Header se pravilno prikaže na 380px
- [ ] Kurs dropdown prikazuje vsa poglavja z ustreznimi statusnimi ikonami
- [ ] Chapter dropdown prikazuje vse lekcije v aktivnem poglavju
- [ ] Progress label prikazuje pravilne vrednosti (Ch. X/total · Lek. Y/total)
- [ ] Oba dropdowna se zapreta ob kliku drugje
- [ ] Navigacija prek dropdowna deluje (klik na poglavje/lekcijo navigira)
- [ ] Samo en dropdown odprt naenkrat
- [ ] Ni horizontalnega scrolla na mobilnem
- [ ] `html-design-skill.md` posodobljen — sekcija "Lesson header" dodana
