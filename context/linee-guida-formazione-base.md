# Linee guida — Formazione di base sull'AI generativa

## Principio fondante

La formazione non è un pacchetto standard: viene progettata specificamente per ogni committente a partire dai suoi processi reali, dal livello di maturità digitale del personale e dagli strumenti già in uso. Due aziende dello stesso settore possono ricevere percorsi molto diversi.

---

## Fase 0 — Assessment pre-formazione

Prima di progettare qualsiasi modulo, si raccolgono due tipi di input:

1. **Questionario di assessment** (→ vedi `contesto_questionario_assesment.md`): compilato dal titolare o referente aziendale, mappa i workflow, il livello di digitalizzazione, gli strumenti in uso, l'esperienza AI già presente e le aspettative. Produce uno scoring "Opportunità AI" per area di processo.
2. **Colloqui con le figure di riferimento**: incontri brevi con 1-3 responsabili di funzione per validare le priorità emerse dal questionario e raccogliere esempi concreti di lavoro quotidiano (documenti, email, report, pratiche ricorrenti) da usare come materiale esercitativo.

L'output di questa fase è il **programma operativo personalizzato**, che include:
- livello di partenza stimato (base / intermedio / avanzato)
- Top 3 aree di processo su cui costruire la parte pratica
- strumenti AI selezionati (vedi sezione dedicata)
- peso da dare ai temi trasversali (governance, privacy, prompt engineering)

---

## Struttura della formazione

### Durata minima

**15 ore** di formazione effettiva, esclusi i tempi di assessment. La distribuzione in sessioni è definita caso per caso in accordo con il committente, tenendo conto della disponibilità del personale, di eventuali fondi interprofessionali attivati e della complessità del percorso.

Formati tipici (non vincolanti):
- 4 incontri da ~4 ore (mezza giornata)
- 3 incontri da ~5 ore
- moduli brevi da 2-3 ore per aziende con difficoltà a liberare il personale

### Proporzione teorico/pratico

| Componente | Peso indicativo | Note |
|---|---|---|
| Parte pratica (casi reali, esercitazioni) | 60-70% | Priorità assoluta |
| Parte teorica (funzionamento AI, normativa) | 20-25% | Necessaria, non negoziabile |
| Discussione, Q&A, riflessione collettiva | 10-15% | Favorisce il consolidamento |

### Modalità didattica

**Misto: dimostrazione + esercizio individuale.**
Il formatore mostra su schermo un caso d'uso reale dell'azienda; i partecipanti replicano autonomamente sul proprio dispositivo. Ogni esercitazione è ancorata a un processo o documento concreto dell'azienda (non esempi generici).

---

## Approccio didattico: pratica prima, teoria lungo il percorso

La formazione adotta un approccio **induttivo**: si parte sempre dal fare, non dallo spiegare. La teoria non viene somministrata in blocco all'inizio, ma introdotta gradualmente man mano che emerge dalla pratica.

**Prima lezione**: solo un accenno iniziale — cos'è un LLM (in termini minimi, senza tecnicismi) e quali soluzioni esistono sul mercato. Subito dopo si entra nella pratica con casi reali dell'azienda.

**Nelle lezioni successive**: le caratteristiche dei singoli strumenti, le differenze tra loro, i meccanismi di funzionamento (token, contesto, allucinazioni, ecc.) e le peculiarità normative vengono introdotti **nel momento in cui diventano rilevanti** per l'esercitazione in corso. Non come moduli separati, ma come approfondimenti contestuali.

Questo approccio riduce la resistenza iniziale nei partecipanti meno digitali e rende immediatamente percepibile il valore pratico della formazione.

---

## Struttura modulare tipo

La sequenza seguente è orientativa; l'ordine e il peso di ciascun blocco vengono adattati al programma operativo del committente.

### Blocco A — Avvio: orientamento minimo + prime prove (2-3 ore)
Contenuti:
- Accenno sintetico: cos'è un LLM, quali strumenti esistono (chatbot generalisti vs AI integrata negli strumenti di lavoro) — nessun approfondimento, solo mappa d'insieme
- Subito pratica: prime esercitazioni su casi semplici ma reali, scelti dall'assessment
- Cosa osservare negli output: qualità, tono, errori evidenti — senza ancora spiegare perché accadono

Modalità: accenno teorico brevissimo (15-20 min), poi subito esercitazioni guidate

### Blocco B — Normativa e responsabilità (1,5-2 ore)
Contenuti:
- AI Act: classificazione del rischio, obblighi pratici per le PMI, cosa cambia nel quotidiano
- GDPR applicato all'uso dell'AI: quali dati non si inseriscono nei chatbot, consenso, titolarità
- Policy aziendale: perché serve, cosa deve contenere (rimandi durante tutta la formazione)
- Shadow AI: cos'è, perché è un rischio, come gestirlo

Modalità: lezione frontale + discussione su casi concreti dell'azienda. Rimandi normativi vengono poi integrati nei moduli pratici ogni volta che si tocca un tema sensibile.

