# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import os

FD="/sessions/inspiring-practical-hawking/mnt/.claude/skills/canvas-design/canvas-fonts"
LOGO="/sessions/inspiring-practical-hawking/mnt/formazione-ai/context/logo_piamarta_formazione.png"
OUT="/sessions/inspiring-practical-hawking/mnt/outputs/brochure_v27.pdf"

for name,fn in [("BS","BigShoulders-Bold"),("OF","Outfit-Bold"),
                ("IS","InstrumentSans-Regular"),("ISB","InstrumentSans-Bold"),
                ("GM","GeistMono-Regular"),("GMB","GeistMono-Bold")]:
    pdfmetrics.registerFont(TTFont(name,f"{FD}/{fn}.ttf"))

W,H=A4  # 595.276 x 841.89
def Y(top): return H-top   # convert top-down y to reportlab bottom-up

# colours
PAPER=(0.969,0.965,0.945); INK=(0.039,0.086,0.157); ACID=(0.847,0.953,0.306)
COBALT=(0.176,0.357,1.0); LINEDK=(0.153,0.224,0.361); GREY=(90/255,107/255,133/255)
MIST=(159/255,176/255,200/255); BODYDK=(201/255,212/255,230/255)
LINEP1=(0.847,0.835,0.788); LINEP2=(0.788,0.812,0.863); NODEGREY=(0.239,0.314,0.439)
ACIDDK=(0.616,0.706,0.0); WHITE=(1,1,1)

c=canvas.Canvas(OUT,pagesize=A4)
c.setTitle("Formazione AI generativa su misura — Piamarta Formazione")

def rect(x0,top0,x1,top1,fill):
    c.setFillColorRGB(*fill)
    c.rect(x0,Y(top1),x1-x0,top1-top0,fill=1,stroke=0)
def line(x0,top0,x1,top1,col,w):
    c.setStrokeColorRGB(*col); c.setLineWidth(w)
    c.line(x0,Y(top0),x1,Y(top1))
def circ(cx,ctop,r,fill=None,stroke=None,w=1):
    if fill: c.setFillColorRGB(*fill)
    if stroke: c.setStrokeColorRGB(*stroke); c.setLineWidth(w)
    c.circle(cx,Y(ctop),r,fill=1 if fill else 0,stroke=1 if stroke else 0)

def txt(x,base_top,text,font,size,col,align="l"):
    c.setFillColorRGB(*col); c.setFont(font,size)
    if align=="l": c.drawString(x,Y(base_top),text)
    elif align=="r": c.drawRightString(x,Y(base_top),text)

def mono(x,base_top,text,font,size,col,align="l",track=None):
    if track is None: track=size*0.22
    w=pdfmetrics.stringWidth(text,font,size)+track*max(0,len(text)-1)
    xx = x-w if align=="r" else x
    to=c.beginText(xx,Y(base_top)); to.setFont(font,size)
    to.setFillColorRGB(*col); to.setCharSpace(track); to.textOut(text); to.setCharSpace(0)
    c.drawText(to)

def wrap(text,font,size,maxw):
    words=text.split(); lines=[]; cur=""
    for wd in words:
        t=(cur+" "+wd).strip()
        if pdfmetrics.stringWidth(t,font,size)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=wd
    if cur: lines.append(cur)
    return lines

def para(x,base_top,text,font,size,col,maxw,leading):
    for i,ln in enumerate(wrap(text,font,size,maxw)):
        txt(x,base_top+i*leading,ln,font,size,col)
    return wrap(text,font,size,maxw)

# =================== PAGE 1 ===================
rect(0,0,W,841.9,PAPER)
rect(0,0,W,511.9,INK)
rect(0,777.9,W,841.9,ACID)

# header
mono(48,56.0,"PIAMARTA LAVORO E SVILUPPO — A.F.G.P.","GMB",8.0,ACID,track=1.35)
mono(547.3,56.0,"FORMAZIONE AZIENDALE / AI GENERATIVA","GM",8.0,MIST,align="r",track=1.35)
line(48,68,547.3,68,LINEDK,0.7)

# hero title (new text), 4 lines @72, spacing 66, acid last line
TS=72; SP=66
txt(48,135,"NON UN CORSO AI","BS",TS,WHITE)
txt(48,135+SP,"A CATALOGO.","BS",TS,WHITE)
txt(48,135+2*SP,"IL VOSTRO","BS",TS,WHITE)
txt(48,135+3*SP,"CORSO AI.","BS",TS,ACID)

