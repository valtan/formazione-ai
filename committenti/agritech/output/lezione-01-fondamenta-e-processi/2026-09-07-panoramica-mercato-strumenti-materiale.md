---
titolo: "Panoramica del mercato: le principali famiglie di strumenti AI, senza vincitori"
committente: Agritech
lezione: "Giornata 1 — Apertura del percorso e prima raccolta di processi"
blocco_in_aula: "Frontale (10', 18:00–18:10)"
tipo_sessione: teorica
livello: misto
durata_stimata: "10 min in aula (il documento copre molto di più: è base di conoscenza per il formatore)"
target: "PMI — dipendenti e titolari, pubblico non tecnico; uffici commerciale, tecnico, amministrazione, acquisti"
obiettivi_apprendimento:
  - "Distinguere le due famiglie principali di strumenti AI generativa: chatbot generalisti standalone e AI integrata nella suite di produttività già in uso"
  - "Riconoscere che esistono anche famiglie minori (alternative europee, modelli aperti/locali) rilevanti in scenari specifici, senza doverle approfondire oggi"
  - "Capire perché il percorso non indica 'il migliore' strumento: il confronto è sempre relativo a un uso, un contesto e dei dati, non assoluto"
  - "Sapere che la scelta dello strumento aziendale per Agritech non è ancora stata fatta e arriverà più avanti nel percorso, in coordinamento con il referente tecnico"
prerequisiti: "Utile ma non indispensabile aver seguito, nella stessa giornata, il blocco introduttivo su cos'è un LLM (`2026-09-07-modulo-ai-e-llm-materiale.md`)"
data_redazione: "2026-09-03"
stato: "bozza da validare con il formatore"
---

# Panoramica del mercato: le principali famiglie di strumenti, senza vincitori

## Come usare questo documento

Questo non è il testo della lezione: è la base di conoscenza da cui il blocco viene ricavato. In aula il blocco dura dieci minuti; il resto serve al formatore per reggere le domande e per costruire slide sapendo che cosa c'è dietro ogni affermazione.

Un vincolo di impostazione, prima di tutto: le linee guida del progetto (`context/linee-guida-formazione-base.md`, Blocco A) sono esplicite sul fatto che, in prima giornata, la panoramica di mercato dev'essere **solo un accenno — mappa d'insieme, nessun approfondimento**. L'approfondimento vero, con le famiglie di modelli linguistici (inclusi quelli cinesi ed europei) e la mappa concettuale di Projects, Skills e Plugin/MCP, è previsto in giornata 3 (`scaletta-lezione.md` della giornata 3) e resta interamente lì. Questo documento è più esteso della sezione che entrerà in aula proprio perché serve anche a preparare quella giornata: il formatore può leggerlo per intero ora e riusarne le parti più tecniche più avanti, ma **in aula, oggi, si resta ai primi due livelli della mappa (§2)**.

Il principio che regge l'intero documento, e che va detto esplicitamente in aula, è quello indicato nel profilo del percorso (`context/profilo-formatore.md` e `committenti/agritech/brief.md`): il confronto tra strumenti è sempre **comparativo**, mai a senso unico. Anche se il percorso è orientato alla famiglia Claude, la panoramica resta onesta sulle alternative, perché la scelta dello strumento aziendale per Agritech non è ancora stata presa (si veda §7).

---

## 1. Perché questo argomento conta per un'azienda

Chi non lavora nel settore tecnologico incontra il tema "quale AI usare" quasi sempre attraverso il marketing — pubblicità, articoli entusiastici, il collega che consiglia "quella che uso io" — e questo produce due distorsioni tipiche in aula. La prima è credere che esista un solo strumento "giusto" e che sceglierne un altro sia un errore: non è così, perché strumenti diversi hanno equilibri diversi tra capacità, costo, integrazione e gestione dei dati, e quale equilibrio conviene dipende dal contesto. La seconda distorsione è l'effetto opposto: la sensazione di dover scegliere subito, da soli, tra decine di nomi che cambiano ogni mese, e che sbagliare la scelta comprometta tutto. Anche questo è falso: il mercato si muove rapidamente (§8) e le aziende più prudenti trattano la scelta dello strumento come **revisionabile**, non come un investimento definitivo — esattamente come fa questo percorso per Agritech (§7).

