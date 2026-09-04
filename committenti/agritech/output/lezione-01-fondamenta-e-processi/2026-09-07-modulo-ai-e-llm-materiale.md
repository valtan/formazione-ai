---
titolo: "Che cos'è l'AI, cosa la distingue dall'AI generativa e come funziona un modello linguistico"
committente: Agritech
lezione: "Giornata 1 — Apertura del percorso e prima raccolta di processi"
blocco_in_aula: "Inquadramento frontale (15')"
tipo_sessione: teorica
livello: misto
durata_stimata: "15 min in aula (il documento copre molto di più: è base di conoscenza per il formatore)"
target: "PMI — dipendenti e titolari, pubblico non tecnico; uffici commerciale, tecnico, amministrazione, acquisti"
obiettivi_apprendimento:
  - "Distinguere l'intelligenza artificiale in senso ampio dall'AI generativa, e riconoscere che la prima è già presente in azienda da anni"
  - "Spiegare in una frase che cosa fa un modello linguistico quando genera una risposta"
  - "Capire da dove viene ciò che il modello sa: dati di addestramento, data di aggiornamento, fasi dell'addestramento"
  - "Ricondurre i comportamenti anomali (invenzioni, risposte diverse alla stessa domanda, informazioni non aggiornate) al funzionamento del modello, non a un guasto"
  - "Spiegare perché il salto dell'AI generativa è avvenuto in questi anni, e perché la barriera caduta è quella dell'accesso e non della tecnologia"
prerequisiti: "Nessuno"
data_redazione: "2026-08-28"
stato: "bozza da validare con il formatore"
---

# Che cos'è l'AI, cosa la distingue dall'AI generativa e come funziona un modello linguistico

## Come usare questo documento

Questo non è il testo della lezione: è la base di conoscenza da cui la lezione viene ricavata. In aula il blocco dura una quindicina di minuti e ne userà una parte; il resto serve al formatore per reggere le domande, scegliere quali esempi tenere e quali tagliare, e costruire le slide sapendo che cosa c'è dietro ogni affermazione.

Il documento è volutamente autosufficiente: ogni concetto è spiegato per intero, senza rimandare a fonti esterne. È scritto in modo indipendente dal resto della giornata, quindi non contiene agganci ad altre attività della lezione: può essere collocato dove il formatore preferisce nella scaletta.

Due avvertenze di metodo, valide per tutto il testo. La prima: si spiega il funzionamento senza tecnicismi, ma senza dire cose false per semplificare. Ogni semplificazione usata in aula è indicata insieme al suo limite, perché una semplificazione presentata come verità produce, tre lezioni dopo, un fraintendimento che costa tempo. La seconda: il pubblico è composto da persone che useranno questi strumenti sul lavoro, non da persone che devono costruirli. Il criterio per decidere quanto scendere nel dettaglio è sempre lo stesso — serve a capire meglio *che cosa aspettarsi* dallo strumento, o è curiosità tecnica?

---

## 1. Perché questa distinzione conta per un'azienda

Nel linguaggio corrente "intelligenza artificiale" ha finito per significare "ChatGPT e simili". È una scorciatoia comprensibile, perché è con gli assistenti conversazionali che la maggior parte delle persone ha avuto il primo contatto diretto con l'AI, ma per un'azienda produce tre effetti indesiderati.

Il primo è che rende invisibile ciò che l'azienda già fa. Un'impresa che filtra la posta indesiderata, che legge automaticamente i dati da una fattura, che usa un gestionale con previsione della domanda o un controllo qualità con telecamera sta già usando intelligenza artificiale da anni. Chi crede che l'AI sia arrivata nel 2023 pensa di partire da zero, quando invece parte da un'esperienza aziendale che si può valorizzare.

Il secondo effetto è che confonde le aspettative. L'AI "classica" che l'azienda già usa ha caratteristiche opposte a quelle dell'AI generativa: fa una cosa sola, la fa in modo prevedibile e ripetibile, e quando sbaglia lo si nota subito. L'AI generativa fa moltissime cose diverse, non garantisce di rispondere due volte allo stesso modo, e quando sbaglia lo fa in modo elegante e plausibile. Chi porta le aspettative della prima sulla seconda si fida troppo; chi porta le aspettative della seconda sulla prima si fida troppo poco.

Il terzo effetto riguarda gli obblighi. Le regole europee sull'AI non si applicano a "ChatGPT": si applicano ai sistemi di intelligenza artificiale in senso ampio, e quindi anche a strumenti che l'azienda non ha mai catalogato come AI. Il tema si affronta nella giornata dedicata alla normativa, ma la distinzione concettuale va posta qui, perché senza di essa quel discorso non ha appigli.

---

## 2. Che cos'è l'intelligenza artificiale

### 2.1 Una definizione di lavoro

Si può chiamare intelligenza artificiale un sistema informatico che, a partire da dati in ingresso, produce risultati — previsioni, classificazioni, decisioni, contenuti — usando regole che in larga parte non sono state scritte a mano da un programmatore, ma ricavate automaticamente da esempi.

È una definizione di lavoro, utile per questo corso perché centrata sull'AI basata su apprendimento, che è quella diffusa oggi. La definizione adottata dalla normativa europea è più ampia e comprende anche sistemi costruiti su regole scritte a mano: chi deve ragionare di obblighi non può usare la definizione ristretta.

