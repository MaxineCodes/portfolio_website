---
title: Schriftelijke vaardigheden portfolio
date: 2026-04-01
description: Ja, het hele portfolio.
---

# Hoofdstuk 1・Inleiding

## Introductie portfolio

Dit portfolio documenteert de ontwikkeling van de schrijfvaardigheid van de student binnen de cursus "Schrijfvaardigheid  en Rapporteren" aan de Hanze Hogeschool Groningen in de periode januari-april 2026. De cursus richt zich op het opbouwen van competenties voor zowel zakelijke als academische teksten: een vaardigheid die essentieel is voor een toekomstige carrière in de ICT-sector.

## Persoonlijke Leerdoelen

Voor de opleiding HBO-ICT worden van studenten veel verslagen verwacht. De cursus schriftelijke vaardigheden bereidt de student hier op voor door competenties op te bouwen. AI brengt veel onzekerheid in de markt, vooral voor sectoren als ICT. Hierdoor is theoretische kennis belangrijker dan ooit. Hogere functies brengen hogere verantwoordelijkheden, en rapporteren is een onmisbare tool om de communicatie tussen ICT’ers en niet-ICT’ers te bevorderen.

Het leren schrijven van zowel zakelijke als academische rapportages of verslagen is daarom het leerdoel van de student.

## Vooruitblik

In hoofdstuk 2 wordt het verzamelen van informatie behandelt met een vergelijkende analyse tussen twee AI-chatbots. Hoofdstuk 3 richt zich op ordenen en stijl, met een zelfreflectie op persoonlijke schrijfproblemen. Vervolgens brengt hoofdstuk 4 deze concepten van zakelijk schrijven naar webteksten en optimalisatie voor zoekmachines. Hoofdstuk 5 biedt een introductie aan zakelijk en academisch rapporteren, wat verder uitbloeit tot hoofdstuk 5 waar alle competenties tot de test worden gezet in een casusopdracht. Hoofdstuk 7 bespreekt de leerdoelen en reflecteert op de cursus in het algemeen.

# Hoofdstuk 2・Informatie Verzamelen

## 2.1・Inleiding

