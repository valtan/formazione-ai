# Normative di riferimento — sintesi per uso didattico

> **Ultimo aggiornamento: 27 agosto 2026** (ricerca su fonti primarie: EUR-Lex,
> Gazzetta Ufficiale, governo.it, Garante Privacy, più dottrina professionale).
> Fonti puntuali in fondo al file. Prossima revisione consigliata: **entro il 30
> novembre 2026** — il quadro si muove ancora (decreti attuativi italiani in
> pubblicazione, Digital Omnibus "dati" in negoziato).

---

## 0. Mappa rapida — cosa citare e in che ordine

| Livello | Fonte | Serve per rispondere a |
|---|---|---|
| UE — dati personali | **GDPR** (Reg. UE 2016/679) | "posso mettere questo dato nel prompt?" |
| UE — sistemi di AI | **AI Act** (Reg. UE 2024/1689), come modificato dal **Digital Omnibus on AI** (Reg. UE 2026/1744) | "che obblighi ho se uso/compro un sistema di AI?" |
| UE — in corso | **Digital Omnibus "dati"** (proposta COM(2025) 837) | "il GDPR sta cambiando?" → sì, ma **non è ancora legge** |
| IT — legge quadro AI | **Legge 23 settembre 2025, n. 132** | principi nazionali, lavoro, professioni, nuovi reati |
| IT — responsabilità dell'impresa | **D.Lgs. 231/2001** e successive modifiche | "l'azienda risponde se un dipendente usa male l'AI?" |
| IT — prassi | Provvedimenti del **Garante Privacy** | casi concreti da usare in aula |

