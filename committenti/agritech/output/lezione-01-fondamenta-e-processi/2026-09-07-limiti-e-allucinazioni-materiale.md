---
titolo: "Limiti e allucinazioni: perché l'output va sempre verificato"
committente: Agritech
lezione: "Giornata 1 — Apertura del percorso e prima raccolta di processi"
blocco_in_aula: "Frontale + esempi (10', 17:50–18:00)"
tipo_sessione: teorica
livello: misto
durata_stimata: "10 min in aula (il documento copre molto di più: è base di conoscenza per il formatore)"
target: "PMI — dipendenti e titolari, pubblico non tecnico; uffici commerciale, tecnico, amministrazione, acquisti"
obiettivi_apprendimento:
  - "Definire che cos'è un'allucinazione e perché non è un guasto occasionale ma una proprietà strutturale del modo in cui un LLM genera testo"
  - "Riconoscere le situazioni in cui il rischio di allucinazione è più alto: fatti puntuali, numeri, citazioni, informazioni recenti, argomenti di nicchia, richieste vaghe"
  - "Collocare le allucinazioni dentro una famiglia più ampia di limiti dell'AI generativa (bias, dipendenza cognitiva, assenza di responsabilità del sistema) senza confonderle con essi"
  - "Applicare una regola pratica di verifica prima di usare un output AI in un contesto che conta: un'email a un cliente, un dato in un documento, un riferimento normativo"
prerequisiti: "Utile ma non indispensabile aver seguito, nella stessa giornata, il blocco introduttivo su cos'è un LLM (`2026-09-07-modulo-ai-e-llm-materiale.md`, in particolare §3.1 e §3.6)"
data_redazione: "2026-09-03"
stato: "bozza da validare con il formatore"
---

# Limiti e allucinazioni: perché l'output va sempre verificato

## Come usare questo documento

Questo non è il testo della lezione: è la base di conoscenza da cui il blocco viene ricavato. In aula il blocco dura dieci minuti; il resto serve al formatore per reggere le domande, scegliere gli esempi giusti per Agritech e costruire le slide sapendo che cosa c'è dietro ogni affermazione.

Una nota di raccordo, da leggere prima di preparare le slide. La scaletta della giornata (`scaletta-lezione.md`) colloca questo blocco **prima** dell'esercizio di gruppo sul prompting (Fase A, 18:10–18:35), ma lo descrive come "aggancio agli errori emersi nell'esercizio". Le due cose, lette insieme, sono in tensione: l'esercizio non è ancora avvenuto quando si arriva a questo blocco. Il documento propone quindi due modi per tenere fede allo spirito dell'aggancio senza un evento passato a cui appoggiarsi, e il formatore sceglie quello più naturale in aula (si veda la nota degli errori comuni §9 e la nota di raccordo in chiusura, §10):

1. **Aggancio in avanti** — si presenta il tema come una lente che i partecipanti useranno tra poco: "tenete a mente questo, perché tra venti minuti lo vedremo dal vivo nel vostro stesso lavoro di gruppo". Il richiamo si chiude poi rapidamente durante il debrief della Fase A, con un commento di trenta secondi.
2. **Inversione dell'ordine** — se il formatore preferisce un aggancio autentico e non un rimando, un'alternativa è scambiare l'ordine dei due blocchi da 10 minuti (Limiti e allucinazioni ↔ Panoramica del mercato) con l'apertura dell'esercizio Fase A, spostando "Limiti e allucinazioni" subito dopo il debrief di Fase A. È un cambio di scaletta, quindi va deciso e comunicato, non eseguito in autonomia.

Il resto del documento è scritto in modo indipendente da quale opzione si sceglierà.

Due avvertenze di metodo, riprese dal materiale sulla stessa giornata e valide anche qui. La prima: si spiega senza tecnicismi ma senza dire cose false per semplificare; ogni semplificazione porta con sé il proprio limite. La seconda: il pubblico userà questi strumenti sul lavoro, non li costruirà — il criterio per scendere nel dettaglio è sempre "serve a capire meglio cosa aspettarsi dallo strumento?".

---

## 1. Perché questo argomento conta per un'azienda