Il valore di questo blocco, in dieci minuti, non è insegnare a scegliere: è dare una mappa che permetta ai partecipanti di collocare correttamente ciò che sentono nominare — in aula, nei media, dai colleghi — dentro un numero piccolo di categorie con caratteristiche riconoscibili, invece di trattare ogni nome nuovo come un oggetto isolato e incomprensibile.

---

## 2. La mappa in due famiglie (quella che entra in aula oggi)

Il modo più semplice per orientarsi tra i tanti nomi che circolano è chiedersi: **da dove parte l'utente per usare lo strumento?** Da questa domanda nascono le due famiglie che contano davvero per la prima giornata.

### 2.1 Famiglia 1 — Chatbot generalisti (standalone)

Sono assistenti a cui ci si rivolge direttamente, attraverso un sito web o un'app dedicata, con una conversazione a sé stante: si apre una pagina o un'app, si scrive una richiesta, si riceve una risposta. Non richiedono che l'azienda abbia già in uso una suite specifica, e in genere hanno un piano gratuito che permette di provarli senza costi.

Le quattro famiglie di chatbot generalisti che il percorso userà come riferimento comparativo (`context/profilo-formatore.md`) sono **Claude** (Anthropic), **ChatGPT** (OpenAI), **Gemini** (Google) e **Copilot** nella sua versione consumer, cioè l'assistente gratuito integrato in Windows, Edge e nel sito copilot.microsoft.com (Microsoft) — da non confondere con Microsoft 365 Copilot, che appartiene alla famiglia 2. Tutti e quattro fanno, nel nucleo, la stessa cosa: rispondono a domande, riassumono, scrivono, traducono, ragionano su un testo o un'immagine caricati nella conversazione. Le differenze pratiche, quelle che contano per un ufficio, riguardano il costo, i limiti d'uso, la finestra di contesto, la disponibilità di funzioni accessorie (ricerca web, generazione di immagini, esecuzione di codice) e — punto che ritornerà nel percorso — le condizioni con cui gestiscono i dati che gli si scrivono.

### 2.2 Famiglia 2 — AI integrata negli strumenti di lavoro

Sono funzioni AI che non si usano a sé stanti, ma **dentro** i programmi che l'ufficio già usa ogni giorno: la posta, i documenti, i fogli di calcolo, le riunioni. Non si apre una conversazione separata: si preme un pulsante o si scrive un'istruzione dentro Word, Excel, Outlook, Teams, Gmail, Documenti o Fogli Google, e la risposta compare nello stesso strumento, spesso con accesso diretto ai contenuti — email, file, calendario — dell'account aziendale, nei limiti dei permessi già assegnati alla persona.

I due prodotti di riferimento sono **Microsoft 365 Copilot** (per le aziende che usano la suite Microsoft 365) e **Google Workspace con Gemini** (per le aziende che usano Google Workspace). La differenza pratica rispetto alla famiglia 1 non è tanto nella qualità delle risposte — il motore che c'è dietro è spesso imparentato con quello della versione standalone dello stesso fornitore — quanto nel **contesto disponibile**: uno strumento integrato può leggere, se autorizzato, i documenti e le email della persona che lo usa, mentre un chatbot generalista parte sempre da zero, a meno che non gli si incolli o carichi il materiale a mano.

### 2.3 Perché la distinzione conta più del singolo nome

Il messaggio da lasciare in aula, se del blocco resta una sola cosa, è questo: **la domanda utile non è "qual è la migliore AI", ma "questo compito parte da una conversazione a sé o da dentro un documento che sto già scrivendo?"**. La risposta orienta subito verso una famiglia, prima ancora di aver scelto un fornitore preciso — ed è un criterio che resta valido anche quando i nomi dei prodotti, che cambiano spesso (§8), saranno diversi da quelli di oggi.

---

## 3. Uno sguardo oltre le due famiglie principali (solo per completezza — non approfondire in aula)

Un mercato descritto con sole due famiglie sarebbe incompleto, e vale la pena che il formatore le conosca anche se in dieci minuti restano al più un cenno di una frase. Non sono materia della giornata 1: tornano, con più spazio, in giornata 3.

