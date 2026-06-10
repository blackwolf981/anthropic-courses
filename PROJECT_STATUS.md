# PROJECT_STATUS.md
_Zadnja posodobitev: 2026-06-09_

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

**Cowork skupaj:** 5 poglavij · 15 lekcij · 81 features · 113 notes · 118 vprašanj

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
- Implementirali Cowork Ch4 "Deli in varuj" (L11–L14) — _add_ch4.py
- Implementirali Cowork Ch5 "Certifikat Prep" (L15) — _add_ch5_cowork.py
  - 10 ref kartic · 4 notes · 12 scenario vprašanj · 3 refleksije (Q|A format)
- Cowork skupaj: 5 poglavij, 15 lekcij, 81 features, 113 notes, 118 vprašanj
- _reinject.py + _verify.py → brez duplikatov, vse zeleno (index.html 340 KB)

## Next
- [ ] Preveriti ali Anthropic ponuja certifikat za Cowork
- [ ] Firebase tracking / napredek (deferred)
- [ ] Odločiti kateri kurz je naslednji

## Odprta vprašanja
- Cowork certifikat: ali Anthropic ponuja uradni certifikat?
- Firebase tracking: deferred na kasnejši korak

## Diagram
Zadnji state diagram: 2026-06-07 — ob branju ponudi prikaz.

## Workflow reminder
- App = planiranje, vsebina, odločitve
- Terminal = izvajanje, kodiranje, deployment
- Ob začetku seje: uploadaj svež `index.html` + `PROJECT_STATUS.md`
- Ob koncu seje: posodobi `PROJECT_STATUS.md`