Delle tre cose che un'azienda deve sapere sull'AI generativa prima di adottarla — che cos'è, che cosa può fare, che cosa può sbagliare — la terza è quella più spesso saltata nelle presentazioni commerciali e quella con le conseguenze più dirette. Un errore di un foglio di calcolo tradizionale si vede: una cella con la formula sbagliata restituisce un numero assurdo, o un errore. Un errore di un assistente conversazionale, quasi sempre, non si vede: è scritto bene, è formattato bene, ha lo stesso tono sicuro di tutto il resto della risposta. La differenza tra un output corretto e uno sbagliato non sta nell'aspetto, sta nel contenuto — ed è per questo che verificare non è un passaggio facoltativo per i più prudenti, è parte del lavoro tanto quanto scrivere il prompt.

Le conseguenze di non verificare non sono ipotetiche. Un dato inventato che finisce in un'offerta commerciale, un riferimento normativo sbagliato citato in una comunicazione a un cliente, una specifica tecnica indicata in un capitolato che non corrisponde a quella reale: sono tutti scenari in cui l'errore prodotto dall'AI diventa un errore dell'azienda, con lo stesso peso — commerciale, contrattuale, reputazionale — di un errore scritto direttamente da una persona. Il paragrafo §5 riporta due casi reali in cui questo è successo davvero, in un tribunale, a un'azienda vera.

Questo blocco non serve a scoraggiare l'uso dell'AI generativa: il resto del percorso è costruito apposta per portare i partecipanti a usarla ogni giorno. Serve a stabilire, fin dal primo giorno, un riflesso: **l'output si legge sempre prima di usarlo**, e per gli usi che contano si verifica anche il contenuto, non solo la forma.

---

## 2. Che cos'è un'allucinazione

Un'**allucinazione** è un contenuto che il modello presenta come un fatto, con lo stesso tono sicuro con cui presenta i contenuti corretti, ma che è inventato: un dato che non esiste, una citazione che non esiste, un evento che non è mai accaduto, un dettaglio tecnico plausibile ma sbagliato. Il termine è tecnico ed è quello adottato in tutto il settore (in inglese *hallucination*); non implica nulla di simile a un'esperienza percettiva umana, è un nome scelto per analogia e ormai consolidato.

Tre caratteristiche distinguono un'allucinazione da un errore comune, e vale la pena fissarle in aula perché sono quelle che rendono il fenomeno insidioso.

**Non è segnalata.** Un programma tradizionale che non riesce a completare un'operazione, di solito, restituisce un errore o un valore vuoto. Un modello linguistico non ha un equivalente affidabile di "non lo so": produce comunque una risposta completa, formattata, sicura di sé. Non esiste, nell'interfaccia di un assistente conversazionale, un segnale coerente che distingua "questo lo so con certezza" da "questo l'ho ricostruito nel modo più plausibile che ho trovato".

**È plausibile, non casuale.** Un'allucinazione tipica non è un errore grossolano che salta all'occhio: è un dato verosimile, coerente con il contesto, spesso vicino alla realtà ma non esatto — un numero di articolo di legge sbagliato di una cifra, il nome di una norma quasi giusto, una cifra plausibile ma inventata. Questa somiglianza con il vero è ciò che rende il controllo necessario anche quando l'output "sembra" corretto.

**Non è un difetto isolato di uno strumento specifico.** Non è un bug che un aggiornamento futuro elimina, ed è una precisazione importante da dare in aula perché la domanda "ma i modelli più recenti non l'hanno risolto?" arriva quasi sempre. Il fenomeno si riduce di frequenza col migliorare dei modelli e con l'aggiunta di strumenti di verifica (ricerca web integrata, citazione delle fonti), ma non ha una soluzione strutturale nota, perché discende dal modo stesso in cui un LLM genera testo (§3). Ogni fornitore serio lo dichiara nelle proprie condizioni d'uso.

---

## 3. Perché succede: il meccanismo