### Blocco C — Prompt engineering pratico (2-3 ore)
Contenuti:
- Anatomia di un prompt efficace: contesto, ruolo, compito, formato, vincoli
- Prompt per le aree di processo prioritarie dell'azienda (costruiti ad hoc sull'assessment)
- Iterazione e raffinamento: come migliorare un output deludente
- Errori comuni e come evitarli

Modalità: esercitazione individuale su casi reali. I prompt vengono scritti in italiano e commentati nel materiale distribuito.

### Blocco D — Applicazioni operative (6-8 ore, cuore del corso)
Contenuti: interamente personalizzati sulle **Top 3 aree di processo** emerse dall'assessment.

Struttura tipo per ciascuna area:
1. Presentazione del caso d'uso (documento/processo reale dell'azienda)
2. Dimostrazione dal formatore
3. Esercitazione individuale guidata
4. Debriefing collettivo: cosa ha funzionato, cosa no, quali limiti sono emersi

**Gli approfondimenti teorici vengono introdotti qui, quando servono.** Se durante un'esercitazione emerge un'allucinazione, si spiega cosa sono le allucinazioni. Se si confrontano due strumenti su un caso d'uso, si approfondiscono le differenze tra di loro. Se si tratta un dato potenzialmente sensibile, si richiama la normativa. La teoria è sempre ancorata a qualcosa che i partecipanti hanno appena sperimentato.

Temi trasversali integrati contestualmente (non in blocco separato):
- funzionamento dei singoli strumenti e differenze pratiche tra loro
- limiti dell'AI (allucinazioni, bias, assenza di ragionamento causale)
- verifica degli output (fact-checking, stile, tono)
- gestione dei dati sensibili durante l'uso
- integrazione nel flusso di lavoro esistente

### Blocco E — Valutazione e consolidamento (1-2 ore)
Contenuti:
- Quiz di autovalutazione (conoscenze e competenze)
- Riflessione individuale: 2-3 casi d'uso prioritari da sperimentare nella settimana successiva
- Indicazioni per l'uso autonomo dopo la formazione
- Raccolta feedback sul percorso

---

## Selezione degli strumenti AI

Gli LLM e gli strumenti da utilizzare nella formazione si decidono **dopo l'assessment**, sulla base di:

| Scenario | Strumenti da privilegiare |
|---|---|
| Azienda usa Microsoft 365 | Microsoft 365 Copilot + ChatGPT/Claude come standalone |
| Azienda usa Google Workspace | Gemini for Workspace + Claude/ChatGPT come standalone |
| Nessuna suite cloud strutturata | ChatGPT e/o Claude come chatbot generalisti |
| Presenza di dati molto sensibili | Strumenti con opzioni enterprise (data residency, nessun training sui dati) |
| Budget limitato, no abbonamenti | Solo versioni gratuite; indicare limiti e rischi |

La formazione è sempre **comparativa**: si mostra come strumenti diversi rispondono alla stessa richiesta, senza dichiarare un vincitore assoluto.

---

## Calibrazione sul livello dei partecipanti

Il livello di partenza (base / intermedio / avanzato) viene stimato dall'assessment e condiziona:

- **Livello base** (bassa digitalizzazione, nessuna esperienza AI): più tempo sul Blocco A e C, esempi molto concreti, ritmo lento, esercizi a bassa posta prima di affrontare i processi reali
- **Livello intermedio** (buona digitalizzazione, uso sporadico AI): Blocco A più rapido, focus su prompt engineering e applicazioni operative, attenzione alla qualità degli output
- **Livello avanzato** (uso corrente AI, buona maturità digitale): Blocco A ridotto al minimo, spazio a casi d'uso complessi, automazioni semplici, governance e policy

In gruppi eterogenei, il formatore adotta il ritmo del livello più basso e prevede esercizi opzionali aggiuntivi per i partecipanti più avanzati.

---

## Elementi invarianti (presenti in ogni percorso)

Indipendentemente dal livello e dal settore, la formazione deve sempre includere:

- almeno una sessione dedicata ai **limiti dell'AI** (allucinazioni, bias, dipendenza cognitiva)
- almeno un approfondimento su **privacy e sicurezza dei dati** nell'uso quotidiano
- esempi e prompt in **italiano**, calati nel settore del committente
- esercitazioni su **processi reali** dell'azienda, non casi generici
- un momento di discussione su **come integrare l'AI senza sostituire il giudizio umano**

---

## Punti da personalizzare per ogni committente

I seguenti elementi sono sempre indicati come `[DA PERSONALIZZARE]` nei materiali:
- nome e settore dell'azienda
- strumenti AI selezionati
- casi d'uso operativi (Blocco D)
- prompt di esempio (costruiti sui processi reali)
- riferimenti normativi specifici al settore (es. dati sanitari, dati finanziari)
- eventuali policy aziendali già in essere

---

## Riferimenti interni

- `contesto_questionario_assesment.md` — struttura e logica del questionario pre-formazione
- `glossario-it.md` — terminologia uniforme da usare in tutti i materiali
- `normative-riferimento.md` — fonti normative (AI Act, GDPR, normativa italiana)
- `profilo-formatore.md` — indicazioni sul ruolo e approccio del formatore
