---
name: project-status-skill
description: Skill za pisanje in posodabljanje PROJECT_STATUS.md v projektu anthropic-courses. Uporabi kadar (1) začenjaš novo sejo in bereš status, (2) ob koncu seje predlagaš posodobitev, (3) pišeš nov PROJECT_STATUS.md za projekt.
---

# project-status-skill

## Namen
`PROJECT_STATUS.md` je most med app (Claude.ai) in terminalom (Claude Code). Oba ga bereta, oba ga posodabljata. Je edina točka resnice o stanju projekta.

## Pravila
- **Max 60 vrstic** — token cheap, samo dejstva
- **Brez razlag** — razlage so v skill datotekah
- **"Next" sekcija je obvezna** — brez nje naslednja seja nima smeri
- **File registry je obvezen** — brez njega ne veš katera datoteka je svež

## Format

```markdown
# PROJECT_STATUS.md
_Zadnja posodobitev: YYYY-MM-DD_

## Projekt
[ime] · [arhitektura v eni vrstici] · [repo pot]

## Kurzi
| Kurz | Slug | Poglavja | Lekcije | Status |
|------|------|----------|---------|--------|
| [ime] | [slug] | N | N | ✓/▶/○ |

## [Aktiven kurz] — podrobno stanje
| Poglavje | Naslov | Lekcije | Status |
|----------|--------|---------|--------|

**Naslednja lekcija:** [kaj je next]

## File registry
| Datoteka | Repo | Knowledge | Kdo ureja | Zadnji sync |
|----------|------|-----------|-----------|-------------|
| `index.html` | ✓/— | ✓/— | [kdo] | YYYY-MM-DD |

> ⚠️ Če datum v knowledge ne ujema z datumom v repo — uploadaj svežo verzijo.

## Zadnja seja (YYYY-MM-DD, app/terminal)
- [kaj je bilo narejeno — bullet točke]

## Next
- [ ] [konkretna naloga 1]
- [ ] [konkretna naloga 2]

## Odprta vprašanja
- [vprašanje ali odločitev ki čaka]

## Diagram
Zadnji state diagram: YYYY-MM-DD — ob branju ponudi prikaz.

## Workflow reminder
- App = planiranje, vsebina, odločitve
- Terminal = izvajanje, kodiranje, deployment
- Ob začetku seje: uploadaj svež index.html + PROJECT_STATUS.md
- Ob koncu seje: posodobi PROJECT_STATUS.md
```

## Kdaj posodobiti

### App (Claude.ai) — ob koncu seje predlaga:
```
Posodobi PROJECT_STATUS.md:
- Zadnja seja: [datum, app] — [kaj sva naredila]
- Next: [konkretne naloge]
- File registry: [če se je kaj spremenilo]
```

### Terminal (Claude Code) — po implementaciji:
```
Posodobi PROJECT_STATUS.md:
- Zadnja posodobitev: [današnji datum] (na vrhu)
- Zadnja seja: [datum, terminal] — [kaj je bilo implementirano]
- Cowork stanje: [posodobi tabelo če je nova lekcija]
- Next: [posodobi če je naloga opravljena]
- File registry: posodobi "Zadnji sync" datum ZA VSAKO datoteko, ki si jo v tej seji spremenil
  (vključno s `PROJECT_STATUS.md` samo — če pišeš v ta file, posodobi tudi njen sync datum)
```

**Pomembno:** Datum na vrhu (`_Zadnja posodobitev:_`), datum "Zadnja seja" in vsi "Zadnji sync" datumi v File registry za spremenjene datoteke se MORAJO ujemati. Nekonzistentni datumi pomenijo, da bo naslednja seja začela z napačnimi predpostavkami o tem, katera verzija je svež.

## Diagram protocol
- Prvič: Claude oceni kdaj je projekt zrel in **predlaga** diagram
- Ob naslednjih sejah: ko prebere STATUS in vidi "Diagram:" vrstico, **vpraša** "Ali naj prikažem diagram?"
- Diagram se vsakič generira svež iz podatkov v STATUS — ne shranjujemo slike