**Alternative europee.** Accanto ai grandi fornitori statunitensi esistono fornitori con sede nell'Unione Europea — il più noto è l'azienda francese **Mistral AI**, il cui assistente conversazionale, storicamente chiamato *Le Chat*, è stato ridenominato **Mistral Vibe** nella primavera-estate 2026 con un ampliamento delle funzioni (in particolare verso compiti di scrittura di codice) `[DA VERIFICARE prima della lezione — il prodotto è stato rinominato di recente ed è ragionevole aspettarsi ulteriori cambiamenti]`. Il motivo per cui queste alternative vengono menzionate nelle aziende con requisiti stringenti sulla residenza dei dati è la sede legale e, in alcuni piani, la possibilità di trattamento dei dati interamente su infrastrutture europee — un tema che tornerà quando si parlerà di GDPR e trasferimenti internazionali di dati (giornata 3).

**Modelli aperti e installabili in locale.** Esiste infine una famiglia tecnicamente più impegnativa: modelli il cui funzionamento interno (i cosiddetti "pesi" del modello) è reso disponibile per essere scaricato ed eseguito su server propri, invece che tramite un servizio online di un fornitore. Il vantaggio è che, in teoria, nessun dato esce mai dall'azienda; il costo è che serve competenza tecnica interna e hardware adeguato, e le prestazioni dei modelli aperti restano tipicamente qualche passo indietro rispetto ai modelli di punta dei grandi fornitori. È l'opzione a cui si guarda tipicamente solo in presenza di dati estremamente sensibili (`context/linee-guida-formazione-base.md`, tabella "Selezione degli strumenti AI") — per Agritech non risulta, allo stato, un requisito emerso.

---

## 4. Le famiglie una per una: cosa sono, punti di forza, limiti generali

Le informazioni di questa sezione — nomi dei piani, prezzi, funzioni — sono una **fotografia della situazione a inizio settembre 2026**, verificata tramite ricerca web al momento della redazione (§9). È materia che cambia con frequenza mensile o più rapida: **il formatore la deve ricontrollare poco prima di ogni utilizzo in aula**, non solo alla stesura di questo documento.

### 4.1 Claude (Anthropic)

Assistente conversazionale con un piano gratuito e piani a pagamento (indicativamente: Pro attorno ai 20 $/mese, Max su due fasce di utilizzo più ampie, oltre a piani Team ed Enterprise per le aziende e un piano Education) `[DA VERIFICARE — prezzi esatti al momento della lezione]`. È noto per l'attenzione dichiarata alla sicurezza e per prestazioni solide su compiti di scrittura, analisi di documenti lunghi e programmazione. Offre funzioni di lavoro strutturato (raccolte di documenti di riferimento riutilizzabili, competenze personalizzabili) che il percorso userà più avanti, quando si parlerà di Projects e Skills (giornata 3). Punto di attenzione generale, comune del resto a tutta la famiglia 1: fuori dai piani aziendali, il trattamento dei dati inseriti nelle conversazioni segue le condizioni del piano consumer, non quelle di un contratto enterprise.

### 4.2 ChatGPT (OpenAI)

Probabilmente il nome più riconosciuto tra il pubblico non tecnico, con una gamma di piani che si è ampliata nel tempo (Free, un piano intermedio più economico, Plus, Pro, oltre a Business ed Enterprise per le aziende) `[DA VERIFICARE — nomi e prezzi esatti dei piani al momento della lezione: la gamma si è modificata più volte nel 2026]`. Punti di forza generalmente riconosciuti: un ecosistema molto ampio di funzioni accessorie (generazione di immagini, navigazione web, esecuzione di codice, creazione di assistenti personalizzati) e una base di utenti che lo rende spesso il primo strumento con cui una persona entra in contatto con l'AI generativa. Una curiosità utile da citare in aula per il messaggio di fondo del punto §8: a inizio settembre 2026 il modello di punta più recente ha assunto nomi interni per livello di capacità (varianti indicate come "Sol", "Terra", "Luna" all'interno della stessa generazione) `[DA VERIFICARE — nomenclatura in rapida evoluzione]` — un esempio concreto di quanto velocemente cambino le etichette tecniche, che è un'ottima ragione per non impararle a memoria.

