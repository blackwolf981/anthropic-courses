# -*- coding: utf-8 -*-
# Dodaja Chapter 5 "Certifikat Prep" v cowork kurs.
# IDs: features 72-81, notes 110-113, questions 107-118, section 15
import json

with open('_courses_migrated.json', 'r', encoding='utf-8') as f:
    courses = json.load(f)

chapter5 = {
    "id": 5,
    "title": "Certifikat Prep",
    "objectives": [
        "Imeti vse ključne koncepte Cowork 101 na enem mestu za hitro ponovitev pred izpitom",
        "Razumeti kritične razlike med podobnimi koncepti, ki se pogosto zamenjujejo",
        "Prepoznati najpogostejše pasti in napačne odgovore na certifikatskem izpitu",
        "Zaključiti tečaj z zanesljivim, celostnim razumevanjem Claude Cowork"
    ],
    "reflections": [
        "Kakšna je ključna razlika med skillom in pluginom?|Skill uči Claude, KAKO narediti en specifičen proces — je reusable playbook. Plugin pakira več skills skupaj z connectors in know-how za cel delovni tok — skills so gradniki, plugin je end-to-end rešitev za distribucijo ekipi.",
        "Kdaj je Cowork napačna izbira?|Ko je naloga enkratna brez ponovitvene vrednosti, ko je tveganje napake visoko brez nadzornega protokola (zaupni podatki, neponovljiva dejanja), ali ko je obseg nejasno definiran. Dobra delegacija zahteva jasen izid, ponovitveno vrednost in majhno tveganje.",
        "Katera je razlika med direktno deljenim skillom in marketplace objavo?|Direktna delitev (ZIP) je za testiranje — ročna namestitev, ročne posodobitve, ena oseba. Marketplace je za produkcijo — centralna namestitev, samodejne posodobitve, lastnik odgovoren za vzdrževanje za celotno ekipo."
    ],
    "sections": [
        {
            "id": 15,
            "lesson": 15,
            "title": "Quick Reference: Vse na enem mestu",
            "features": [
                {
                    "id": 72, "section_id": 15, "sort_order": 1,
                    "name": "Cowork vs Chat vs Code",
                    "icon": "ti-scale",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Trije načini, tri vloge — pravi izbor za vsako nalogo",
                    "what_it_does": "Chat: vprašanja, brainstorming, kratki odgovori — interaktivno, brez avtonomije. Cowork: delegiranje celotne naloge z deliverable — autonomno, multi-step, dostop do orodij in datotek. Code: pisanje in debugiranje kode v razvojnem okolju.",
                    "when_to_use": "Cowork: ko imaš nalogo z več koraki, jasnim izhodom in vrednostjo ponovitve. Chat: ko hočeš dialog ali hiter odgovor, ne delegacijo.",
                    "when_not": "Ne delegiraj Cowork enkratnih ad-hoc poizvedb — tam je Chat hitrejši in primeren.",
                    "why_it_matters": "Pravi način za pravo nalogo je temeljna odločitev. Zmotna izbira pomeni ali preveč ali premalo moči."
                },
                {
                    "id": 73, "section_id": 15, "sort_order": 2,
                    "name": "Permission mode",
                    "icon": "ti-shield-check",
                    "badge_type": "caution", "badge_text": "referenca",
                    "short_desc": "Tri stopnje avtonomije — privzeta je varna",
                    "what_it_does": "Privzeto: Claude vpraša za odobritev pri občutljivih dejanjih (pošiljanje, brisanje, oddaja). Razširjeno: samodejno za preizkušene in zaupane naloge. Blokirano: samo branje in analiza, brez urejanja.",
                    "when_to_use": "Privzeto za vsako novo nalogo. Razširi šele, ko je naloga preizkušena, ponovljiva in ji popolnoma zaupaš.",
                    "when_not": "Nikoli ne razširi dovoljenja za naloge z zaupnimi podatki, finančnimi transakcijami ali neponovljivimi dejanji.",
                    "why_it_matters": "Permission mode je tvoja prva obrambna linija. Privzeto je varna — sprememba je tvoja odgovornost."
                },
                {
                    "id": 74, "section_id": 15, "sort_order": 3,
                    "name": "Global instructions",
                    "icon": "ti-user",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Kdo si in kako delaš — enkrat napiši, vedno velja",
                    "what_it_does": "Global instructions so aktivne v vsakem pogovoru in projektu. Vključujejo: tvojo vlogo in odgovornosti, stil komuniciranja, preference glede izpisa, jezikovne nastavitve, kontekst ekipe in dela.",
                    "when_to_use": "Za informacije, ki so resnične v vsakem kontekstu — niso vezane na en projekt ali delovni tok.",
                    "when_not": "Ne vključuj zaupnih podatkov, gesel ali API ključev. Ne vključuj informacij, ki so resnične le v enem projektu — to gre v projekt.",
                    "why_it_matters": "Global instructions so Coworkova osnova — brez njih Claude začne vsakič od nič, brez konteksta o tebi."
                },
                {
                    "id": 75, "section_id": 15, "sort_order": 4,
                    "name": "Projects",
                    "icon": "ti-folder",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Kontekst enega delovnega toka — datoteke, zgodovina, odločitve",
                    "what_it_does": "Projekt hrani: specifičen kontekst tega delovnega toka (datoteke, protokoli, pretekle odločitve), zgodovino nalog, skills in plugins vezane na ta kontekst. Ločen od global instructions.",
                    "when_to_use": "Ko delaš ponavljajoče se delo na enem področju — finance, marketing, strankina podpora. En projekt = en delovni tok.",
                    "when_not": "Ne vključuj informacij, ki veljajo za vse projekte — to gre v global instructions.",
                    "why_it_matters": "Global instructions = kdo si. Project = v čem delaš zdaj. Skupaj dajta Cowork celoten kontekst."
                },
                {
                    "id": 76, "section_id": 15, "sort_order": 5,
                    "name": "Skills — struktura in trigger",
                    "icon": "ti-book",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Navodila + assets — sproži se samodejno, ko je relevantno",
                    "what_it_does": "Skill ima dve komponenti: Instructions (kaj, kdaj, kako — trigger pogoj in postopek) in Assets (predloge, primeri, referenčni materiali). Cowork skill samodejno prepozna in aktivira, ko je naloga relevantna — brez eksplicitnega klica.",
                    "when_to_use": "Za vsak ponavljajoč se proces z jasnimi koraki in pričakovanim izpisom — poročilo, analiza, komunikacija s stranko.",
                    "when_not": "Ne piši skilla za enkratno nalogo. Ne deli skilla brez vsaj enega eval cikla.",
                    "why_it_matters": "Skill je reusable playbook — enkrat napišeš, stokrat izvajaš brez ponovnega razlage."
                },
                {
                    "id": 77, "section_id": 15, "sort_order": 6,
                    "name": "Plugins — dve obliki",
                    "icon": "ti-plug-connected",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "End-to-end proces ali paket skillов — ekspertiza ekipe v enem",
                    "what_it_does": "Oblika 1 — End-to-end proces: skills za vsak korak skupaj v en delovni tok (npr. monthly-close plugin). Oblika 2 — Paket skillов: set neodvisnih skills, ki jih ekipa najpogosteje dosega skupaj (npr. finance plugin). Plugin = skills + connectors + know-how.",
                    "when_to_use": "Ko hočeš distribuirati znanje ekipi kot paket — ne kot posamezne skille, ki jih vsak namesti posebej.",
                    "when_not": "Ne ustvari plugina iz enega samega skilla — za to zadostuje skill.",
                    "why_it_matters": "Skill uči Claude postopek. Plugin pakira postopke in connectors ter jih naredi dostopne ekipi kot infrastrukturo."
                },
                {
                    "id": 78, "section_id": 15, "sort_order": 7,
                    "name": "Eval sistem — cikel validacije",
                    "icon": "ti-refresh",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Test → prilagodi → ponovi — dokler ni 80 % zeleno, 0 % rdeče",
                    "what_it_does": "Eval sistem v skill creator: generira testne primere → Claude jih izvede → barvna ocena (zelena/rumena/rdeča). Cikel: preberi navodilo → poišči dvoumnost → popravi → ponovi eval. Ready: 80 % zeleno, 0 % rdeče.",
                    "when_to_use": "Vedno preden skill deliš z ekipo, vgradiš v plugin ali nastaviš kot del avtomatiziranega workflow-a.",
                    "when_not": "Za osebne, eksperimentalne skille, ki jih sam/a nadziraš in ne distribuiraš.",
                    "why_it_matters": "Nevalidiran deljeni skill je napaka pri vsakem zagonu — za celotno ekipo, ne le enkrat."
                },
                {
                    "id": 79, "section_id": 15, "sort_order": 8,
                    "name": "Claude v Chromu",
                    "icon": "ti-brand-chrome",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "Most za brskalniška orodja brez Cowork priključka",
                    "what_it_does": "Claude odpre spletno stran, bere vsebino, klikne in navigira — v istem pogovoru, kjer Cowork gradi deliverable. Dela v obstoječi seji brskalnika (ne more se prijaviti sam). Privzeto vpraša za odobritev pred občutljivimi dejanji.",
                    "when_to_use": "Ko orodje živi v brskalniku in nima Cowork priključka — Tableau, CRM portali, interni sistemi za enotno prijavo.",
                    "when_not": "Ko orodje ima Cowork priključek — ga uporabi neposredno, brez brskalnika.",
                    "why_it_matters": "Večina poslovnih orodij nima API-ja. Chrome jih vse odklene za Cowork delegacijo."
                },
                {
                    "id": 80, "section_id": 15, "sort_order": 9,
                    "name": "Claude za M365",
                    "icon": "ti-apps",
                    "badge_type": "when", "badge_text": "referenca",
                    "short_desc": "En pogovor, štiri aplikacije — Word, Excel, PowerPoint, Outlook",
                    "what_it_does": "Claude kot add-in znotraj Office aplikacij: Excel (formule, analiza, variance po vrsticah), PowerPoint (native grafikoni, slide master), Word (osnutki, sledene izmene), Outlook (triaža z delovnim kontekstom). En pogovor nosi kontekst skozi vse štiri aplikacije.",
                    "when_to_use": "Ko si v Office datoteki in hočeš Clauda tam — dela na datoteki, ki jo imaš odprto, ne v ločenem oknu.",
                    "when_not": "Ko naloga zahteva podatke iz več virov in konča z novim deliverable — takrat je Cowork boljša izbira.",
                    "why_it_matters": "Claude pride k tebi — ne menjavaš zavihkov, ne copijaš vsebine med aplikacijami."
                },
                {
                    "id": 81, "section_id": 15, "sort_order": 10,
                    "name": "Varno delegiranje — formula",
                    "icon": "ti-lock-check",
                    "badge_type": "caution", "badge_text": "referenca",
                    "short_desc": "Kaj + Kje + Kdaj + Česa ne — štirje elementi varnega navodila",
                    "what_it_does": "Štirje elementi: Kaj (konkretno dejanje — arhiviraj, pošlji, posodobi), Kje (mapa, datoteka ali orodje), Kdaj (kriterij: starejše od X, s statusom Y, brez oznake Z), Česa ne (ne briši, ne pošlji brez potrditve). Plus: nastavi minimalen dostop, ogradi delovni prostor.",
                    "when_to_use": "Vsakič, ko navodilo vključuje urejanje, brisanje, pošiljanje ali oddajanje — vsako dejanje, ki ni enostavno razveljaviti.",
                    "when_not": "Za navodila branja in analize — tam splošno navodilo zadostuje, ker ne more povzročiti trajne škode.",
                    "why_it_matters": "Nejasno navodilo + avtonomno dejanje = nepričakovan izid. Formula to prepreči z eksplicitnimi mejami."
                }
            ],
            "notes": [
                {"id": 110, "section_id": 15, "note_type": "desc", "sort_order": -2,
                 "content": "Ta lekcija je tvoj kompaktni pregled pred certifikatom. Vsaka kartica povzema ključni koncept kurza — preden začneš izpit, preberi vsako in se prepričaj, da razumeš razlike, ne le definicije."},
                {"id": 111, "section_id": 15, "note_type": "tip", "sort_order": -1,
                 "content": "Certifikatski izpit testira razumevanje konceptov in razlik med njimi — ne zapomnitve definicij. Fokusiraj se na: kdaj Cowork, kdaj Chat; skill vs plugin; global instructions vs project; Chrome vs M365; direktna delitev vs marketplace."},
                {"id": 112, "section_id": 15, "note_type": "subsection-header", "sort_order": 10,
                 "content": "Najpogostejše pasti na izpitu"},
                {"id": 113, "section_id": 15, "note_type": "warning", "sort_order": 11,
                 "content": "<strong>Tri pasti:</strong> (1) Skill in plugin nista zamenljiva — skill je postopek, plugin je paket postopkov za ekipo. (2) Global instructions in project nista isti zadevi — global velja povsod, project le v enem delovnem toku. (3) Chrome ni nadomestek za Cowork priključek — Chrome je most le za orodja BREZ priključka."}
            ],
            "questions": [
                {
                    "id": 107,
                    "q": "Hočeš, da Claude vsak ponedeljek samodejno obdela prodajno poročilo. Katera Cowork funkcija to omogoči?",
                    "options": ["Chat prompt vsak ponedeljek ročno", "Dispatch — načrtovana naloga s časovnim sproženjem", "Global instructions z urnikom nalog", "Plugin za poročila brez urnika"],
                    "correct": 1,
                    "explanation": "Dispatch je Cowork funkcija za načrtovane, ponavljajoče se naloge — določiš urnik, Claude nalogo izvede samodejno ob pravem času."
                },
                {
                    "id": 108,
                    "q": "Kolega ti pošlje skill ZIP brez opisa. Kaj je PRVI korak?",
                    "options": ["Namesti takoj in preizkusi v produkciji", "Zavrni — brez opisa skill ni zaupanja vreden", "Preizkusi v eval sistemu in preberi navodila preden namestiš", "Pošlji Anthropic v pregled"],
                    "correct": 2,
                    "explanation": "Preden namestiš tuj skill v produkcijo, ga preizkusi v eval sistemu in preberi navodila — ugotovi, kaj počne in ali deluje kot pričakovano."
                },
                {
                    "id": 109,
                    "q": "Imaš CRM sistem brez API-ja. Hočeš, da Claude triažira tickete in rezultate doda v Cowork nalogo. Katera funkcija to omogoči?",
                    "options": ["Cowork plugin za CRM", "Claude v Chromu — bere in navigira brez priključka", "Global instructions z CRM navodili", "M365 Outlook connector"],
                    "correct": 1,
                    "explanation": "Claude v Chromu odpre CRM v brskalniku, bere tickete in navigira — brez API-ja ali priključka. Rezultate prenese v Cowork nalogo."
                },
                {
                    "id": 110,
                    "q": "Si v Excelu in hočeš primerjati dejanske vrednosti Q3 s planom ter dodati komentar variance v stolpec F. Katera orodja je najprimernejša?",
                    "options": ["Cowork naloga z Excel prilogo", "Chat z Excel prilogo", "Claude za M365 znotraj Excela", "Python skill v Cowork"],
                    "correct": 2,
                    "explanation": "Claude za M365 dela neposredno v odprtem Excel zvezku — piše formule, primerja podatke in dodaja komentarje variance brez menjave zavihkov."
                },
                {
                    "id": 111,
                    "q": "Tvoj skill ima 60 % zelenih in 20 % rdečih eval ocen. Kaj narediš?",
                    "options": ["Objavi z opozorilom o znanih napakah", "Deli direktno — kolegi bodo sporočili, kje ne deluje", "Popravi navodila, ponovi eval — ne deli pred 0 % rdečih", "Začni skill pisati znova od nič"],
                    "correct": 2,
                    "explanation": "20 % rdečih pomeni: skill ni ready. Popravi dvoumno besedilo v navodilih, ponovi eval. Deli šele, ko dosežeš 80 % zelenih in 0 % rdečih."
                },
                {
                    "id": 112,
                    "q": "Katera informacija SPADA v global instructions in katera v projekt?",
                    "options": ["Global: ime projekta; Projekt: tvoja vloga", "Global: kdo si in kako delaš (povsod resnično); Projekt: kontekst tega delovnega toka", "Global: vsi skilli; Projekt: vsa navodila za ekipo", "Med njima ni razlike — obe sta sistemski navodili"],
                    "correct": 1,
                    "explanation": "Global instructions = kdo si in kako delaš (velja povsod). Project = kontekst tega delovnega toka (specifičen, ne velja drugje). Zamenjava pomeni, da Cowork nima pravega konteksta ob pravem času."
                },
                {
                    "id": 113,
                    "q": "Hočeš distribuirati finance skill celotni Finance ekipi za trajno produkcijsko rabo. Katera pot je PRAVILNA?",
                    "options": ["Pošlji ZIP vsem po e-pošti", "Objavi v team marketplace — centralna namestitev in posodobitve", "Dodaj skill datoteko v skupni Drive", "Pošlji Anthropic za uradno objavo v globalnem marketplace"],
                    "correct": 1,
                    "explanation": "Team marketplace je prava pot za produkcijsko distribucijo — centralna namestitev, samodejne posodobitve, lastnik odgovoren. ZIP je le za testiranje z eno osebo."
                },
                {
                    "id": 114,
                    "q": "Daš Cowork navodilo: 'Počisti stare projekte v Drive-u.' Zakaj je to tvegano?",
                    "options": ["Ker Cowork ne podpira brisanja datotek", "Ker 'staro' ni definirano — Claude sam odloči, kaj to pomeni", "Ker Drive zahteva Admin pravice za brisanje", "Ker Cowork vedno vpraša za potrditev pri brisanju"],
                    "correct": 1,
                    "explanation": "'Staro' brez kriterija pusti prostor za napačno interpretacijo obsega. Varno navodilo bi glasilo: 'Arhiviraj projekte brez aktivnosti v zadnjih 180 dneh v mapo /Arhiv — ne briši ničesar.'"
                },
                {
                    "id": 115,
                    "q": "Katerega elementa NIMA skill, ga pa ima plugin?",
                    "options": ["Instructions (navodila za postopek)", "Assets (predloge in primeri)", "Connectors in ekipna distribucija kot paket", "Trigger mehanizem za samodejno aktivacijo"],
                    "correct": 2,
                    "explanation": "Skill = Instructions + Assets. Plugin = skills + connectors + know-how za distribucijo ekipi. Plugin je paket skillов z ekipno infrastrukturo — skill sam tega nima."
                },
                {
                    "id": 116,
                    "q": "Kateri pogoj mora biti izpolnjen, da je delegacija naloge Cowork smiselna?",
                    "options": ["Naloga mora biti krajša od 5 minut", "Naloga mora imeti jasen izid, ponovitveno vrednost in majhno tveganje", "Naloga mora vključevati vsaj eno datoteko", "Claude mora imeti API priključek za vse vire"],
                    "correct": 1,
                    "explanation": "Dobra delegacija zahteva tri pogoje: jasen izid (veš, kako izgleda uspeh), ponovitvena vrednost (se bo ponovila), majhno tveganje (napaka je popravljiva). Brez teh je Chat hitrejša izbira."
                },
                {
                    "id": 117,
                    "q": "Claude v Chromu hoče klikniti 'Pošlji' na obrazcu. Kaj se zgodi privzeto?",
                    "options": ["Samodejno klikne — to je namen Chrome integracije", "Pošlje e-poštno obvestilo in čaka", "Vpraša za tvojo odobritev pred občutljivim dejanjem", "Blokira dejanje in zahteva geslo"],
                    "correct": 2,
                    "explanation": "Privzeto Claude vpraša za odobritev pred vsakim občutljivim dejanjem v Chromu — klik, pošiljanje, oddaja. Ti odobravaš ali zavrneš. Nadzor ostane pri tebi."
                },
                {
                    "id": 118,
                    "q": "Kateri je pravilen vrstni red za varno distribucijo skilla ekipi?",
                    "options": ["Napiši → Marketplace → Testiraj sproti", "Napiši → Eval → Popravi → Eval OK → Marketplace", "Eval → Napiši → Marketplace", "Napiši → Direktna delitev vsem → Marketplace po testiranju"],
                    "correct": 1,
                    "explanation": "Pravi vrstni red: Napiši navodila → Testiraj z eval → Popravi dvoumnosti → Ponovi eval do 80 % zeleno → Objavi v marketplace. Direktna delitev je le za začetno testiranje z eno osebo, ne z ekipo."
                }
            ]
        }
    ]
}

# Find cowork course and add chapter 5
cowork = next((c for c in courses if c.get('slug') == 'cowork'), None)
if not cowork:
    print('ERROR: cowork kurs ni najden!')
    exit(1)

existing_ids = [ch['id'] for ch in cowork['chapters']]
if 5 in existing_ids:
    print('ERROR: Chapter 5 že obstaja! ID-ji:', existing_ids)
    exit(1)

cowork['chapters'].append(chapter5)

with open('_courses_migrated.json', 'w', encoding='utf-8') as f:
    json.dump(courses, f, ensure_ascii=False, separators=(',', ':'))

print('OK: Chapter 5 dodan v cowork kurs.')
print(f'Cowork ima zdaj {len(cowork["chapters"])} poglavij.')
sections = chapter5['sections']
for s in sections:
    print(f'  - Section {s["id"]}: {s["title"]} | {len(s["features"])} features, {len(s["notes"])} notes, {len(s["questions"])} questions')