# subtitle
sub="Formazione sull'AI generativa progettata su misura, a partire dai processi reali della vostra azienda: i vostri documenti, i vostri strumenti, le vostre persone."
para(48,389.9,sub,"IS",13.0,BODYDK,470,18)

# constellation (decorative) top-right — kept, FIG caption removed
CL=LINEDK
for a,b in [((478,341.9),(508,296.9)),((508,296.9),(548,326.9)),((548,326.9),(552,266.9)),
            ((552,266.9),(515,246.9)),((515,246.9),(482,271.9)),((508,296.9),(515,246.9)),
            ((548,326.9),(545,379.9)),((478,341.9),(545,379.9))]:
    line(a[0],a[1],b[0],b[1],CL,0.8)
for (cx,ct,r,col) in [(478,341.9,2.4,NODEGREY),(508,296.9,4.2,ACID),(548,326.9,3.4,COBALT),
                      (552,266.9,4.2,ACID),(515,246.9,2.4,NODEGREY),(482,271.9,3.4,COBALT),
                      (545,379.9,2.4,NODEGREY)]:
    circ(cx,ct,r,fill=col)

# IL PERCORSO block
line(48,437.9,547.3,437.9,LINEDK,0.7)
mono(48,451.9,"IL PERCORSO","GMB",8.0,ACID)
def detail(x,base,bold,rest):
    txt(x,base,bold,"ISB",10.5,WHITE)
    bw=pdfmetrics.stringWidth(bold,"ISB",10.5)
    txt(x+bw+4,base,rest,"IS",10.5,MIST)
detail(48,475.9,"15 ore"," modulari e flessibili")
detail(298,475.9,"Su misura"," per il tuo settore e team")
detail(48,498.9,"In sede"," o da remoto, in accordo")
detail(298,498.9,"Follow-up"," consulenza opzionale")

# four cards
cols=[48,177.3,306.6,436]
for cx in cols:
    line(cx,580.9,cx+93.3,580.9,COBALT,2.0)
cards=[("01","Su misura","Costruita sull'analisi dei vostri processi."),
       ("02","Flessibile","Formati e orari definiti insieme: mezze giornate o moduli brevi, al ritmo del vostro personale."),
       ("03","Pratica","Oltre il 60% del tempo in esercitazioni su casi reali dell'azienda. Niente esempi generici."),
       ("04","Risultati","Personale consapevole degli strumenti AI e processi aziendali ottimizzati, fin da subito.")]
for cx,(num,title,body) in zip(cols,cards):
    mono(cx,583.9,num,"GMB",9.0,COBALT,track=0.0)
    txt(cx,607.9,title,"OF",15.0,INK)
    para(cx,627.9,body,"IS",9.5,GREY,120,12.5)

# bottom CTA (acid band)
txt(48,815.9,"Assessment iniziale gratuito","OF",16.0,INK)
# arrow
aw=pdfmetrics.stringWidth("Assessment iniziale gratuito","OF",16.0)
ax=48+aw+14
c.setStrokeColorRGB(*INK); c.setLineWidth(1.4)
c.line(ax,Y(810.9),ax+24,Y(810.9))
c.line(ax+24,Y(810.9),ax+18,Y(806.9)); c.line(ax+24,Y(810.9),ax+18,Y(814.9))
txt(547.3,814.9,"poi un preventivo su misura. Senza impegno.","IS",11.5,INK,align="r")

c.showPage()

# =================== PAGE 2 ===================
rect(0,0,W,841.9,PAPER)
mono(48,56.0,"I RISULTATI","GMB",8.0,COBALT)
mono(547.3,56.0,"PIÙ DI UN CORSO","GM",8.0,GREY,align="r")
line(48,68,547.3,68,LINEP1,0.7)

# hero
txt(48,118,"I RISULTATI RESTANO","BS",52,INK)
txt(48,160,"IN AZIENDA.","BS",52,COBALT)
hero2="Non solo formazione: analizziamo i vostri processi e vi accompagniamo nel trovare le soluzioni AI davvero utili — per l'azienda e per le persone."
para(48,192,hero2,"IS",12.5,GREY,499,17)