Il punto decisivo di questa definizione di lavoro è nella seconda metà. Ciò che distingue un sistema di AI da un normale programma non è la difficoltà del compito, né il fatto che sembri "intelligente": è **da dove vengono le regole che il sistema applica**.

Un programma tradizionale funziona per istruzioni esplicite. Qualcuno ha deciso, scrivendolo, che se l'importo supera una certa soglia allora serve l'autorizzazione del responsabile, e che se il codice cliente non è presente in anagrafica allora l'ordine va respinto. Il comportamento del programma è la somma di queste decisioni umane. Se il programma sbaglia, esiste sempre una riga precisa da correggere.

Un sistema di AI funziona per apprendimento da esempi. Nessuno ha scritto la regola che riconosce una fattura da un documento di trasporto: al sistema sono state mostrate grandi quantità di fatture e di documenti di trasporto già classificati, e il sistema ha ricavato da solo le regolarità che li distinguono. Quelle regolarità esistono, ma sono espresse in una forma numerica che nessuno ha scritto e che, per i sistemi più complessi, nessuno riesce a leggere per intero. Se il sistema sbaglia, non esiste una riga da correggere: si interviene sugli esempi o sul modo in cui il sistema è stato addestrato.

Questa differenza ha una conseguenza pratica che vale la pena esplicitare in aula: nell'AI l'errore non è un difetto occasionale da riparare una volta per tutte, è una caratteristica statistica del sistema. Un sistema addestrato bene sbaglia poco, ma sbaglia sempre. Nessun fornitore serio promette lo zero.

### 2.2 La mappa: quattro cerchi uno dentro l'altro

Il modo più efficace per orientarsi è pensare a quattro insiemi concentrici, dal più ampio al più stretto.

L'**intelligenza artificiale** è l'insieme più grande: comprende tutto ciò che fa svolgere a una macchina compiti che associamo all'intelligenza umana. È un'etichetta che esiste dagli anni Cinquanta e che ha compreso, nel tempo, anche sistemi che oggi non chiameremmo più così.

Dentro c'è l'**apprendimento automatico** (*machine learning*): i sistemi che ricavano le proprie regole dai dati anziché riceverle scritte. È qui che sta la stragrande maggioranza dell'AI usata oggi in azienda.

Dentro l'apprendimento automatico c'è l'**apprendimento profondo** (*deep learning*): una famiglia di tecniche basate su reti neurali artificiali, cioè strutture matematiche organizzate in molti strati successivi, capaci di trattare dati non strutturati come immagini, suoni e testo libero. È ciò che ha reso possibile, negli ultimi quindici anni, il riconoscimento vocale e visivo affidabile.

Dentro l'apprendimento profondo c'è l'**AI generativa** che si usa oggi: i sistemi che non si limitano a classificare o prevedere, ma producono contenuto nuovo — testo, immagini, audio, codice, tabelle.

Il messaggio da portare a casa non è la nomenclatura, che si dimentica in mezz'ora: è che **l'AI generativa è un ramo recente di una pianta molto più vecchia**, e che i due tipi convivranno in azienda invece di sostituirsi.

### 2.3 La differenza che conta davvero: riconoscere contro produrre

Sotto le etichette c'è una distinzione operativa semplice, ed è l'unica che i partecipanti devono ricordare.

L'AI non generativa **sceglie tra risposte già definite**. Il sistema antispam decide fra due sole possibilità, indesiderata o no. Il sistema di lettura automatica delle fatture decide quale numero, fra quelli presenti sul foglio, è l'imponibile. Il modello previsionale del gestionale sceglie un numero all'interno di un intervallo plausibile. In tutti questi casi lo spazio delle risposte possibili è deciso in anticipo da chi ha progettato il sistema, e il compito dell'AI è collocarsi dentro quello spazio nel modo più corretto possibile.

L'AI generativa **costruisce una risposta che non esisteva**. Non sceglie fra opzioni predefinite: compone parola dopo parola, pixel dopo pixel, un risultato che nessuno ha preparato in anticipo e che non è archiviato da nessuna parte. Se si pone due volte la stessa domanda si ottengono due testi diversi, entrambi legittimi.

Da questa differenza discendono tutte le altre, ed è utile renderle esplicite. Le due famiglie si comportano in modo opposto su tre dimensioni che contano nel lavoro quotidiano — quanto sono ripetibili, quanti compiti diversi coprono, e quanto è facile accorgersi che hanno sbagliato.

| Dimensione | AI non generativa (antispam, lettura fatture, previsione domanda) | AI generativa (assistenti conversazionali) |
|---|---|---|
| Stesso input, output | Sempre identico | Può variare a ogni richiesta, entro variazioni ragionevoli |
| Compiti coperti | Uno solo, quello per cui è stata addestrata | Molti, anche mai visti prima |
| Errore tipico | Evidente: la fattura finisce nella casella sbagliata | Nascosto: la risposta è ben scritta, sicura di sé e sbagliata |
| Chi se ne accorge | Il sistema o un controllo automatico a valle | Solo una persona competente che verifica |
| Dove sta il lavoro umano | Progettare e mantenere il sistema | Formulare la richiesta e **verificare l'esito**, ogni volta |