Regola d'aula: **prima il GDPR** (riguarda tutti, subito), **poi l'AI Act**
(riguarda soprattutto chi fornisce o adotta sistemi), **infine 231/Legge 132**
(riguarda l'organizzazione, non il singolo utente).

---

## 1. GDPR (Regolamento UE 2016/679)

Aspetti rilevanti per l'uso aziendale di AI generativa:

- **Art. 5** — Principi: minimizzazione dei dati, limitazione della finalità, esattezza, sicurezza
- **Art. 6** — Basi giuridiche del trattamento (consenso, contratto, interesse legittimo, ecc.)
- **Art. 9** — Categorie particolari di dati (salute, biometrici, ecc.) — divieto generale, deroghe strette
- **Art. 22** — Diritto a non essere sottoposti a decisioni automatizzate con effetti significativi
- **Art. 25** — Privacy by design e by default
- **Art. 35** — DPIA (valutazione d'impatto) per trattamenti ad alto rischio
- **Artt. 55-56** — Competenza delle autorità e **meccanismo dello sportello unico** (autorità capofila): non è tecnicismo, ha già ribaltato una sanzione italiana (vedi § 6)

### Implicazioni pratiche per la formazione
- Mai inserire dati personali di clienti/colleghi in prompt verso chatbot pubblici
- Verificare dove sono i server e chi è il titolare/responsabile → trasferimenti internazionali
- Distinguere uso "consumer" e uso "business/enterprise" degli **stessi** strumenti: cambiano contratto, conservazione dei dati e uso per l'addestramento

---

## 2. AI Act (Reg. UE 2024/1689) — testo aggiornato dal Digital Omnibus

In vigore dal 1° agosto 2024, con applicazione graduale. **Il calendario originale
è cambiato**: il *Digital Omnibus on AI* (§ 3) ha rinviato la parte più pesante.

### Classificazione del rischio (invariata nell'impianto)
- **Rischio inaccettabile** (pratiche vietate, art. 5): social scoring, manipolazione subliminale, identificazione biometrica remota in tempo reale in luoghi pubblici (con eccezioni). Applicabili **dal 2 febbraio 2025**.
  - Il Digital Omnibus ha **aggiunto due divieti**: generazione/manipolazione di materiale intimo non consensuale e materiale pedopornografico.
- **Alto rischio** (all. III e all. I): selezione del personale, valutazione degli studenti, accesso al credito, infrastrutture critiche, ecc. → obblighi di conformità rigorosi.
- **Rischio limitato**: chatbot, contenuti sintetici, deepfake → obblighi di **trasparenza** (art. 50).
- **Rischio minimo**: la gran parte degli usi d'ufficio.

### Calendario aggiornato (post-Omnibus)

| Data | Cosa |
|---|---|
| 2 febbraio 2025 | Pratiche vietate (art. 5) + obbligo di alfabetizzazione AI (art. 4) |
| 2 agosto 2025 | Modelli per finalità generali (GPAI), governance UE, sanzioni |
| **2 agosto 2026** | **Obblighi di trasparenza (art. 50)**: dichiarare che si interagisce con un'AI, marcare i contenuti sintetici, informare su riconoscimento emozioni e categorizzazione biometrica |
| 2 dicembre 2026 | Entrano in applicazione i due nuovi divieti aggiunti dall'Omnibus. Scade anche il periodo transitorio per la **marcatura** dei sistemi generativi già sul mercato prima del 2 agosto 2026 |
| **2 dicembre 2027** | Sistemi **ad alto rischio dell'Allegato III** (rinviati dal 2 agosto 2026) |
| **2 agosto 2028** | Sistemi ad alto rischio **integrati in prodotti** (All. I, sez. A: macchine, dispositivi medici, giocattoli…) |

### Sanzioni (art. 99)
Fino a **35 mln €** o 7% del fatturato mondiale (pratiche vietate); fino a
**15 mln €** o 3% (altri obblighi, incluso art. 50).

### Punto che ci riguarda direttamente: art. 4 (alfabetizzazione AI)
Il Digital Omnibus ha **attenuato** l'art. 4: da obbligo di garantire un livello
sufficiente di competenza a **obbligo di adottare misure a sostegno dello
sviluppo** dell'alfabetizzazione AI, senza pretendere un livello specifico.

> **Come dirlo in aula, senza vendere paura**: l'obbligo di formare le persone
> non è sparito, è diventato meno prescrittivo. Resta un obbligo di condotta
> dell'organizzazione, e resta il fatto che la formazione è il modo più
> economico per ridurre il rischio 231/GDPR. Non usare l'art. 4 come leva
> commerciale minacciosa: è scorretto e ora anche impreciso.

---

## 3. Digital Omnibus — attenzione: sono **due** cose diverse

Errore ricorrente (anche nella stampa): parlare del "Digital Omnibus" come di un
unico testo. La Commissione ha presentato il pacchetto il **19 novembre 2025** e
da lì l'iter si è **sdoppiato**.

### 3a. Digital Omnibus **on AI** → è legge
**Regolamento (UE) 2026/1744** dell'8 luglio 2026, che modifica i regolamenti
2024/1689 (AI Act), 2018/1139 e 2023/1230 — *semplificazione dell'attuazione
delle regole armonizzate sull'intelligenza artificiale*.
**In vigore dal 27 luglio 2026.**

Cosa cambia, in sintesi:
- **rinvio** dell'alto rischio (vedi tabella § 2);
- definizione più stretta di "componente di sicurezza";
- **art. 4 attenuato** (alfabetizzazione AI);
- **nuovo art. 4-bis**: trattamento eccezionale di categorie particolari di dati per rilevare e correggere le distorsioni (bias), con pseudonimizzazione, limiti tecnici e cancellazione;
- due nuovi divieti nell'art. 5;
- semplificazione della registrazione in banca dati UE (all. VIII) e dei codici di buone pratiche;
- competenza esclusiva dell'Ufficio UE per l'IA sui sistemi basati su modelli generalisti dello stesso fornitore e su quelli integrati nelle piattaforme molto grandi;
- accesso prioritario delle PMI agli spazi di sperimentazione normativa (sandbox).

### 3b. Digital Omnibus **"dati"** → **non è legge**
Proposta **COM(2025) 837** su GDPR, ePrivacy/cookie, Data Act, NIS2.
Stato al 27 agosto 2026: **ancora in negoziato**. In Consiglio il testo di
compromesso non ha raggiunto la maggioranza qualificata alla fine della
presidenza cipriota (30 giugno 2026); dal 1° luglio 2026 il dossier è in mano
alla presidenza irlandese. In Parlamento è assegnato alle commissioni ITRE e
LIBE (relatrici Aura Salla e Marina Kaljurand). Pareri congiunti EDPB-EDPS:
21 gennaio 2026 (parte AI) e 11 febbraio 2026 (parte dati).

Temi aperti più discussi: definizione di **dato personale**, base del
**legittimo interesse** per l'addestramento di sistemi di AI, regole su
cookie/tracciamento, notifica dei **data breach**.

> **Regola d'aula tassativa**: il GDPR di oggi è quello del 2016. Finché la
> proposta non è approvata e pubblicata in GUUE, **non va insegnata come
> normativa vigente**. Al massimo: "è in discussione una riforma, questi sono i
> punti in gioco".

---

## 4. Legge italiana sull'AI — Legge 23 settembre 2025, n. 132

*Disposizioni e deleghe al Governo in materia di intelligenza artificiale*.
Pubblicata in **GU n. 223 del 25 settembre 2025**, **in vigore dal 10 ottobre 2025**.
È la prima legge nazionale organica sull'AI in UE; **non sostituisce l'AI Act**,
lo accompagna sul piano nazionale.

Contenuti utili in aula:
- **Principi**: centralità della persona, trasparenza, cybersicurezza, non discriminazione, accessibilità.
- **Lavoro (art. 11)**: obbligo di **informare i lavoratori** sull'impiego di AI in assunzione, gestione del rapporto e valutazione della prestazione; istituzione di un **Osservatorio** presso il Ministero del Lavoro.
- **Professioni intellettuali (art. 13)**: l'AI è **strumento di supporto**, prevale il lavoro umano; obbligo di **comunicare al cliente** l'uso di sistemi di AI.
- Ulteriori capi su sanità, PA, giustizia, cybersicurezza, diritto d'autore.
- **Autorità nazionali**: **AgID** (promozione e sviluppo), **ACN** (vigilanza, ispezioni, sanzioni).
- **Deleghe al Governo** (12 mesi) per decreti su reati, sanzioni e tutele civili → vedi § 5.

### Disposizioni penali (art. 26)
- **Nuova aggravante comune, art. 61 n. 11-*decies* c.p.**: reato commesso mediante sistemi di AI usati come mezzo insidioso, o che abbiano ostacolato la difesa o aggravato le conseguenze. Aumento fino a **un terzo**.
- **Nuovo art. 612-*quater* c.p. — "Illecita diffusione di contenuti generati o alterati con sistemi di intelligenza artificiale"** (deepfake): chi cagiona un danno ingiusto diffondendo senza consenso immagini, video o voci falsificati con AI e idonei a ingannare sulla loro genuinità → **reclusione da 1 a 5 anni**. Procedibile **a querela**, d'ufficio nei casi previsti (vittima minore o incapace, pubblico ufficiale per ragioni funzionali, connessione con altro delitto procedibile d'ufficio).
- Aggravanti su fattispecie esistenti quando il mezzo è l'AI: art. 294 c.p. (attentati ai diritti politici), art. 2637 c.c. (aggiotaggio), art. 185 TUF (manipolazione del mercato), art. 171 l. 633/1941 (diritto d'autore).

