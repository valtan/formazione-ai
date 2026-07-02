# -*- coding: utf-8 -*-
"""Brochure Formazione AI — variante v2.7 — filosofia "Processo Vivo"."""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

FONTS = "/sessions/blissful-gallant-johnson/mnt/.claude/skills/canvas-design/canvas-fonts"
LOGO  = "/sessions/blissful-gallant-johnson/mnt/formazione-ai/context/logo_piamarta_formazione.png"
OUT   = "/sessions/blissful-gallant-johnson/mnt/outputs/brochure_v29.pdf"

pdfmetrics.registerFont(TTFont("Display",  f"{FONTS}/BigShoulders-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Head",     f"{FONTS}/Outfit-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body",     f"{FONTS}/InstrumentSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("BodyB",    f"{FONTS}/InstrumentSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono",     f"{FONTS}/GeistMono-Regular.ttf"))
pdfmetrics.registerFont(TTFont("MonoB",    f"{FONTS}/GeistMono-Bold.ttf"))

INK    = HexColor("#0A1628")
COBALT = HexColor("#2D5BFF")
ACID   = HexColor("#D8F34E")
PAPER  = HexColor("#F7F6F1")
GREY   = HexColor("#5A6B85")
MIST   = HexColor("#9FB0C8")
BODYINK= HexColor("#C9D4E6")
LINEINK= HexColor("#27395C")
LINEPAP= HexColor("#D8D5C9")

W, H = A4
M = 48

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Formazione AI generativa su misura — Piamarta Formazione (variante v2.7)")
c.setAuthor("Piamarta Lavoro e Sviluppo — A.F.G.P.")

def T(x, y, s, font, size, color, align="l", tracking=0):
    c.setFont(font, size)
    c.setFillColor(color)
    if tracking:
        c.drawString(x, y, "")  # ensure font set
        cur = x
        for ch in s:
            c.drawString(cur, y, ch)
            cur += pdfmetrics.stringWidth(ch, font, size) + tracking
        return
    if align == "l":
        c.drawString(x, y, s)
    elif align == "r":
        c.drawRightString(x, y, s)
    elif align == "c":
        c.drawCentredString(x, y, s)

def hline(x0, x1, y, color, w=0.8):
    c.setStrokeColor(color); c.setLineWidth(w); c.line(x0, y, x1, y)

def arrow(x, y, length, color, w=2.2):
    """Freccia disegnata vettorialmente (niente glyph -> niente Helvetica)."""
    c.setStrokeColor(color); c.setLineWidth(w); c.setLineCap(1)
    c.line(x, y, x + length, y)
    h = 4.2
    c.line(x + length, y, x + length - h, y + h)
    c.line(x + length, y, x + length - h, y - h)

# =================== PAGINA 1 ===================
c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)

HERO_BOT = 528
c.setFillColor(INK); c.rect(0, HERO_BOT, W, H - HERO_BOT, fill=1, stroke=0)

# eyebrow
T(M, 789, "PIAMARTA LAVORO E SVILUPPO — A.F.G.P.", "MonoB", 8, ACID, tracking=1.4)
T(W - M, 789, "FORMAZIONE AZIENDALE / AI GENERATIVA", "Mono", 8, MIST, align="r")
hline(M, W - M, 781, LINEINK, 0.8)

# titolo display
T(M, 715, "NON UN CORSO", "Display", 64, PAPER)
T(M, 659, "A CATALOGO.", "Display", 64, PAPER)
T(M, 603, "IL VOSTRO.", "Display", 64, ACID)

# sottotitolo
T(M, 571, "Non solo formazione: analizziamo i vostri processi e vi accompagniamo nel trovare", "Body", 11.5, BODYINK)
T(M, 555, "le soluzioni AI davvero utili — per l'azienda e per le persone.", "Body", 11.5, BODYINK)

# --- motivo a nodi nell'hero (sacca destra), senza didascalia ---
g1_nodes = [(470,735),(520,713),(446,690),(506,663),(541,701),(479,636),(527,611)]
g1_links = [(0,1),(1,4),(1,3),(0,2),(2,5),(3,5),(3,6),(5,6)]
g1_acid = 6
g1_grey = {2,4}
c.setStrokeColor(LINEINK); c.setLineWidth(0.9)
for a,b in g1_links:
    c.line(g1_nodes[a][0],g1_nodes[a][1],g1_nodes[b][0],g1_nodes[b][1])
for idx,(nx,ny) in enumerate(g1_nodes):
    if idx==g1_acid: col=ACID; r=4.0
    elif idx in g1_grey: col=MIST; r=2.6
    else: col=COBALT; r=3.0
    c.setFillColor(col); c.circle(nx,ny,r,fill=1,stroke=0)

# --- 6 card ---
cards = [
    ("Processi più rapidi", ["Meno tempo speso sulle operazioni", "ripetitive di ogni giorno."]),
    ("Persone autonome",   ["Il team usa l'AI con metodo, senza", "dipendere da supporto esterno."]),
    ("Meno errori",        ["Criteri chiari per verificare e", "validare ciò che l'AI produce."]),
    ("Dati al sicuro",     ["Uso conforme a GDPR e AI Act,", "senza esporre informazioni sensibili."]),
    ("Soluzioni su misura",["Prompt e casi d'uso sui vostri", "processi, da estendere ad altri reparti."]),
    ("Competenze che restano",["Il know-how rimane in azienda, non", "se ne va con il fornitore esterno."]),
]
colx = [M, 309]
rowy = [488, 384, 280]
for i, (title, lines) in enumerate(cards):
    x = colx[i % 2]; y = rowy[i // 2]
    c.setStrokeColor(COBALT); c.setLineWidth(3); c.setLineCap(0)
    c.line(x, y + 20, x + 26, y + 20)
    T(x, y, title, "Head", 15, INK)
    for j, ln in enumerate(lines):
        T(x, y - 18 - j*13, ln, "Body", 10, GREY)

# --- sezione "Perché è diverso" (al posto della CTA pag.1) ---
hline(M, W - M, 190, LINEPAP, 0.8)
T(M, 168, "PERCHÉ È DIVERSO", "MonoB", 8, COBALT, tracking=1.6)

diff = [
    ("01", "Su misura",  ["Costruito sull'analisi", "dei vostri processi", "reali."]),
    ("02", "Flessibile", ["Formati e orari definiti", "insieme, al ritmo del", "personale."]),
    ("03", "Pratica",    ["Oltre il 60% del tempo", "su casi reali", "dell'azienda."]),
    ("04", "Risultati",  ["Persone autonome e", "processi più", "efficienti."]),
]
dcolw = (W - 2*M) / 4
for k, (num, title, lines) in enumerate(diff):
    x = M + k*dcolw
    T(x, 136, num, "MonoB", 12, COBALT)
    c.setStrokeColor(COBALT); c.setLineWidth(2); c.line(x, 127, x + 20, 127)
    T(x, 105, title, "Head", 13, INK)
    for j, ln in enumerate(lines):
        T(x, 87 - j*12, ln, "Body", 9, GREY)

c.showPage()

# =================== PAGINA 2 ===================
c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)

# eyebrow
T(M, 789, "IL METODO", "MonoB", 8, COBALT, tracking=1.6)
T(W - M, 789, "DALL'ASSESSMENT AI RISULTATI", "Mono", 8, GREY, align="r")
hline(M, W - M, 781, LINEPAP, 0.8)

# motivo a nodi (FIG. 01) in alto a destra
import math
nodes = [(470,736),(512,718),(498,688),(536,700),(548,676),(520,662)]
c.setStrokeColor(HexColor("#C9CFDC")); c.setLineWidth(0.7)
links = [(0,1),(1,2),(1,3),(3,4),(2,5),(4,5)]
for a,b in links:
    c.line(nodes[a][0],nodes[a][1],nodes[b][0],nodes[b][1])
for idx,(nx,ny) in enumerate(nodes):
    col = ACID if idx==4 else (COBALT if idx in (0,3) else HexColor("#C9CFDC"))
    c.setFillColor(col); c.setStrokeColor(col)
    r = 3.4 if idx==4 else 2.6
    c.circle(nx,ny,r,fill=1,stroke=0)

# titolo
T(M, 731, "COME", "Display", 52, INK)
T(M + pdfmetrics.stringWidth("COME ", "Display", 52), 731, "LAVORIAMO.", "Display", 52, COBALT)

# sottotitolo
T(M, 703, "Ogni percorso parte dai vostri processi reali — strumenti, documenti e mansioni", "Body", 11.5, GREY)
T(M, 687, "della vostra azienda. Niente pacchetti standard.", "Body", 11.5, GREY)

# --- il percorso ---
hline(M, W - M, 655, LINEPAP, 0.8)
T(M, 635, "IL PERCORSO — DALL'ASSESSMENT AI RISULTATI", "MonoB", 8, COBALT, tracking=1.4)

# timeline verticale (sinistra)
tlx = M + 4
fasi = [
    ("FASE 01", "Assessment gratuito", ["Questionario e brevi colloqui mappano", "workflow, strumenti e opportunità AI."]),
    ("FASE 02", "Programma e preventivo", ["Un programma operativo personalizzato", "sulle vostre priorità e un preventivo chiaro."]),
    ("FASE 03", "Formazione pratica", ["Minimo 15 ore: si parte dal fare,", "esercitazioni sui vostri documenti reali."]),
    ("FASE 04", "Risultati in azienda", ["L'AI usata con metodo: i processi chiave", "diventano più rapidi e affidabili."]),
    ("FOLLOW-UP — OPZIONALE", "Consulenza continuativa", ["Accompagnamento opzionale dopo il", "corso, per l'evoluzione dei processi."]),
]
ty = 596
gap = 93
node_x = tlx + 5
# linea verticale di collegamento
c.setStrokeColor(HexColor("#C9CFDC")); c.setLineWidth(1.2)
c.line(node_x, ty - (len(fasi)-1)*gap - 2, node_x, ty + 6)
for i,(eyebrow, title, lines) in enumerate(fasi):
    y = ty - i*gap
    last = (i == len(fasi)-1)
    col = ACID if i==3 else COBALT
    c.setFillColor(PAPER); c.setStrokeColor(col); c.setLineWidth(1.6)
    c.circle(node_x, y, 5.2, fill=1, stroke=1)
    c.setFillColor(col)
    c.circle(node_x, y, 2.0, fill=1, stroke=0)
    tx = node_x + 16
    T(tx, y + 9, eyebrow, "Mono", 7, GREY, tracking=1.0)
    T(tx, y - 4, title, "Head", 13.5, INK if not last else INK)
    for j, ln in enumerate(lines):
        T(tx, y - 20 - j*12, ln, "Body", 9, GREY)

# box "IL FORMATO" (destra) allineato in alto con FASE 01
bx = W/2 + 40
bw = W - M - bx
by_top = 618
by_bot = 196
c.setFillColor(INK)
c.roundRect(bx, by_bot, bw, by_top - by_bot, 10, fill=1, stroke=0)
T(bx + 20, by_top - 28, "IL FORMATO", "MonoB", 9, ACID, tracking=1.6)
hline(bx + 20, bx + bw - 20, by_top - 40, LINEINK, 0.8)
fmt = [
    ("15 ore", "moduli e flessibili"),
    ("Su misura", "per il tuo settore e team"),
    ("In sede o da remoto", "organizzato in accordo"),
    ("Follow-up", "consulenza opzionale"),
]
fy = by_top - 70
fgap = (by_top - 40 - by_bot - 24) / len(fmt)
for i,(t,s) in enumerate(fmt):
    yy = fy - i*fgap
    c.setFillColor(ACID); c.rect(bx + 20, yy + 1, 7, 7, fill=1, stroke=0)
    T(bx + 36, yy, t, "BodyB", 11, PAPER)
    T(bx + 36, yy - 13, s, "Body", 9, MIST)

# =================== CTA / CHIUSURA (Ink) ===================
cta_h = 168
c.setFillColor(INK); c.rect(0, 0, W, cta_h, fill=1, stroke=0)

T(M, cta_h - 42, "Prenotate l'assessment", "Display", 30, PAPER)
T(M, cta_h - 72, "gratuito", "Display", 30, ACID)
aw = pdfmetrics.stringWidth("gratuito", "Display", 30)
arrow(M + aw + 16, cta_h - 82, 34, ACID, 2.4)
T(M, cta_h - 96, "Un incontro conoscitivo e un questionario. Nessun costo, nessun vincolo.", "Body", 10.5, BODYINK)

# contatti mono (>= 7.5pt)
T(M, 44, "PIAMARTA LAVORO E SVILUPPO — A.F.G.P. · ASSOCIAZIONE FORMAZIONE GIOVANI PIAMARTA", "Mono", 7.5, MIST, tracking=0.5)
T(M, 30, "Via Enrico Ferri 73, Brescia · Tel. 030 6481405 · piamartalavoroesviluppo@piamarta.it · www.afgp.it/ples.html", "Mono", 7.5, MIST, tracking=0.3)
T(M, 18, "Ente accreditato Regione Lombardia per i Servizi al Lavoro e alla Formazione", "Mono", 7, GREY, tracking=0.3)

# --- LOGO in riquadro chiaro (PNG fondo bianco) ---
img = ImageReader(LOGO)
iw, ih = img.getSize()
ratio = iw / ih
box_h = 58
logo_h = 34
logo_w = logo_h * ratio
pad = 12
box_w = logo_w + 2*pad
bxr = W - M - box_w
byr = cta_h - 30 - box_h
c.setFillColor(PAPER)
c.roundRect(bxr, byr, box_w, box_h, 6, fill=1, stroke=0)
c.drawImage(img, bxr + pad, byr + (box_h - logo_h)/2, width=logo_w, height=logo_h, mask='auto')

c.showPage()
c.save()
print("OK", OUT)