L'ultima riga è il motivo per cui esiste un corso di dodici giornate. Con l'AI tradizionale il lavoro umano sta a monte, una volta sola, ed è lavoro da tecnici; con l'AI generativa il lavoro umano sta a valle, tutte le volte, ed è lavoro di chi la usa.

### 2.4 L'AI che è già in azienda senza chiamarsi così

Vale la pena passare qualche minuto su esempi che i partecipanti riconoscono, perché è il momento in cui l'argomento smette di essere astratto. Gli esempi seguenti sono formulati in modo generico e vanno adattati a ciò che l'azienda usa davvero `[DA PERSONALIZZARE — verificare con il referente tecnico quali di questi strumenti sono effettivamente in uso in Agritech]`.

Il **filtro della posta indesiderata** è probabilmente il sistema di AI con cui ogni partecipante interagisce più spesso: nessuno gli ha scritto le regole per riconoscere un messaggio truffaldino, le ha ricavate da quantità enormi di messaggi già classificati, e continua a impararle perché ogni volta che qualcuno segnala un messaggio come indesiderato fornisce un nuovo esempio.

La **lettura automatica dei documenti** — il riconoscimento ottico che estrae numero, data e importo da una fattura scansionata e li scrive nel gestionale — è AI applicata a immagini e testo. Interessa direttamente amministrazione e acquisti.

La **previsione della domanda o del riordino** nei gestionali evoluti stima quanto servirà di un articolo nelle prossime settimane, sulla base dello storico, della stagionalità e talvolta di variabili esterne. È AI di tipo predittivo, quella storicamente più diffusa nelle aziende industriali.

Il **controllo qualità con telecamera**, dove esiste, riconosce difetti su un pezzo confrontandolo con migliaia di esempi di pezzi conformi e non conformi. Interessa in particolare l'ufficio tecnico.

Infine il **completamento automatico** della tastiera del telefono e la **traduzione automatica**: entrambi sono già oggi, in molte implementazioni, forme di AI basata su testo, e il completamento automatico è il ponte più diretto verso la spiegazione dei modelli linguistici, perché fa la stessa cosa in scala minuscola.

### 2.5 Perché proprio adesso

È la domanda che segue naturalmente da tutto quello che precede, e in aula arriva quasi sempre: se l'intelligenza artificiale esiste dagli anni Cinquanta e le reti neurali da decenni, perché il salto è avvenuto in questi anni e non prima?

La risposta più onesta è che non c'è stata una scoperta improvvisa. Non è stato capito qualcosa di nuovo su come funziona l'intelligenza: sono maturate una dopo l'altra quattro condizioni — alcune disponibili da tempo, altre arrivate di recente — che nessuna da sola bastava, e che solo verso la fine degli anni Dieci si sono trovate tutte insieme.

La prima è **un'architettura adatta**. Nel 2017 un gruppo di ricerca di Google pubblica un lavoro — *Attention Is All You Need* — che introduce il *transformer*, il modo di organizzare una rete neurale su cui sono costruiti oggi tutti i principali modelli linguistici. La sua caratteristica decisiva non è essere "più intelligente" delle precedenti, ma essere **parallelizzabile**: i sistemi precedenti dovevano elaborare il testo una parola dopo l'altra, in sequenza, il che rendeva l'addestramento su grandi quantità di testo troppo lento e faticoso il tenere insieme legami fra parti lontane del testo. Il transformer può elaborare in parallelo l'intero testo che riceve, e questo ha reso praticabile un addestramento di dimensioni fino a quel momento fuori portata. Va precisato subito, per non creare confusione con quanto si dirà più avanti: la parallelizzazione riguarda l'addestramento e la lettura della richiesta, mentre la risposta continua a essere generata un pezzo alla volta (§3.5).

La seconda è **la potenza di calcolo**. Le schede grafiche sviluppate per i videogiochi si sono rivelate, quasi per caso, lo strumento adatto: fanno moltissimi calcoli semplici in parallelo, che è esattamente ciò che serve per addestrare una rete neurale. Dai primi anni Dieci in poi questa combinazione ha reso economicamente affrontabili addestramenti che negli anni Novanta sarebbero costati quanto un programma spaziale.

La terza è **la disponibilità dei dati**. Un modello linguistico impara da testo, e la quantità di testo digitalizzato e accessibile è cresciuta enormemente con la diffusione del web. È una condizione che semplicemente non esisteva prima: negli anni Novanta l'architettura giusta e il calcolo giusto non sarebbero bastati, perché mancava il materiale.

La quarta è la meno intuitiva ed è quella che ha convinto le aziende a investire cifre enormi: **la constatazione empirica che aumentare la scala paga**. Aumentando insieme dimensione del modello, quantità di dati e calcolo impiegato, i risultati migliorano in modo sorprendentemente regolare — con una precisazione che vale la pena tenere: ciò che migliora in modo prevedibile è la capacità generale del modello di prevedere il testo, mentre quanto migliorerà su un compito specifico resta difficile da anticipare. Compaiono inoltre capacità che nessuno aveva esplicitamente addestrato, come eseguire un compito nuovo dopo averne visti due o tre esempi nella richiesta; su quanto queste capacità arrivino davvero "di colpo" gli studiosi discutono, perché dipende molto da come le si misura. Che la scala funzionasse così non era affatto scontato e non tutti ci credevano: una volta misurato, è diventato razionale investire su scala industriale.