### 4.3 Gemini (Google)

Assistente di Google, disponibile come app e sito standalone (famiglia 1) e integrato in Google Workspace (famiglia 2). Anche qui la gamma consumer è su più livelli (un piano gratuito e piani a pagamento crescenti per capacità del modello e spazio di archiviazione incluso) `[DA VERIFICARE — nomi e prezzi esatti al momento della lezione]`. Punto di forza generalmente riconosciuto: l'integrazione stretta con l'ecosistema Google (Gmail, Drive, Documenti, Fogli, Ricerca), utile soprattutto per le aziende che già usano Google Workspace come suite di produttività.

### 4.4 Copilot e Microsoft 365 Copilot (Microsoft)

Vanno tenuti distinti con attenzione, perché il nome condiviso genera confusione anche tra utenti esperti. **Copilot** (consumer) è l'assistente gratuito integrato in Windows, nel browser Edge e raggiungibile via sito o app: funziona come chatbot generalista, senza accesso privilegiato ai dati aziendali. **Microsoft 365 Copilot** è invece un prodotto per le aziende, aggiunto come componente a pagamento sopra un abbonamento Microsoft 365 Business o Enterprise già esistente, che si integra dentro Word, Excel, Outlook, Teams e PowerPoint con accesso — nei limiti dei permessi della persona — a email, documenti e riunioni dell'organizzazione. Il costo dell'add-on aziendale si aggira, secondo le fonti consultate, sull'ordine dei 30 $ per utente al mese sopra il canone della suite `[DA VERIFICARE — cifra indicativa, va confermata al momento della lezione e dipende dal piano Microsoft 365 di base già in uso]`.

### 4.5 Google Workspace con Gemini

È l'equivalente Google di Microsoft 365 Copilot: le funzioni Gemini integrate dentro Gmail, Documenti, Fogli e Meet, disponibili nei piani Workspace per le aziende (Business Starter, Standard, Plus, con prezzi crescenti per utente al mese) `[DA VERIFICARE — cifre esatte al momento della lezione]`. Per un'azienda che già usa Google Workspace, è tipicamente l'opzione con il minor attrito di adozione, perché non introduce un secondo abbonamento indipendente ma si affianca a strumenti già familiari.

### 4.6 Confronto sintetico: funzionalità dei tre prodotti principali (Claude, ChatGPT, Gemini)

Oltre al confronto per famiglia (§5), è utile un confronto diretto sulle funzionalità tra i tre chatbot generalisti su cui il percorso si concentra — Claude, ChatGPT, Gemini — perché è la domanda che i partecipanti fanno più spesso in aula ("ma allora questi tre cosa sanno fare, di preciso?"). Le informazioni seguenti sono state verificate tramite ricerca web al momento della redazione (3 settembre 2026, si veda §12) e vanno trattate con la stessa cautela di §4: restano volatili, il formatore deve ricontrollarle prima di ogni uso in aula. Per evitare di presentare come fatti stabili numeri che sulle fonti consultate cambiano rapidamente (dimensione esatta della finestra di contesto, prezzi, date precise di rilascio di una funzione), qui ci si limita a differenze funzionali qualitative — presenti/assenti, tipo di funzione — che sono più stabili.

**Ricerca web e funzioni creative.** Tutti e tre offrono ricerca web integrata con risultati aggiornati. Sulla generazione di immagini, invece, c'è una differenza netta da segnalare esplicitamente in aula perché contro-intuitiva: Claude non genera immagini nativamente (accetta testo e immagini in input, restituisce solo testo), mentre ChatGPT e Gemini la offrono nativamente, e su alcuni piani superiori anche funzioni di generazione video `[DA VERIFICARE — disponibilità e piani esatti al momento della lezione]`. L'esecuzione di codice (per calcoli, analisi dati, script) è disponibile su tutti e tre tramite uno strumento dedicato.

