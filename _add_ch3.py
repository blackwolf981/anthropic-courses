# -*- coding: utf-8 -*-
import json

with open('_courses_migrated.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

chapter3 = {
    "id": 3,
    "title": "Use Claude wherever you work",
    "objectives": [
        "Prepoznaj vrste dela, ki jih Claude v Chromu odklene",
        "Poveži Chrome in Cowork v eno nalogo",
        "Prepoznaj, kaj Claude naredi znotraj Word, Excel, PowerPoint in Outlook",
        "Prenesi delo med M365 aplikacijami z enim pogovorom",
        "Odloči, kdaj uporabiš Cowork in kdaj Claude znotraj dokumenta"
    ],
    "reflections": [
        "V katerih brskalniških orodjih v svojem delu ni Cowork priključka?",
        "Katera M365 aplikacija bi ti prinesla največ, če bi v njej imel Claudea?",
        "Kje v svojem tednu bi Chrome + Cowork rešil eno ročno nalogo?"
    ],
    "sections": [
        {
            "id": 9,
            "lesson": 9,
            "title": "Lekcija 9: Claude in Chrome",
            "features": [
                {
                    "id": 46, "section_id": 9, "sort_order": 1,
                    "name": "Most za brskalniška orodja",
                    "icon": "ti-plug-connected",
                    "badge_type": "when", "badge_text": "kdaj to pride prav",
                    "short_desc": "Claude v Chromu bere in ukrepa na spletnih straneh brez priključka",
                    "what_it_does": "Claude odpre spletno stran, prebere vsebino, klikne in navigira — vse v Chromu. Deluje na vsakem orodju, ki živi v brskalniku, pa naj ima API ali ne.",
                    "when_to_use": "Ko orodje živi v brskalniku in nima Cowork priključka — Tableau, CRM, interni portali, nabavni sistemi.",
                    "when_not": "Ko orodje ima Cowork priključek — takrat ga použij neposredno, brez brskalnika.",
                    "why_it_matters": "Večina poslovnih orodij nima API-ja. Chrome je most, ki jih vse odklene."
                },
                {
                    "id": 47, "section_id": 9, "sort_order": 2,
                    "name": "Chrome in Cowork skupaj",
                    "icon": "ti-arrows-split-2",
                    "badge_type": "when", "badge_text": "kombinacija",
                    "short_desc": "Claude zbere podatke v Chromu, deliverable zgradi v Cowork",
                    "what_it_does": "Claude deluje na obeh površinah v istem pogovoru — v Chromu bere in ukrepa, v Cowork gradi deliverable iz zbranih podatkov.",
                    "when_to_use": "Ko naloga zahteva podatke iz brskalniških orodij in konča z deliverable v Cowork — povzetek strank, analiza tekmovalcev, poročilo.",
                    "when_not": "Ko so vsi viri že v Cowork priključkih — brskalnik ni potreben.",
                    "why_it_matters": "Ena delegacija, dve površini, en pogovor. Brez copy-paste, brez menjave zavihkov."
                },
                {
                    "id": 48, "section_id": 9, "sort_order": 3,
                    "name": "Notranje nadzorne plošče",
                    "icon": "ti-layout-dashboard",
                    "badge_type": "when", "badge_text": "kje deluje",
                    "short_desc": "Tableau, Looker, BI orodja — Claude jih prebere in prenese v Cowork",
                    "what_it_does": "Claude odpre interno nadzorno ploščo, izvleče metrike in prenese podatke v Cowork naloge — brez ročnega copy-paste.",
                    "when_to_use": "Ko metrike živijo v Tableau ali Looker in jih vsak teden rabiš za poročilo ali Cowork nalogo.",
                    "when_not": "Ko so podatki dostopni prek API-ja ali Cowork priključka — ga uporabi neposredno.",
                    "why_it_matters": "BI orodja so polna podatkov, ki jih potrebuješ, a nimajo API-ja. Chrome jih odklene."
                },
                {
                    "id": 49, "section_id": 9, "sort_order": 4,
                    "name": "Portali brez API-ja",
                    "icon": "ti-building-store",
                    "badge_type": "when", "badge_text": "kje deluje",
                    "short_desc": "CRM, nabavni portali, sistemi za enotno prijavo — brez priključka",
                    "what_it_does": "Claude se orientira po portalu, izvleče kar potrebuješ in ukrepa tako, kot bi ti — triažira tickete, navigira, povleče podatke.",
                    "when_to_use": "Ko nabavni portal nima API-ja. Ko CRM zahteva ročno triažo. Ko sistem strank živi za enotno prijavo.",
                    "when_not": "Ko sistem ima Cowork priključek — takrat ga uporabi neposredno.",
                    "why_it_matters": "Večina podjetij ima vsaj en tak sistem. Chrome jih vse odklene."
                },
                {
                    "id": 50, "section_id": 9, "sort_order": 5,
                    "name": "Spletne aplikacije za prijavo",
                    "icon": "ti-lock-open",
                    "badge_type": "when", "badge_text": "kje deluje",
                    "short_desc": "Vsaka spletna aplikacija, ki zahteva prijavo, postane scriptable",
                    "what_it_does": "Claude deluje v seji, ki si jo ti vzpostavil. Ne potrebuje tvojega gesla — dela v obstoječi seji brskalnika.",
                    "when_to_use": "Ko si prijavljen v orodje in hočeš, da Claude naredi nalogo namesto tebe, brez da mu daš geslo.",
                    "when_not": "Ko nisi prijavljen — Claude se ne more prijaviti sam.",
                    "why_it_matters": "Varne aplikacije za prijavo ostanejo varne. Claude dela le v seji, ki si jo sam vzpostavil."
                },
                {
                    "id": 51, "section_id": 9, "sort_order": 6,
                    "name": "Ostaneš v nadzoru",
                    "icon": "ti-hand-stop",
                    "badge_type": "caution", "badge_text": "pazi",
                    "short_desc": "Za občutljiva dejanja Claude vedno vpraša za odobritev",
                    "what_it_does": "Privzeto Claude pred vsakim občutljivim dejanjem — klik, pošiljanje, oddaja — vpraša za dovoljenje. Vsako dejanje odobravaš ali zavrneš.",
                    "when_to_use": "Vedno — to je privzeto obnašanje, ki te ščiti pred nepričakovanimi dejanji.",
                    "when_not": "Ne izključuj tega brez razloga — kontrola je tvoja zaščita.",
                    "why_it_matters": "Avtomatizacija v brskalniku je močna. Nadzor ostane pri tebi."
                }
            ],
            "notes": [
                {"id": 64, "section_id": 9, "note_type": "desc", "sort_order": -3,
                 "content": "Claude v Chromu je most za orodja, ki živijo v brskalniku in nimajo Cowork priključka. Bere, klikne in navigira po straneh — v istem pogovoru, kjer Cowork gradi deliverable."},
                {"id": 65, "section_id": 9, "note_type": "youtube", "sort_order": -2,
                 "content": "IypXvHej9eY"},
                {"id": 66, "section_id": 9, "note_type": "tip", "sort_order": -1,
                 "content": "Vzorec: kadar pomisliš »bi dal Claude-u ta kontekst, a je na spletu« — Claude v Chromu je odgovor."},
                {"id": 67, "section_id": 9, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Primer z Cowork"},
                {"id": 68, "section_id": 9, "note_type": "desc", "sort_order": 2,
                 "content": "V Cowork napišeš: *Odpri nadzorno ploščo zdravja strank v Chromu, izvleči vse račune z rdečo ali rumeno oznako, in za vsakega povleči aktivnost zadnjih 30 dni iz mape v Drive in iz #customer-success v Slack. Zgradi enostransko povzetek za moj petkov klic.*\n\nClaude preda naloge Chromu, povleče podatke, poveže kontekst iz Drive in Slack, in zgradi povzetek v tvoji mapi."},
                {"id": 69, "section_id": 9, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Pazi na"},
                {"id": 70, "section_id": 9, "note_type": "warning", "sort_order": 4,
                 "content": "**Prijava je tvoja stvar.** Claude se ne more prijaviti v orodje namesto tebe. Najprej se prijavi sam — Claude dela v seji, ki si jo vzpostavil."},
                {"id": 71, "section_id": 9, "note_type": "warning", "sort_order": 5,
                 "content": "**Bodi premišljen glede dostopa.** Claude ima dostop do vsega, kar je odprto v Chromu. Za občutljive strani preglej dejanja pred odobritvijo."}
            ],
            "questions": [
                {
                    "id": 65,
                    "q": "Za kaj primarno uporabiš Claude v Chromu?",
                    "options": [
                        "Za zamenjavo Cowork priključkov",
                        "Za orodja v brskalniku, ki nimajo Cowork priključka",
                        "Za urejanje HTML kode spletnih strani",
                        "Za hitrejše brskanje po spletu"
                    ],
                    "correct": 1,
                    "explanation": "Claude v Chromu je most za orodja brez priključka — bere, klikne in navigira po spletnih straneh."
                },
                {
                    "id": 66,
                    "q": "Ali se Claude v Chromu lahko prijavi v orodje namesto tebe?",
                    "options": [
                        "Da, Claude shrani gesla varno",
                        "Da, prek varnega tunela",
                        "Ne, dela le v seji, ki si jo sam vzpostavil",
                        "Odvisno od nastavitev varnosti"
                    ],
                    "correct": 2,
                    "explanation": "Claude ne more prijaviti sam — dela v obstoječi seji brskalnika, ki si jo ti vzpostavil."
                },
                {
                    "id": 67,
                    "q": "Kaj se zgodi, ko Claude hoče narediti občutljivo dejanje v Chromu?",
                    "options": [
                        "Samodejno ga izvede, da ne izgublja časa",
                        "Pošlje e-poštno opozorilo",
                        "Blokira nalogo in čaka na pomoč",
                        "Privzeto te vpraša za odobritev"
                    ],
                    "correct": 3,
                    "explanation": "Za občutljiva dejanja Claude privzeto vpraša za dovoljenje — ti odobravaš ali zavrneš vsako dejanje."
                },
                {
                    "id": 68,
                    "q": "Kako Chrome in Cowork delujeta skupaj v istem pogovoru?",
                    "options": [
                        "Zamenjata drug drugega za različne naloge",
                        "Chrome nadomesti Cowork priključke",
                        "Claude zbira podatke v Chromu, deliverable gradi v Cowork",
                        "Cowork nadzira Chrome v ozadju"
                    ],
                    "correct": 2,
                    "explanation": "Ena delegacija, dve površini: Chrome za branje in ukrepanje, Cowork za gradnjo deliverable."
                },
                {
                    "id": 69,
                    "q": "Kateri primer je najboljši za Claude v Chromu?",
                    "options": [
                        "Pisanje e-pošte v Gmailu",
                        "Izvlek metrik iz interne Tableau plošče brez API-ja",
                        "Upravljanje datotek v Google Drive",
                        "Pošiljanje sporočil v Slack"
                    ],
                    "correct": 1,
                    "explanation": "Tableau nadzorne plošče nimajo Cowork priključka — Chrome je most za branje in prenašanje teh metrik."
                },
                {
                    "id": 70,
                    "q": "Kdaj je Claude v Chromu napačna izbira?",
                    "options": [
                        "Ko je orodje za prijavo",
                        "Ko orodje živi na spletu",
                        "Ko orodje ima Cowork priključek",
                        "Ko je stran v tujem jeziku"
                    ],
                    "correct": 2,
                    "explanation": "Če orodje ima Cowork priključek, ga uporabi neposredno — Chrome je most le za orodja brez priključka."
                },
                {
                    "id": 71,
                    "q": "Kaj pomeni vzorec za Claude v Chromu?",
                    "options": [
                        "Zberi podatke in jih copiraj v Excel",
                        "Kadar pomisliš »bi dal Claude-u ta kontekst, a je na spletu« — Chrome je odgovor",
                        "Odpri Cowork in čakaj na ukaz",
                        "Namesti vtičnik za vsako stran posebej"
                    ],
                    "correct": 1,
                    "explanation": "Kadar koli imaš kontekst na spletu, ki bi ga Claude potreboval, je Claude v Chromu pravi most."
                },
                {
                    "id": 72,
                    "q": "Katera vrsta portala je idealna za Claude v Chromu?",
                    "options": [
                        "Portal z Cowork priključkom",
                        "Portal s polnim REST API-jem",
                        "CRM portal brez API-ja, ki zahteva ročno triažo",
                        "Portal z GraphQL vmesnikom"
                    ],
                    "correct": 2,
                    "explanation": "CRM in drugi portali brez API-ja so natanko tisto, za kar je Claude v Chromu narejen."
                }
            ]
        },
        {
            "id": 10,
            "lesson": 10,
            "title": "Lekcija 10: Claude for Microsoft 365",
            "features": [
                {
                    "id": 52, "section_id": 10, "sort_order": 1,
                    "name": "Claude znotraj dokumenta",
                    "icon": "ti-file-text",
                    "badge_type": "when", "badge_text": "kdaj to pride prav",
                    "short_desc": "Claude kot add-in v Word, Excel, PowerPoint in Outlook",
                    "what_it_does": "Claude se prikaže kot add-in znotraj Office aplikacij — dela neposredno na datoteki, ki jo imaš odprto, ne v ločenem oknu.",
                    "when_to_use": "Ko si že v Office dokumentu in hočeš Claudea, ki razume kontekst tega dokumenta — ne le odgovarja na splošna vprašanja.",
                    "when_not": "Ko naloga zahteva podatke iz več virov in konča z novim deliverable — takrat je Cowork boljša izbira.",
                    "why_it_matters": "Claude pride k tebi — ne menjavaš zavihkov, ne copijaš vsebine. Dela na datoteki, ki jo imaš odprto."
                },
                {
                    "id": 53, "section_id": 10, "sort_order": 2,
                    "name": "Excel: analiza in formule",
                    "icon": "ti-table",
                    "badge_type": "when", "badge_text": "v Excelu",
                    "short_desc": "Analizira podatke, piše formule, debugira #REF! napake",
                    "what_it_does": "Claude analizira podatke, piše kompleksne formule, debugira napake in izvaja scenarijska testiranja — ne da bi pokvaril model.",
                    "when_to_use": "Najmočnejša poteza: *Povleči dejanske vrednosti iz lista Q3, jih primerjaj s planom Q3 v istem zvezku, in zapiši komentar o varianci v stolpec F ob vsaki vrstici.*",
                    "when_not": "Ko potrebuješ podatke iz zunanjega vira, ki ni v zvezku — takrat Cowork ali Chrome.",
                    "why_it_matters": "Formule in analiza so srce Excela. Claude jih piše, debugira in razloži — brez ročne intervencije."
                },
                {
                    "id": 54, "section_id": 10, "sort_order": 3,
                    "name": "PowerPoint: diapozitivi in grafikoni",
                    "icon": "ti-presentation",
                    "badge_type": "when", "badge_text": "v PowerPointu",
                    "short_desc": "Prebere slide master in ustvari usklajene native diapozitive",
                    "what_it_does": "Claude prebere obstoječ slide master, pisave in barvno shemo, nato gradi ustrezne diapozitive z native, urljivimi grafikoni — ne prilepljene slike.",
                    "when_to_use": "Najmočnejša poteza: *Vzemi analizo, ki sem jo naredil v Excelu, in jo pretvori v tri diapozitive za QBR po naši predlogi.*",
                    "when_not": "Ko diapozitiv ne potrebuje podatkov — morda hitreje ročno.",
                    "why_it_matters": "Grafikoni so native in urljivi. Claude gradi diapozitive, ki jih ti urejaš dalje."
                },
                {
                    "id": 55, "section_id": 10, "sort_order": 4,
                    "name": "Word: pisanje in urejanje",
                    "icon": "ti-file-description",
                    "badge_type": "when", "badge_text": "v Wordu",
                    "short_desc": "Osnutki, revizije, preoblikovanje — s sledenimi izmenami",
                    "what_it_does": "Claude piše, revidira in preoblikuje besedilo na mestu. Dela s komentarji in sledenimi izmenami. Vleka kontekst iz priključenih virov za utemeljitev osnutka.",
                    "when_to_use": "Najmočnejša poteza: *Napiši izvršilni povzetek na podlagi telesa tega memoranduma in izvornih podatkov v dodatku.*",
                    "when_not": "Ko je dokument v končni obliki in potrebuješ le formatiranje — morda hitreje ročno.",
                    "why_it_matters": "Word dokumenti redko nastanejo iz nič. Claude doda kontekst iz tvojih virov in gradi na tistem, kar že imaš."
                },
                {
                    "id": 56, "section_id": 10, "sort_order": 5,
                    "name": "Outlook: e-pošta s kontekstom",
                    "icon": "ti-mail",
                    "badge_type": "when", "badge_text": "v Outlooku",
                    "short_desc": "Triažira pošto in gradi odgovore z delovnim kontekstom",
                    "what_it_does": "Claude pride v Outlook z kontekstom iz celotnega tvojega dela — prejšnjih sporočil, koledarja in nedavnih odločitev.",
                    "when_to_use": "Ko moraš triažirati dolgo verigo in napisati odgovor, ki odraža celoten delovni kontekst — ne le to e-pošto.",
                    "when_not": "Ko je e-pošta rutinska in ne zahteva konteksta — hitreje ročno.",
                    "why_it_matters": "E-poštni odgovori so pogosto zapleteni. Claude ve, kaj se je dogajalo — ne začne od nič."
                },
                {
                    "id": 57, "section_id": 10, "sort_order": 6,
                    "name": "Cowork ali M365?",
                    "icon": "ti-scale",
                    "badge_type": "caution", "badge_text": "pametna odločitev",
                    "short_desc": "Preprosto pravilo za pravi kontekst",
                    "what_it_does": "Cowork, ko delo izhaja iz več virov in konča z deliverable. M365, ko si v Office datoteki in hočeš, da Claude uredi tam in prenese kontekst med aplikacijami.",
                    "when_to_use": "Cowork: gradnja briefa iz 20 datotek in 3 Slack kanalov. M365: odpri Excel, refiniraj model, prenesi v PowerPoint.",
                    "when_not": "Ni treba izbirati — večina resnega dela uporablja oba: Cowork za sestavine, M365 za rafinirani produkt.",
                    "why_it_matters": "Ne gre za tekmovanje — Claude se prikaže, kjer si. Obe površini delujeta skupaj."
                }
            ],
            "notes": [
                {"id": 72, "section_id": 10, "note_type": "youtube", "sort_order": -2,
                 "content": "F6dzjaBCBtU"},
                {"id": 73, "section_id": 10, "note_type": "desc", "sort_order": -1,
                 "content": "Claude se prikaže kot add-in znotraj Word, Excel, PowerPoint in Outlook — dela na datoteki, ki jo imaš odprto, in prenaša kontekst med aplikacijami v istem pogovoru."},
                {"id": 74, "section_id": 10, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Prenesi delo med aplikacijami"},
                {"id": 75, "section_id": 10, "note_type": "desc", "sort_order": 2,
                 "content": "En pogovor, štiri aplikacije:\n\n• **Outlook → Word:** E-pošta pristane v nabiralniku. *Odpri brief v Wordu in začni memo po naši predlogi.* Word se odpre — Claude ve, kaj je pošiljatelj zahteval.\n• **Word → Excel:** *Zgradi model tržnega obsega na podlagi predpostavk v memo.* Excel izvleče predpostavke in zgradi večtabularni model s formulami.\n• **Excel → PowerPoint:** *Pretvori to v upravljalni odbor po predlogi naše stranke.* Deck se zgradi s native grafikoni iz Excela.\n• **PowerPoint → Outlook:** *Najdi 30 minut s ekipo do četrtka.* Povabilo se pripravi z udeleženci in čaka, da ga pošlješ."},
                {"id": 76, "section_id": 10, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Kdaj Cowork, kdaj M365?"},
                {"id": 77, "section_id": 10, "note_type": "desc", "sort_order": 4,
                 "content": "Preprosto pravilo:\n\n• **Cowork:** Ko delo izhaja iz več virov in konča z deliverable — brief iz 20 datotek, poročilo iz Salesforce in Slack kanalov.\n• **M365:** Ko si v Office datoteki in hočeš, da Claude uredi tam in prenese kontekst v naslednjo aplikacijo.\n\nVečina resnega dela uporablja oba — Cowork za sestavine, M365 za rafinirani produkt."},
                {"id": 78, "section_id": 10, "note_type": "tip", "sort_order": 5,
                 "content": "**Preizkusi zdaj:** Namesti Claude add-in za M365 aplikacijo, ki jo največ uporabljaš. Odpri pravo datoteko in poskusi eno potezo — refiniraj formulo, zgradi diapozitiv iz odstavka, ali napiši odgovor na e-pošto."},
                {"id": 79, "section_id": 10, "note_type": "tip", "sort_order": 6,
                 "content": "**Naslednji korak:** Claude se pojavi povsod — v Chromu, v M365, v Cowork. Poglavje 4 se obrne k temu, kako zagotoviti, da je delo, ki ga naredi, dobro."}
            ],
            "questions": [
                {
                    "id": 73,
                    "q": "Kje se Claude prikaže v Microsoft 365?",
                    "options": [
                        "Samo v Outlooku",
                        "V vseh Office aplikacijah kot spletna storitev",
                        "Kot add-in znotraj Word, Excel, PowerPoint in Outlook",
                        "Samo v Excel in Word"
                    ],
                    "correct": 2,
                    "explanation": "Claude se prikaže kot add-in v vseh štirih Office aplikacijah — Word, Excel, PowerPoint in Outlook."
                },
                {
                    "id": 74,
                    "q": "Katera je najmočnejša poteza Clauda v Excelu?",
                    "options": [
                        "Samodejno pošiljanje poročil po e-pošti",
                        "Primerjava dejanskih vrednosti Q3 s planom in komentar variance po vrsticah",
                        "Uvoz podatkov iz interneta v realnem času",
                        "Prikaz Tableau grafikonov v Excelu"
                    ],
                    "correct": 1,
                    "explanation": "Claude v Excelu je najmočnejši pri navzkrižnem primerjanju in pisanju komentarjev variance — vse v istem zvezku."
                },
                {
                    "id": 75,
                    "q": "Kdaj je Cowork boljša izbira kot Claude v M365?",
                    "options": [
                        "Ko delaš v Excelu",
                        "Ko pišeš e-pošto v Outlooku",
                        "Ko naloga izhaja iz več virov in konča z deliverable",
                        "Ko imaš odprt PowerPoint"
                    ],
                    "correct": 2,
                    "explanation": "Cowork je prava izbira, ko zbiraš podatke iz 20+ datotek in gradaš nov deliverable. M365 je za rafinirano delo v dokumentih."
                },
                {
                    "id": 76,
                    "q": "Kaj naredi Claude v Outlooku?",
                    "options": [
                        "Pošilja e-pošto samodejno brez potrditve",
                        "Bere e-pošto in se uči tvojih navad",
                        "Triažira pošto in gradi odgovore z delovnim kontekstom",
                        "Organizira mape in filtre"
                    ],
                    "correct": 2,
                    "explanation": "Claude v Outlooku ve za prejšnje niti, koledar in nedavne odločitve — gradi odgovore, ki odražajo celoten kontekst."
                },
                {
                    "id": 77,
                    "q": "Ali Claude v M365 prenaša kontekst med aplikacijami?",
                    "options": [
                        "Ne, vsaka aplikacija je ločena seja",
                        "Da, en pogovor nosi kontekst skozi vse 4 Office aplikacije",
                        "Samo med Word in Outlook",
                        "Samo med Excel in PowerPoint"
                    ],
                    "correct": 1,
                    "explanation": "Ena pogovorna seja prenaša kontekst: iz Outlooka v Word, iz Worda v Excel, iz Excela v PowerPoint — in nazaj."
                },
                {
                    "id": 78,
                    "q": "Kakšen je ključni razloček med Claude v M365 in Claude v Cowork?",
                    "options": [
                        "M365 je hitrejši, Cowork je pametnejši",
                        "M365 za rafinirano delo v dokumentih; Cowork za gradnjo deliverables iz več virov",
                        "M365 dela brez interneta, Cowork zahteva internet",
                        "M365 je za podjetja, Cowork za posameznike"
                    ],
                    "correct": 1,
                    "explanation": "Obe sta močni, a za različne momente: M365 za urejanje v dokumentu, Cowork za sestavne deliverable."
                },
                {
                    "id": 79,
                    "q": "Kakšne grafikone Claude ustvari v PowerPointu?",
                    "options": [
                        "Prilepljene slike iz spleta",
                        "PDF izvozi iz Excela",
                        "Native, urljive grafikone — ne prilepljene slike",
                        "Statične tabele iz besedila"
                    ],
                    "correct": 2,
                    "explanation": "Claude ustvari native, urljive grafikone — ki jih ti urejaš dalje."
                },
                {
                    "id": 80,
                    "q": "Kaj pomeni »en pogovor, štiri aplikacije«?",
                    "options": [
                        "Hkrati odpri vse 4 Office aplikacije",
                        "En Claudeov pogovor nosi kontekst skozi Word, Excel, PowerPoint in Outlook",
                        "Pošlji isto sporočilo v vse 4 aplikacije",
                        "Claude nadzira 4 ločene seje hkrati"
                    ],
                    "correct": 1,
                    "explanation": "En pogovor nosi kontekst skozi vse aplikacije — ni treba začeti znova ali kopirati besedila med njimi."
                }
            ]
        }
    ]
}

# Find cowork course and add chapter 3
cowork = next((c for c in courses if c.get('slug') == 'cowork'), None)
if not cowork:
    print('ERROR: cowork kurs ni najden!')
    exit(1)

existing_ids = [ch['id'] for ch in cowork['chapters']]
if 3 in existing_ids:
    print('ERROR: Chapter 3 že obstaja! ID-ji:', existing_ids)
    exit(1)

cowork['chapters'].append(chapter3)

with open('_courses_migrated.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, ensure_ascii=False, separators=(',', ':'))

print('OK: Chapter 3 dodan v cowork kurs.')
print(f'Cowork ima zdaj {len(cowork["chapters"])} poglavij.')
sections = chapter3['sections']
for s in sections:
    print(f'  - Section {s["id"]}: {s["title"]} | {len(s["features"])} features, {len(s["notes"])} notes, {len(s["questions"])} questions')