Le quattro condizioni si leggono meglio insieme, guardando che cosa mancava finché non sono arrivate.

| Condizione | Che cosa mancava prima | Quando è maturata |
|---|---|---|
| Architettura parallelizzabile (transformer) | I modelli elaboravano il testo in sequenza: addestramento troppo lento, legami a distanza difficili da tenere | 2017 |
| Potenza di calcolo a costo sostenibile | L'addestramento su larga scala era fuori portata economica | Dai primi anni Dieci, con l'uso delle schede grafiche |
| Grandi quantità di testo digitalizzato | Non esisteva materiale sufficiente da cui imparare | Con la diffusione del web, anni Duemila-Dieci |
| Evidenza che aumentare la scala paga | Nessuna misura che giustificasse investimenti enormi in un modello più grande | Attorno al 2020, con i primi grandi modelli |

Manca però ancora un pezzo, ed è quello che riguarda più da vicino le persone in aula. Nel 2020 e nel 2021 i grandi modelli linguistici esistevano già ed erano potenti, ma restavano riservati a chi vi accedeva su richiesta, attraverso strumenti per sviluppatori o interfacce sperimentali, e sapeva impostare il testo perché il modello lo continuasse in modo utile. Quello che è cambiato alla fine del 2022, con l'uscita di ChatGPT il 30 novembre, non è stata soprattutto la potenza grezza del modello sottostante: è stato l'insieme fra **un addestramento specifico a seguire istruzioni** (§3.4) e **una forma d'uso accessibile a chiunque**, la conversazione. Una tecnologia che nei laboratori esisteva già da un paio d'anni è diventata utilizzabile senza mediazioni.

Vale la pena dirlo esplicitamente in aula, perché ha una conseguenza sul modo in cui i partecipanti si collocano rispetto a ciò che stanno imparando: **il salto tecnico e il salto percepito non coincidono**. La barriera caduta nel 2022 è stata più di accesso che di potenza bruta. E poiché la barriera caduta è quella dell'accesso, la competenza che serve oggi per usare bene questi strumenti non è una competenza informatica: è saper descrivere con precisione un compito che si conosce bene. È esattamente il motivo per cui un corso come questo si rivolge agli uffici e non alla funzione informatica.

Due avvertenze per chiudere, entrambe da tenere se qualcuno chiede "e adesso cosa succede". La prima è che nulla di tutto questo dice che la macchina abbia iniziato a pensare: le quattro condizioni riguardano scala e accessibilità, non una comprensione nuova dell'intelligenza. La seconda è che il ritmo degli ultimi anni non è una garanzia sui prossimi: ci sono ragioni per pensare che continui — investimenti, margini di miglioramento noti — e ragioni per pensare che rallenti, dal costo energetico alla quantità finita di testo di buona qualità disponibile. In aula conviene dirlo così, senza previsioni: per un'azienda la conseguenza pratica non cambia, ed è che le scelte di strumento vanno prese come scelte revisionabili, non come investimenti definitivi.

---

## 3. Come funziona un modello linguistico

Da qui in avanti l'oggetto è uno solo: il **modello linguistico di grandi dimensioni** (*large language model*, da qui in poi LLM), cioè il motore che sta dentro gli assistenti conversazionali che il percorso userà.

### 3.1 Che cosa fa, in una frase

Un LLM è un sistema che, dato un testo, calcola quale sia la continuazione più plausibile e la produce un pezzo alla volta.

Questa frase va detta in aula esattamente così, perché è insieme corretta e sorprendente. Tutto ciò che un assistente conversazionale sa fare — rispondere a una domanda, riassumere un capitolato, tradurre una mail, riscrivere un testo in tono più formale — è quella singola operazione ripetuta migliaia di volte. Non ci sono moduli separati per il riassunto e per la traduzione: c'è un unico meccanismo che continua il testo, e le diverse funzioni emergono dal fatto che continuazioni plausibili di richieste diverse sono cose diverse.

La reazione tipica dei partecipanti è di incredulità: se fa solo questo, perché sembra ragionare? La risposta onesta è che per prevedere bene la continuazione di un testo qualsiasi bisogna avere colto moltissime regolarità del mondo — grammaticali, logiche, fattuali, argomentative — e queste regolarità, applicate su larga scala, producono un comportamento che assomiglia molto al ragionamento. Se sia ragionamento "vero" è una domanda su cui gli esperti non concordano, e in aula conviene dirlo così, senza risolverla. Ciò che è importante per il lavoro è la conseguenza: il sistema è ottimizzato per produrre risposte **plausibili**, non per produrre risposte **vere**. Nella grande maggioranza dei casi le due cose coincidono, perché nei testi su cui è stato addestrato il vero è molto più frequente del falso. Quando non coincidono, il sistema non se ne accorge e nemmeno segnala il dubbio.

### 3.2 I token: l'unità di misura del testo

Il modello non lavora su parole intere ma su **token**, cioè frammenti di testo. Un token può essere una parola breve e frequente, oppure un pezzo di parola più lunga o rara, oppure un segno di punteggiatura o uno spazio. Una parola comune tende a corrispondere a un solo token; una parola tecnica, un nome proprio o un codice articolo si spezza in più token.

