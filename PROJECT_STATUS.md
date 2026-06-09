# PROJECT_STATUS.md
_Zadnja posodobitev: 2026-06-09 (seja 3)_

## Projekt
**anthropic-courses** · single HTML file (`index.html`) · mobile-first · multi-kurs
Repo: `C:\Users\andre\OneDrive\Documents\GitHub\anthropic-courses`

## Kurzi
| Kurz | Slug | Poglavja | Lekcije | Status |
|------|------|----------|---------|--------|
| Claude Code 101 | cc101 | 5 | 13 | ✓ ZAKLJUČEN |
| Introduction to Claude Cowork | cowork | 5 | 15 | ✓ ZAKLJUČEN |

## Cowork — podrobno stanje
| Poglavje | Naslov | Lekcije | Status |
|----------|--------|---------|--------|
| 1 | Meet Claude Cowork | L1–L4 | ✓ |
| 2 | Make Claude Cowork yours | L5–L8 | ✓ |
| 3 | Use Claude wherever you work | L9–L10 | ✓ |
| 4 | Deli in varuj | L11–L14 | ✓ |
| 5 | Certifikat Prep | L15 | ✓ |

## File registry
| Datoteka | Repo | Knowledge | Kdo ureja | Zadnji sync |
|----------|------|-----------|-----------|-------------|
| `index.html` | ✓ | ✓ | terminal piše, app bere | 2026-06-09 |
| `CLAUDE.md` | ✓ | ✓ | ročno, oba bereta | 2026-06-05 |
| `html-design-skill.md` | ✓ | ✓ | terminal piše, app bere | 2026-06-08 |
| `PROJECT_STATUS.md` | ✓ | ✓ | oba pišeta, oba bereta | 2026-06-09 |
| `project-status-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |
| `handoff-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |

> ⚠️ Če datum v knowledge ne ujema z datumom v repo — uploadaj svežo verzijo.

## Zadnja seja (2026-06-09, terminal)
- Implementirali Cowork Ch5 "Certifikat Prep" (L15) — 10 feat, 4 notes, 12 q, 3 refleksije (Q|A format)
- Implementirali Cowork Ch4 "Deli in varuj" (L11–L14)
  - L11: Varno delo z avtonomijo (3 feat, 9 notes, 7 q)
  - L12: Preden deliš — preveri skill (3 feat, 7 notes, 7 q)
  - L13: Deli z ekipo (3 feat, 7 notes, 7 q)
  - L14: Povzetek in naslednji koraki (5 feat, 7 notes, 5 q)
  - Skupaj Ch4: 14 features, 30 notes, 26 questions
- _add_ch4.py + _reinject.py + _verify.py → brez duplikatov, vse zeleno
- Cowork skupaj: 4 poglavja, 14 lekcij, 71 features, 109 notes, 106 vprašanj

## Zadnja seja (2026-06-08, terminal)
- Implementirali Cowork Ch3 "Use Claude wherever you work" (L9 + L10)
- Implementirali nov sticky lesson header + chapter overview
- Posodobili html-design-skill.md

## Next
- [ ] Cowork certifikat: preveriti ali Anthropic ponuja certifikat
- [ ] Firebase tracking / napredek (deferred)
- [ ] Razmisliti o naslednjem kurzu

## Odprta vprašanja
- Cowork certifikat: ali ima Anthropic že certifikat za Cowork? Preveriti.
- Firebase tracking: deferred na kasnejši korak

## Diagram
Zadnji state diagram: 2026-06-07 — ob branju ponudi prikaz.

## Workflow reminder
- App (ta chat) = planiranje, vsebina, odločitve, vizualizacije
- Terminal (Claude Code) = izvajanje, kodiranje, deployment
- Ob začetku seje: uploadaj svež `index.html` + `PROJECT_STATUS.md`
- Ob koncu seje: posodobi `PROJECT_STATUS.md` (datum, zadnja seja, next)