Per capire perché le allucinazioni non sono un difetto risolvibile occorre richiamare, in una frase, come funziona un modello linguistico (per l'approfondimento completo, si veda `2026-09-07-modulo-ai-e-llm-materiale.md`, §3.1 e §3.5): un LLM calcola, un pezzo di testo alla volta, quale sia la continuazione più **plausibile** di ciò che ha davanti. Non ha, da nessuna parte nella propria architettura, un modulo separato che verifica se un'affermazione è vera prima di scriverla. Il vero e il plausibile, nella grandissima maggioranza dei casi, coincidono — perché nei testi su cui il modello è stato addestrato il vero è molto più frequente del falso — ma quando non coincidono il sistema non se ne accorge, e continua a scrivere con la stessa sicurezza.

Da questo meccanismo derivano cinque condizioni che aumentano concretamente il rischio, ed è la lista più utile da avere in mente quando si valuta un output.

**Fatti puntuali.** Nomi propri, date, cifre esatte, numeri di articoli di legge, titoli precisi di documenti: sono l'informazione più difficile da ricostruire in modo plausibile ma corretto, perché richiede di riprodurre esattamente un dettaglio invece di una tendenza generale del linguaggio. Un riassunto concettuale di una norma è quasi sempre più affidabile del numero esatto dell'articolo che la contiene.

**Argomenti di nicchia o poco documentati.** Normativa regionale di dettaglio, prassi interne di un singolo settore, specifiche tecniche di prodotti di aziende piccole, dati che non sono mai stati pubblicati online: tutto ciò su cui il modello ha visto pochi esempi durante l'addestramento è terreno fertile per l'invenzione plausibile, perché il modello "generalizza" da ciò che somiglia di più, anche quando somiglia poco.

**Informazioni successive alla data di aggiornamento del modello.** Se lo strumento non ha una funzione di ricerca web attiva in quel momento, tutto ciò che riguarda l'attualità — normativa appena entrata in vigore, prezzi correnti, chi ricopre oggi un ruolo — è una richiesta esposta a errore, perché il modello risponde comunque, attingendo a ciò che sapeva all'ultimo aggiornamento, senza segnalare che l'informazione potrebbe essere superata.

**Richieste vaghe o sottospecificate.** Quando il prompt non fornisce un dettaglio necessario, il modello non si ferma a chiederlo (salvo che lo strumento sia impostato per farlo): lo **inventa**, nel modo più plausibile compatibile con il resto della richiesta. È il punto di contatto più diretto con l'esercizio di prompting della giornata (si veda §10): un prompt che lascia impliciti il destinatario, il tono o i dati specifici di un'email costringe il modello a colmare quei vuoti da solo, e ciò che sceglie di mettere al posto del vuoto è, in piccolo, lo stesso meccanismo che produce un'allucinazione su un fatto.

**Richieste che spingono verso una risposta gradita.** Quando una domanda contiene già, in modo esplicito o implicito, l'aspettativa di chi la pone — "questo prodotto rispetta la normativa X, vero?", "conferma che questi dati sono corretti" — il modello tende a assecondare l'aspettativa più spesso di quanto farebbe partendo da una domanda neutra. Il fenomeno si chiama compiacenza (*sycophancy*) e non è un capriccio: nasce dal modo in cui i modelli vengono allineati alle preferenze umane durante l'addestramento (`2026-09-07-modulo-ai-e-llm-materiale.md`, §3.4), che premia le risposte percepite come utili e concordanti più spesso di quanto punisca quelle corrette ma sgradite.

---

## 4. Le forme più comuni di allucinazione

Gli esempi che seguono sono costruiti per essere riconoscibili dagli uffici presenti in aula (commerciale, tecnico, amministrazione, acquisti) e sono **scenari illustrativi**, non casi reali documentati: servono a mostrare il meccanismo, non a riportare un fatto accaduto. Vanno presentati in aula dicendolo esplicitamente, per non confonderli con i casi reali del §5.

**Cifre e specifiche inventate.** Si chiede a un assistente il valore di una tolleranza meccanica, la portata di un componente, la percentuale di un'aliquota: il modello restituisce un numero plausibile, formattato come se fosse un dato di scheda tecnica, che può non corrispondere a nulla di reale. Il rischio è massimo quando il numero non viene poi confrontato con la scheda tecnica o il capitolato originali.

**Citazioni e riferimenti inventati.** Si chiede quale norma regoli un aspetto della documentazione di trasporto internazionale, o quale articolo di un contratto tipo disciplini una clausola: il modello può restituire un numero di articolo, un titolo di legge o persino un estremo giurisprudenziale del tutto plausibili ma inesistenti. È la forma di allucinazione più studiata e quella con le conseguenze più gravi documentate (§5.2).

**Entità inventate.** Il nome di un fornitore "tipico" per un certo materiale, un numero di certificazione, un codice prodotto: se il modello non conosce il dato reale e la richiesta non lascia spazio a un "non lo so", tende a produrre un'entità verosimile per il contesto (il nome suona plausibile per il settore, il formato del codice è quello giusto) ma inventata.

**Incoerenza interna.** A volte l'allucinazione si nota non confrontando l'output con una fonte esterna, ma leggendo l'output stesso con attenzione: due cifre che dovrebbero coincidere e non coincidono, un totale che non torna con le righe che lo compongono, una data citata due volte in modo diverso nello stesso testo. È il segnale più economico da controllare, perché non richiede altra fonte che il testo stesso.

**Compiacenza.** Si chiede conferma di qualcosa che si crede vero ma non lo è — "questa clausola è standard, giusto?" — e il modello conferma, invece di segnalare il dubbio. È la forma più difficile da intercettare, perché non produce un dato palesemente strano: rafforza un errore che l'utente ha già in testa.

---

## 5. Due casi reali, per capire la posta in gioco

### 5.1 Il chatbot di Air Canada e lo sconto per lutto (2022–2024)

Nel 2022 un cliente, Jake Moffatt, chiese al chatbot del sito di Air Canada informazioni sullo sconto per lutto (*bereavement fare*). Il chatbot rispose che lo sconto poteva essere richiesto compilando un modulo online entro 90 giorni dall'emissione del biglietto, **anche dopo il viaggio**. Sulla base di questa indicazione, Moffatt acquistò un biglietto a tariffa piena, contando di ottenere in seguito la differenza. La pagina ufficiale della compagnia, però, diceva altro: lo sconto per lutto **non è applicabile a viaggi già avvenuti** e va richiesto prima della partenza. Quando Moffatt presentò la richiesta, Air Canada la respinse, sostenendo — questo è il punto centrale del caso — di **non essere responsabile** delle informazioni fornite dal proprio chatbot, definito "un'entità legale separata".

Il Civil Resolution Tribunal della British Columbia (Canada) ha respinto questa difesa: ha stabilito che un'azienda risponde di tutte le informazioni presenti sul proprio sito, comprese quelle generate dal proprio assistente automatico, e che il cliente non aveva motivo di ritenere la risposta del chatbot meno affidabile della pagina informativa. La decisione, resa nota nel febbraio 2024, ha condannato Air Canada a risarcire la differenza tra le due tariffe.

Il punto da portare in aula non è il chatbot in sé — Agritech non ne userà uno pubblico rivolto ai clienti nel breve periodo — ma il principio, che vale per qualunque output AI usato nel lavoro quotidiano: **l'azienda risponde del contenuto che un suo strumento AI produce e che una persona usa verso l'esterno**, indipendentemente da chi (o cosa) lo ha scritto materialmente. Lo stesso principio vale, in scala più piccola, per un'email a un cliente scritta con l'aiuto di un assistente e mai riletta.

### 5.2 L'avvocato che citò cause inventate da ChatGPT (Mata v. Avianca, 2023)

Nel 2023, in una causa civile davanti alla Corte distrettuale degli Stati Uniti per il distretto meridionale di New York (*Mata v. Avianca, Inc.*), gli avvocati della parte attrice presentarono un atto difensivo che citava numerosi precedenti giurisprudenziali a sostegno della propria tesi. La controparte non riuscì a rintracciare quelle sentenze, perché **non esistevano**: erano state generate da ChatGPT, usato dall'avvocato per la ricerca giuridica senza alcuna verifica successiva sulle banche dati ufficiali. Le citazioni erano formalmente corrette — nomi di parti plausibili, numeri di fascicolo nel formato giusto, massime coerenti con l'argomento — ma inventate.

Il giudice P. Kevin Castel sanzionò gli avvocati coinvolti con un'ammenda di 5.000 dollari, rilevando "incongruenze" nei riassunti delle sentenze citate e definendo parte dell'analisi legale presentata come priva di senso. Il caso, diventato un riferimento internazionale nella discussione su AI e professioni, mostra con chiarezza il punto più insidioso delle allucinazioni: **la forma era impeccabile**. Solo il controllo sulla fonte primaria — la banca dati della giurisprudenza reale — ha potuto smascherarle; nessuna lettura per quanto attenta del solo testo prodotto dall'AI lo avrebbe permesso.

Il parallelo con il lavoro d'ufficio è diretto: qualunque riferimento normativo, tecnico o contrattuale prodotto da un assistente AI va controllato sulla fonte primaria (`context/normative-riferimento.md`, per le norme; la scheda tecnica originale, per le specifiche) prima di essere inserito in un documento che esce dall'azienda.

---

## 6. Altri limiti da conoscere, oltre le allucinazioni

Le allucinazioni sono il limite più visibile e quello con l'aggancio più immediato in aula, ma non sono l'unico. Un quadro corretto ne comprende almeno altri quattro, anche se in questo blocco di dieci minuti entra al massimo un cenno a ciascuno; gli approfondimenti hanno le loro giornate dedicate più avanti nel percorso.

**Bias (distorsioni).** Se nei testi di addestramento certe associazioni sono più frequenti di altre — fra mansioni e generi, fra provenienze e caratteristiche — quelle associazioni ricompaiono nelle risposte, senza che il sistema le proponga intenzionalmente (`2026-09-07-modulo-ai-e-llm-materiale.md`, §3.3). È un limite distinto dall'allucinazione: un contenuto affetto da bias può essere fattualmente corretto e comunque distorto nell'impostazione, nel tono o nella scelta degli esempi.

**Dipendenza cognitiva.** È il rischio di delegare all'AI non solo l'esecuzione di un compito ma anche il giudizio su di esso, fino a perdere l'abitudine a controllare, o la competenza per farlo. Non è un limite dello strumento, è un rischio nell'uso che se ne fa: si previene mantenendo sempre, su ogni output usato per una decisione che conta, un passaggio umano di lettura critica — lo stesso riflesso richiesto per le allucinazioni, applicato più in generale.

**Gestione dei dati e riservatezza.** Ogni informazione scritta in un prompt esce dal perimetro dell'azienda verso il fornitore dello strumento, in modi che dipendono dal prodotto, dal piano di abbonamento e dalle impostazioni. Non è un tema che riguarda la qualità dell'output, ma la sicurezza di ciò che si condivide per ottenerlo: ha un approfondimento dedicato in giornata 2 (regole di prudenza sui dati) e in giornata 3 (quadro normativo). In questo blocco basta il cenno: **verificare l'output e proteggere i dati sono due attenzioni diverse, servono entrambe**.

**Assenza di ragionamento causale robusto e di calcolo affidabile.** Un modello linguistico simula il ragionamento e simula il calcolo aritmetico più di quanto li esegua in senso stretto, e su passaggi lunghi o numeri complessi entrambe le simulazioni possono incrinarsi (`2026-09-07-modulo-ai-e-llm-materiale.md`, §3.6). È un limite distinto dall'allucinazione ma con lo stesso rimedio: verificare, specie sui numeri.

Il filo che tiene insieme questi quattro limiti e le allucinazioni è lo stesso: **nessuno di questi si elimina scegliendo lo strumento "giusto" o aspettando la prossima versione**. Si gestiscono con abitudini di verifica, non si risolvono a monte.

---

## 7. Come si riconosce un'allucinazione: segnali d'allarme

Non esiste un modo automatico e infallibile di riconoscere un'allucinazione leggendo solo il testo prodotto — è proprio il punto del §5.2 — ma alcuni segnali, presi insieme, devono alzare il livello di attenzione:

- un tono di sicurezza uniforme, identico su un dato verificabile e su uno inventato: la fiducia con cui è scritto un testo non è mai un indicatore di correttezza;
- dettagli insolitamente precisi su un argomento su cui ci si aspetterebbe imprecisione (una cifra con più decimali del necessario, un numero di articolo molto specifico su una materia di nicchia);
- citazioni, link o riferimenti che non è possibile aprire e verificare direttamente in quel momento;
- risposte diverse alla stessa domanda fattuale posta in momenti diversi, quando ci si aspetterebbe un fatto stabile (da non confondere con la normale variabilità di stile, §3.5 del documento sul funzionamento degli LLM);
- una risposta che conferma esattamente ciò che si sperava di sentirsi dire, su un punto che si sarebbe dovuto verificare comunque.

Nessuno di questi segnali, da solo, prova che un contenuto sia inventato — e la loro assenza non prova il contrario. Sono indizi che aumentano la probabilità di dover controllare, non un sostituto del controllo.

---

## 8. Come si verifica: una regola pratica

La regola che vale la pena lasciare in aula, semplice apposta perché resti, è graduata sul rischio dell'uso che si farà dell'output:

**Per un uso interno, informale, a bassa posta** (una bozza da rivedere, un'idea da scartare o tenere, un riassunto per orientarsi) — una lettura critica è sufficiente: il costo di un errore residuo è basso e il tempo risparmiato vale la rinuncia a un controllo puntuale.

**Per un uso che esce dall'azienda o entra in un documento che conta** (un'email a un cliente o fornitore, un dato in un'offerta o in un capitolato, un riferimento normativo, una cifra che finisce in un contratto) — la regola è categorica: **si verifica sempre sulla fonte primaria**, prima di usare il contenuto. Se l'output cita una norma, si controlla il testo della norma (per Agritech, punto di partenza `context/normative-riferimento.md`, aggiornato dal formatore); se cita una specifica tecnica, si controlla la scheda originale; se cita un dato interno, si controlla il gestionale o il documento sorgente.

Due precisazioni evitano due scorciatoie che sembrano verifiche e non lo sono. La prima: **chiedere conferma allo stesso assistente non è una verifica**. Un modello può confermare un'informazione inventata con la stessa disinvoltura con cui l'ha inventata la prima volta, perché sta di nuovo generando la continuazione più plausibile, non consultando un archivio di verità. La seconda: **un secondo assistente diverso aiuta, ma non sostituisce la fonte primaria** — due strumenti indipendenti che convergono sullo stesso errore non sono impossibili, specie se l'errore nasce da una lacuna comune nei dati di addestramento; sono un indizio in più, non una prova.

---

## 9. Errori comuni e fraintendimenti

*"Se è scritto con sicurezza e in modo fluente, è probabilmente vero."* È l'errore più diffuso e il più pericoloso, perché la fiducia con cui un testo è scritto è una proprietà dello stile, non del contenuto: un modello scrive un'allucinazione con la stessa fluidità di un fatto corretto.

*"L'ho verificato chiedendo di nuovo all'AI."* Non è una verifica, per la ragione spiegata al §8: si rischia di confermare un errore invece di scoprirlo.

*"Con i modelli più recenti il problema è sparito."* Si è ridotto, non è sparito, e non ha una soluzione strutturale nota (§2): resta una proprietà del modo in cui questi sistemi generano testo.

*"Le allucinazioni riguardano solo argomenti esotici o specialistici."* Riguardano soprattutto i fatti puntuali (§3), che possono comparire su qualunque argomento, anche il più comune: un nome, una data, una cifra.

*"Se ha sbagliato un numero, sbaglierà sempre lo stesso numero."* Non è detto: la stessa domanda posta due volte può produrre due risposte diverse (variabilità, `2026-09-07-modulo-ai-e-llm-materiale.md` §3.5), quindi ripetere la domanda non è un modo affidabile né per confermare né per correggere un errore.

---

## 10. Il legame con l'esercizio di prompting della giornata

Che si scelga l'aggancio in avanti o l'inversione dell'ordine (si veda "Come usare questo documento"), il collegamento sostanziale con l'esercizio Fase A/B (18:10–18:35) è questo: quando un prompt lascia impliciti dei dettagli — il destinatario di un'email, il tono, i dati concreti da includere — chi scrive il prompt sta lasciando al modello lo stesso tipo di vuoto che, su un fatto, produce un'allucinazione. Il modello non chiede: **riempie**, nel modo più plausibile compatibile con ciò che ha ricevuto. Le note per il formatore sull'esercizio (`2026-09-07-esercizio-prompting-note-formatore.md`) indicano già di osservare, durante il debrief della Fase A, quali gruppi hanno specificato destinatario, tono e dati e quali li hanno lasciati impliciti: è materiale pronto per il richiamo a questo blocco, in entrambe le direzioni.

---

## 11. Glossario dei termini introdotti

I termini seguono `context/glossario-it.md`. Nel blocco da dieci minuti ne bastano due o tre: allucinazione, e — se emerge una domanda — bias e compiacenza.

**Allucinazione** — un'informazione inventata dal modello e presentata come vera, in genere ben scritta e plausibile, senza alcun segnale che la distingua da un contenuto corretto.

**Compiacenza** (*sycophancy*) — la tendenza di un modello ad assecondare l'aspettativa espressa o implicita in una domanda, anche a scapito della correttezza.

**Bias** (distorsione) — la ricomparsa nelle risposte delle associazioni sistematiche presenti nei testi di addestramento.

**Dipendenza cognitiva** — l'uso passivo di uno strumento AI, senza mantenere un controllo critico sull'output, con il rischio di perdere nel tempo l'abitudine e la competenza per farlo.

**Fonte primaria** — il documento o l'archivio originale (una norma, una scheda tecnica, un gestionale) su cui va verificato un contenuto prodotto dall'AI, distinto dallo strumento AI stesso, che non è mai una fonte primaria di sé stesso.

---

## 12. Punti aperti e da personalizzare

`[DA PERSONALIZZARE]` Gli esempi illustrativi del §4 sono generici e vanno confrontati, se il formatore lo ritiene utile, con un caso vicino al lavoro reale di Agritech (una specifica tecnica, un dato di capitolato, un riferimento a documentazione export) — coerente con le aree di personalizzazione indicate nel brief (`committenti/agritech/brief.md`, "Personalizzazioni richieste").

`[DA VERIFICARE]` La scelta tra "aggancio in avanti" e "inversione dell'ordine" (si veda "Come usare questo documento") va decisa dal formatore prima di costruire le slide della giornata, perché cambia la sequenza dei due blocchi da 10 minuti.

`[DA VERIFICARE]` Se in aula si intende citare la data esatta della sanzione nel caso Mata v. Avianca (§5.2), verificarla prima della lezione: le fonti consultate per questo documento concordano sull'anno (2023) e sull'importo (5.000 $), non sul mese esatto.

**Nota per il formatore.** Nel blocco da dieci minuti non entra tutto. La selezione che regge meglio è: la definizione di allucinazione con l'accento su "non è segnalata" (§2), una frase sul meccanismo — "il modello scrive la continuazione più plausibile, non quella verificata" (§3) — un solo esempio reale tra i due del §5 (Air Canada è il più immediato per un pubblico non giuridico), e la regola pratica in forma di frase sola: "quello che resta in azienda o esce verso l'esterno, si controlla sempre sulla fonte" (§8). Il resto del documento serve per le domande e per i richiami nelle giornate successive, dove il tema torna (giornata 2, ancorato agli errori del workshop di prompting; giornata 3, dentro il quadro normativo).

---

## 13. Fonti e risorse

Il caso Air Canada / Moffatt e il caso Mata v. Avianca sono eventi reali, verificati tramite ricerca web al momento della redazione (3 settembre 2026). Il resto del documento poggia su conoscenza consolidata sul funzionamento degli LLM, già coperta e messa a fonte in `2026-09-07-modulo-ai-e-llm-materiale.md`.

- [Air Canada dovrà risarcire un cliente che aveva ricevuto informazioni fuorvianti da un chatbot — Il Post](https://www.ilpost.it/2024/02/17/air-canada-chatbot-risarcimento/)
- [Responsabilità per errore del chatbot: il caso Moffatt vs Air Canada — Altalex](https://www.altalex.com/documents/news/2024/03/26/responsabilita-errore-chatbot-caso-moffatt-air-canada)
- [BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot — American Bar Association, Business Law Today](https://businesslawtoday.org/2024/02/bc-tribunal-confirms-companies-remain-liable-for-information-provided-by-ai-chatbot/)
- [Mata v. Avianca, Inc. — Wikipedia](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.)
- [Fake Cases, Real Consequences: Misuse of ChatGPT — Goldberg Segalla](https://www.goldbergsegalla.com/app/uploads/2023/10/Fake-Cases-Real-Consequences-Misuse-of-ChatGPT-Christoper-F.-Lyon-NY-Litigator.pdf)