Come ordine di grandezza puramente indicativo, in italiano una parola tende a valere attorno a un token e mezzo, con variazioni ampie secondo il tipo di testo. L'italiano è meno efficiente dell'inglese da questo punto di vista, e la ragione non è la lunghezza delle parole: i sistemi di tokenizzazione sono stati costruiti su testi in larga prevalenza inglesi e frammentano di più tutte le altre lingue. Una pagina di testo fitto si aggira quindi attorno al migliaio di token, un capitolato di venti pagine attorno alle ventimila. Sono stime grossolane, buone per farsi un'idea di scala e non per fare conti: il rapporto esatto dipende dallo strumento.

I token meritano cinque minuti perché sono l'unità in cui si misurano due cose che i partecipanti incontreranno di continuo: **quanto testo il modello riesce a considerare per volta** (la finestra di contesto) e **quanto costa** l'uso professionale a consumo. Nei piani gratuiti e in abbonamento individuale, invece, i limiti d'uso sono in genere espressi in numero di messaggi per finestra temporale e cambiano nel tempo: chi cercasse un contatore di token nel proprio piano non lo troverebbe. Oltre a questo i token non servono, e non vale la pena andare oltre.

### 3.3 Da dove viene ciò che il modello "sa": i dati di addestramento

Un LLM viene costruito facendogli elaborare un'enorme quantità di testo: pagine web, libri, documentazione tecnica, articoli, codice informatico, discussioni pubbliche, materiale acquistato o concesso in licenza. Le proporzioni esatte e l'elenco delle fonti non sono resi pubblici in modo completo da nessuno dei principali fornitori, e in aula conviene dirlo apertamente invece di lasciarlo intuire: è una delle ragioni per cui il tema del diritto d'autore sui dati di addestramento è oggetto di controversie legali tuttora aperte `[DA VERIFICARE — se si intende citare un caso specifico, verificarne lo stato aggiornato prima della lezione]`.

Da questa massa di testo derivano tre conseguenze che spiegano gran parte dei comportamenti osservabili.

**Il modello conosce bene ciò che è ben rappresentato nei testi, e male ciò che non lo è.** Sa moltissimo di argomenti generali e discussi ovunque; sa molto meno di nicchie tecniche poco documentate, di normativa locale di dettaglio, di prodotti di aziende piccole. Ed è del tutto ignaro di ciò che non è mai stato pubblicato: i listini dell'azienda, lo storico dei fornitori, le condizioni negoziate con un cliente, la prassi interna dell'ufficio. Questo è il punto più utile da fissare per un'azienda: **il modello non sa nulla di voi finché non glielo dite**. Le funzionalità che sembrano contraddire questa affermazione — la memoria delle conversazioni, i progetti con documenti allegati, i collegamenti agli archivi aziendali — non fanno eccezione: non aggiungono conoscenza al modello, gli mettono davanti dei testi al momento della richiesta. Il meccanismo si chiama ancoraggio ai documenti e si affronta più avanti nel percorso.

**Il modello ha una data di aggiornamento.** L'addestramento si ferma a un certo punto, e da quel punto in poi il modello non sa più nulla del mondo, salvo che lo strumento sia collegato a una ricerca web o a fonti esterne — cosa che oggi molti prodotti fanno, ma non sempre e non in tutte le versioni. Chiedere a un modello quale sia la normativa vigente, quale il prezzo corrente di un materiale o chi ricopra oggi un certo ruolo è una richiesta esposta a errore, e il modello risponderà comunque, con la stessa sicurezza con cui risponde a tutto il resto.

**Il modello eredita le distorsioni dei testi.** Se in ciò che ha letto certe associazioni sono più frequenti di altre — fra mansioni e generi, fra provenienze e caratteristiche, fra settori e stereotipi — quelle associazioni ricompaiono nelle risposte. Non è una scelta del sistema, è un riflesso statistico del materiale. Ha ricadute concrete nei testi che si scrivono per l'esterno, e va tenuto presente in tutte le attività in cui l'output riguarda persone.

### 3.4 Le tre fasi dell'addestramento

Costruire un assistente basato su un LLM comporta tipicamente almeno tre passaggi successivi — le pipeline reali variano da fornitore a fornitore e oggi ne comprendono altri, in particolare un addestramento dedicato al ragionamento. La distinzione è utile perché ciascuno spiega comportamenti diversi, e perché smonta l'idea che il modello sia stato "programmato per rispondere così".

**Il pre-addestramento** è la fase lunga e costosa. Al sistema viene mostrato testo e viene chiesto ripetutamente di prevedere il token successivo; ogni volta che sbaglia, i suoi parametri interni — molti miliardi di valori numerici — vengono corretti di una quantità minima. Ripetuto un numero enorme di volte su un'enorme quantità di testo, questo procedimento fa emergere nei parametri le regolarità della lingua e, con esse, molta conoscenza del mondo. Alla fine di questa fase il sistema è bravissimo a continuare testo, ma non è ancora un assistente: se gli si scrive una domanda, è altrettanto plausibile che risponda oppure che aggiunga altre tre domande simili, come farebbe un questionario.

**L'ottimizzazione con esempi di istruzioni** (*instruction tuning*, una forma di *fine-tuning*) trasforma il continuatore di testo in un assistente. Al modello vengono mostrate molte coppie richiesta-risposta scritte o selezionate da persone, che gli insegnano il formato dello scambio: quando arriva una domanda, la continuazione appropriata è una risposta.