**Documenti e materiale di riferimento.** Tutti e tre permettono di caricare file nella conversazione per farli analizzare. Ciascuno offre inoltre una funzione per raccogliere materiale di riferimento riutilizzabile tra conversazioni, con un nome diverso: "Projects" in Claude, "Projects" e assistenti personalizzati ("GPT" configurabili) in ChatGPT, "Gems" in Gemini (assistenti con istruzioni fisse e file di riferimento propri). Claude e ChatGPT hanno inoltre introdotto una forma di memoria che riassume il contenuto rilevante delle conversazioni precedenti `[DA VERIFICARE — tempistica di rilascio e disponibilità per piano al momento della lezione]`.

**Uso quotidiano.** Tutti e tre sono disponibili via web, app desktop e app mobile, con un piano gratuito che dà accesso a una versione con funzioni o limiti d'uso ridotti rispetto ai piani a pagamento `[DA VERIFICARE — limiti esatti del piano gratuito al momento della lezione]`. La differenza pratica più rilevante per un'azienda che usa già Google Workspace è che Gemini, oltre a esistere come chatbot a sé stante, è integrato direttamente dentro Gmail, Documenti, Fogli e Meet (si ricollega alla famiglia 2, §2.2) — un vantaggio di comodità che gli altri due non hanno nella stessa forma nativa, salvo passare per Microsoft 365 Copilot nel caso di ChatGPT/famiglia OpenAI legata a un'integrazione Microsoft.

Anche questo confronto resta comparativo, non un verdetto: la sezione §6 spiega perché "nessuno è il migliore" vale anche a livello di singole funzionalità, non solo di famiglia.

---

---

## 5. Uno sguardo d'insieme: pro e contro generali per famiglia

La tabella seguente riassume, a livello generale e non specifico per prodotto, i pro e i contro tipici delle due famiglie principali. Va letta come punto di partenza per una discussione, non come un verdetto: ogni riga ha eccezioni a seconda del prodotto e del piano scelto.

| Aspetto | Famiglia 1 — Chatbot generalisti | Famiglia 2 — AI integrata nella suite |
|---|---|---|
| Avvio | Immediato, spesso gratuito, nessuna dipendenza da altri strumenti aziendali | Richiede la suite di produttività (Microsoft 365 o Google Workspace) già attiva, più un costo aggiuntivo |
| Contesto disponibile | Solo ciò che l'utente incolla o carica nella conversazione | Accesso diretto, se autorizzato, a email, documenti e calendario della persona |
| Curva di adozione | Richiede di imparare un'interfaccia nuova e l'abitudine di "andare a chiedere" | Si inserisce dentro strumenti già noti, meno attrito iniziale |
| Flessibilità di compiti | Molto ampia: qualunque compito descrivibile a parole | Ottimizzata sui compiti tipici dello strumento ospitante (scrivere in Word, analizzare in Excel, riassumere in Teams) |
| Costo per l'azienda | Scalabile per singola persona o piccoli team, piani individuali semplici da attivare | Tipicamente un costo per utente aggiuntivo sopra un abbonamento già esistente, spesso pensato per il dispiegamento su più persone |

Questa tabella non sostituisce una valutazione fatta sui processi reali dell'azienda — che è esattamente ciò che l'assessment e le prime giornate del percorso raccoglieranno — ma è la base concettuale su cui quella valutazione si costruirà.

---

## 6. Perché nessuno è "il migliore": il criterio giusto è il confronto per uso

La domanda "qual è la migliore AI" è mal posta, ed è utile spiegare in aula perché, con un esempio concreto piuttosto che con un principio astratto. Chiedere alla stessa domanda a due strumenti diversi produce quasi sempre due risposte entrambe ragionevoli, scritte in modo diverso, con punti di forza diversi — non una giusta e una sbagliata. Uno strumento può essere più efficace per scrivere in tono formale, un altro per sintetizzare un documento lungo, un altro ancora per lavorare dentro un foglio di calcolo perché ci vive già dentro. La scelta giusta non è quindi "quale vince in assoluto", ma **quale si adatta meglio a un uso, con i vincoli reali dell'azienda che la userà**: quali suite già usa, quanto sono sensibili i dati che tratterà, quale budget ha, quanta formazione può permettersi di dare al personale.

Questo principio non è una scelta di comodo per evitare di prendere posizione: è il motivo tecnico per cui il percorso di Agritech è costruito così com'è. La scelta dello strumento aziendale arriva **dopo** l'assessment (`context/linee-guida-formazione-base.md`, "Selezione degli strumenti AI"), non prima, proprio perché dipende da fattori che si raccolgono nelle prime giornate, non da una classifica generica.

