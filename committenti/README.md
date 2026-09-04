# committenti/

Una sottocartella per ciascuna azienda/cliente, con **tutto** il materiale che
la riguarda: brief, programma, output finali, comunicazione dedicata e note.

## Convenzione di naming

`<nome-azienda-snake-case>/` — es. `rossi-spa/`, `bianchi-srl/`

## Cosa contiene ogni cartella committente

```
committenti/<nome-committente>/
├── brief.md            — Brief del cliente (chi è, cosa serve, vincoli)
├── programma.md         — Programma concordato del corso
├── output/              — Deliverable finali (slide, dispense, esercitazioni)
│   └── AAAA-MM-GG-<titolo>.<ext>
├── comunicazione/        — Materiale di comunicazione specifico per questo cliente
│   └── AAAA-MM-GG-<tipo>-<titolo>.<ext>
└── note/                 — Appunti post-sessione, verifiche di allineamento, feedback
```

Materiale di comunicazione o marketing **non** legato a un committente
specifico (es. la brochure generale della tua offerta) va invece in
`interno/comunicazione-offerta/` — vedi `interno/README.md`.

## Naming dei file

- Data ISO (`AAAA-MM-GG`) all'inizio per ordinamento naturale
- Tipologia esplicita nel nome
- Suffisso `-bozza` per versioni non finali
- Suffisso `-v2`, `-v3` per versioni successive

## Per iniziare un nuovo committente

1. Copia `_template/` rinominandola con il nome del cliente (mantiene già
   `output/`, `comunicazione/` e `note/`)
2. Compila il `brief.md`
3. Chiedi a Claude di costruire il `programma.md` a partire dal brief