**L'allineamento tramite feedback** è la fase che regola il comportamento. Risposte diverse allo stesso input vengono confrontate e si indica quale è migliore — più utile, più chiara, più onesta, meno dannosa — e queste preferenze vengono usate per orientare il modello. Il confronto è svolto da persone incaricate e, in misura crescente, da altri modelli sotto supervisione umana. È qui che si stabilisce il tono, la disponibilità a rifiutare richieste problematiche, l'abitudine a segnalare i propri limiti.

Da questa terza fase discende un'osservazione importante per un pubblico aziendale: **il comportamento di un assistente riflette scelte fatte da chi lo ha costruito**. Due strumenti costruiti sullo stesso principio possono avere tono, cautele e rifiuti diversi perché diverse sono state le preferenze usate per allinearli. Non esiste un assistente "neutro", ed è una delle ragioni per cui il confronto fra strumenti diversi sullo stesso compito è un esercizio istruttivo e non un puntiglio.

### 3.5 Che cosa succede quando si preme invio

La sequenza è più semplice di quanto ci si aspetti, e vale la pena percorrerla una volta.

Il testo scritto dall'utente viene spezzato in token e passato al modello insieme a tutto ciò che fa parte del contesto: le istruzioni generali dello strumento, il resto della conversazione, gli eventuali documenti allegati — per intero se stanno nella finestra, altrimenti, a seconda del prodotto, solo le porzioni che il sistema giudica pertinenti alla richiesta. Il modello calcola quali token potrebbero venire dopo, assegnando a ciascuno una probabilità; ne sceglie uno, lo aggiunge al testo, e ricomincia il calcolo con il testo così allungato. Va avanti così fino a quando la continuazione più plausibile è "qui finisce la risposta". È esattamente il motivo per cui le risposte compaiono a schermo scorrendo: non sono pronte e poi mostrate, sono costruite mentre si leggono.

Un dettaglio di questo meccanismo spiega una delle domande più frequenti in aula. La scelta del token successivo non prende sempre il più probabile in assoluto: negli assistenti conversazionali la generazione include, per impostazione predefinita, un margine di casualità, governato da un parametro chiamato **temperatura** — di norma non modificabile dall'utente nelle interfacce di uso comune, mentre lo è nell'uso tecnico via programmazione. È il motivo per cui la stessa domanda, posta due volte, può produrre due risposte diverse. Non è un'incoerenza né un malfunzionamento: è una scelta di progetto, perché prendere sempre il token più probabile produce testi rigidi e ripetitivi. Non è nemmeno una regola ferrea nei due sensi: su domande brevi e fattuali la risposta risulta spesso identica, e in configurazione tecnica la casualità si può azzerare. La conseguenza pratica da fissare è quindi più prudente: **sulla riproducibilità di un LLM non si può contare**. Se un'attività richiede che lo stesso input dia sempre lo stesso risultato — un calcolo, una classificazione da riportare a sistema, una procedura certificata — un assistente conversazionale non è lo strumento adatto, o va usato dentro controlli che ne verifichino l'esito.

Un secondo dettaglio riguarda il fatto che il modello, di per sé, non ha memoria. Ogni richiesta gli arriva insieme a tutta la conversazione precedente: è questo che dà l'impressione della continuità. Quando la conversazione supera la finestra di contesto il comportamento dipende dal prodotto: alcuni tagliano le parti più vecchie, altri le riassumono automaticamente e reinseriscono il riassunto, altri ancora bloccano la conversazione e chiedono di aprirne una nuova. Va aggiunto che l'esperienza dell'assistente che "si dimentica" un'istruzione data all'inizio di uno scambio lungo compare spesso anche **prima** di aver saturato la finestra, perché l'aderenza alle porzioni centrali di un contesto molto ampio tende a degradare: non basta restare sotto il limite perché il problema non si presenti. Le funzioni di memoria offerte da alcuni prodotti aggirano il problema salvando note fra una conversazione e l'altra e reinserendole nel contesto, ma il principio non cambia: ciò che non è nel contesto, per il modello non esiste.

### 3.6 Quattro cose che un LLM non è

Ogni fraintendimento di questo elenco produce, nell'uso quotidiano, un errore prevedibile.

**Non è un archivio.** Non contiene i testi su cui è stato addestrato e non li consulta per rispondere: contiene i parametri numerici che quei testi hanno modellato. È il motivo per cui può riportare in modo impreciso una citazione, un articolo di legge o un dato che pure "conosce": non lo sta leggendo da nessuna parte, lo sta ricostruendo.

**Non è un motore di ricerca.** Alcuni strumenti sanno cercare sul web, ma è una funzione aggiuntiva che si attiva in certi casi e non in altri; il modello in sé non consulta nulla. Distinguere se la risposta che si sta leggendo viene dal modello o da una fonte consultata è una competenza pratica, e si riconosce dagli indicatori espliciti dell'interfaccia — l'avviso che la ricerca è in corso o attiva — non dalla semplice presenza di link nel testo: un modello può generare riferimenti verosimili e inesistenti. I link vanno comunque aperti, per verificare che esistano e che dicano ciò che la risposta sostiene.