---

## 7. Il caso specifico di Agritech: la scelta non è ancora fatta

Per questa giornata vale una precisazione che il formatore deve avere chiara, perché è probabile che qualcuno in aula lo chieda direttamente: **Agritech non ha ancora scelto lo strumento AI aziendale**. Secondo quanto risulta al momento (`committenti/agritech/brief.md`), la decisione si prenderà nelle prime giornate del percorso ("fase Fondamenta"), in coordinamento con il referente tecnico interno, l'Ing. Linetti, e non è vincolata a un acquisto già fatto prima dell'inizio del corso. Il percorso è orientato, nell'impostazione generale, verso la famiglia di prodotti Claude, ma questo non significa che le altre famiglie non vadano conosciute: la panoramica resta comparativa per tutto il percorso (`context/linee-guida-formazione-base.md`), e i partecipanti — che dalla giornata 2 avranno dispositivi individuali disponibili — potranno nel frattempo usare lo strumento a cui hanno già accesso, gratuito o personale, qualunque esso sia.

`[DA VERIFICARE]` Quali strumenti siano già in uso in azienda (suite di produttività, gestionale, CRM, archivio disegni tecnici) non risulta ancora mappato: è uno degli elementi che l'assessment formale dovrà raccogliere, perché determina se affiancare Microsoft 365 Copilot o Google Workspace con Gemini alla panoramica comparativa dei chatbot generalisti.

---

## 8. Perché il mercato cambia così in fretta (un cenno, non un approfondimento)

Vale la pena dedicare in aula una sola frase a questo punto, perché spiega perché la mappa di oggi non va imparata a memoria: negli ultimi anni ogni fornitore ha rilasciato nuove versioni dei propri modelli più volte l'anno, spesso con cambi di nome che confondono anche chi segue il settore da vicino — il caso delle etichette interne del modello più recente di ChatGPT (§4.2) è un esempio, non un'eccezione. La conseguenza pratica per un'azienda non è rincorrere ogni annuncio, ma tenere ferma la mappa per famiglie (§2), che cambia molto più lentamente dei singoli nomi di prodotto, e rivalutare la scelta specifica dello strumento a intervalli regolari, non una volta per sempre.

---

## 9. Errori comuni e fraintendimenti

*"Uno di questi è oggettivamente il migliore, gli altri sono scelte sbagliate."* Non esiste un vincitore assoluto: esiste uno strumento più adatto a un uso specifico, con vincoli specifici (§6).

*"Se la mia azienda usa Microsoft, devo per forza usare i prodotti Microsoft anche per l'AI."* Non è obbligatorio: un chatbot generalista di un altro fornitore può comunque essere usato in autonomia, anche se non è integrato nella suite. L'integrazione (famiglia 2) è un vantaggio di comodità, non un vincolo tecnico.

*"L'assistente integrato nella suite è sempre meglio di un chatbot a sé, perché 'sa già tutto' dell'azienda."* Accede a più contesto se autorizzato, ma questo non significa automaticamente risposte migliori su ogni compito: dipende dal compito.

*"Tanto la scelta la fa l'IT, a me non serve saperne nulla."* Chi userà lo strumento ogni giorno è chi meglio può segnalare, durante l'assessment e le prime giornate, quali vincoli reali del proprio lavoro contano per la scelta — è proprio ciò che il percorso di Agritech sta raccogliendo in queste settimane.

---

## 10. Glossario dei termini introdotti

I termini seguono `context/glossario-it.md`. Nel blocco da dieci minuti bastano "chatbot generalista" e "AI integrata": gli altri servono per le domande o per la giornata 3.

**Chatbot generalista** — un assistente AI a cui ci si rivolge in una conversazione a sé stante, tramite sito o app dedicata, indipendente dagli altri strumenti di lavoro dell'azienda.

**AI integrata (negli strumenti di lavoro)** — funzioni AI incorporate dentro i programmi di produttività già in uso (posta, documenti, fogli di calcolo, videoconferenza), con accesso, nei limiti dei permessi, ai contenuti dell'account aziendale.

