---
name: handoff-skill
description: Skill za pisanje handoff dokumentov — strukturiranih MD datotek, ki terminalu (Claude Code) jasno razložijo idejo, arhitekturo ali odločitev. Uporabi kadar (1) app in terminal morata komunicirati o kompleksni ideji, (2) terminal rabi kontekst za implementacijo ki ga ni mogoče opisati v kratkem promptu, (3) planiraš novo poglavje ali lekcijo za implementacijo.
---

# handoff-skill

## Namen
Handoff dokument je datoteka v repo, ki jo terminal prebere in takoj razume — brez dolgega tekstovnega prompta. App ga pripravi, terminal ga izvede.

## Kaj terminal razume
Terminal (Claude Code) bere besedilne datoteke. Razume:
- ✓ Markdown (.md) — struktura, tabele, koda, seznami
- ✓ JSON — sheme, podatkovne strukture
- ✓ HTML komentarji — tehnične opombe v kodi
- ✗ Rendered HTML — vidi kodo, ne vizualnega rezultata
- ✗ Slike — ne vidi vizualnih elementov
- ✗ Interaktivnost — razume logiko, ne izkušnje

## Format handoff dokumenta

```markdown
# HANDOFF: [naziv naloge]
_Datum: YYYY-MM-DD | Pripravil: app | Za: terminal_

## Cilj
[En stavek: kaj mora terminal narediti]

## Kontekst
[Zakaj to delamo — max 3 bullet točke]

## Stanje pred implementacijo
- Aktivni file: `index.html`
- Kurz: [slug] · Poglavje: N · Zadnja lekcija: LN
- Relevantni IDs: section max=[N], feature max=[N], note max=[N], question max=[N]

## Kar je treba narediti
### [Korak 1]
[Opis koraka]

### [Korak 2]
[Opis koraka]

## Vsebina za implementacijo
[JSON struktura ali tabela z vsebino]

## Preverjanje po implementaciji
- [ ] JSON valid
- [ ] ID-ji unikatni znotraj kurza
- [ ] Render deluje na mobilnem
- [ ] Vprašanja dodana (5–10)

## Opombe
[Kar ne sme iti narobe / znane pasti]
```

## Kdaj napisati handoff

Napiši handoff ko:
- Planiraš novo poglavje ali lekcijo (vsebina je kompleksna)
- Terminalу razlagaš arhitekturno odločitev
- Je naloga večkoračna in zahteva natančen vrstni red

Ne piši handoff ko:
- Je naloga enostavna (terminal jo razume iz kratkega prompta)
- Gre za popravek napake (direkten prompt je hitrejši)

## Lokacija v repo
```
anthropic-courses/
└── handoffs/
    └── HANDOFF_[datum]_[naziv].md
```

Terminal prebere: `"Preberi handoffs/HANDOFF_2026-06-05_cowork_pog3.md in implementiraj"`

## Primer — nova lekcija

```markdown
# HANDOFF: Cowork Poglavje 3 — Lekcija 1
_Datum: 2026-06-05 | Pripravil: app | Za: terminal_

## Cilj
Dodaj Lekcijo 1 v Poglavje 3 kurza "cowork" v index.html

## Stanje pred implementacijo
- Kurz: cowork · trenutno 2 poglavji, 8 lekcij
- Novo poglavje ID: 3, nova sekcija ID: začni od max+1

## Vsebina
[tabela z features, notes, questions]

## Preverjanje
- [ ] JSON valid
- [ ] IDs unikatni znotraj cowork kurza
- [ ] Render na 380px
- [ ] Min 5 vprašanj
```