**Non è un calcolatore.** Un modello che prevede token non esegue aritmetica; la simula, e su numeri lunghi o passaggi multipli sbaglia. Molti strumenti oggi delegano i conti a un vero calcolatore o a codice eseguito a parte, ma non sempre e non in modo visibile. I risultati numerici vanno verificati.

**Non impara dalle conversazioni mentre le fa.** L'apprendimento avviene nelle fasi di addestramento, non durante l'uso: un modello non "diventa più bravo" perché lo si corregge in chat, e la correzione vale solo per la conversazione in corso. Questione distinta, e importante per l'azienda, è se i testi inseriti vengano **conservati e usati per addestramenti futuri**: dipende dal prodotto, dal piano di abbonamento e dalle impostazioni, cambia nel tempo, e va verificato per lo strumento che l'azienda sceglierà `[DA VERIFICARE — da confermare per lo strumento aziendale, in coordinamento con il referente tecnico; il tema si approfondisce nella giornata dedicata alla normativa]`.

---

## 4. Che cosa ne segue nel lavoro quotidiano

Le proprietà descritte sopra non sono curiosità: sono la spiegazione di tutto ciò che i partecipanti sperimenteranno nelle settimane successive. Conviene chiudere il blocco mostrando il legame, senza svilupparlo — ciascuno di questi punti ha il suo spazio più avanti nel percorso.

Il modello produce testo plausibile, quindi può produrre **contenuto falso scritto benissimo**: è quella che si chiama allucinazione, e riguarda soprattutto riferimenti puntuali — nomi, date, cifre, articoli di legge, fonti. Non si elimina; si gestisce verificando ciò che è verificabile e non delegando mai il controllo finale allo strumento.

Il modello ha una data di aggiornamento e non conosce l'azienda, quindi **il contesto va fornito**: è la ragione per cui esiste una tecnica del prompt, e per cui una richiesta ben costruita produce risultati incomparabilmente migliori della stessa richiesta buttata lì.

Il modello riceve tutto ciò che gli si scrive, quindi **ciò che si scrive è una decisione**. Dati personali, dati di clienti e fornitori, informazioni coperte da riservatezza: il tema è normativo e organizzativo prima che tecnico, e ha una giornata dedicata.

Il modello non è riproducibile e non è un calcolatore, quindi **non tutti i compiti sono suoi**. Una parte importante del percorso consiste esattamente nel riconoscere quali attività dell'ufficio si prestano e quali no.

---

## 5. Analogie utilizzabili in aula, e i loro limiti

Le analogie funzionano se dichiarate come tali e se se ne indica il punto di rottura. Le tre seguenti sono state scelte perché sono verificabili dall'esperienza diretta dei partecipanti.

**Il completamento automatico della tastiera del telefono.** È l'analogia più fedele al meccanismo: anche il telefono propone la parola successiva sulla base di ciò che è stato scritto finora. Un LLM fa la stessa cosa con una capacità incomparabilmente maggiore di tenere conto del contesto — non le ultime due parole ma l'equivalente di molte decine o centinaia di pagine, con differenze enormi fra strumenti e piani — e questo salto di scala cambia la natura del risultato. *Dove si rompe*: il completamento del telefono non risponde a domande e non segue istruzioni; se qualcuno conclude "quindi è solo un correttore automatico", l'analogia ha fatto danno e va corretta subito.

**Il collaboratore appena assunto con un'enorme cultura generale.** Ha letto moltissimo, si esprime bene in diverse lingue, sa impostare un documento in qualunque formato gli si chieda. Ma è il suo primo giorno: non conosce i vostri clienti, non ha accesso ai vostri archivi, non sa come si fanno le cose qui dentro, e ha il difetto di non ammettere mai di non sapere. Con lui si lavora bene se gli si dà il contesto e se si rilegge ciò che produce. *Dove si rompe*: un collaboratore impara dall'esperienza e dopo sei mesi non ha più bisogno delle stesse spiegazioni; il modello ricomincia da capo ogni volta, salvo ciò che gli viene rimesso davanti.

**La ricetta invece della dispensa.** Chi cerca un dato in un archivio apre un cassetto e prende ciò che c'è; il modello non ha cassetti, ha un metodo per ricostruire qualcosa che assomigli molto a ciò che dovrebbe esserci. È il modo più rapido per spiegare perché una citazione può risultare quasi giusta. *Dove si rompe*: l'analogia suggerisce che il modello sbagli sempre, mentre nella maggior parte dei casi la ricostruzione è corretta — il problema è che l'errore, quando c'è, non si distingue dal resto.

Da evitare, invece, l'analogia con il cervello umano. Le reti neurali si chiamano così per una lontanissima ispirazione storica, ma dire che il modello "funziona come un cervello" è falso e produce, in un pubblico non tecnico, attribuzioni di intenzione e coscienza che poi vanno smontate una per una.

---

## 6. Errori comuni e fraintendimenti

Le convinzioni che seguono ricorrono con regolarità in aula. Vale la pena anticiparle: intercettate qui, non tornano più.

*"L'AI è arrivata con ChatGPT."* È arrivata da decenni, ed è già in azienda. Ciò che è cambiato di recente è che è diventata utilizzabile da chiunque, senza intermediari tecnici. Il cambiamento sta nell'accesso, non nell'esistenza.

