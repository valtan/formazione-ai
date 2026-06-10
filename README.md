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