---

## 5. D.Lgs. 231/2001 — responsabilità amministrativa degli enti e AI

**Cos'è, in una frase da aula**: il D.Lgs. 8 giugno 2001, n. 231 prevede che
**l'azienda risponda in proprio** (sanzioni pecuniarie in "quote", interdittive,
confisca) per una lista **chiusa** di reati commessi nel suo interesse o
vantaggio da apicali o sottoposti. Si difende dimostrando di aver adottato ed
efficacemente attuato un **Modello di organizzazione, gestione e controllo
(MOG 231)** e di aver nominato un **Organismo di Vigilanza**.

Il catalogo dei reati presupposto (artt. 24 e ss.) è cresciuto per stratificazione
in 25 anni. Voci già oggi rilevanti per un uso scorretto dell'AI, **senza bisogno
di norme nuove**:

- **art. 24-bis** — delitti informatici e trattamento illecito di dati (accessi abusivi, danneggiamento di sistemi; sanzioni inasprite dalla **L. 90/2024** sulla cybersicurezza)
- **art. 25-ter** — reati societari (es. false comunicazioni sociali costruite su output non verificati)
- **art. 25-sexies** — abusi di mercato
- **art. 25-*novies*** — violazione del diritto d'autore
- **art. 24** — truffa ai danni dello Stato e indebita percezione di erogazioni

### Novità in arrivo: art. 25-*vicies* (AI)
La Legge 132/2025 **non ha modificato direttamente** il catalogo 231. Lo fa il
**decreto legislativo attuativo**, che ha seguito questo iter:
approvazione preliminare in CdM il **10 giugno 2026** → trasmissione alle Camere
per i pareri il 24 giugno 2026 → **approvazione definitiva in CdM il 4 agosto 2026**.

Contenuto: nuovo **art. 25-*vicies* del D.Lgs. 231/2001**, con due reati presupposto:

| Reato presupposto | Sanzione pecuniaria all'ente |
|---|---|
| **art. 437-*bis* c.p.** (nuovo) — omessa adozione di misure tecniche di sicurezza e di sorveglianza umana su sistemi di AI ad alto rischio; alterazione illecita | da **600 a 1.000 quote** |
| **art. 612-*quater* c.p.** — illecita diffusione di contenuti generati o alterati con AI | da **200 a 700 quote** |

Il nuovo **art. 437-*bis* c.p.** punisce, in sintesi, l'omissione di misure
idonee a prevenire malfunzionamenti di sistemi di AI ad alto rischio e
l'omissione della sorveglianza umana: reclusione da 1 a 5 anni se ne deriva
pericolo per la vita o l'incolumità individuale, da 2 a 8 anni se il pericolo
riguarda l'incolumità pubblica o la sicurezza dello Stato; pene più severe per
l'alterazione illecita.