*"Se sbaglia, vuol dire che è difettoso."* Sbagliare è una proprietà del sistema, non un guasto. Il metro di giudizio non è "sbaglia o no" ma "sbaglia abbastanza poco, in modo abbastanza riconoscibile, da farmi risparmiare tempo netto".

*"Mi ha risposto in modo diverso da ieri, quindi non è affidabile."* La variabilità è progettata. Va distinta dall'inaffidabilità: due risposte diverse possono essere entrambe corrette.

*"Cerca su internet e mi riporta ciò che trova."* Solo se lo strumento ha quella funzione ed è attiva in quel momento. Altrimenti sta ricostruendo dalla propria conoscenza, ferma alla data di aggiornamento.

*"Non posso usarlo, i miei dati finiscono in pasto all'AI."* Merita una risposta seria e non liquidatoria: dipende dallo strumento, dal piano e dalle impostazioni, e la differenza fra un piano gratuito e un contratto aziendale è sostanziale. Il tema si affronta per intero più avanti; qui basta non archiviare la preoccupazione come infondata, perché non lo è.

*"Prima o poi imparerà da solo il mio lavoro."* Non nel modo in cui lo si intende. Il modello non impara dall'uso; il patrimonio che l'azienda costruisce sta nei documenti, nei contesti e nelle istruzioni riutilizzabili che le persone imparano a preparare — cioè in ciò che il percorso costruirà nei cicli applicativi.

---

## 7. Glossario dei termini introdotti

I termini seguono `context/glossario-it.md`. Vanno introdotti solo se effettivamente usati in aula: nel blocco da quindici minuti ne bastano tre o quattro.

**Intelligenza artificiale** — nella definizione di lavoro usata qui: sistema informatico che ricava dai dati, anziché ricevere scritte, le regole con cui produce previsioni, classificazioni o contenuti. La definizione normativa europea è più ampia (vedi §2.1).

**Apprendimento automatico** (*machine learning*) — l'insieme delle tecniche con cui un sistema ricava le proprie regole da esempi.

**AI generativa** — la famiglia di sistemi che produce contenuto nuovo (testo, immagini, audio, codice) invece di scegliere fra risposte predefinite.

**Modello linguistico di grandi dimensioni** (LLM) — il motore degli assistenti conversazionali: prevede e genera testo un token alla volta.

**Token** — l'unità minima di testo su cui lavora il modello: una parola breve, un pezzo di parola lunga, un segno di punteggiatura.

**Finestra di contesto** — la quantità di testo che il modello riesce a considerare in una volta sola, comprensiva delle istruzioni dello strumento, della conversazione e di ciò che entra dei documenti allegati.

**Prompt** — l'istruzione che si dà al modello. Resta invariato in italiano.

**Allucinazione** — un'informazione inventata dal modello e presentata come vera, in genere ben scritta e plausibile.

**Temperatura** — il parametro che regola quanta casualità c'è nella scelta del token successivo, e quindi quanto le risposte possono variare fra loro. Nelle interfacce di uso comune non è modificabile dall'utente.

**Ottimizzazione** (*fine-tuning*) — l'addestramento aggiuntivo su esempi selezionati con cui un modello pre-addestrato viene specializzato o trasformato in assistente.

**Bias** (distorsione) — la ricomparsa nelle risposte delle associazioni sistematiche presenti nei testi di addestramento.

---

## 8. Punti aperti e da personalizzare

`[DA PERSONALIZZARE]` Gli esempi di AI già presente in azienda (§2.4) vanno confermati con il referente tecnico Agritech: citare strumenti che l'azienda non usa indebolisce l'argomento, citare quelli giusti lo rende immediato.

`[DA VERIFICARE]` La questione della conservazione dei testi inseriti e del loro uso per addestramenti futuri (§3.6) va verificata sullo strumento che l'azienda sceglierà, e ricontrollata poco prima della lezione: è materia che cambia.

`[DA VERIFICARE]` Se in aula si vorranno citare contenziosi in corso sul diritto d'autore dei dati di addestramento (§3.3), lo stato dei procedimenti va verificato prima della lezione.

**Nota per il formatore.** Nel blocco da quindici minuti non entra tutto. La selezione che regge meglio è: la mappa dei quattro cerchi ridotta all'osso, la distinzione fra riconoscere e produrre (§2.3), due esempi di AI già in azienda, la frase che definisce che cosa fa un LLM (§3.1), il fatto che il modello non conosce l'azienda e ha una data di aggiornamento (§3.3), e la variabilità delle risposte (§3.5). Del "perché adesso" (§2.5) in quindici minuti entra una frase sola — *non una scoperta improvvisa, ma quattro condizioni che a un certo punto si sono trovate insieme; e nel 2022 è caduta una barriera di accesso più che di potenza* — che però conviene dire, perché è la risposta a una domanda che in aula arriva comunque. Il resto della sezione serve per quando arriva davvero. Il resto del documento serve per le domande e per le lezioni successive.

---

## 9. Fonti e risorse

Le due date puntuali citate in §2.5 sono state verificate con le fonti qui sotto; le altre collocazioni temporali della stessa sezione sono indicative. Il resto del documento poggia su conoscenza consolidata e non su fonti puntuali.

- [Attention Is All You Need — voce di sintesi sul lavoro che introduce il transformer (2017)](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need)
- [Introducing ChatGPT — annuncio di OpenAI, 30 novembre 2022](https://openai.com/index/chatgpt/)