In het kader van deze opdracht wordt onderzocht hoe verschillende chatbots informatie verzamelen en presenteren. Hoofdstuk 2.2 richt zich  specifiek op een vergelijkende analyse tussen ChatGPT en DeepSeek, twee prominente large-language-models (LLM's). Het centrale onderzoeksvraag is: op welke manier verschillen de antwoorden van deze twee tools wanneer zij worden gevraagd naar de  trainingskosten van DeepSeek zelf?
Deze analyse is relevant omdat het inzicht biedt in de onderliggende biases en culturele verschillen van de bedrijven die de chatbots ontwikkelen.

Eerst worden de antwoorden van beide chatbots gepresenteerd, gevolgd door een analyse over de verschillen in toon en inhoud. De sectie sluit af met een reflectie over de betrouwbaarheid van teksten door LLM's.  

 

## 2.2・Lesopdracht 1

### Opdrachtomschrijving:

Zoek een kwestie uit waarover ChatGPT en DeepSeek totaal verschillende antwoorden geven, zoals in de Taiwan-kwestie. Zoek vervolgens zelf op internet wie (het meest) gelijk heeft en volgens welke bronnen dat zo is.

Schrijf in je portfolio de vraag op die je hebt gesteld, laat de twee verschillende antwoorden zien, beschrijf in 100-200 woorden welke tekstbot (het meest) gelijk heeft en op grond van welke bronnen je dat denkt.

### Deepseek: 

De kern van DeepSeeks vermogen om tegen lage kosten te trainen, is een systematische innovatie van algoritme tot engineering, waardoor de trainingskosten zijn teruggebracht tot **5,57 miljoen dollar**, slechts een tiende of zelfs minder van vergelijkbare modellen.

- **Op architectonisch vlak** wordt gebruikgemaakt van het **Mixture-of-Experts (MoE) model**. Hoewel het totaal aantal parameters 671 miljard bedraagt, worden er per keer slechts 37 miljard geactiveerd. Dit werkt als een team van experts waarbij alleen de juiste specialisten worden ingezet, wat inefficiënte berekeningen door het hele systeem voorkomt.

- **Op algoritmisch vlak** wordt **Sparse Attention** gebruikt, waardoor de computationele complexiteit wordt verlaagd van O(n²) naar O(n log n). Dit vermindert de trainingsbelasting per sessie met 40% en zorgt voor een versnelling van 2 tot 3 keer bij het verwerken van lange teksten.

- **Wat betreft precisie** is DeepSeek de pionier in grootschalige **FP8 low-precision training**, waardoor data wordt "afgeslankt" en het geheugengebruik en de rekenkracht bijna worden gehalveerd.

- **Op engineering-vlak** wordt door middel van **Multi-head Latent Attention (MLA)** het videogeheugengebruik teruggebracht tot 1/7 van dat van traditionele modellen. In combinatie met gradiëntcompressie en communicatie-optimalisatie wordt de efficiëntie van het cluster bijna verdubbeld. 

    Door de synergie van deze technologieën heeft DeepSeek met slechts 2048 H800 GPU's hetzelfde resultaat behaald als clusters waar voorheen tienduizenden GPU's voor nodig waren, waardoor het trainen van grote modellen niet langer een "duur speeltje" voor techreuzen is.

### ChatGPT:

DeepSeek heeft de trainingskosten verlaagd door een combinatie van efficiëntietechnieken te gebruiken in plaats van één enkele doorbraak. De belangrijkste methode is 'Mixture-of-Experts', waarbij per taak slechts een deel van het model wordt geactiveerd, wat rekenkracht bespaart. Daarnaast zijn geoptimaliseerde attention-methoden, multi-token voorspelling en een nauwe afstemming tussen hardware en software toegepast om geheugengebruik en tijd te beperken. Distillatie—het leren van sterkere AI-modellen—heeft de trainingsbehoefte verder teruggebracht. De veelgenoemde kosten van ongeveer 6 miljoen dollar dekken alleen de uiteindelijke trainingsronde, exclusief eerdere experimenten, dataverwerking en infrastructuur, waardoor de totale investering aanzienlijk hoger uitviel.

 

### Analyse

Teksten zijn vrijwel nooit objectief. De toon, de context, de inhoud, maar ook wat er niet aanwezig is in de tekst, duiden op de subjectieve ervaring van de schrijver. Gelukkig bestaat tegenwoordig AI, een automatisch algoritme dat compleet objectieve informatie kan geven dankzij de afwezigheid van een menselijk hart, toch?

Naast het feit dat AI getraind is op de collectieve schrijfwerken van het internet, waar zeker veel vooroordelen en partijdigheid bestaan, wordt de gegenereerde output ook gestuurd door het bedrijf dat het AI-model traint, door middel van het selecteren en sturen van LoRa’s en welke outputs wel of niet goedgekeurd worden.

Gegeven de vraag: "Met welke methode heeft DeepSeek zijn trainingskosten zo laag gehouden?" (vertalingen: "With what method did DeepSeek manage to train its algorithm so cheaply?" en "DeepSeek是如何以如此低廉的成本训练其算法的？") was ChatGPT erg bereid om controverses aan te duiden en kritiek te leveren op het proces. DeepSeek daarentegen focust het antwoord vooral op de technische details en implementaties zonder deze controverses naar het licht te brengen.

In hoeverre dit een reflectie is van de verschillen in de normen en waarden van de culturen-China staat meer bekend om technologische vooruitgang met een blind oog voor sociale kwesties, wat in contrast staat met Amerika, waar juist sociale vooruitgang een grote belangstelling is geweest, is een geheel ander onderwerp.

Het is belangrijk om de oorsprong, vooroordelen en politieke kleur van de AI-modellen in gedachten te houden, omdat zelfs 100% correcte informatie veel subjectiviteit met zich mee kan brengen.

 

## 2.2・Slot

De analyse in dit hoofdstuk maakt duidelijk dat AI-tools niet neutrale informatiebronnen zijn. ChatGPT benoemt expliciet de controverses rondom DeepSeek’s trainingskosten, terwijl DeepSeek deze achterwege liet. Het verschil in welke informatie wel en niet gepresenteerd wordt laat mogelijk zien hoe culturele en commerciële belangen de teksten door AI kunnen beïnvloeden.

 

# Hoofdstuk 3・Ordenen en Stijl

## 3.1・Inleiding

Hoofdstuk 3 behandelt ordenend schrijven en de toepassing voor goed leesbare, zakelijke teksten met een duidelijk doel en logisch structuur. Dit hoofdstuk bevat als eerste een korte samenvatting over de college, gevolgd door een reflectie over verbeterpunten wat betreft schrijfstijl.

## Samenvatting College 2

**Het schrijfproces**

Tijdens het schrijfproces kan je beter gewoon beginnen, en dan continu itereren en verbeteren. De tekst zal nooit in 1 klap perfect zijn. Begin met het verzamelen van informatie, bepaal de rode draad en doelgroep, bouw daarna het structuur van je document met hoofdstukken. Dit dwingt je om doelbewust na te denken. Extern schema: de structuur, oftewel de pilaren en stalen frame van de tekst. Hoofdstukken, enz. Intern schema: de inhoud, de vormgeving van de muur of ramen. Binnen de alinea's. Met behulp van schema's kun je beter de structuur sturen om de hoofdboodschap van het document te ondersteunen.

**Stijl** Stijl is wat de tekst differentieert van andere teksten. Wat een goede stijl is is subjectief en ligt aan het doel van de schrijver. In de meeste gevallen, is het van belang dat het niet te technisch en formeel is, maar ook niet te gemakkelijk.

Blijf dicht bij (formeel) spreektaal. Vermijd technische termen, afhankelijk van de doelgroep. Voor technische programmeer-documentatie zijn termen als architecture-paradigms en polymorphic-inheritance wel OK. Wissel korte en lange zinnen met elkaar af. Volledige zinnen: met onderwerp en persoonsvorm.

**Vermijd tangconstructies.** Een tangconstructie is een zinsconstructie waarbij woorden of zinsdelen die bij elkaar horen ver uit elkaar staan. https://onzetaal.nl/taalloket/tangconstructie

**Schrijf nauwkeurig.** Geen vage taal, gebruik datums, vermijd woorden als "misschien" en afzwakkende formuleringen. Vermijd assumpties: wat voor de ene "gezond verstand" is, is voor een ander misschien onbekende informatie. Houdt meervoud en tijd consistent. Schrijf actief, dus vermijd de lijdende vorm. 

## 3.2・Lesopdracht 2

### Opdrachtomschrijving:

Ga naar “Omgaan met schrijf problemen” en lees over de meest voorkomende schrijfproblemen. Kies er minimaal twee die op jou van toepassing zijn en lees welke adviezen je krijgt om de problemen op te lossen. Schrijf een verhaal waarin je betoogt wat je van de adviezen vindt. Ben je het ermee eens of niet? En wat ga jij doen om je schrijven te verbeteren?

**Gekozen schrijfproblemen:**

Ik heb geen talent voor schrijven; het kost me zo veel tijd.

Ik ben altijd ontevreden over het eindresultaat

**Verhaal**

_"Ik heb geen talent voor schrijven; het kost me zo veel tijd."_

Schrijven kost mij veel tijd. Talent geloof ik niet zo in, als mens kunnen wij alles leren, onze breinen zijn erg complex, capaciteit genoeg dus. Maar, schrijven kost mij veel tijd, ik ben uren bezig met de opmaak, de volgorde van zinnen aanpassen, alinea's verplaatsen, ga zo maar door, en dan heb ik het nog niet eens zelf goed doorgelezen.

Het advies vraagt: "wat is te veel tijd?" en wordt er uit gelegd dat dat heel erg afhankelijk is van de zwaarte van het onderwerp. Ik vind schrijven erg moeilijk en er komt veel bij kijken, maar dit komt misschien ook omdat ik het erg serieus probeer te nemen.

Verder zegt het advies om de juiste werkwijze aan te gaan met een goede planning. Het maken van een planning ben ik altijd slecht in geweest, ik krijg tientallen ideeën in een keer, en ben daarna bezig om ze te sorteren. Ik denk dat dit advies wel bruikbaar kan zijn, maar ik moet een process maken dat mijn eigen is.

Onderwerpen dat ik leuk vind om over te vertellen, vind ik ook leuk om over te schrijven en kosten mij lang niet zo veel tijd als een schoolopdracht zoals bij schrijfvaardigheid. Voor dat ik aan programmeren deed, deed ik aan schilderen, visuele beelden maken zowel op papier als digitaal. Ik ben een creatief mens, en in alles dat ik maak stop ik een stukje van mijzelf. Dit maakt het process langzamer, en ik weet niet of dit zo snel op te lossen is.

_"Ik ben altijd ontevreden over het eindresultaat."_

"Deze constatering kan twee oorzaken hebben, die eigenlijk tegenovergesteld aan elkaar zijn: je bent óf te gemakzuchtig, óf juist te kritisch." Kritisch zijn op je eigen werk zit vaker alleen maar in de weg, en dat herken ik erg goed. Het afronden van een project is duizenden malen moeilijker dan iets nieuws beginnen. Ik leg de lat erg hoog voor mezelf, en ik ben bang om te falen. Ik voel me altijd alsof ik op een plaats belandt dat eigenlijk boven mijn capaciteiten is, en dat men er snel achter zal komen dat ik helemaal zo slim niet ben.

_"Hoewel het belangrijk is dat je een goed eindproduct levert, moet je het belang ervan ook kunnen relativeren en de taak niet te zwaar opvatten."_

Als ik minder bang ben om te falen, en een onvoldoende durf te riskeren, ben ik ook sneller klaar met mijn werk.

## 3.3・Slot

Logische structuur en een prettig te lezen schrijfstijl is essentieel voor de toegankelijkheid voor een document, zeker als het gelezen wordt door partijen met weinig tijd. Het college en de zelfreflectie tonen aan dat goed zakelijk schrijven een planmatig proces vraagt.

 

# Hoofdstuk 4・Webteksten en SEO

## 4.1・Inleiding

Veel schrijfprincipes voor zakelijk schrijven vertalen ook direct naar het schrijven van webteksten. In dit hoofdstuk worden deze principes naar het schrijven voor websites. Hiervoor is extra aandacht nodig voor de toegankelijkheid van de informatie voor bezoekers en de indexering door zoekmachines.

Na een samenvatting van het college gaat dit sectie een fictief ICT bedrijf _Frame Bakery_ met twee webteksten voor de website.

## Samenvatting College 3

Een website bestaat over het algemeen van vormgeving en tekst. De vormgeving is erg belangrijk om de lezer naar de tekst te brengen, maar de tekst geeft uiteindelijk de informatie. een goede "first impression" is essentieel. Tekst is ook belangrijk om hoog in zoek resultaten te verschijnen. Zoekmachines gebruiken tekst om te bepalen welke website het best aansluit op de zoek-query. SEO (search engine optimisation) is de naam dat hier voor gebruikt wordt. Door de juiste zoekwoorden te benutten in de tekst maak je de kans groter dat je vindbaar bent via een zoekmachine. Voor het beste resultaat, gebruik je zowel short tail als long tail door elkaar. Overmatig gebruik van zoekwoorden kan het tegenovergestelde effect hebben, een zoekmachine kan dit registeren als spam. Een mogelijke oplossing: synoniemen. Ook is het belangrijk om afbeeldingen met goede namen en alt-tags met de zoektermen te gebruiken zodat een zoekmachine deze sneller kan vinden.

Short tail: weinig zoekwoorden die veel gebruikt worden. Long tail: veel zoekwoorden die weinig gebruikt worden.

Nadat je de lezer op je website hebt, wil je dat de informatie zo snel mogelijk beschikbaar is. De homepage is vaak de eerste kennismaking, maak de informatie gemakkelijk vindbaar en leesbaar. Houdt rekening mee met de reden waarom de lezer hier is, en breng de lezer de waarde die ze uit je website, of tekst, hopen te zoeken. Schrijf dus niet te langdradig en gebruik duidelijke kopjes. De belangrijkste informatie moet in de eerste twee alinea's of kopjes te vinden zijn, mensen lezen een website vaak in een F-patroon, houdt hier dus rekening mee met het beschikbaar maken van de informatie. Ook is het erg belangrijk om de mobiele layout van de website in de gaten te houden, er zijn meer mobiele gebruikers dan op PC.

 

## 4.2・Lesopdracht

### Opdrachtomschrijving:

Beschrijf welk ICT-bedrijf je met je medestudent (naam!) zou willen oprichten + wat je doelgroep is + welke zoekwoorden jouw publiek heeft voor het product/de dienst dat/die je aanbiedt.

- Schrijf twee teksten voor deze site (allebei: ongeveer 150 woorden)
    
- Tekst 1 is voor de homepage: beschrijf wat je aanbiedt en wat de voordelen ervan zijn voor je doelgroep
    
- Tekst 2 is voor een onderliggende pagina: hierin stel je je bedrijf op een aantrekkelijke manier voor
    
- Voldoe in beide UNIEKE teksten aan alle besproken eisen (val met de deur in huis, denk aan je doel, spreek de lezer aan, schrijf kort maar krachtig enz.)
    
- Verwerk twee zoekwoorden in de eerste alinea van beide teksten en markeer deze duidelijk
    

### ICT-Bedrijf idee:

**Frame Bakery** Frame Bakery is een bedrijf dat out-sourcing services biedt voor kleinschalige 3D/VFX film- en animatieproducties door het leveren van expertise op kort en tijdelijk termijn.

**Doelgroep:** kleine filmstudio's, onafhankelijke producties en indie-gameontwikkelaars met een krap budget maar wel cultuur-verrijkende film-ideeën.

**Zoektermen:** animatie, outsourcing, snel, tijdelijk, filmproject, indie, studio, flexibel

Veel film-professionals zitten de laatste tijd zonder werk, of zijn contracten te kort en is er weinig baanzekerheid, terwijl veel producties vastlopen vanwege hoge personeelskosten of langere contracteisen vanuit personeel.

Via Frame Bakery kunnen professionals met een standaard contract bezig aan verschillende producties en blijven ze aan de slag, en hebben filmstudio's altijd mensen tot hun beschikking die hen helpt om verder te komen.

### Tekst 1: Homepage

**Digitale film-productie outsourcing**

Meer personeel nodig dan verwacht? Komt de deadline dichterbij dan geanticipeerd? Versterk uw productie met **vertrouwde outsourcing expertise** op het moment dat u het meest onder druk staat. Frame Bakery biedt ervaren specialisten in animatie, rigging, modelling, compositing, lighting en pipeline-ondersteuning, klaar om **direct snelle ondersteuning** te bieden. **Wij begrijpen de onvoorspelbaarheid van creatieve projecten** en bieden daarom flexibele, tijdelijke contracten aan, met nauwe en transparante communicatie: allemaal tegen **indie-vriendelijke tarieven**.

Het kiezen van de juiste outsourcing-partner kan het succes van uw project maken of breken. Daarom stemmen wij onze diensten volledig af op uw unieke productie-eisen. Van pre- tot post-productie leveren wij de juiste ondersteuning, precies wanneer uw team ze het meest nodig heeft. **Geen lange contracten, geen vaste lasten, geen langdurige verplichtingen**: snel, tijdelijk en op maat.

### Tekst 2: Onze Missie

**Wij geloven in projecten met passie, ondersteund door ervaren professionals.** Frame Bakery is ontstaan uit een gedeelde frustratie binnen de animatie- en filmindustrie: te veel waardevolle, kleinschalige film- en animatieprojecten zinken of worden downsized vanwege dure, stapelende personeelskosten. Tegelijkertijd zitten veel getalenteerde professionals zonder stabiel werk, krijgen beginnende talenten weinig kans om ervaring op te doen, en verleren zelfs veteranen hun vak door gebrek aan werk.

Daarom besloten wij een fundamenteel andere aanpak te nemen. Frame Bakery biedt **tijdelijke expertondersteuning** en **flexibele filmcreatie** precies op maat, zodat u als studio of producent geen langdurige verplichtingen aangaat voor last-minute staffing of gespecialiseerde skills. Ons model is een win-win: wij matchen uw project aan ons grote, zorgvuldig samengestelde netwerk aan filmprofessionals.

Onze teams werken met standaardcontracten, wat werkzekerheid biedt voor ons personeel. Dit stelt ons in staat een unieke leeromgeving te creëren waar beginnende professionals zij aan zij werken met zeer ervaren experts om hun vaardigheden te versterken. Het resultaat is een betrouwbare en groeiende pool van talent, klaar om uw creatieve visie te versterken tegen voorspelbare kosten. Samen houden we waardevolle projecten én carrières in stand tijdens deze turbulente tijden voor de industrie.

 

## 4.3・Slot

Hoofdstuk 4 laat zien dat SEO en lezersgericht schrijven elkaar kunnen versterken. Korte, doelbewuste alinea’s en relevante keywords helpen zowel zoekmachines als bezoekers van de website.

 

# Hoofdstuk 5・Rapporteren

## 5.1・Inleiding

Hoofdstuk 5 behandelt de structuur en stijl van zowel zakelijke als academische rapportages dat objectiviteit als belangrijkste stelt. De structuur is erg belangrijk en is van tevoren al bepaald.

Eerst wordt een samenvatting van de college weergeven, gevolgd door een herschrijving van een inleiding voor “de groene bezorger” dat wordt afgesloten met een argumentatie.

 

### Samenvatting College 4

Rapporten, of verslagen, brengen problemen/trends in kaart. Vaak eindigen ze in een oplossing of advies. In het onderwijs heet een rapport vaak een werkstuk, scriptie of these. _"If it's not documented, it didn't happen."_ Voor een rapport is de stijl/toon neutraal. Gebruik geen ik-vorm of wij-vorm.

**Vaste rapportonderdelen:**

- **Omslag**
    
- Omslag is de eerste impressie met een plaatje, titel, auteur(s) en subtitel.
    
- **Titelpagina**
    
- Nogmaals titel, ondertitel, en auteur(s).
    
- Naam van organisatie, datum/plaats.
    
- Paginanummers beginnen vanaf hier.
    
- **Samenvatting** (optioneel bij reflectieverslag/portfolio)
    
- Geen hoofdstuk, geen nummer. Het liefst 1 tot max. 2 A4.
    
- Zelfstandig leesbaar.
    
- Samenvatting wordt het vaakst gelezen.
    
- **Voorwoord** (optioneel)
    
- Ik-vorm is toegestaan. Ruimte voor persoonlijke opmerkingen.
    
- **Inhoudsopgave**
    
- Overzicht van alle onderdelen die na inhoudsopgave komen.
    
- Inleiding eerst, inleiding is hoofdstuk 1.
    
- Overzichtelijke opmaak.
    
- **Inleiding**
    
- Introduceer het onderwerp.
    
- Bedoeld voor alle lezers, ook niet technische.
    
- Moet de lezer nieuwsgierig maken, maar houdt het algemeen.
    
- Schets een aanleiding voor dit rapport.
    
- Aanleiding: alles dat heeft geleid tot de praktijkvraag.
    
- Formuleer de praktijkvraag en doelstelling.
    
- Noteer de precieze praktijkvraag.
    
- Wees SMART: specifiek, meetbaar, acceptabel, realistisch, tijdgebonden.
    
- Doelstelling geeft precies aan wat er bereikt moet worden.
    
- Operationaliseer de begrippen: leg termen vast, geef definities.
    
- Formuleer het doel van dit rapport.
    
- Geef een vooruitblik op de inhoud.
    
- Hoofdstuk 1 blabla, hoofdstuk 2, enz.
    
- **Kernhoofdstukken**
    
- Ieder hoofdstuk heeft een korte inleiding en een kort slot.
    
- **Conclusie** (met eventueel advies/aanbevelingen)
    
- Korte samenvatting van wat er is besproken in de kernhoofdstukken.
    
- Terugkoppeling naar de inleiding. Inleiding en conclusie horen bij elkaar.
    
- **Literatuurlijst** (zo nodig)
    
- **Bijlagen** (zo nodig)
    
- In het rapport staat een korte omschrijving van wat er in de bijlage staat, daarnaast wordt er alleen verwezen.
    
- "Bijlage 1 + titel"
    
- **Overi****g****:** symbolenlijst, verklarende woordenlijst, register (zo nodig)
    

 

## 5.2・Lesopdracht 4

### Opdrachtomschrijving:

Neem de juiste volgorde van de inleiding van De Groene Bezorger. Beschrijf in 100-200 woorden of je snapt hoe zo’n inleiding moet worden geschreven en waarom op deze manier. Geef argumenten voor je standpunt.

### Inleiding De Groene Bezorger:

**Introductie onderwerp** Hoe sneller, hoe beter! Het kan de hedendaagse online-consument niet snel genoeg gaan. Vandaag besteld, gisteren in huis... Wil een organisatie inspelen op de behoefte van de consument van vandaag, dan is het aan te raden een snelle, efficiënte en klantvriendelijke website mét webshop aan te bieden.

**Aanleiding** De Groene Bezorger is een onderneming uit Groningen die groente- en fruitpakketten verkoopt. De consument kan deze pakketten bestellen in de winkel aan het Damsterdiep. Vervolgens krijgt de consument elke week een groente- en fruitpakket thuisbezorgd: precies genoeg om een hele week van te kunnen eten. De Groene Bezorger onderscheidt zich door een groot aanbod aan exotisch fruit en biologisch geteelde groente en fruit. Aanleiding voor de opdracht aan Hanzenadvies is het gegeven dat de bestellingen de laatste twee jaar aanzienlijk teruglopen. Oorzaak hiervan is de groeiende concurrentie. De Groene Bezorger heeft er belang bij dat de bestellingen op korte termijn weer toenemen, anders dreigt de onderneming failliet te gaan. Het probleem is dat de concurrenten de producten online aanbieden. De consument kan dezelfde producten bij de concurrent gemakkelijk en snel online bestellen via een webshop. Ook de levering verloopt bij de concurrent sneller dan bij De Groene Bezorger.

**Opdracht** De concrete opdracht van De Groene Bezorger aan Hanzenadvies luidt: "Verbeter de huidige website zodat deze klantvriendelijker is”.

**Doelstelling (SMART)** De doelstelling van deze opdracht is als volgt geformuleerd: “Binnen twee maanden wordt een website opgeleverd die aan de gestelde eisen voor klantvriendelijkheid voldoet"

**Operationalisering van de gehanteerde begrippen** Het onderstaande beschrijft aan welke eisen de website moet voldoen, wil de website klantvriendelijker genoemd worden. De website kan klantvriendelijker genoemd worden als:

de nieuwe website een online webshop aanbiedt waar alle pakketten online besteld kunnen worden

de website een snellere levering van de pakketten garandeert: levering na onlinebestelling uiterlijk binnen twee dagen

de verwachte levertijd wordt aangegeven voordat de klant definitief online bestelt

de nieuwe website een chatfunctie bevat voor meer informatie

het e-mailadres op alle schermen herkenbaar in beeld is

de nieuwe website een forum en klachtenbox biedt

de nieuw website ingaat op actualiteiten, nieuws en aanbiedingen.

**Doel van het rapport** Het doel van het rapport is De Groene Bezorger te informeren over de uitvoering van de opdracht de bestaande website klantvriendelijker te maken. Een onderneming zonder goedlopende webshop is al gauw in het nadeel. Daarom heeft opdrachtgever De Groene Bezorger aan bureau Hanzenadvies gevraagd de huidige website te verbeteren. Voorliggend rapport beschrijft de uitwerking van deze opdracht.

**Vooruitblik op het rapport** De volgende hoofdstukken gaan uitgebreid in op bovenstaande verbeteringen. Elk hoofdstuk werkt een verbetering uit. Hoofdstuk 1 behandelt... Vervolgens gaat hoofdstuk 2 in op.... Daarna bespreekt hoofdstuk 3... In hoofdstuk 4 komen aan de orde.... enz. De conclusie ten slotte biedt een helder overzicht van alle verbeteringen die gerealiseerd zijn.

### Argumentatie

De structuur van de inleiding volgt een logische volgorde voor de lezer: van algemeen naar specifiek, van probleem naar oplossing. Ook volgt het nu de volgorde als beschreven op de PowerPoint.

Eerst wordt het brede onderwerp geïntroduceerd: het belang van een snelle, klantvriendelijke webshop, wat de aandacht trekt van zowel technische als niet-technische lezers. Vervolgens wordt de situatie en aanleiding bij de opdrachtgever geschetst: De Groene Bezorger, dalende verkopen door concurrentie, wat het praktische probleemstelling duidelijk maakt. Daarna volgt de precieze opdracht en de SMART-doelstelling, die duidelijk maken wat er moet gebeuren. De operationalisering definieert vervolgens de vage term "klantvriendelijker" in meetbare criteria om duidelijkheid te brengen en misverstanden weg te halen. Het doel van het rapport zelf legt uit wat de lezer kan verwachten van het document. Ten slotte geeft een vooruitblik over de rest van het rapport.

 

## 5.3・Slot

Hoofdstuk 5 geeft aan dat een vaste logische structuur van essentie is voor een effectief rapport. Met de samenvatting, inleiding en conclusie kan de lezer snel de belangrijkste informatie vinden. De inleiding wordt vaker gelezen dan de inhoud,, waardoor het belangrijk is dat de lezer hier voldoende informatie uit kan halen.

 

# Hoofdstuk 6: Casusopdracht

## 6.1・Inleiding

Hoofdstuk 6 presenteert de casusopdracht: een volledige inleiding voor een ICT rapport geschreven tijdens het college. Deze opdracht toetst de eerder behandelde vaardigheden: informatie verzamelen, ordenen en stijl, en rapporteren in klassikale situatie met tijdsdruk.

Dit hoofdstuk bevat de opdrachtbeschrijving en de volledige inleiding voor ITANN, het bedrijf in het ICT rapport.

## 6.2・Opdracht: Eindopdracht

### Opdrachtomschrijving:

Jullie schrijven tijdens deze les een inleiding van een ICT-rapport, gebaseerd op een casus van webtechnologie. Ook als je deze casus niet (goed) kent, kun je hem gebruiken. Je mag ook een andere casus van webtechnologie gebruiken, als er maar een inleiding uitkomt die voldoet aan de beschreven eisen.

 

### Opdracht: Hoofdstuk 1: Inleiding 

Webtechnologie bieden een onmisbare functie in het ondersteunen van moderne organisatie- of bedrijfsprocessen door het beheer van gegevens en data gestructureerd en efficient te houden. Met een database kunnen gegevens op een georganiseerde manier opgeslagen en beheerd worden, en met behulp van user-friendly webinterfaces kan deze data beheerd worden door zowel docenten als administratoren, aangepast op de rechten die verleend moeten worden per type gebruiker.

ITANN (IT Academy Noord-Nederland) biedt al jarenlang cursussen programmeren voor een gevarieerde doelgroep van kinderen, jongeren, en jong-volwassenen. Naar aanleiding van groeiende interesse in programmeervaardigheden onder oudere doelgroepen, breidt ITANN nu uit naar cursussen speciaal voor gepensioneerden: "Van Senioren naar Seniorcoder". Hiervoor wordt een compleet nieuw cursuspakket en digitaal ecosysteem ontworpen speciaal voor de eisen van cursisten met hogere leeftijd, docenten, en administratoren, dat momenteel ontbreekt in de markt. Security zal ook zorgvuldig behandeld worden om gegevens van cursisten veilig te houden.

In opdracht van ITANN zal SMART-IT een webapplicatie ontwikkelen als hoofdonderdeel van het digitale ecosysteem voor de ondersteuning van het nieuwe cursuspakketaanbod. Deze webapplicatie zal een front-end interface, de 'webportal', bieden voor docenten en administratoren om gegevens veilig te beheren. CRUD-operaties worden achter de schermen, in de back-end, toegepast op de verschillende tabellen in de database: klanten, docenten, talen en lessen. Via de frontend zullen cursisten ook informatie kunnen zien over hun cursussen, en zal dit uitgebreid kunnen worden naar een omgeving waar inschrijven voor andere cursussen ook mogelijk is.

Het doel van dit rapport is om een functionele webapplicatie te ontwikkelen dat aansluit bij de wensen van de ITANN. Door inzicht te krijgen in de vereiste functionaliteiten en om een werkend prototype te ontwikkelen dat voldoet aan deze vereisten.

In dit rapport wordt onder webapplicatie verstaan: een softwaretoepassing die via een web-browser toegankelijk is via een front-end interface, en gebruikmaakt van een achterliggende, back-end database. Onder CRUD-operaties wordt verstaan: de basisbewerkingen Create, Read, Update en Delete, waarmee gegevens kunnen worden aangemaakt, geraadpleegd, aangepast en verwijderd.

Het doel van dit rapport is om verslag te doen van de uitvoering van de opdracht door ITANN, IT Academy Noord-Nederland aan SMART-IT.

De opbouw van dit rapport is als volgt: Hoofdstuk 2 beschrijft de theoretisch-technische details van de webinterface en zal hoofdstuk 3 dieper duiken op het ontwerp van de database. Hier op verder zal Hoofdstuk 4 de beveiligingsdetails behandelen. Vervolgens gaat hoofdstuk 5 in op de ontwikkelmethode, gekozen architectuur, en aanpakdetails. Hoofdstuk 6 bevat een weergave van het ontwikkeld resultaat. Daarna biedt hoofdstuk 7 de conclusies en aanbevelingen voor verdere ontwikkelingen. Hoofdstuk 8 ten slotte gaat in op de evaluatie en reflectie op het project. 

## 6.3・Slot

De inleiding geschreven voor ITANN door de student is een demonstratie van de geculmineerde vaardigheden die de student heeft opgedaan door het schrijven van dit portfolio.

 

# Hoofdstuk 7: Conclusie

Heb ik nieuwe, relevante vaardigheden geleerd ten opzichte van mijn leerdoelen?


# Bronvermelding

## Gebruik van bronnen

Voor dit rapport is uitsluitend gebruikgemaakt van het lesmateriaal dat via de colleges en PowerPoints van de opleiding beschikbaar is gesteld, Hanze Library Guides, en van AI (ChatGPT, DeepSeek) enkel ter ondersteuning van de lesopdracht van hoofdstuk 2. Alle inhoudelijke keuzes en conclusies zijn door de student zelf gemaakt.

## Literatuurlijst:

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, kalenderweek 7). _S__chriftelijke Vaardigheden_ _1__.__3 College 1_ _–_ _i__nformatie verzamelen 1.3_ (PowerPoint-slides). Opleiding HBO-ICT, Hanzehogeschool Groningen.

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, roosterweek 8). _S__chriftelijke Vaardigheden_ _1__.__3 College 2_ _-_ _ordenen_ _en_ _stijl_ (PowerPoint-slides).

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, roosterweek 10). _S__chriftelijke Vaardigheden_ _1__.__3 College 3_ _-_ _webteksten_ _+ SEO_ _(_PowerPoint-slides).

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, roosterweek 11). _S__chriftelijke Vaardigheden_ _1__.__3 College 4_ _–_ _rapporteren_  (PowerPoint-slides).

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, roosterweek 11). _S__chriftelijke Vaardigheden_ _1__.__3_ _–_ _Opdracht les 4_ (PowerPoint-slides).

Hanzehogeschool Groningen, Opleiding HBO-ICT. (2026, roosterweek 13). _S__chriftelijke Vaardigheden_ _1__.__3 College 5_ _–_ _vervolg_ _rapporteren_  (PowerPoint-slides). Opleiding HBO-ICT, Hanzehogeschool Groningen.

Universiteit van Amsterdam. (n.d.) _Omgaan met schrijfproblemen._ (Webartikel). https://taalwinkel.uva.nl/studievaardigheden/schrijven-schrijfproces/omgaan-met-schrijfproblemen/omgaan-met-schrijfproblemen.html

OpenAI. (2026). _ChatGPT (GPT-5)_. [https://chat.openai.com/](https://chat.openai.com/ "https://chat.openai.com/")

DeepSeek. (2026). _Deep__S__eek(DeepSeek-V3.2)_. [https://chat.deepseek.com/](https://chat.deepseek.com/ "https://chat.deepseek.com/")