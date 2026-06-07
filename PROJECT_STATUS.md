# PROJECT_STATUS.md
_Zadnja posodobitev: 2026-06-07_

## Projekt
**anthropic-courses** · single HTML file (`index.html`) · mobile-first · multi-kurs
Repo: `C:\Users\andre\OneDrive\Documents\GitHub\anthropic-courses`

## Kurzi
| Kurz | Slug | Poglavja | Lekcije | Status |
|------|------|----------|---------|--------|
| Claude Code 101 | cc101 | 5 | 13 | ✓ ZAKLJUČEN |
| Introduction to Claude Cowork | cowork | 3 | 10 | ▶ V TEKU |

## Cowork — podrobno stanje
| Poglavje | Naslov | Lekcije | Status |
|----------|--------|---------|--------|
| 1 | Meet Claude Cowork | L1–L4 | ✓ |
| 2 | Make Claude Cowork yours | L5–L8 | ✓ |
| 3 | Use Claude wherever you work | L9–L10 | ✓ |
| 4 | (prihodnje) | — | ○ |

**Naslednja lekcija:** Poglavje 4 — vsebina še ni določena, definiramo v naslednji seji.

## File registry
| Datoteka | Repo | Knowledge | Kdo ureja | Zadnji sync |
|----------|------|-----------|-----------|-------------|
| `index.html` | ✓ | ✓ | terminal piše, app bere | 2026-06-07 |
| `CLAUDE.md` | ✓ | ✓ | ročno, oba bereta | 2026-06-05 |
| `html-design-skill.md` | ✓ | ✓ | terminal piše, app bere | 2026-06-05 |
| `PROJECT_STATUS.md` | ✓ | ✓ | oba pišeta, oba bereta | 2026-06-07 |
| `project-status-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |
| `handoff-skill.md` | ✓ | — | app predlaga, terminal shrani | 2026-06-05 |

> ⚠️ Če datum v knowledge ne ujema z datumom v repo — uploadaj svežo verzijo.

## Zadnja seja (2026-06-07, terminal)
- Implementirali Cowork Ch3 "Use Claude wherever you work" (L9 + L10)
- L9: Claude in Chrome (YT: IypXvHej9eY) — 6 features, 8 notes, 8 questions
- L10: Claude for Microsoft 365 (YT: F6dzjaBCBtU) — 6 features, 8 notes, 8 questions
- Vsebina iz PDF-jev v projektni mapi
- Workflow: _add_ch3.py → _reinject.py → _verify.py (0 duplikatov)

## Next
- [ ] Definiraj vsebino Poglavja 4 za Cowork kurs (v naslednji seji)
- [ ] Terminal: implementiraj Poglavje 4

## Odprta vprašanja
- Cowork Poglavje 4: kateri koncepti/teme? (definiramo v naslednji seji)
- Cowork certifikat: ali ima Anthropic že certifikat za Cowork? Preveriti.
- Firebase tracking: deferred na kasnejši korak

## Diagram
Zadnji state diagram: 2026-06-07 — ob branju ponudi prikaz.

## Workflow reminder
- App (ta chat) = planiranje, vsebina, odločitve, vizualizacije
- Terminal (Claude Code) = izvajanje, kodiranje, deployment
- Ob začetku seje: uploadaj svež `index.html` + `PROJECT_STATUS.md`
- Ob koncu seje: posodobi `PROJECT_STATUS.md` (datum, zadnja seja, next)
