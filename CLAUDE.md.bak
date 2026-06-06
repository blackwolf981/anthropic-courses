# CLAUDE.md

Navodila za Claude Code pri delu na projektu **anthropic-courses**.

## 1. Project overview

**anthropic-courses** je interaktivna, **mobile-first** učna platforma za Anthropic Academy kurze.

- **Trenutni kurzi:** Claude Code 101 (zaključen v starem projektu, vir za migracijo), Claude Cowork (naslednji)
- **Ciljna publika:** tech-savvy non-developers (marketing, consulting, business, project management) + začetni razvijalci
- **Sekundarni cilj:** predloga za šolski/dobrodelni projekt (osnovna in srednja šola)
- **Jezik:** slovenščina (privzeto) za vse razlage; angleščina za vse tehnične termine (Claude Code, Cowork, Artifacts, Skills, MCP, Hooks, Plan Mode, Plugins…) — **nikoli prevedeni**. Zasnovano za enostavno lokalizacijo (IT, DE, FR, PL, GR, RU, FI, SV…)
- **Cilj:** prijetna interaktivna izkušnja, ki uporabnika pripravi na pravi Anthropic certifikat — ne le razlaga konceptov, ampak ga tudi preverja s kvizi

## 2. Architecture

- **En sam HTML file** (`index.html`) — brez build koraka, brez bundlerja, brez serverja
- Vsebina živi v JS konstanti **`COURSES`** (array kurzov); render engine bere `COURSES` in gradi DOM
- **Mobile-first:** base CSS = telefon (~380 px); desktop je `@media (min-width: …)` razširitev — nikoli obratno
- **Navigacija:** bottom navigation bar (3 ikone — Kurzi · Vsebina · Kviz), full-screen lesson view, content drawer namesto sidebara, sticky header s progress barom
- **Multi-kurs:** preklapljanje med kurzi znotraj iste aplikacije; vsak kurz ima `slug`
- **Slike:** zunanje v `assets/courses/{slug}/` (nikoli base64); konvencija `slika_NN_CX_LX.png`
- **Vsebino dodajamo prek Python skripta** (parse → modify `COURSES` → write) — nikoli ročno; render funkcij se ne dotikamo

Podrobna specifikacija dizajna in komponent je v **`html-design-skill.md`** (registriran kot skill). **Preberi ga preden dodajaš katerokoli komponento ali vsebino.**

### Navigacijsko stanje

```js
let currentCourseId   = 1;
let currentChapterId  = 1;
let currentSectionId  = null;  // null = chapter overview; number = lesson view
let selectedFeatureId = null;
let quiz              = null;
```

`render()` je edina vstopna točka — preriše vse glede na stanje.

### DATA shema

```
COURSES → course { id, slug, title, subtitle, chapters[] }
          └ chapter { id, title, objectives[], reflections[], sections[] }
            └ section { id, lesson, title, features[], notes[], questions[] }
```

ID-ji unikatni **znotraj kurza** (slug loči kurze).

## 3. Workflow

- **Vedno predlagaj strukturo vsebine za odobritev PRED kodiranjem.** Počakaj na eksplicitno "zeleno luč" / "zelena luč".
- **Andrej ne piše kode.** Claude gradi, Andrej pregleda in odobri.
- Po implementaciji: **programska verifikacija** (JSON valid, ID-ji unikatni, render deluje) pred zaključkom.
- Vsaka nova lekcija **mora** dobiti `questions` (5–10 vprašanj).

## 4. Okolje

- **OS:** Windows · terminal: CMD · deployment: GitHub Desktop
- **Mapa:** `C:\Users\andre\OneDrive\Documents\GitHub\anthropic-courses` (GitHub mapa = delovna mapa, ena sama)
- **Repo:** zaseben med gradnjo → public + GitHub Pages ko je ready (ali Netlify z geslom za password protection)
- **Tracking/profili (Firebase):** načrtovano za kasnejši korak; "Napredek" (4. nav ikona) pride takrat

## 5. Mobile-first pravila

- Touch targeti ≥ 44×44 px; `:active` stanja (ne samo `:hover`)
- Slike/video `max-width: 100%`
- Bottom nav ne prekriva vsebine (`padding-bottom: var(--bottomnav-h)`)
- `env(safe-area-inset-bottom)` za iPhone notch
- Deluje na ~380 px brez horizontalnega scrolla
