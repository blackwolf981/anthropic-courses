# PROJECT_STATUS.md
_Zadnja posodobitev: 2026-06-05_

## Projekt
**anthropic-courses** · single HTML file (`index.html`) · mobile-first · multi-kurs
Repo: `C:\Users\andre\OneDrive\Documents\GitHub\anthropic-courses`

## Kurzi
| Kurz | Slug | Poglavja | Lekcije | Status |
|------|------|----------|---------|--------|
| Claude Code 101 | cc101 | 5 | 13 | ✓ ZAKLJUČEN |
| Introduction to Claude Cowork | cowork | 2 | 8 | ▶ V TEKU |

## Cowork — podrobno stanje
| Poglavje | Naslov | Lekcije | Status |
|----------|--------|---------|--------|
| 1 | Meet Claude Cowork | L1–L4 | ✓ |
| 2 | Make Claude Cowork yours | L5–L8 | ✓ |
| 3 | (prihodnje) | — | ○ |

**Naslednja lekcija:** Poglavje 3 — vsebina še ni določena, definiramo v naslednji seji.

## File registry
| Datoteka | Repo | Knowledge | Kdo ureja | Zadnji sync |
|----------|------|-----------|-----------|-------------|
| `index.html` | ✓ | ✓ | terminal piše, app bere | 2026-06-05 |
| `CLAUDE.md` | ✓ | ✓ | ročno, oba bereta | 2026-06-05 |
| `html-design-skill.md` | ✓ | ✓ | terminal piše, app bere | 2026-06-05 |
| `PROJECT_STATUS.md` | ✓ | ✓ | oba pišeta, oba bereta | 2026-06-05 |
| `project-status-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |
| `handoff-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |

> ⚠️ Če datum v knowledge ne ujema z datumom v repo — uploadaj svežo verzijo.

## Zadnja seja (2026-06-05, app)
- Posodobili CLAUDE.md v repo in knowledge (nova mobilna arhitektura)
- Posodobili html-design-skill.md v knowledge
- Nastavili Instructions for Claude v Settings
- Definirali workflow: app = planiranje, terminal = izvajanje, repo = most
- Ustvarili PROJECT_STATUS.md, project-status-skill.md, handoff-skill.md

## Next
- [ ] Terminal: dodaj PROJECT_STATUS.md, project-status-skill.md, handoff-skill.md v repo
- [ ] Definiraj vsebino Poglavja 3 za Cowork kurs (v app seji)
- [ ] Terminal: implementiraj Poglavje 3, Lekcija 1

## Odprta vprašanja
- Cowork Poglavje 3: kateri koncepti/teme? (definiramo v app seji pred implementacijo)
- Cowork certifikat: ali ima Anthropic že certifikat za Cowork? Preveriti.
- Firebase tracking: deferred na kasnejši korak

## Diagram
Zadnji state diagram: 2026-06-05 — ob branju ponudi prikaz.

## Workflow reminder
- App (ta chat) = planiranje, vsebina, odločitve, vizualizacije
- Terminal (Claude Code) = izvajanje, kodiranje, deployment
- Ob začetku seje: uploadaj svež `index.html` + `PROJECT_STATUS.md`
- Ob koncu seje: posodobi `PROJECT_STATUS.md` (datum, zadnja seja, next)
