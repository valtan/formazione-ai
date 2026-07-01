#!/usr/bin/env bash
#
# setup-formazione-ai.sh
#
# Crea la struttura cartelle e i file di contesto per il progetto Cowork
# "Formazione AI in azienda".
#
# Genera cartelle, README esplicativi in ogni sottocartella, e file di
# contesto pre-compilati (profilo formatore, glossario IT, normative,
# brief committente). I file già esistenti NON vengono sovrascritti.
#
# Uso:
#   ./setup-formazione-ai.sh
#       Crea la struttura nella cartella corrente.
#
#   ./setup-formazione-ai.sh /percorso/cartella
#       Crea la struttura nella cartella specificata.
#
# Requisiti: bash 4+, locale UTF-8 (di default su tutte le distro moderne).

set -euo pipefail

# ============================================================
# CONFIGURAZIONE
# ============================================================

TARGET="${1:-$(pwd)}"

# Colori ANSI (disabilitati se stdout non è un terminale)
if [[ -t 1 ]]; then
    CYAN='\033[0;36m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    RED='\033[0;31m'
    NC='\033[0m'
else
    CYAN='' ; GREEN='' ; YELLOW='' ; RED='' ; NC=''
fi

# ============================================================
# VERIFICA
# ============================================================

if [[ ! -d "$TARGET" ]]; then
    echo -e "${RED}Errore: la cartella '$TARGET' non esiste. Crea prima la cartella di progetto Cowork.${NC}" >&2
    exit 1
fi

# Risolvi percorso assoluto per output più chiaro
TARGET="$(cd "$TARGET" && pwd)"

echo
echo -e "${CYAN}Creazione struttura in: $TARGET${NC}"
echo

# ============================================================
# CREAZIONE CARTELLE
# ============================================================

folders=(
    "context"
    "committenti"
    "committenti/_template"
    "templates"
    "outputs"
    "archivio"
)

for folder in "${folders[@]}"; do
    full="$TARGET/$folder"
    if [[ -d "$full" ]]; then
        echo -e "  ${YELLOW}~ $folder${NC} (già esistente)"
    else
        mkdir -p "$full"
        echo -e "  ${GREEN}+ $folder${NC}"
    fi
done

echo
echo -e "${CYAN}Creazione file di contesto...${NC}"
echo

# ============================================================
# HELPER
# ============================================================

create_file_if_missing() {
    local rel_path="$1"
    local content="$2"
    local full="$TARGET/$rel_path"

    if [[ -f "$full" ]]; then
        echo -e "  ${YELLOW}~ $rel_path${NC} (già esistente, NON sovrascritto)"
        return 0
    fi

    mkdir -p "$(dirname "$full")"
    printf '%s\n' "$content" > "$full"
    echo -e "  ${GREEN}+ $rel_path${NC}"
}

# ============================================================
# CONTENUTI FILE
# ============================================================

README_ROOT=$(cat <<'EOF'
# Formazione AI in azienda

Progetto Cowork per la progettazione e produzione di materiale didattico
per percorsi di **formazione aziendale sull'AI generativa**.

## Struttura

- `context/` — File che Claude legge **prima** di ogni task (profilo, glossario, normative)
- `committenti/` — Una sottocartella per ciascuna azienda cliente
- `templates/` — Slide master, dispense-tipo, layout esercitazione
- `outputs/` — Deliverable finali (organizzati per committente)
- `archivio/` — Versioni vecchie e materiale di ispirazione

## Convenzioni

- Output finali in `outputs/<nome-committente>/AAAA-MM-GG-<titolo>.<ext>`
- Bozze con suffisso `-bozza`, versioni successive con `-v2`, `-v3`
- Non sovrascrivere file in `templates/` o `context/` senza conferma esplicita
EOF
)

README_CONTEXT=$(cat <<'EOF'
# context/

Cartella dei **file di contesto stabili**. Claude (Cowork) li legge all'inizio
di ogni task per inquadrare il lavoro.

## File presenti

- `profilo-formatore.md` — Chi sono, come lavoro, approccio didattico
- `glossario-it.md` — Terminologia italiana uniforme per AI/ML
- `normative-riferimento.md` — Sintesi GDPR, AI Act, normative italiane
- `architettura-progetto.md` — Mappa e filosofia della struttura della cartella

## Quando aggiornare

- Quando cambia il mio modo di lavorare
- Quando aggiungo terminologia nuova al glossario
- Quando entra in vigore una normativa nuova
EOF
)

PROFILO=$(cat <<'EOF'
# Profilo formatore

> Compila ogni sezione. Più è specifico, meglio Claude calibra il materiale.

## Chi sono
Valentino Tanadini, educatore e coordinatore presso un Centro di Formazione
Professionale (CFP) in Italia.
Insegno [meccanica agraria, cybersecurity awareness, ...] a studenti di scuola
secondaria (16-17 anni).
Coordino programmi di formazione professionale e curo materiali didattici.

## Esperienza con l'AI
- [Es: uso quotidiano di Claude e ChatGPT per progettazione didattica]
- [Es: sviluppo di estensioni Chrome per docenti — ProfGPT]
- [Es: workflow di automazione con n8n + Telegram + AI]

## Approccio didattico
- Privilegio la pratica sul teorico
- Esempi sempre concreti, dal mondo del lavoro italiano
- Linguaggio accessibile, evito gergo non spiegato
- Affronto sempre limiti e rischi degli strumenti, non solo i benefici

## Pubblico tipo della formazione aziendale
- Dipendenti italiani eterogenei
- Prevalentemente non tecnici (amministrazione, vendite, HR, back-office)
- Livello di partenza basso
- Possibile diffidenza verso l'AI

## Strumenti AI che tratto
- **Chatbot generalisti**: Claude, ChatGPT, Gemini, Microsoft Copilot
- **AI integrata**: Microsoft 365 Copilot, Google Workspace con Gemini

## Vincoli e preferenze di stile
- Lingua: italiano
- Citazioni normative: GDPR, AI Act UE, normativa italiana
- Esempi: PMI italiane, no scenari Silicon Valley
- Slide: max 5-6 punti per slide, narrazione nelle note del relatore
EOF
)

GLOSSARIO=$(cat <<'EOF'
# Glossario IT — Terminologia AI uniforme

Fonte di verità per i termini italiani usati nei materiali didattici.

## Termini base

| Inglese | Italiano (preferito) | Note |
|---|---|---|
| prompt | prompt | Invariato. Alla prima occorrenza spiegare come "istruzione data all'AI". |
| hallucination | allucinazione | Quando l'AI inventa informazioni false ma plausibili. |
| LLM | modello linguistico di grandi dimensioni | Estendere alla prima occorrenza, poi LLM. |
| token | token | Invariato. Spiegare come "unità minima di testo". |
| agent / AI agent | agente AI | Sistema AI che esegue azioni autonomamente. |
| context / context window | contesto / finestra di contesto | Quanto l'AI "ricorda" nella conversazione. |
| fine-tuning | ottimizzazione (fine-tuning) | Mantenere inglese tra parentesi alla prima occorrenza. |
| grounding | ancoraggio | Quando l'AI si appoggia a documenti verificati. |
| RAG | RAG / generazione aumentata da ricerca | Tecnica di ancoraggio su documenti. |
| chain-of-thought | catena di ragionamento | Visualizzazione passaggi logici dell'AI. |
| zero-shot / few-shot | senza esempi / con pochi esempi | Modalità di prompting. |
| temperature | temperatura | Parametro di creatività/casualità. |
| embedding | rappresentazione vettoriale (embedding) | Mantenere inglese alla prima occorrenza. |
| inference | inferenza | Esecuzione del modello su un input. |
| guardrail | guardrail / vincoli di sicurezza | Limiti imposti al modello. |
| jailbreak | jailbreak / aggiramento dei vincoli | Tentativo di bypassare limiti. |
| bias | bias / distorsione | Pregiudizio sistematico nei risultati. |
| AGI | intelligenza artificiale generale | Estendere sempre. |
| GenAI | AI generativa | Estendere alla prima occorrenza. |
| multimodal | multimodale | Modello che gestisce testo + immagini + audio. |

## Termini da NON usare

- ❌ "robottino", "robot AI" → ✅ "assistente AI", "chatbot"
- ❌ "il computer pensa" → ✅ "il modello genera"
- ❌ "intelligenza" senza qualificare → ✅ "intelligenza artificiale" o "modello"
- ❌ "magia", "miracolo", "rivoluzione" → evitare nei materiali professionali

## Note d'uso

- Alla **prima occorrenza** di un termine tecnico, mettere la versione italiana
  con quella inglese tra parentesi.
- Dalla seconda in poi, usare la forma più breve.
- I termini in inglese mantenuti invariati (prompt, token, RAG) vanno in
  *corsivo* nelle dispense.
EOF
)

NORMATIVE=$(cat <<'EOF'
# Normative di riferimento — sintesi per uso didattico

> Riferimenti rapidi da citare nei materiali. **Verificare l'aggiornamento
> prima di usarli in aula** — questa sintesi può invecchiare.

## GDPR (Regolamento UE 2016/679)

Aspetti rilevanti per l'uso aziendale di AI generativa:

- **Art. 5** — Principi: minimizzazione dei dati, finalità, accuratezza, sicurezza
- **Art. 6** — Basi giuridiche del trattamento (consenso, contratto, interesse legittimo, ecc.)
- **Art. 9** — Dati particolari (sanitari, biometrici, ecc.) — divieto generale di trattamento via AI senza basi forti
- **Art. 22** — Diritto a non essere sottoposti a decisioni automatizzate con effetti rilevanti
- **Art. 25** — Privacy by design e by default
- **Art. 35** — DPIA (Valutazione d'Impatto) obbligatoria per trattamenti ad alto rischio

### Implicazioni pratiche per la formazione
- Mai inserire dati personali di clienti/colleghi in prompt verso chatbot pubblici
- Verificare la geografia dei server (UE vs USA) → trasferimenti internazionali
- Distinguere uso "consumer" vs uso "business/enterprise" degli stessi strumenti

## AI Act (Regolamento UE 2024/1689)

In vigore dal 1° agosto 2024, con applicazione graduale.

### Classificazione del rischio
- **Rischio inaccettabile** (vietati): social scoring, manipolazione subliminale,
  identificazione biometrica in tempo reale in luoghi pubblici (con eccezioni)
- **Alto rischio**: AI in selezione personale, valutazione studenti, accesso al
  credito, ecc. → obblighi di conformità rigorosi
- **Rischio limitato**: chatbot, deepfake → obblighi di trasparenza
- **Rischio minimo**: la maggior parte degli usi generali

### Obblighi che possono toccare le PMI
- Trasparenza: dichiarare che si sta interagendo con AI
- Marcatura dei contenuti generati da AI
- Formazione del personale sull'uso (Art. 4 sull'AI Literacy)

## Riferimenti italiani

- **Codice Privacy** (D.Lgs. 196/2003 e modifiche): integrazione del GDPR
- **Garante Privacy**: provvedimenti recenti su ChatGPT (marzo 2023) e successivi
- **CAD** (Codice dell'Amministrazione Digitale): per uso AI nella PA

## Da verificare prima di citare in aula

- Aggiornamenti del Garante Privacy nell'ultimo trimestre
- Linee guida nazionali emergenti sull'AI Act
- Provvedimenti sanzionatori recenti (utili come case study)

> [DA AGGIORNARE PERIODICAMENTE]
EOF
)

README_COMMITTENTI=$(cat <<'EOF'
# committenti/

Una sottocartella per ciascuna azienda/cliente del percorso formativo.

## Convenzione di naming

`<nome-azienda-snake-case>/` — es. `rossi-spa/`, `bianchi-srl/`

## Cosa contiene ogni cartella committente

- `brief.md` — Brief del cliente (chi è, cosa serve, vincoli)
- `programma.md` — Programma concordato del corso
- `note-sessioni.md` — Appunti post-sessione (feedback, modifiche da fare)

## Per iniziare un nuovo committente

1. Copia `_template/` rinominandola con il nome del cliente
2. Compila il `brief.md`
3. Chiedi a Claude di costruire il programma a partire dal brief
EOF
)

BRIEF_TEMPLATE=$(cat <<'EOF'
# Brief committente — [NOME AZIENDA]

> Compila tutte le sezioni prima di chiedere a Claude di costruire il programma.

## Anagrafica
- **Ragione sociale**:
- **Settore**:
- **Dimensione** (n. dipendenti):
- **Sede**:
- **Referente HR/formazione**:

## Obiettivi del percorso
- **Obiettivo principale**:
- **Risultati attesi a fine corso**:
- **Indicatori di successo**:

## Pubblico
- **N. partecipanti**:
- **Ruoli/funzioni rappresentate**:
- **Livello AI di partenza** (nullo / base / intermedio):
- **Eventuali resistenze attese**:

## Vincoli
- **Durata totale** (ore):
- **Distribuzione** (es. 4 mezze giornate, 2 giornate piene...):
- **Modalità** (in presenza / online / blended):
- **Strumenti già in uso in azienda** (Microsoft 365 / Google Workspace / altro):
- **Vincoli di policy interna sull'AI**:

## Personalizzazioni richieste
- **Logo / brand**:
- **Esempi di settore richiesti**:
- **Casi d'uso prioritari**:

## Note
[Spazio libero per appunti dalla prima call con il cliente]
EOF
)

README_TEMPLATES=$(cat <<'EOF'
# templates/

Modelli riusabili per produrre materiale didattico in modo coerente.

## Cosa metterci

- Slide master (.pptx) con palette, logo, layout standard
- Dispensa-tipo (.docx) con stili impostati
- Layout esercitazione standard
- Template quiz / rubric di valutazione

## Regola

Claude **non deve modificare** i file in questa cartella senza conferma esplicita.
Sono "sorgenti di verità" per la coerenza grafica/strutturale.
EOF
)

README_OUTPUTS=$(cat <<'EOF'
# outputs/

Deliverable finali, organizzati per committente.

## Convenzione

```
outputs/
└── <nome-committente>/
    ├── AAAA-MM-GG-modulo-1-introduzione.pptx
    ├── AAAA-MM-GG-modulo-1-dispensa.docx
    └── AAAA-MM-GG-modulo-1-esercitazioni.docx
```

## Naming

- Data ISO (`AAAA-MM-GG`) all'inizio per ordinamento naturale
- Tipologia esplicita nel nome
- Suffisso `-bozza` per versioni non finali
- Suffisso `-v2`, `-v3` per versioni successive
EOF
)

README_ARCHIVIO=$(cat <<'EOF'
# archivio/

Materiale vecchio o di sola ispirazione. Claude può leggerlo ma **non deve
trattarlo come fonte di verità**.

## Cosa metterci

- Versioni precedenti di slide ormai superate
- Materiali di altri formatori usati come ispirazione
- Bozze abbandonate ma potenzialmente recuperabili
- Articoli/screenshot di ispirazione
EOF
)

# ============================================================
# CREAZIONE FILE
# ============================================================

create_file_if_missing "README.md"                              "$README_ROOT"
create_file_if_missing "context/README.md"                      "$README_CONTEXT"
create_file_if_missing "context/profilo-formatore.md"           "$PROFILO"
create_file_if_missing "context/glossario-it.md"                "$GLOSSARIO"
create_file_if_missing "context/normative-riferimento.md"       "$NORMATIVE"
create_file_if_missing "committenti/README.md"                  "$README_COMMITTENTI"
create_file_if_missing "committenti/_template/brief.md"         "$BRIEF_TEMPLATE"
create_file_if_missing "templates/README.md"                    "$README_TEMPLATES"
create_file_if_missing "outputs/README.md"                      "$README_OUTPUTS"
create_file_if_missing "archivio/README.md"                     "$README_ARCHIVIO"

# ============================================================
# RIEPILOGO
# ============================================================

echo
echo -e "${CYAN}=== Struttura creata ===${NC}"
echo
echo "Prossimi passi:"
echo "  1. Apri context/profilo-formatore.md e completa le sezioni vuote"
echo "  2. Verifica/integra context/glossario-it.md"
echo "  3. Aggiorna context/normative-riferimento.md se serve"
echo "  4. Salva il file architettura-progetto.md in context/ (separato)"
echo "  5. Incolla le istruzioni V3 nel campo 'Istruzioni' del progetto Cowork"
echo
