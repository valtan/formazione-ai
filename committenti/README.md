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
