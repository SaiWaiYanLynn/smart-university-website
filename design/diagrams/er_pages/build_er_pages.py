"""Splits 02_er.mmd into one overview and six group diagrams, renders them and joins them in one PDF.
Run from design/diagrams: python3 er_pages/build_er_pages.py OUT_DIR"""
import re, sys, os, subprocess, json, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=open(os.path.join(ROOT,'02_er.mmd'),encoding='utf-8').read()
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
TMP=os.path.join(ROOT,'er_pages','tmp'); os.makedirs(TMP,exist_ok=True)
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
rel_re=re.compile(r'^  ([A-Z_]+) (\S+) ([A-Z_]+) : (.+)$')
rels=[m.groups() for l in SRC.split('\n') for m in [rel_re.match(l)] if m]
blocks={m.group(1):m.group(0) for m in re.finditer(r'^  ([A-Z_]+) \{\n(?:    .*\n)*?  \}',SRC,re.M)}
ents=list(blocks)
assert len(ents)==44, len(ents)
GROUPS=[
 ('1 People and access',['USER','STUDENT_RECORD','STAFF_PROFILE','ADVISOR_LINK','CHANNEL_LINK','FACULTY','PROGRAM']),
 ('2 Bookings',['RESOURCE','SLOT','RESERVATION','ADVISOR_BRIEF','NOTIFICATION']),
 ('3 Requests and money',['REQUEST','REQUEST_EVENT','REQUEST_FILE','AGENT_CHECK','CHARGE','PAYMENT','APPLICATION']),
 ('4 Conversations and memory',['CONVERSATION','MESSAGE','MEMORY_FACT','WATCH','PENDING_QUESTION','FEEDBACK','TRACE_STEP']),
 ('5 Documents and knowledge',['DOCUMENT','DOCUMENT_CHUNK','UNANSWERED_QUESTION','SOURCE_CONFLICT','CONTENT_ITEM']),
 ('6 Study, library, control',['COURSE','PROGRAM_COURSE','ENROLLMENT','CLASS_SESSION','ATTENDANCE','STUDY_PLAN','ADVISEE_SIGNAL','BOOK','LOAN','AUDIT_LOG','MODEL_USAGE','EVAL_RUN','CONTACT_MESSAGE']),
]
assert sorted(e for _,g in GROUPS for e in g)==sorted(ents)
CFG='---\nconfig:\n  layout: elk\n  theme: base\n  themeVariables:\n    primaryColor: "#F0FDFA"\n    primaryBorderColor: "#0F766E"\n    primaryTextColor: "#18181B"\n    lineColor: "#52525B"\n    fontFamily: "Inter, Helvetica, Arial"\n---\n'
def render(name,body):
    f=os.path.join(TMP,name+'.mmd'); open(f,'w',encoding='utf-8').write(CFG+body)
    svg=os.path.join(TMP,name+'.svg')
    subprocess.run(['npx','-y','@mermaid-js/mermaid-cli@11','-i',f,'-o',svg,'-b','white'],check=True,capture_output=True)
    t=open(svg,encoding='utf-8').read()
    m=re.search(r'viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"',t); w,h=float(m.group(3)),float(m.group(4))
    sc=min(3400/w,2.5); W,H=int(w*sc)+2,int(h*sc)+2
    png=os.path.join(OUT,name+'.png'); hp=png+'.html'
    open(hp,'w').write(f'<html><body style="margin:0;background:#fff"><img src="file://{svg}" style="width:{W}px;height:{H}px;display:block"></body></html>')
    subprocess.run([CHROME,'--headless=new','--disable-gpu','--hide-scrollbars',f'--window-size={W},{H}','--default-background-color=ffffff',f'--screenshot={png}','file://'+hp],check=True,capture_output=True)
    os.remove(hp); return svg,W,H
pages=[]
# overview: all entities, names only, so the relations can be read
ov='erDiagram\n'+'\n'.join(f'  {a} {c} {b} : {l}' for a,c,b,l in rels)+'\n'
pages.append(('Overview: all 44 entities and their relations',)+render('00_overview',ov))
for title,g in GROUPS:
    body='erDiagram\n'
    used=set(g)
    for a,c,b,l in rels:
        if a in g or b in g:
            body+=f'  {a} {c} {b} : {l}\n'; used|={a,b}
    for e in g: body+=blocks[e]+'\n'
    for e in sorted(used-set(g)): body+=f'  {e}\n'
    name=title.split(' ')[0].zfill(2)+'_'+re.sub(r'[^a-z]+','_',title.lower()[2:]).strip('_')
    pages.append((title+'. Entities of other groups show only their name.',)+render(name,body))
# one PDF: one page per diagram, landscape A3
h=['<html><head><meta charset="utf-8"><style>@page{size:A3 landscape;margin:10mm}body{margin:0;font-family:Helvetica,Arial,sans-serif}.p{page-break-after:always;height:277mm;display:flex;flex-direction:column}h1{font-size:15pt;margin:0 0 4mm}.i{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}img{max-width:100%;max-height:100%}.k{font-size:9pt;color:#444;margin-top:3mm}</style></head><body>']
for t,png,W,H in pages:
    h.append(f'<div class="p"><h1>Thales University: entity relationship diagram. {html.escape(t)}</h1><div class="i"><img src="file://{png}" style="width:100%;height:100%;object-fit:contain"></div><div class="k">Notation (crow\'s foot): || exactly one, o| zero or one, |{{ one or many, o{{ zero or many. PK primary key, FK foreign key, UK unique. 44 entities, 49 relations, one PostgreSQL 16 database.</div></div>')
h.append('</body></html>')
hp=os.path.join(TMP,'all.html'); open(hp,'w').write(''.join(h))
subprocess.run([CHROME,'--headless=new','--disable-gpu','--no-pdf-header-footer',f'--print-to-pdf={os.path.join(OUT,"Thales ER diagram.pdf")}','file://'+hp],check=True,capture_output=True)
print([ (p[0][:30],p[2],p[3]) for p in pages])
