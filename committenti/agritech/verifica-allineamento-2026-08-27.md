# Verifica allineamento programma (giornate 1-3) vs note delle call di preparazione

> Confronto tra `programma.md` (validato per le giornate 1-3) e le due call
> interne dei formatori AFGP:
> - **Call 11 agosto 2026** — "Call preparazione corso Agritech — Formatori AFGP" (Piardi, Tanadini, Tierney)
> - **Call 14 agosto 2026** — "Programmazione Agritech" (Tanadini, Tierney)
>
> Le note sono trascrizioni automatiche (Gemini): trattate come indicative, non come verbale ufficiale.

## Esito sintetico

Il programma è **in gran parte allineato** sulla sequenza normativa/prompting e sull'impianto
generale, ma emergono **due conflitti sostanziali** (composizione gruppi, disponibilità
computer nelle giornate 1-3) e alcuni dettagli operativi da integrare. Non ho modificato
`programma.md` o `brief.md`: i punti sotto vanno decisi prima di aggiornarli.

---

## 🔴 Conflitti da risolvere

### 1. Composizione dei due gruppi — il documento di programma è internamente contraddittorio

Il file di programma originale contiene **due indicazioni diverse**:

- Sottotitolo in apertura del documento: *"Commerciale + Ufficio Tecnico"* / *"Amministrazione + ufficio acquisti"*
- Tabella al punto 4 (riportata in `programma.md`): **Gruppo A** = Commerciale + Acquisti; **Gruppo B** = Amministrazione + Tecnico

La **call dell'11 agosto** conferma la versione del sottotitolo, con le parole di Stefano Piardi:
> "suddivisione dei partecipanti in due gruppi: una parte commerciale e ufficio tecnico, e una parte amministrativa, contabile e acquisti"

Questo è l'**opposto** della tabella che ho riportato in `programma.md` §4 e che regge tutti i
"focus casi d'uso" dei cicli 1-3 (export/contrattualistica per il Gruppo A, disegni tecnici/dati
amministrativi per il Gruppo B).

**Impatto:** la comunicazione dei gruppi avviene in **giornata 3** (validata). Se la composizione
è invertita, cambia anche la coerenza dei focus dei cicli successivi (non ancora validati, ma
già impostati sulla versione attuale).

**Decisione richiesta:** quale coppia è corretta — (Commerciale+Acquisti / Amministrazione+Tecnico)
come da tabella §4, o (Commerciale+Tecnico / Amministrazione+Acquisti) come da call e sottotitolo?

### 2. Computer/dispositivi individuali: "dal quarto giorno", non da subito

La call del **14 agosto** è esplicita:
> "Saranno utilizzati computer per le esercitazioni dal quarto giorno per massimizzare il coinvolgimento."

e nel dettaglio:
> "...garantire che i partecipanti abbiano a disposizione strumenti informatici (computer o
> dispositivi mobili) a partire dalla **quarta** giornata del corso, per evitare inattività.
> Viene ipotizzato l'uso di computer condivisi in piccoli gruppi qualora le risorse fossero
> limitate..."