> ⚠️ **`[DA VERIFICARE]` prima di citarlo in aula come diritto vigente**: alla
> data di questo aggiornamento (27/08/2026) **non risulta ancora pubblicato in
> Gazzetta Ufficiale**. Finché non lo è, si dice "approvato in via definitiva dal
> Consiglio dei Ministri il 4 agosto 2026, in attesa di pubblicazione", **non**
> "è in vigore". Controllare su Normattiva/Gazzetta Ufficiale prima di ogni
> lezione che tocchi il tema.

### Cosa NON dire
- ❌ "Con l'AI Act l'azienda risponde ex 231 di qualunque violazione." **Falso**: la responsabilità 231 scatta solo per i reati elencati, non per gli illeciti amministrativi dell'AI Act.
- ❌ "Il deepfake è già reato presupposto 231." **Non ancora** (vedi sopra): è reato dal 10 ottobre 2025, ma l'aggancio al 231 arriva col decreto attuativo.
- ✅ Messaggio corretto: *l'uso disinvolto dell'AI non crea una nuova responsabilità dal nulla, ma può far entrare l'azienda da porte già aperte — reati informatici, diritto d'autore, reati societari — e il MOG 231 va aggiornato di conseguenza.*

---

## 6. Garante Privacy — casi utili come esempio in aula

- **OpenAI / ChatGPT — sanzione da 15 mln € (provv. dicembre 2024)**: raccolta dati per l'addestramento, base giuridica, informativa, verifica dell'età; imposta anche una campagna informativa di sei mesi. **Attenzione: la sanzione è stata annullata dal Tribunale di Roma (marzo 2026) per incompetenza del Garante italiano**, in applicazione del meccanismo dello sportello unico (autorità capofila irlandese, artt. 55-56 GDPR). Ottimo caso per spiegare che *il merito della contestazione e la competenza a decidere sono due cose diverse*. `[DA VERIFICARE se la sentenza è stata impugnata]`
- **Replika — 5 mln € (aprile 2025)**: chatbot relazionale, base giuridica e tutela dei minori.
- **Character.AI — 158.000 € (provvedimento del 9 luglio 2026)**: informative inadeguate, DPIA tardiva, nomina tardiva del rappresentante UE, tutele insufficienti per i minori, verifica dell'età difettosa. Prescrizioni: verifica dell'età funzionante, *cooling-off* contro la ri-registrazione dei minori bloccati, account dei minori privati per impostazione predefinita; 120 giorni per riferire.
- **Blocco di ChatGPT (marzo 2023)**: utile solo come episodio storico, non come regola vigente.

---

## 7. Da verificare prima di ogni ciclo d'aula

1. **Pubblicazione in GU del decreto attuativo** con l'art. 25-*vicies* 231 e l'art. 437-*bis* c.p. (approvato in via definitiva il 4/8/2026).
2. **Digital Omnibus "dati"**: se e quando esce dal negoziato — finché è proposta, non si insegna.
3. Nuovi provvedimenti del Garante nell'ultimo trimestre (i casi freschi funzionano meglio in aula dei principi).
4. Eventuali linee guida della Commissione UE sull'art. 50 (trasparenza) e sull'attuazione dell'Omnibus.
5. Scadenza del 2 dicembre 2026 (nuovi divieti + fine del transitorio sulla marcatura): dopo quella data la tabella del § 2 va rivista.

---

## 8. Fonti consultate (27 agosto 2026)

**Fonti primarie**
- Regolamento (UE) 2026/1744 — EUR-Lex: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Proposta COM(2025) 837 (Digital Omnibus "dati") — EUR-Lex: https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=celex:52025PC0837
- Legge 23 settembre 2025, n. 132 — GU n. 223 del 25/09/2025
- Legislative Train Schedule, Parlamento europeo — file "Digital Package"
- Garante Privacy, comunicato Character.AI (9 luglio 2026): https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10269594
- Garante Privacy, comunicato ChatGPT/OpenAI (dicembre 2024): https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432
- Ministero del Lavoro, pacchetto attuativo L. 132/2025

**Dottrina e approfondimenti professionali** (usati per l'inquadramento, non come fonte di norma)
- Sistema Penale — decreti attuativi AI e art. 437-*bis* c.p.
- Revilaw / Next Generation Business — art. 25-*vicies* D.Lgs. 231/2001
- Bonelli Erede — impatti della L. 132/2025 sui Modelli 231
- Agenda Digitale, Altalex, Diritto.it, Brocardi — L. 132/2025 e novità penali
- Studio Previti, Il Sole 24 Ore NT+ Diritto — Tribunale di Roma su OpenAI e sportello unico
- Goodwin, Cloud Security Alliance — applicabilità dell'art. 50 dal 2 agosto 2026 e periodo transitorio al 2 dicembre 2026

> Regola del progetto: se una norma non è in questo file, nei materiali va
> segnata come `[DA VERIFICARE]`, non citata a memoria.