**Modello aperto (*open-weight*)** — un modello linguistico i cui parametri sono resi disponibili per essere eseguiti su infrastrutture proprie, invece che tramite il servizio online di un fornitore.

**Sovranità digitale / dati** — la possibilità di sapere e controllare dove (in quale paese, sotto quale giurisdizione) vengono trattati i dati inseriti in uno strumento AI; criterio rilevante nella scelta per aziende con requisiti stringenti sulla residenza dei dati.

---

## 11. Punti aperti e da personalizzare

`[DA VERIFICARE]` Tutti i prezzi e i nomi dei piani citati nel §4 vanno riverificati poco prima della lezione: sono la parte del documento più esposta a essere superata dagli eventi, per definizione dell'argomento stesso.

`[DA VERIFICARE]` Gli strumenti già in uso in Agritech (suite di produttività, gestionale, CRM) non risultano ancora mappati (§7): condiziona se il blocco vada arricchito, in una prossima revisione, con un cenno più specifico alla famiglia 2 pertinente per l'azienda.

`[DA PERSONALIZZARE]` Se prima della giornata 1 emergesse un'indicazione più precisa sulla suite di produttività già in uso in Agritech, vale la pena anticipare in aula, con una frase, quale delle due famiglie 2 (Microsoft 365 Copilot o Google Workspace con Gemini) sia più rilevante per l'azienda — resta comunque un cenno, l'approfondimento è in giornata 3.

**Nota per il formatore.** Nel blocco da dieci minuti non entra tutto, e qui meno che altrove: la mappa in due famiglie (§2) è l'unico contenuto che deve arrivare per intero. Se il tempo lo consente, un secondo livello utile è la frase di chiusura del §6 — "non esiste il migliore in assoluto, esiste il più adatto a un uso" — perché è il principio che regge tutto il resto del percorso, comparativo per costruzione. Tutto il resto (§3, §4, §8) è materiale di supporto alle domande e preparazione per la giornata 3, non contenuto da esporre oggi.

---

## 12. Fonti e risorse

Le informazioni su piani, prezzi e nomi dei prodotti sono state verificate tramite ricerca web al momento della redazione (3 settembre 2026) e vanno considerate una fotografia di quel momento, non un dato stabile.

- [Claude Subscription Plans & Pricing 2026 — IntuitionLabs](https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs)
- [Piani ChatGPT | Free, Go, Plus, Pro, Business ed Enterprise — pagina ufficiale OpenAI](https://chatgpt.com/pricing/)
- [GPT-5.6: Frontier intelligence that scales with your ambition — OpenAI](https://openai.com/index/gpt-5-6/)
- [GPT-5.6 in ChatGPT — OpenAI Help Center](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)
- [Gemini pricing 2026: Free vs Pro vs Ultra and API costs — eesel AI](https://www.eesel.ai/blog/gemini-pricing)
- [Microsoft Copilot vs Microsoft 365 Copilot Explained — m365.fm](https://www.m365.fm/blog/microsoft-copilot-vs-microsoft-365-copilot-explained/)
- [M365 Copilot Pricing 2026: $30/User Plus Base Plan Cost — explainx.ai](https://www.explainx.ai/blog/microsoft-365-copilot-pricing-licensing-2026)
- [Le Chat (AI) — Wikipedia](https://en.wikipedia.org/wiki/Le_Chat_(AI))
- [Mistral Vibe (formerly Le Chat) — pagina ufficiale Mistral AI](https://mistral.ai/products/vibe/)
- [Mistral remplace Le Chat par Vibe pour sortir du simple chatbot — Siècle Digital](https://siecledigital.fr/2026/06/01/mistral-remplace-le-chat-par-vibe-pour-sortir-du-simple-chatbot/)
- [Claude Features 2026: Projects, Artifacts, Memory, Computer Use, Skills, MCP — Suprmind](https://suprmind.ai/hub/claude/features/)
- [ChatGPT Plans 2026: Free vs Plus vs Pro Compared — IntuitionLabs](https://intuitionlabs.ai/articles/chatgpt-plans-comparison)
- [Google Gemini 2026: Models, Features, Pricing — Suprmind](https://suprmind.ai/hub/gemini/)
