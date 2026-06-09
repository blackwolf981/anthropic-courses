# -*- coding: utf-8 -*-
# Dodaja Chapter 4 "Deli in varuj" v cowork kurs.
# IDs: features 58-71, notes 80-109, questions 81-106
import json

with open('_courses_migrated.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

chapter4 = {
    "id": 4,
    "title": "Deli in varuj",
    "objectives": [
        "Razloži, kako varno delati s Cowork v porazdeljenem delovnem okolju",
        "Preveri skill ali plugin, preden ga deliš z ekipo",
        "Poveži vse 4 module v svojo osebno Cowork prakso"
    ],
    "reflections": [
        "Katera varnostna navada bo najpomembnejša v tvojem delovnem okolju?",
        "Kateri skill ali plugin bi šel najprej v delitev z ekipo?",
        "Kaj je bil tvoj največji 'aha' moment v Cowork 101?"
    ],
    "sections": [
        {
            "id": 11,
            "lesson": 11,
            "title": "Lekcija 11: Varno delo z avtonomijo",
            "features": [
                {
                    "id": 58, "section_id": 11, "sort_order": 1,
                    "name": "Permission mode — Cowork vedno vpraša",
                    "icon": "ti-shield-check",
                    "badge_type": "caution", "badge_text": "pazi",
                    "short_desc": "Privzeto Cowork ne ukrepa brez odobritve pri občutljivih dejanjih",
                    "what_it_does": "Cowork deluje v stopnjah: samodejno za branje in analizo; odobritev pred izvedbo, pošiljanjem ali brisanjem; popolna blokada za kritične sistemske spremembe.",
                    "when_to_use": "Kadar daš Cowork dostop do datotek, e-pošte ali orodij — privzeto se ustavi preden ukrepa.",
                    "when_not": "Izklopi odobritev le za naloge, ki si jih že testiral/a in jim popolnoma zaupaš.",
                    "why_it_matters": "Avtonomni sistemi so močni. Nadzor ostane pri tebi — in tako mora biti."
                },
                {
                    "id": 59, "section_id": 11, "sort_order": 2,
                    "name": "Specifično navodilo > splošno",
                    "icon": "ti-pencil",
                    "badge_type": "when", "badge_text": "ključni koncept",
                    "short_desc": "Kako pišeš navodilo, določa, kaj Claude naredi",
                    "what_it_does": "Splošno navodilo ('počisti datoteke') pusti prostor za napačno interpretacijo obsega. Specifično navodilo ('arhiviraj PDF-je starejše od 90 dni v /Arhiv/2024') ne pusti.",
                    "when_to_use": "Vedno, ko naloga vključuje urejanje, brisanje ali pošiljanje — bodite eksplicitni glede obsega, mape in kriterijev.",
                    "when_not": "Pri nalogah za branje, analizo ali osnutke je splošno navodilo sprejemljivo — ne more povzročiti trajne škode.",
                    "why_it_matters": "Nejasno navodilo + avtonomno dejanje = nepričakovan izid. Specifično navodilo je tvoja zaščita."
                },
                {
                    "id": 60, "section_id": 11, "sort_order": 3,
                    "name": "Kdaj Cowork ni pravo orodje",
                    "icon": "ti-x",
                    "badge_type": "caution", "badge_text": "kdaj ne",
                    "short_desc": "Scenariji, kjer je ročni nadzor boljša izbira",
                    "what_it_does": "Cowork ni primeren, kadar: tveganje napake je nesprejemljivo (zaupni podatki, finančne transakcije brez nadzora); naloga je ad-hoc in se ne bo ponovila; obseg je nejasno definiran.",
                    "when_to_use": "Ko je tveganje majhno, naloga se ponavlja in znaš opisati jasne kriterije uspeha.",
                    "when_not": "Ko je naloga enkratna brez ponovitvene vrednosti ali ko so v igri zaupni podatki brez nadzornega protokola.",
                    "why_it_matters": "Dober presodek, kdaj delegirati in kdaj ne, je enako pomemben kot Cowork sam."
                }
            ],
            "notes": [
                {"id": 80, "section_id": 11, "note_type": "desc", "sort_order": -2,
                 "content": "Cowork deluje z avtonomijo — to je njegova moč. Ta lekcija pokrije, kako to moč usmeriti varno: kako nastaviš delovni prostor, kako pišeš navodila in kdaj se je bolje ustaviti in premisliti."},
                {"id": 81, "section_id": 11, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Nastavi delovni prostor varno"},
                {"id": 82, "section_id": 11, "note_type": "desc", "sort_order": 2,
                 "content": "Načelo: Claude ne more napraviti napake z nečim, do česar ne more dostopati. Preden daš Cowork nalogo, premisli: katera mapa, datoteka ali orodje je v dosegu?\n\n• Ustvari ločene mape za testiranje in produkcijo.\n• Daj dostop samo tistemu, kar je potrebno za to nalogo.\n• Za nove, nepreizkušene naloge začni z branjem — šele nato z ukrepanjem."},
                {"id": 83, "section_id": 11, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Prompt, ki ne pušča prostora za napako"},
                {"id": 84, "section_id": 11, "note_type": "desc", "sort_order": 4,
                 "content": "Primerjava:\n\n❌ **Splošno:** *Počisti stare datoteke na Drive-u.*\nClaude sam odloči, kaj je 'staro' in kaj 'čistenje'.\n\n✅ **Specifično:** *Arhiviraj PDF-je v mapi /Poročila starejše od 90 dni v /Arhiv/2024. Ne briši ničesar.*\nClaude ve natanko, kaj narediti — in česa ne."},
                {"id": 85, "section_id": 11, "note_type": "tip", "sort_order": 5,
                 "content": "Vzorec za varno navodilo: **Kaj** (arhiviraj/pošlji/posodobi) + **Kje** (katera mapa/datoteka) + **Kdaj** (kriterij: starejše od, s statusom X) + **Česa ne** (ne briši, ne pošlji brez potrditve)."},
                {"id": 86, "section_id": 11, "note_type": "subsection-header", "sort_order": 6,
                 "content": "Kdaj se ustavi in premisli"},
                {"id": 87, "section_id": 11, "note_type": "desc", "sort_order": 7,
                 "content": "Trije scenariji, kjer hitrost ni vrednota:\n\n1. **Zaupni podatki:** Ko naloga vključuje finančne, kadrovske ali strankine podatke — ne delegiraj brez pregleda.\n2. **Neponovljiva dejanja:** Ko brisanje, pošiljanje ali objavljanje ni enostavno razveljaviti.\n3. **Nejasno navodilo:** Ko nisi prepričan/a, kako bi Claude interpretiral tvojega navodila — preizkusi najprej z branjem."},
                {"id": 88, "section_id": 11, "note_type": "warning", "sort_order": 8,
                 "content": "**Porazdeljeni delovni tokovi:** Ko Cowork deluje kot del večjega pipeline-a (npr. Dispatch → Cowork → skupni Drive), premisli, kdo nadzira izhod in kdaj. Avtomatizacija brez pregleda je tveganje."}
            ],
            "questions": [
                {
                    "id": 81,
                    "q": "Kaj je privzeto obnašanje Cowork pri občutljivih dejanjih?",
                    "options": ["Samodejno izvede brez opozorila", "Pošlje e-poštno obvestilo", "Vpraša za odobritev preden ukrepa", "Blokira nalogo in zahteva geslo"],
                    "correct": 2,
                    "explanation": "Privzeto Cowork vpraša za dovoljenje pri občutljivih dejanjih — klik, pošiljanje, oddaja. Ti odobravaš ali zavrneš vsako dejanje."
                },
                {
                    "id": 82,
                    "q": "Zakaj je specifično navodilo varnejše od splošnega?",
                    "options": ["Ker Claude hitreje procesira specifična navodila", "Ker ne pušča prostora za napačno interpretacijo obsega ali kriterijev", "Ker Cowork zahteva specifičen format", "Ker splošnih navodil Cowork ne sprejme"],
                    "correct": 1,
                    "explanation": "Splošno navodilo pušča prostor za interpretacijo. Specifično navodilo določi natanko kaj, kje in česa ne — brez prostora za napako."
                },
                {
                    "id": 83,
                    "q": "Kateri primer navodila je VARNEJŠI?",
                    "options": ["'Počisti stare datoteke na Drive-u'", "'Arhiviraj PDF-je v mapi /Poročila starejše od 90 dni v /Arhiv/2024 — ne briši ničesar'", "'Uredi vse datoteke za ta teden'", "'Dodaj datoteke v Drive'"],
                    "correct": 1,
                    "explanation": "Specifično navodilo navede mapo, kriterij (starejše od 90 dni) in omejitev (ne briši) — brez prostora za napačno dejanje."
                },
                {
                    "id": 84,
                    "q": "Kateri scenarij je primeren za Cowork?",
                    "options": ["Posamična naloga, ki se ne bo ponovila", "Nejasno definirana naloga, kjer Cowork sam odloča o obsegu", "Ponavljajoča se naloga z jasnimi kriteriji in majhnim tveganjem", "Brisanje zaupnih finančnih podatkov brez nadzora"],
                    "correct": 2,
                    "explanation": "Cowork je najmočnejši za ponavljajoče se naloge z jasnimi kriteriji. Za visoko tveganje ali ad-hoc delo je ročni nadzor boljša izbira."
                },
                {
                    "id": 85,
                    "q": "Kateri so elementi varnega navodila?",
                    "options": ["Kaj + Kje + Kdaj + Česa ne", "Kdo + Kdaj + Zakaj + Kako", "Ime naloge + datum + ime mape", "Kateri model + kakšen format + kdo to bere"],
                    "correct": 0,
                    "explanation": "Varno navodilo vsebuje: Kaj (dejanje), Kje (mapa/datoteka), Kdaj (kriterij), in Česa ne (omejitve). To ne pušča prostora za napako."
                },
                {
                    "id": 86,
                    "q": "Kdaj je ročni nadzor boljša izbira kot Cowork?",
                    "options": ["Ko je naloga enostavna in kratka", "Ko naloga vključuje neponovljiva dejanja ali zaupne podatke brez nadzornega protokola", "Ko so datoteke v Drive-u", "Ko delaš z M365 aplikacijami"],
                    "correct": 1,
                    "explanation": "Neponovljiva dejanja (brisanje, pošiljanje) in zaupni podatki zahtevajo ročni pregled. Cowork ni primeren za visoko tvegane, enkratne naloge."
                },
                {
                    "id": 87,
                    "q": "Zakaj je 'ograjevanje' delovnega prostora dober varnostni ukrep?",
                    "options": ["Ker Claude dela hitreje z manj dostopa", "Ker Claude ne more napraviti napake z nečim, do česar ne more dostopati", "Ker Cowork zahteva minimalen dostop za delovanje", "Ker ograjevanje šifrira podatke"],
                    "correct": 1,
                    "explanation": "Načelo: Claude ne more napraviti napake z nečim, do česar ne more dostopati. Omeji dostop na to, kar je potrebno za nalogo."
                }
            ]
        },
        {
            "id": 12,
            "lesson": 12,
            "title": "Lekcija 12: Preden deliš — preveri skill",
            "features": [
                {
                    "id": 61, "section_id": 12, "sort_order": 1,
                    "name": "Zakaj je validacija nujna",
                    "icon": "ti-checkup-list",
                    "badge_type": "when", "badge_text": "ključni koncept",
                    "short_desc": "Preden zaupate, testirajte — preden delite, preverite",
                    "what_it_does": "Skill, ki ni bil testiran, je zaveza brez garancije. Eval sistem ti pove, ali skill dosega želen izpis, preden ga deliš ali vgradiš v workflow.",
                    "when_to_use": "Vedno, preden skill deliš z ekipo, vgradiš v plugin ali nastaviš kot del ponovljivega procesa.",
                    "when_not": "Za osebne, eksperimentalne skille, ki jih sam/a nadziraš — stroga validacija ni nujna.",
                    "why_it_matters": "Deljeni skill, ki ne deluje pravilno, škodi celotni ekipi — ne le avtorju."
                },
                {
                    "id": 62, "section_id": 12, "sort_order": 2,
                    "name": "Eval sistem v skill creator",
                    "icon": "ti-chart-bar",
                    "badge_type": "when", "badge_text": "kako deluje",
                    "short_desc": "Skill creator generira testne primere in primerja izpise",
                    "what_it_does": "Skill creator sprejme navodila skilla, generira serijo testnih vhodov in primerja izpis: tvoja pričakovanja vs. dejanski izpis. Razlike so vidne v poročilu.",
                    "when_to_use": "Ko si napisal/a navodila skilla in hočeš vedeti, ali Claude interpretira navodila tako, kot si nameril/a.",
                    "when_not": "Ko skill nima ponavljajočega se vzorca — eval je bolj koristen za procesne skille kot za odprte, kreativne naloge.",
                    "why_it_matters": "Eval naredi nevidno vidno — takoj vidiš, kje Claude razume navodilo in kje ne."
                },
                {
                    "id": 63, "section_id": 12, "sort_order": 3,
                    "name": "Iterativni cikel: test → prilagodi → ponovi",
                    "icon": "ti-refresh",
                    "badge_type": "when", "badge_text": "vzorec",
                    "short_desc": "Eval ni enkratno opravilo — zanke, dokler ne zadeneš",
                    "what_it_does": "Po prvem evalu preglej, kje izpis ne ustreza. Popravi navodilo — bolj specifično, jasnejši kriteriji, dodaj primer. Ponovi eval. Ponavljaj, dokler izpis ne ustreza pričakovanjem.",
                    "when_to_use": "Ko je prvi eval pokazal odstopanje med pričakovanjem in izpisom — to je normalen del razvoja skilla.",
                    "when_not": "Ko si zadovoljen/na z izpisom po vsakem testnem primeru — potem je skill ready.",
                    "why_it_matters": "Prompt engineering za skille je iterativen. En cikel redko zadene — trije so navada."
                }
            ],
            "notes": [
                {"id": 89, "section_id": 12, "note_type": "desc", "sort_order": -2,
                 "content": "Skill, ki si ga zgradil/a za sebe, je koristno orodje. Skill, ki ga deliš z ekipo brez validacije, je tveganje. Ta lekcija pokrije, kako preveriti skill, preden mu zaupaš — ali ga daš v roke kolegom."},
                {"id": 90, "section_id": 12, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Eval sistem v praksi"},
                {"id": 91, "section_id": 12, "note_type": "desc", "sort_order": 2,
                 "content": "Skill creator ti ponudi tri korake:\n\n1. **Testiraj skill** — generira 3–5 vzorčnih nalog, ki jih skill trdi, da zna rešiti.\n2. **Primerjaj izpis** — vsak testni izpis poleg tvojega pričakovanega izpisa ali referenčnega primera.\n3. **Oceni ujemanje** — barvna ocena: zelena (ujema se), rumena (blizu), rdeča (ne ujema)."},
                {"id": 92, "section_id": 12, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Iteracija do želenega izpisa"},
                {"id": 93, "section_id": 12, "note_type": "desc", "sort_order": 4,
                 "content": "Ko eval pokaže rdečo ali rumeno:\n\n1. Preberi navodilo skilla — kje je dvoumno?\n2. Popravi: dodaj primer, specificiraj format, opredeli izjeme.\n3. Ponovi eval — skill creator primerja staro in novo verzijo.\n4. Ponavljaj, dokler večina testnih primerov ne pokaže zelenega."},
                {"id": 94, "section_id": 12, "note_type": "tip", "sort_order": 5,
                 "content": "Pravilo za sprostitev skilla: ready za deljenje, ko 80 % testnih primerov pokaže zeleno in ni nobenega rdečega. Rumene so sprejemljive za odprte, kreativne naloge."},
                {"id": 95, "section_id": 12, "note_type": "warning", "sort_order": 6,
                 "content": "**Ne deli skilla, ki ni prestal vsaj enega eval cikla.** Ko kolegi zaupajo tvojemu skillu v avtomatiziranem workflow-u, neustrezni izpisi povzročijo napake pri vsakem zagonu — ne le enkrat."}
            ],
            "questions": [
                {
                    "id": 88,
                    "q": "Zakaj je validacija skilla nujna, preden ga deliš?",
                    "options": ["Ker Cowork zahteva ID certifikata", "Ker nevalidiran skill škodi celotni ekipi, ki mu zaupa", "Ker eval sistem samodejno deli skill po validaciji", "Ker brez validacije skill ne deluje v pluginu"],
                    "correct": 1,
                    "explanation": "Deljeni skill, ki ne deluje pravilno, povzroča napake pri vsakem zagonu — za vse, ki mu zaupajo."
                },
                {
                    "id": 89,
                    "q": "Kaj naredi eval sistem v skill creator?",
                    "options": ["Samodejno popravi navodila skilla", "Generira testne primere in primerja izpis s pričakovanji", "Objavi skill v marketplace", "Meri hitrost izpisa skilla"],
                    "correct": 1,
                    "explanation": "Eval sistem generira vzorčne naloge, Claude jih izvede, in primerja izpis z referenčnim primerom ali tvojim pričakovanjem."
                },
                {
                    "id": 90,
                    "q": "Kaj pomeni zelena ocena v eval sistemu?",
                    "options": ["Skill je objavljen v marketplace", "Izpis skilla se ujema s pričakovanim izpisom", "Skill potrebuje pregled upravljalca", "Skill je bil testiran vsaj 10-krat"],
                    "correct": 1,
                    "explanation": "Zelena pomeni, da se izpis skilla ujema s tvojim pričakovanim izpisom — skill deluje kot nameravano."
                },
                {
                    "id": 91,
                    "q": "Kateri je pravilen vrstni red razvoja skilla?",
                    "options": ["Objavi → Testiraj → Popravi", "Napiši navodila → Testiraj → Prilagodi → Ponovi", "Popravi → Objavi → Testiraj", "Testiraj → Objavi → Prilagodi"],
                    "correct": 1,
                    "explanation": "Pravi cikel: Napiši navodila → Testiraj z eval sistemom → Prilagodi navodilo → Ponovi eval — dokler ni izpis zadovoljiv."
                },
                {
                    "id": 92,
                    "q": "Kdaj je skill ready za deljenje z ekipo?",
                    "options": ["Ko si ga napisal/a in shranil/a", "Ko 80 % testnih primerov pokaže zeleno in ni nobenega rdečega", "Ko ga je odobril upravljalec", "Ko ga je testirala vsaj ena oseba"],
                    "correct": 1,
                    "explanation": "Praktično pravilo: 80 % zelenih in brez rdečih ocen. Rumene so sprejemljive za kreativne, odprte naloge."
                },
                {
                    "id": 93,
                    "q": "Za kakšne skille je eval sistem NAJMANJ koristen?",
                    "options": ["Procesne skille z jasnimi koraki", "Ponavljajoče se naloge z vzorčnim izpisom", "Odprte naloge brez jasnega pričakovanega izpisa", "Skille z več navodili"],
                    "correct": 2,
                    "explanation": "Eval sistem primerja izpis z referenčnim primerom — za odprte, kreativne naloge je težko definirati 'pravilen' izpis."
                },
                {
                    "id": 94,
                    "q": "Kaj narediš, ko eval pokaže rdečo oceno?",
                    "options": ["Izbriši skill in začni znova", "Preberi navodilo, poišči dvoumnost, popravi in ponovi eval", "Objavi skill z opozorilom", "Pošlji skill v Anthropic pregled"],
                    "correct": 1,
                    "explanation": "Rdeča ocena pomeni: preberi navodilo, poišči dvoumnost, popravi in ponovi eval — iteracija je normalen del razvoja."
                }
            ]
        },
        {
            "id": 13,
            "lesson": 13,
            "title": "Lekcija 13: Deli z ekipo",
            "features": [
                {
                    "id": 64, "section_id": 13, "sort_order": 1,
                    "name": "Dve poti distribucije",
                    "icon": "ti-arrows-split-2",
                    "badge_type": "when", "badge_text": "kdaj katero",
                    "short_desc": "Direktna delitev za testiranje; marketplace za produkcijo",
                    "what_it_does": "Direktna pot: izvozi skill kot ZIP in ga pošlji kolegom neposredno. Marketplace pot: objavi v team marketplace — vsi v organizaciji ga najdejo, namestijo in dobijo posodobitve samodejno.",
                    "when_to_use": "Direktna pot: za testiranje z eno osebo. Marketplace: ko je skill validiran in ga želi ekipa ali oddelek trajno.",
                    "when_not": "Ne objavljaj v marketplace skillов, ki niso prešli eval — samodejne posodobitve bodo dostavile napako vsem hkrati.",
                    "why_it_matters": "Marketplace je infrastruktura timskega znanja. Direktna delitev je za prototipe."
                },
                {
                    "id": 65, "section_id": 13, "sort_order": 2,
                    "name": "Marketplace ekipe",
                    "icon": "ti-store",
                    "badge_type": "when", "badge_text": "ključni koncept",
                    "short_desc": "Centraliziran katalog validiranih skillов in pluginov za organizacijo",
                    "what_it_does": "Team marketplace je zbirka validiranih skillов in pluginov, ki jih lastnik upravlja in organizacija namešča. Vsak kolegom dostopen skill je tam. Posodobitve so centralne.",
                    "when_to_use": "Ko skill ali plugin želi biti dostopen vsemu oddelku ali organizaciji — ne le eni osebi.",
                    "when_not": "Ko je plugin oseben ali eksperimentalen — ga drži v lokalnem delovnem prostoru.",
                    "why_it_matters": "Marketplace pretvori individualno znanje v organizacijsko infrastrukturo."
                },
                {
                    "id": 66, "section_id": 13, "sort_order": 3,
                    "name": "Dobre navade vzdrževanja skupnih skillов",
                    "icon": "ti-checklist",
                    "badge_type": "when", "badge_text": "vzorec",
                    "short_desc": "Skupni skill brez vzdrževanja zastara in povzroča napake",
                    "what_it_does": "Dobre navade: jasna konvencija poimenovanja, lastnik za vsak skill ali plugin, reden revizijski ritem (mesečno ali kvartalno), dokumentiran changelog za vsako posodobitev.",
                    "when_to_use": "Od prvega dne objave — vzdrževanje je del življenjskega cikla, ne naknadni dodatek.",
                    "when_not": "Za osebne, kratkotrajne skille vzdrževanje ni potrebno.",
                    "why_it_matters": "Skupni skill brez lastnika je napaka v nastajanju."
                }
            ],
            "notes": [
                {"id": 96, "section_id": 13, "note_type": "desc", "sort_order": -2,
                 "content": "Skill ali plugin, ki si ga zgradil/a, ima vrednost onkraj tvojega dela. Ta lekcija pokrije, kako ga prenesti ekipi — pravilno in trajno."},
                {"id": 97, "section_id": 13, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Poti distribucije"},
                {"id": 98, "section_id": 13, "note_type": "desc", "sort_order": 2,
                 "content": "**Direktna delitev (za testiranje):**\n• Izvozi skill kot ZIP iz Cowork → pošlji po e-pošti ali Slack.\n• Prejemnik ga namesti ročno v Cowork.\n• Posodobitve: nova datoteka, nova namestitev.\n\n**Team marketplace (za produkcijo):**\n• Lastnik objavi skill ali plugin v marketplace.\n• Ekipa ga najde in namesti z enim klikom.\n• Posodobitve so centralne — lastnik posodobi enkrat, vsi dobijo novo verzijo."},
                {"id": 99, "section_id": 13, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Dobre navade vzdrževanja"},
                {"id": 100, "section_id": 13, "note_type": "desc", "sort_order": 4,
                 "content": "Konvencija poimenovanja:\n• `[ekipa]-[namen]-[verzija]` — npr. `finance-variance-v2`\n• Jasno ime prepreči duplikate in olajša iskanje v marketplace.\n\nRevizijski ritem:\n• Mesečno: ali skill še deluje? Ali se je Cowork spremenil?\n• Kvartalno: ali skill še ustrezno odraža naš proces?\n\nChangelog:\n• Kratka opomba ob vsaki posodobitvi — kaj se je spremenilo in zakaj."},
                {"id": 101, "section_id": 13, "note_type": "tip", "sort_order": 5,
                 "content": "Pravilo lastništva: vsak objavljeni skill ali plugin ima imenovanega lastnika. Brez lastnika = brez odgovornosti = zastaranje."},
                {"id": 102, "section_id": 13, "note_type": "warning", "sort_order": 6,
                 "content": "**Ne objavljaj v marketplace brez lastnika in verzije.** Ko skill dobiva posodobitve, morajo kolegi vedeti, kdo je odgovoren in kaj se je spremenilo — sicer posodobitev pride brez konteksta."}
            ],
            "questions": [
                {
                    "id": 95,
                    "q": "Katera distribucijska pot je primernejša za testiranje z eno osebo?",
                    "options": ["Team marketplace", "Direktna delitev (ZIP datoteka)", "Anthropic marketplace", "Dispatch pipeline"],
                    "correct": 1,
                    "explanation": "Direktna delitev (ZIP) je hitra in primerna za testiranje — marketplace je za produkcijsko distribucijo celotni ekipi."
                },
                {
                    "id": 96,
                    "q": "Kaj je team marketplace?",
                    "options": ["Spletna trgovina za nakup Cowork licenc", "Centraliziran katalog validiranih skillов in pluginov za organizacijo", "Anthropicov uradni katalog pluginov", "Zbirka brezplačnih skill predlog"],
                    "correct": 1,
                    "explanation": "Team marketplace je interna zbirka skillов in pluginov — lastnik upravlja, ekipa namešča z enim klikom, posodobitve so centralne."
                },
                {
                    "id": 97,
                    "q": "Katera konvencija poimenovanja je PRAVILNA za skill?",
                    "options": ["finance-variance-v2", "moj_skill_november", "skill123", "claude_plugin_final"],
                    "correct": 0,
                    "explanation": "Konvencija [ekipa]-[namen]-[verzija] je jasna in preprečuje duplikate — vsak takoj ve, kaj skill počne, kdo ga vzdržuje in katera verzija je."
                },
                {
                    "id": 98,
                    "q": "Kaj pomeni 'revizijski ritem' za skupni skill?",
                    "options": ["Pogostost dodajanja novih funkcij", "Reden pregled, ali skill še deluje pravilno in odraža aktualni proces", "Potrditveni postopek pred vsako uporabo", "Merjenje hitrosti izpisa"],
                    "correct": 1,
                    "explanation": "Revizijski ritem je redni pregled — mesečno (ali skill deluje?) in kvartalno (ali odraža aktualni proces?)."
                },
                {
                    "id": 99,
                    "q": "Zakaj je lastnik skilla oz. plugina ključen?",
                    "options": ["Ker Cowork zahteva lastnika za vsak objavljeni skill", "Ker brez lastnika ni odgovornosti — skill zastara brez posodobitev", "Ker lastnik dobiva nadomestilo", "Ker samo lastnik ga sme uporabljati"],
                    "correct": 1,
                    "explanation": "Skupni skill brez lastnika je napaka v nastajanju — nihče ni odgovoren za posodobitve, ko se proces ali Cowork spremenita."
                },
                {
                    "id": 100,
                    "q": "Kdaj uporabiš marketplace namesto direktne delitve?",
                    "options": ["Ko testiraš skill z eno osebo", "Ko je skill validiran in ga želi trajno nameščena celotna ekipa ali oddelek", "Ko je skill eksperimentalen", "Ko skill ni prestal eval sistema"],
                    "correct": 1,
                    "explanation": "Marketplace je za produkcijsko distribucijo — ko je skill validiran in ga želi trajno nameščena celotna ekipa."
                },
                {
                    "id": 101,
                    "q": "Kaj vsebuje dober changelog ob posodobitvi skilla?",
                    "options": ["Ime avtorja in datum rojstva", "Kratka opomba, kaj se je spremenilo in zakaj", "Celotno besedilo navodil skilla", "Seznam vseh uporabnikov, ki ga imajo nameščenega"],
                    "correct": 1,
                    "explanation": "Dober changelog je kratka, jasna opomba o spremembi in razlogu — dovolj za kolege, da razumejo posodobitev."
                }
            ]
        },
        {
            "id": 14,
            "lesson": 14,
            "title": "Lekcija 14: Povzetek in naslednji koraki",
            "features": [
                {
                    "id": 67, "section_id": 14, "sort_order": 1,
                    "name": "Modul 1: Spoznal/a si Cowork",
                    "icon": "ti-player-play",
                    "badge_type": "when", "badge_text": "povzetek",
                    "short_desc": "Kaj je Cowork, kako se razlikuje, kaj zmore, prva naloga",
                    "what_it_does": "Spoznal/a si delegiranje kot drugačen miselni model — ne 'vprašaj Claude', ampak 'delegiraj Claude'. Opišeš izid, Cowork naredi načrt, izvede in vrne dokončan deliverable.",
                    "when_to_use": "Ko imaš nalogo z več koraki, jasnim izhodom in vrednostjo ponovitve.",
                    "when_not": "Za razmišljanje, brainstorming in kratke odgovore — Chat ostaja najboljša izbira.",
                    "why_it_matters": "Delegiranje je ključni miselni preskok. Kdor ga naredi, od Cowork dobi desetkrat več."
                },
                {
                    "id": 68, "section_id": 14, "sort_order": 2,
                    "name": "Modul 2: Prilagodil/a si Cowork",
                    "icon": "ti-settings",
                    "badge_type": "when", "badge_text": "povzetek",
                    "short_desc": "Global instructions, projects, skills, plugins — 4 gradniki",
                    "what_it_does": "Naučil/a si se, kako Cowork uči o tebi (global instructions), o tvojem delu (projects), o tvojih procesih (skills) in o strokovnem znanju tvoje ekipe (plugins).",
                    "when_to_use": "Vsak gradnik ima svojo vlogo — skupaj tvorijo kontekst, ki naredi Cowork boljšega in hitrejšega z vsakim novim deliverable.",
                    "when_not": "Ni treba začeti z vsemi štirimi — začni z global instructions in enim projektom.",
                    "why_it_matters": "Compound efekt: več Cowork ve o tebi in tvojem delu, boljši in hitrejši so deliverables."
                },
                {
                    "id": 69, "section_id": 14, "sort_order": 3,
                    "name": "Modul 3: Claude povsod",
                    "icon": "ti-world",
                    "badge_type": "when", "badge_text": "povzetek",
                    "short_desc": "Chrome za brskalniška orodja; M365 znotraj Office dokumentov",
                    "what_it_does": "Odkril/a si dve razširitvi: Claude v Chromu za orodja brez Cowork priključka, in Claude za M365 znotraj Word, Excel, PowerPoint in Outlook — en pogovor, štiri aplikacije.",
                    "when_to_use": "Chrome: ko orodje živi v brskalniku brez priključka. M365: ko si v Office datoteki in hočeš Clauda tam, ne v ločenem oknu.",
                    "when_not": "Ko ima orodje Cowork priključek — ga uporabi neposredno, brskalnik ni potreben.",
                    "why_it_matters": "Claude se prikaže povsod, kjer delaš — ne le v eni aplikaciji."
                },
                {
                    "id": 70, "section_id": 14, "sort_order": 4,
                    "name": "Modul 4: Deli in varuj",
                    "icon": "ti-share",
                    "badge_type": "when", "badge_text": "povzetek",
                    "short_desc": "Varno, validirano, organizacijsko — trije stebri",
                    "what_it_does": "Naučil/a si se, kako delati z avtonomijo varno (permission mode, specifični prompti), kako preveriti skill pred deljenjem (eval sistem, iterativni cikel), in kako ga prenesti ekipi (marketplace, navade vzdrževanja).",
                    "when_to_use": "Ko je skill ali plugin validiran in ready za ekipo — ne prej.",
                    "when_not": "Ne deli pred validacijo. Ne zanemari vzdrževanja po objavi.",
                    "why_it_matters": "Osebni workflow → timska infrastruktura. To je največja vrednost Cowork."
                },
                {
                    "id": 71, "section_id": 14, "sort_order": 5,
                    "name": "Naprej: tvoja akcijska lista",
                    "icon": "ti-checklist",
                    "badge_type": "when", "badge_text": "naslednji korak",
                    "short_desc": "Pet konkretnih akcij za naslednji teden",
                    "what_it_does": "1. Napiši global instructions — kdo si in kako delaš.\n2. Ustvari projekt za enega od tvojih delovnih tokov.\n3. Zgradi skill za en ponavljajoč se proces.\n4. Preizkusi Chrome ali M365 na realni nalogi.\n5. Deli en skill ali plugin z eno osebo in zberi povratno informacijo.",
                    "when_to_use": "Takoj — danes. Vsak korak sam po sebi že prinese vrednost.",
                    "when_not": "Ne čakaj, da 'prideš do tega' ali da se naučiš še več. Akcija je učitelj.",
                    "why_it_matters": "Znanje brez prakse izgine. Akcija to prepreči."
                }
            ],
            "notes": [
                {"id": 103, "section_id": 14, "note_type": "desc", "sort_order": -2,
                 "content": "Prišel/a si do konca Cowork 101. V štirih modulih si prešel/a od prvega srečanja s Cowork do tega, da znaš varno delegirati, graditi in deliti svojo Cowork prakso."},
                {"id": 104, "section_id": 14, "note_type": "subsection-header", "sort_order": 1,
                 "content": "Preizkusi zdaj"},
                {"id": 105, "section_id": 14, "note_type": "desc", "sort_order": 2,
                 "content": "Pet akcij za naslednji teden:\n\n1. **Global instructions** — odpri Cowork in napiši, kdo si in kako delaš. Vzame 10 minut, prinese vrednost pri vsaki naslednji nalogi.\n2. **Projekt** — ustvari projekt za en delovni tok (marketing, finance, strankina podpora).\n3. **Skill** — identificiraj en ponavljajoč se proces in ga zapiši kot skill.\n4. **Chrome ali M365** — preizkusi na eni realni nalogi iz tvojenga vsakodnevnega dela.\n5. **Deli** — pošlji en skill kolegom in zberi povratno informacijo."},
                {"id": 106, "section_id": 14, "note_type": "subsection-header", "sort_order": 3,
                 "content": "Poglobi znanje"},
                {"id": 107, "section_id": 14, "note_type": "desc", "sort_order": 4,
                 "content": "Priporočeni naslednji kurzi:\n\n• **AI Fluency: Framework & Foundations** — razumevanje AI modelov in zmogljivosti\n• **AI Capabilities and Limitations** — kaj AI zna in česa ne\n• **Claude 101** — spremljevalni kurz za osnove dela z AI asistentom\n• **Claude use-case library** — konkretni primeri za tvojo panogo"},
                {"id": 108, "section_id": 14, "note_type": "tip", "sort_order": 5,
                 "content": "Daj nam povratno informacijo: Kaj je bilo v Cowork 101 najbolj koristno? Kaj bi izboljšal/a? Tvoje mnenje oblikuje naslednji kurz."},
                {"id": 109, "section_id": 14, "note_type": "desc", "sort_order": 6,
                 "content": "**Hvala, ker si bil/a z nami.** Cowork 101 je le začetek — pravi napredek pride z vajo. Delegiraj, ne le vprašaj. Gradaj, ne le beri. Deli, ne le shrani."}
            ],
            "questions": [
                {
                    "id": 102,
                    "q": "Kateri je NAJPOMEMBNEJŠI prvi korak po zaključku kurza?",
                    "options": ["Namestiti vse plugine iz marketplace", "Napisati global instructions — kdo si in kako delaš", "Zgraditi 10 skillов v prvem tednu", "Preizkusiti vse funkcije pred deljenjem"],
                    "correct": 1,
                    "explanation": "Global instructions je temeljni gradnik — Cowork takoj ve, kdo si in kako delaš, kar izboljša vsak naslednji deliverable."
                },
                {
                    "id": 103,
                    "q": "Kateri modul je poučeval o 4 gradnikih (global instructions, projects, skills, plugins)?",
                    "options": ["Modul 1: Spoznaj Cowork", "Modul 2: Prilagodi Cowork", "Modul 3: Claude povsod", "Modul 4: Deli in varuj"],
                    "correct": 1,
                    "explanation": "Modul 2 je pokrival vse 4 gradnike, ki Cowork-u dajo kontekst — o tebi, tvojem delu, tvojih procesih in znanju ekipe."
                },
                {
                    "id": 104,
                    "q": "Kaj je bil ključni miselni preskok v Modulu 1?",
                    "options": ["Claude je boljši od ChatGPT", "Cowork deluje le z API-jem", "Iz 'vprašaj Claude' v 'delegiraj Claude'", "Global instructions zamenjajo prompting"],
                    "correct": 2,
                    "explanation": "Modul 1 je poudaril preskok: ne vprašaj Claude za odgovor — delegiraj Claude celotno nalogo z jasnim izhodom."
                },
                {
                    "id": 105,
                    "q": "Kako Chrome in M365 skupaj razširita Cowork?",
                    "options": ["Chrome zamenja Cowork, M365 zamenja Chat", "Chrome za orodja brez priključka; M365 za delo znotraj Office dokumentov", "Chrome za video vsebino, M365 za besedilo", "Oba sta le za Enterprise naročnike"],
                    "correct": 1,
                    "explanation": "Chrome odklene brskalniška orodja brez priključka. M365 prinese Clauda v Word, Excel, PowerPoint in Outlook — skupaj Claude deluje povsod, kjer delaš."
                },
                {
                    "id": 106,
                    "q": "Kaj je največja vrednost deljenja skillов in pluginov z ekipo?",
                    "options": ["Prihranek pri Cowork naročnini", "Osebni workflow postane timska infrastruktura", "Hitrejši eval sistem", "Samodejni changelog"],
                    "correct": 1,
                    "explanation": "Ko deliš skill z ekipo, se osebno znanje in proces preneseta v skupno infrastrukturo — vsi imajo koristi od tvojega dela."
                }
            ]
        }
    ]
}

# Find cowork course and add chapter 4
cowork = next((c for c in courses if c.get('slug') == 'cowork'), None)
if not cowork:
    print('ERROR: cowork kurs ni najden!')
    exit(1)

existing_ids = [ch['id'] for ch in cowork['chapters']]
if 4 in existing_ids:
    print('ERROR: Chapter 4 že obstaja! ID-ji:', existing_ids)
    exit(1)

cowork['chapters'].append(chapter4)

with open('_courses_migrated.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, ensure_ascii=False, separators=(',', ':'))

print('OK: Chapter 4 dodan v cowork kurs.')
print(f'Cowork ima zdaj {len(cowork["chapters"])} poglavij.')
sections = chapter4['sections']
for s in sections:
    print(f'  - Section {s["id"]}: {s["title"]} | {len(s["features"])} features, {len(s["notes"])} notes, {len(s["questions"])} questions')