line(48,259.9,547.3,259.9,LINEP1,0.7)
mono(48,249.9,"COSA RESTA IN AZIENDA","GMB",8.0,COBALT)

# result cards (2 cols) with cobalt tick
results=[(48,284.9,"Processi più rapidi","Meno tempo speso sulle operazioni ripetitive di ogni giorno."),
         (312.6,284.9,"Persone autonome","Il team usa l'AI con metodo, senza dipendere da supporto esterno."),
         (48,370.9,"Meno errori","Criteri chiari per verificare e validare ciò che l'AI produce."),
         (312.6,370.9,"Dati al sicuro","Uso conforme a GDPR e AI Act, senza esporre informazioni sensibili."),
         (48,456.9,"Soluzioni su misura","Prompt e casi d'uso sui vostri processi, da estendere ad altri reparti.")]
for x,ticktop,title,body in results:
    rect(x,ticktop,x+22,ticktop+3,COBALT)
    txt(x,ticktop+23,title,"OF",15.0,INK)
    para(x,ticktop+40,body,"IS",10.0,GREY,232,13)

# timeline
line(48,547.9,547.3,547.9,LINEP1,0.7)
mono(48,537.9,"IL PERCORSO — DALL'ASSESSMENT AI RISULTATI","GMB",8.0,COBALT)
line(54,581.9,428.5,581.9,LINEP2,1.0)
nodes=[(54,"FASE 01",["Assessment gratuito"],COBALT),
       (178.8,"FASE 02",["Programma e","preventivo"],COBALT),
       (303.6,"FASE 03",["Formazione pratica"],COBALT),
       (428.5,"FASE 04",["Risultati in azienda"],ACID)]
for cx,lab,lines_,ncol in nodes:
    inner=ACIDDK if ncol==ACID else COBALT
    circ(cx,581.9,6.0,fill=PAPER,stroke=ncol,w=2.2)
    circ(cx,581.9,2.2,fill=inner)
    mono(cx,603.9,lab,"GMB",7.5,COBALT,track=1.4)
    for i,ln in enumerate(lines_):
        txt(cx,615.9+i*12,ln,"ISB",10.0,INK)
# follow-up
rect(54,636.4,58.5,640.9,ACID)
txt(66,644.9,"Follow-up:","ISB",10.0,INK)
fw=pdfmetrics.stringWidth("Follow-up:","ISB",10.0)
txt(66+fw+3,644.9," consulenza continuativa opzionale dopo il corso, per accompagnarvi nell'evoluzione dei processi.".strip(),"IS",10.0,GREY)

# footer ink band
rect(0,686.9,W,691.9,ACID)
rect(0,691.9,W,841.9,INK)
txt(48,729.9,"Prenotate l'assessment gratuito","OF",17.0,ACID)
txt(48,747.9,"Un incontro conoscitivo e un questionario. Nessun costo, nessun vincolo.","IS",10.5,BODYDK)

# logo in footer (paper box, right side of CTA area)
img=Image.open(LOGO); iw,ih=img.size; ar=iw/ih
box_w=138; pad=8
logo_w=box_w-2*pad; logo_h=logo_w/ar
box_h=logo_h+2*pad
box_x1=547.3; box_x0=box_x1-box_w
box_cy=727.0; box_top=box_cy-box_h/2; box_bot=box_cy+box_h/2
rect(box_x0,box_top,box_x1,box_bot,WHITE)
c.drawImage(ImageReader(LOGO),box_x0+pad,Y(box_bot-pad),width=logo_w,height=logo_h,mask='auto')

line(48,763.9,547.3,763.9,LINEDK,0.7)
mono(48,783.9,"PIAMARTA LAVORO E SVILUPPO — A.F.G.P. ASSOCIAZIONE FORMAZIONE GIOVANNI PIAMARTA","GMB",7.5,ACID,track=0.9)
txt(48,799.9,"Via Enrico Ferri 73, Brescia   ·   Tel. 030 6481405   ·   piamartalavoroesviluppo@piamarta.it   ·   www.afgp.it/ples.html","IS",8.6,BODYDK)
txt(48,817.9,"Ente accreditato Regione Lombardia per i Servizi di Formazione","IS",8.5,MIST)

c.showPage()
c.save()
print("saved",OUT, "logo box_h",round(box_h,1),"top",round(box_top,1),"bot",round(box_bot,1))
