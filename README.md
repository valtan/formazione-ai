# Formazione AI in azienda

Progetto Cowork per la progettazione e produzione di materiale didattico
per percorsi di **formazione aziendale sull'AI generativa**.

## Struttura

- `context/` — File che Claude legge **prima** di ogni task (profilo, glossario, normative, brand)
- `committenti/` — Una sottocartella per ciascuna azienda cliente, con **tutto** il materiale che la riguarda (brief, programma, output finali, comunicazione dedicata, note) — vedi `committenti/README.md`
- `interno/` — Materiale trasversale non legato a un committente specifico (comunicazione della tua offerta, materiale da formatore) — vedi `interno/README.md`
- `templates/` — Slide master, dispense-tipo, layout esercitazione
- `archivio/` — Versioni vecchie e materiale di ispirazione

## Branding e stile visivo

Per qualsiasi produzione che include elementi visivi o di comunicazione (brochure, slide, volantini, PDF, social, presentazioni), leggere e applicare:

👉 [`context/brand-style-guide.md`](context/brand-style-guide.md) — sistema colori, tipografia, layout, tono e regole d'uso del logo A.F.G.P.

Il logo ufficiale è in `context/logo_piamarta_formazione.png`.

## Convenzioni

- Materiale per un committente specifico in `committenti/<nome-committente>/{brief.md, programma.md, output/, comunicazione/, note/}`
- Materiale trasversale (offerta generale, non di un cliente) in `interno/comunicazione-offerta/` o `interno/materiale-formatore/`
- Naming file: `AAAA-MM-GG-<titolo>.<ext>` (es. `committenti/agritech/output/2026-09-07-modulo-1-introduzione.pptx`)
- Bozze con suffisso `-bozza`, versioni successive con `-v2`, `-v3`
- Non sovrascrivere file in `templates/` o `context/` senza conferma esplicita
