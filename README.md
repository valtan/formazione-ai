# Formazione AI in azienda

Progetto Cowork per la progettazione e produzione di materiale didattico
per percorsi di **formazione aziendale sull'AI generativa**.

## Struttura

- `context/` — File che Claude legge **prima** di ogni task (profilo, glossario, normative, brand)
- `committenti/` — Una sottocartella per ciascuna azienda cliente
- `templates/` — Slide master, dispense-tipo, layout esercitazione
- `outputs/` — Deliverable finali (organizzati per committente)
- `archivio/` — Versioni vecchie e materiale di ispirazione
- `comunicazione/` — Raccolta di materiale per la comunicazione

## Branding e stile visivo

Per qualsiasi produzione che include elementi visivi o di comunicazione (brochure, slide, volantini, PDF, social, presentazioni), leggere e applicare:

👉 [`context/brand-style-guide.md`](context/brand-style-guide.md) — sistema colori, tipografia, layout, tono e regole d'uso del logo A.F.G.P.

Il logo ufficiale è in `context/logo_piamarta_formazione.png`.

## Convenzioni

- Materiale per la comunicazione in `comunicazione/canale/AAAA-MM-GG-<tipo>-<titolo>.<ext> e versione`  (es. comunicazione/stampa/20260613-Brochure-promozione_corso-v1.0.pdf) 
- Output finali in `outputs/<nome-committente>/AAAA-MM-GG-<titolo>.<ext>`
- Bozze con suffisso `-bozza`, versioni successive con `-v2`, `-v3`
- Non sovrascrivere file in `templates/` o `context/` senza conferma esplicita