Questo è più restrittivo di quanto scritto nel programma originale (nota operativa: "Accessi/licenze
Claude da avere pronti **entro la giornata 2**; in mancanza, prevedere esercitazioni in coppia o
dimostrative"), che trattava l'assenza di accessi come un'eccezione da tamponare, non come il piano.

**Impatto diretto sulla giornata 2** (validata): la scaletta che ho prodotto
(`outputs/agritech/lezione-02-prompting-e-regole/scaletta-lezione.md`) prevede un "workshop
individuale guidato" con test di prompt sui propri dispositivi — coerente con il programma
originale, ma non con l'indicazione "computer dal giorno 4" della call.

**Decisione richiesta:** in giornata 2 i partecipanti scrivono prompt sui propri dispositivi
(anche in coppia), oppure l'esercizio va ridisegnato come dimostrazione/lavoro cartaceo con
prova pratica rimandata alla fase con i computer?

### 3. Scelta dello strumento AI: posticipata, ma le licenze Claude servono già in giornata 2

Call 11 agosto:
> "La selezione dello strumento AI specifico da adottare è posticipata fino a dopo le prime
> sessioni di valutazione, evitando acquisti preventivi non mirati" — da decidere con l'**Ing.
> Linetti** (referente tecnico Agritech, non presente nel brief attuale).

Il programma valido prevede però l'orientamento a Claude fin dall'inizio e licenze pronte per
la giornata 2. Se "le prime sessioni di valutazione" comprendono le giornate 1-3, i due piani
non tornano: le licenze Claude dovrebbero essere già attive prima che la scelta dello strumento
sia formalmente presa.

**Decisione richiesta:** chiarire se "prime sessioni di valutazione" = solo raccolta pre-corso/
giornata 1, in modo che la scelta di Claude come piattaforma di riferimento resti confermabile
per la giornata 2; e prendere contatto con l'Ing. Linetti se non già fatto.

---

## 🟡 Punti allineati, con dettagli da integrare nelle scalette

| Punto | Fonte call | Stato in `programma.md` / scalette | Azione |
|---|---|---|---|
| Normativa spostata interamente in giornata 3, prompting concentrato in giornata 2 | 14 ago: "La trattazione della normativa è spostata alla terza lezione, dedicando la seconda sessione alle attività pratiche di prompting" | Già così | Nessuna — confermato |
| Le prime 3 giornate sono anche fase di assessment via micro-laboratori | 11 ago | Già scritto in `programma.md` §1 e §8 | Nessuna — confermato |
| Metodo CRAFT: **adottato come standard**, non più opzionale | 14 ago: "Il metodo CRAFT è adottato come standard per l'insegnamento e l'applicazione del prompting durante le sessioni pratiche"; dettaglio: introdotto **dopo** un primo tentativo libero dei partecipanti | Scaletta Giornata 1 riporta ancora "in base al tempo introdurre o meno il metodo CRAFT" | Da correggere: CRAFT è confermato, va introdotto in **giornata 2** dopo il primo tentativo libero, non lasciato come opzione di giornata 1 |
| Attività di apertura: strumento specifico = **Mentimeter**, nuvola di concetti, 20-30 min, prima della teoria | 14 ago | Scaletta Giornata 1 usa genericamente "post-it o scheda anonima" | Da aggiornare con lo strumento specifico e il tempo indicato (20-30') |
| Cartellini con il nome per tutti i partecipanti, inclusi i formatori | 14 ago | Non presente nella scaletta Giornata 1 | Da aggiungere come dettaglio operativo di apertura |
| Piano di emergenza: screenshot pre-catturati in caso di malfunzionamento/connessione | 14 ago | Non presente nelle scalette | Da aggiungere come nota trasversale (rilevante soprattutto per le giornate online, 2 e 3) |
| Formatori (Tanadini e Tierney) presenti insieme a tutte le sessioni | 11 ago, 14 ago | Non esplicitato nel programma | Nota organizzativa, non cambia i contenuti didattici |

## 🟢 Osservazioni minori / da verificare separatamente

- **Riferimenti normativi nuovi** citati nella call dell'11 agosto (Legge 132 italiana, "Digital
  Omnibus" europeo) **non sono presenti** in `context/normative-riferimento.md`. Prima di citarli
  nei materiali della giornata 3 vanno verificati e aggiunti a quella fonte di verità — per ora
  restano `[DA VERIFICARE]`, non li ho inseriti nella scaletta.
- La call dell'11 agosto menziona "uffici separati (es. ex ufficio di padre Paolo) invece di
  un'aula con lavagna" a proposito della logistica delle sessioni in presenza: non è chiaro se
  si riferisca alla sede di lavoro dei formatori o all'aula per i partecipanti. Se riguarda l'aula
  Agritech, va verificato perché la giornata 3 (pur online) e soprattutto un'eventuale versione in
  presenza del workshop a tavoli richiedono uno spazio comune, non uffici separati.
- Non ci sono elementi nelle call che modifichino **date, orari o modalità** (presenza/online)
  delle giornate 1-3: il calendario in `programma.md` §5 resta confermato.

---

## Prossimi passi proposti

1. Confermarmi la composizione corretta dei due gruppi (punto 🔴 1) — corregge `programma.md` §4,
   la tabella §5 non cambia, ma cambiano i "focus casi d'uso".
2. Confermarmi il vincolo computer/dispositivi per la giornata 2 (punto 🔴 2) — ridisegna la
   scaletta della giornata 2 se serve.
3. Chiarire il rapporto tra "scelta dello strumento posticipata" e "licenze Claude entro giornata
   2" (punto 🔴 3), eventualmente coinvolgendo l'Ing. Linetti.
4. Con le risposte sopra, aggiorno `programma.md`, `brief.md` (aggiungo Ing. Linetti come referente
   tecnico) e le scalette delle giornate 1 e 2 con i dettagli 🟡 (Mentimeter, CRAFT, cartellini,
   piano di emergenza).

---

## Risoluzione (27/08/2026, dal committente)

1. **Composizione gruppi**: confermata la versione del sottotitolo — **Gruppo A = Commerciale +
   Ufficio Tecnico**, **Gruppo B = Amministrazione + Ufficio Acquisti**. Corretto in `programma.md`
   §4 e nella scaletta di giornata 3.
2. **Dispositivi individuali**: presenti **dalla giornata 2** (non dalla 4), ma senza uno strumento
   aziendale unico ancora scelto. Le esercitazioni di giornata 2 sono state riprogettate per essere
   indipendenti dallo strumento specifico.
3. **Scelta dello strumento AI**: avviene **nelle prime lezioni** (fase Fondamenta), non rimandata
   oltre. Aggiunto il referente tecnico Ing. Linetti al `brief.md`.

**Struttura del programma**: per la sequenza dei contenuti (normativa in giornata 3, prompting in
giornata 2, ecc.) fa fede il documento di programma fornito dal committente, non le note delle call
— che infatti, su questo punto, risultano già coerenti tra loro e con il programma.

File aggiornati di conseguenza: `programma.md`, `brief.md`,
`outputs/agritech/lezione-01-fondamenta-e-processi/scaletta-lezione.md`,
`outputs/agritech/lezione-02-prompting-e-regole/scaletta-lezione.md`,
`outputs/agritech/lezione-03-normativa-e-gruppi/scaletta-lezione.md`.
