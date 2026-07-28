# -*- coding: utf-8 -*-
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/step3a.html",encoding="utf-8").read()
ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'
EY='<div class="eyebrow">07 · Own &amp; Earned Media</div>'
FOOT='<footer class="slide-footer"><span>07 · Own &amp; Earned Media</span><span class="right">'+ART+'</span></footer>'

# ---------- DIVIDER 07 ----------
div07='''<section data-label="07 Own & Earned Media — Divider">
  <div class="slide dark">
    <div class="divider">
      <div class="top-row">
        <span class="ch-eyebrow">07 · Own &amp; Earned Media</span>
        <span style="font-family:var(--font-display);font-weight:900;font-size:28px;color:rgba(255,255,255,.45);letter-spacing:0.06em;">RAYADOS · 2026</span>
      </div>
      <div>
        <div class="ch-num" style="opacity:.12;position:absolute;right:72px;bottom:60px;font-size:480px;line-height:0.8;pointer-events:none;user-select:none;">07</div>
        <p class="ch-title">Own &amp;<br>Earned Media.</p>
        <p class="ch-desc">Las 12 cuentas propias del club generan apenas el 1,4&nbsp;% del volumen, pero el 48,9&nbsp;% del engagement. Este capítulo separa el contenido que Rayados produce (own media) de lo que la conversación dice sobre él (earned media): volumen, plataformas, autores, sentimiento y narrativas — calculado sobre la base completa de 166 467 registros.</p>
      </div>
    </div>
  </div>
</section>
'''

# ---------- 7.1 VOLUMEN + TIMELINE ----------
# barras mensuales (menciones) max 62645 -> 300px
mm={'ABR':12272,'MAY':49772,'JUN':41778,'JUL':62645}
share={'ABR':'38,5%','MAY':'30,5%','JUN':'52,8%','JUL':'55,7%'}
maxm=62645
bars=""
for k,v in mm.items():
    h=round(v/maxm*200)
    vs=f"{v:,}".replace(",", " ")
    bars+=f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;justify-content:flex-end;">
            <div style="font-family:var(--font-display);font-weight:900;font-size:23px;color:var(--ink);">{vs}</div>
            <div style="width:78px;height:{h}px;background:var(--ink);"></div>
            <div style="font-weight:700;font-size:16px;letter-spacing:0.1em;color:var(--n-500);">{k}</div>
            <div class="pill" style="font-size:13px;padding:3px 10px;">own eng {share[k]}</div>
          </div>'''

s71=f'''<section data-label="07.1 Volumen own vs earned + timeline">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>7.1</span><span class="dot">·</span><b>Volumen total y timeline</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Conversación total · 28 abr – 28 jul 2026</p>
      <p class="t-h3" style="margin-bottom:28px;max-width:1150px;">Own media es el 1,4&nbsp;% de las menciones, pero casi la mitad del engagement.</p>
      <div class="row" style="gap:40px;align-items:stretch;">
        <!-- OWN card -->
        <div style="flex:1;border-top:4px solid var(--accent);padding-top:24px;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:14px;">Own media · cuentas propias</p>
          <div class="row" style="gap:36px;">
            <div><div class="bignum small" style="font-size:64px;">2 319</div><p class="t-micro" style="margin-top:4px;">menciones · 1,4&nbsp;%</p></div>
            <div><div class="bignum small accent-color" style="font-size:64px;">10,1 M</div><p class="t-micro" style="margin-top:4px;">interacciones · 48,9&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">12</div><p class="t-micro" style="margin-top:4px;">cuentas oficiales</p></div>
          </div>
        </div>
        <div style="width:1px;background:var(--n-100);"></div>
        <!-- EARNED card -->
        <div style="flex:1;border-top:4px solid var(--ink);padding-top:24px;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);margin-bottom:14px;">Earned media · terceros</p>
          <div class="row" style="gap:36px;">
            <div><div class="bignum small" style="font-size:64px;">164 148</div><p class="t-micro" style="margin-top:4px;">menciones · 98,6&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">10,6 M</div><p class="t-micro" style="margin-top:4px;">interacciones · 51,1&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">49 481</div><p class="t-micro" style="margin-top:4px;">autores únicos</p></div>
          </div>
        </div>
      </div>
      <!-- timeline mensual -->
      <p class="t-eyebrow" style="margin:28px 0 6px;">Timeline por mes · menciones totales</p>
      <div class="chart-wrap" style="height:300px;padding:22px 40px 18px;">
        <div style="display:flex;gap:24px;height:100%;align-items:flex-end;">
          {bars}
        </div>
      </div>
      <p class="t-micro" style="margin-top:12px;color:var(--n-400);">La etiqueta "own eng" indica la proporción del engagement del mes generada por las cuentas propias: crece del 30–38&nbsp;% en abril–mayo al 55,7&nbsp;% en julio, cuando el club domina la conversación con fichajes y Mundial. Abril cubre solo 3 días (28–30).</p>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 7.2 PLATAFORMAS ----------
plat=[
 ("X (Twitter)","115 072","69,1&nbsp;%","3,78 M","33","Volumen y debate en tiempo real",False),
 ("Noticias online","26 337","15,8&nbsp;%","26 K","1","Cobertura mediática y prensa digital",False),
 ("Blogs","8 390","5,0&nbsp;%","6,5 K","1","Análisis de nicho y opinión",False),
 ("TikTok","5 855","3,5&nbsp;%","2,57 M","439","Viralidad joven y formato video",True),
 ("Facebook","4 153","2,5&nbsp;%","3,92 M","943","Comunidad y difusión de own media",False),
 ("Instagram","2 412","1,4&nbsp;%","9,64 M","3 997","Mayor engagement por pieza (own visual)",True),
 ("YouTube","2 080","1,2&nbsp;%","687 K","330","Contenido largo del club",False),
 ("Resto de canales","2 168","1,3&nbsp;%","8 K","4","Podcast, Bluesky, LinkedIn, Foros, Newsletter",False),
]
rows=""
for p,mn,pv,eg,epp,dest,acc in plat:
    st=' style="color:var(--accent);font-weight:700;"' if acc else ''
    rows+=f'''<tr>
            <td class="strong"{st}>{p}</td>
            <td class="num tabular"{st}>{mn}</td>
            <td class="num tabular">{pv}</td>
            <td class="num tabular"{st}>{eg}</td>
            <td class="num tabular">{epp}</td>
            <td style="color:var(--n-600);font-size:18px;">{dest}</td>
          </tr>'''

s72=f'''<section data-label="07.2 Distribución por plataforma">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>7.2</span><span class="dot">·</span><b>Distribución por plataforma</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Menciones y engagement por plataforma · ordenado por menciones</p>
      <p class="t-h3" style="margin-bottom:18px;max-width:1200px;">X manda en volumen; Instagram y Facebook concentran el engagement.</p>
      <table class="tbl" style="font-size:20px;table-layout:fixed;">
        <colgroup><col style="width:250px;"><col style="width:170px;"><col style="width:120px;"><col style="width:170px;"><col style="width:150px;"><col style="width:560px;"></colgroup>
        <thead><tr><th>Plataforma</th><th class="num">Menciones</th><th class="num">% vol</th><th class="num">Engagement</th><th class="num">Eng/pieza</th><th>En qué destaca</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <div style="margin-top:14px;padding:16px 24px;background:var(--n-50);border-left:3px solid var(--accent);">
        <p class="t-small">Instagram (46,7&nbsp;% del engagement) y Facebook (19,0&nbsp;%) concentran la tracción porque ahí publican las cuentas propias del club, cuyos posts acumulan órdenes de magnitud más interacciones por pieza. X aporta el 69&nbsp;% de las menciones pero solo el 18,3&nbsp;% del engagement: es la plaza del debate, no del impacto por pieza.</p>
      </div>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 7.3 TOP AUTORES ----------
authors=[
 (1,"rayados","6 019 K","OWN"),(2,"Rayados","2 493 K","OWN"),(3,"wearerayados","596 K","OWN"),
 (4,"RG La Deportiva","454 K","EARNED"),(5,"delapandillatodalavida","365 K","EARNED"),
 (6,"diegobonti","342 K","EARNED"),(7,"rayadostv","333 K","OWN"),(8,"rayadoos_","258 K","EARNED"),
 (9,"rayados_fb","214 K","OWN"),(10,"Multimedios Deportes","203 K","EARNED"),
 (11,"FOX Sports MX","188 K","EARNED"),(12,"record_mexico","177 K","EARNED"),
 (13,"somosinvictos","161 K","EARNED"),(14,"tiendarayados","160 K","OWN"),(15,"El Tigre Francés","129 K","EARNED"),
]
maxa=6019
def arow(rk,au,eg,org):
    w=round(int(eg.replace(" K","").replace(" ",""))/maxa*100,1)
    pill=('<span class="pill" style="font-size:12px;padding:2px 9px;color:var(--accent);border-color:var(--accent);background:var(--accent-soft);">OWN</span>'
          if org=="OWN" else '<span class="pill pill--neu" style="font-size:12px;padding:2px 9px;">EARNED</span>')
    bar='var(--accent)' if org=="OWN" else 'var(--ink)'
    return f'''<tr>
            <td class="t-micro" style="color:var(--n-400);">{rk}</td>
            <td class="strong"><span class="mono" style="font-size:15px;">{au}</span></td>
            <td>{pill}</td>
            <td class="num tabular">{eg}</td>
            <td><div class="barbar" style="height:12px;"><i style="width:{w}%;background:{bar};"></i></div></td>
          </tr>'''
def atable(rows):
    body="".join(arow(*r) for r in rows)
    return f'''<table class="tbl" style="font-size:18px;">
            <colgroup><col style="width:40px;"><col style="width:230px;"><col style="width:120px;"><col style="width:120px;"><col style="width:120px;"></colgroup>
            <thead><tr><th>#</th><th>Autor</th><th>Origen</th><th class="num">Eng.</th><th></th></tr></thead>
            <tbody>{body}</tbody>
          </table>'''
left=atable(authors[:8]); right=atable(authors[8:])

s73=f'''<section data-label="07.3 Top autores por engagement (own+earned)">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>7.3</span><span class="dot">·</span><b>Principales autores por engagement</b></div></header>
    <div class="frame" style="padding-top:44px;padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Top 15 autores · engagement acumulado · own + earned</p>
      <p class="t-h3" style="margin-bottom:22px;max-width:1250px;">Tres de las cuatro cuentas con mayor engagement son propias del club.</p>
      <div class="row gap-8" style="align-items:flex-start;">
        <div style="flex:1;min-width:0;">{left}</div>
        <div style="flex:1;min-width:0;">{right}</div>
      </div>
      <p class="t-micro" style="margin-top:16px;color:var(--n-400);">Engagement en interacciones (likes, RT, comentarios, shares) sobre la base completa. Las 12 cuentas propias (own) suman 10,1&nbsp;M (48,9&nbsp;%); el resto del top son medios deportivos y fan accounts (earned).</p>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 7.4 SENTIMIENTO ----------
def sbar(neg,neu,pos):
    seg=""
    if neg>0: seg+=f'<div style="background:#B5251D;width:{neg}%;display:flex;align-items:center;justify-content:center;color:white;font-family:var(--font-display);font-weight:900;font-size:26px;">{str(neg).replace(".",",")}%</div>'
    seg+=f'<div style="background:#EAEAE8;width:{neu}%;display:flex;align-items:center;justify-content:center;color:#0A0A0A;font-family:var(--font-display);font-weight:900;font-size:26px;">{str(neu).replace(".",",")}%</div>'
    seg+=f'<div style="background:#1B9E4B;width:{pos}%;display:flex;align-items:center;justify-content:center;color:white;font-family:var(--font-display);font-weight:900;font-size:26px;">{str(pos).replace(".",",")}%</div>'
    return seg

s74=f'''<section data-label="07.4 Distribución de sentimiento own vs earned">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>7.4</span><span class="dot">·</span><b>Distribución de sentimiento</b></div></header>
    <div class="frame" style="padding-top:48px;gap:30px;">
      <div class="row" style="align-items:flex-start;gap:40px;">
        <div class="col gap-3">
          <p class="t-eyebrow">Sentimiento · own vs earned · base completa</p>
          <p class="t-title" style="font-size:50px;max-width:1050px;">El contenido propio es 67&nbsp;% positivo; en las menciones de terceros domina el tono informativo.</p>
        </div>
        <div style="flex-shrink:0;padding-top:6px;"><span class="pill pill--neu" style="font-size:15px;max-width:320px;">Clasificación léxica automatizada · 166 467 registros</span></div>
      </div>

      <div class="col gap-3" style="margin-top:6px;">
        <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);">Own media · cuentas propias (2 319)</p>
        <div style="display:flex;height:64px;border:1px solid var(--n-200);">{sbar(0.0,32.8,67.2)}</div>
      </div>
      <div class="col gap-3">
        <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);">Earned media · terceros (164 148)</p>
        <div style="display:flex;height:64px;border:1px solid var(--n-200);">{sbar(5.5,68.7,25.8)}</div>
      </div>
      <div class="col gap-3">
        <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-400);">Total del corpus (166 467)</p>
        <div style="display:flex;height:48px;border:1px solid var(--n-200);">{sbar(5.4,68.2,26.4)}</div>
      </div>

      <div class="row gap-7" style="margin-top:12px;">
        <div class="col gap-3 fill"><div style="display:flex;align-items:center;gap:10px;"><div style="width:14px;height:14px;background:#B5251D;"></div><span style="font-weight:700;font-size:16px;text-transform:uppercase;color:#B5251D;">Negativo</span></div><p style="font-size:18px;color:var(--n-600);">Crítica a directiva, plantel y rivalidad. Marginal en own media (0&nbsp;%).</p></div>
        <div class="col gap-3 fill"><div style="display:flex;align-items:center;gap:10px;"><div style="width:14px;height:14px;background:#EAEAE8;border:1px solid var(--n-300);"></div><span style="font-weight:700;font-size:16px;text-transform:uppercase;color:var(--n-500);">Neutro</span></div><p style="font-size:18px;color:var(--n-600);">Cobertura informativa y retransmisión. Predomina en earned (68,7&nbsp;%).</p></div>
        <div class="col gap-3 fill"><div style="display:flex;align-items:center;gap:10px;"><div style="width:14px;height:14px;background:#1B9E4B;"></div><span style="font-weight:700;font-size:16px;text-transform:uppercase;color:#0F6B33;">Positivo</span></div><p style="font-size:18px;color:var(--n-600);">Orgullo, ilusión y celebración. Es el registro dominante del own media.</p></div>
      </div>
      <p class="t-micro" style="color:var(--n-400);">Método: clasificación léxica automatizada (léxico positivo/negativo en español) sobre el 100&nbsp;% de los registros; complementa la lectura editorial de terceros del capítulo 05. El predominio neutro refleja el alto peso de menciones informativas y de bajo señal.</p>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 7.5 NARRATIVAS ----------
nar=[
 ("Casa Mundialista · Estadio sede","21 260","6,10 M",100),
 ("Rivalidad Tigres / Japón (Barrial)","18 933","2,30 M",89),
 ("Apertura 2026 · partidos y resultados","17 986","3,45 M",85),
 ("Fichajes y refuerzos","15 733","2,49 M",74),
 ("Era Almeyda · nuevo DT","13 765","2,40 M",65),
 ("Salida de Sergio Canales","6 969","767 K",33),
 ("Crítica directiva / sequía de títulos","5 041","248 K",24),
 ("Rayadas · femenil","2 374","459 K",11),
 ("te Kloese · dirección deportiva","1 360","133 K",6),
]
nrows=""
for nm,mn,eg,w in nar:
    nrows+=f'''<div style="display:grid;grid-template-columns:430px 1fr 120px 120px;gap:20px;align-items:center;">
          <div style="font-weight:700;font-size:20px;color:var(--ink);">{nm}</div>
          <div class="barbar" style="height:20px;"><i style="width:{w}%;background:var(--ink);"></i></div>
          <div class="num tabular" style="text-align:right;font-weight:700;font-size:20px;">{mn}</div>
          <div class="num tabular" style="text-align:right;font-size:18px;color:var(--n-500);">{eg}</div>
        </div>'''

s75=f'''<section data-label="07.5 Narrativas por volumen">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>7.5</span><span class="dot">·</span><b>Principales narrativas</b></div></header>
    <div class="frame" style="padding-top:44px;padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Temas de conversación · ordenados por volumen de menciones</p>
      <p class="t-h3" style="margin-bottom:26px;max-width:1200px;">El Mundial y el Estadio encabezan; la rivalidad con Tigres es el segundo motor de volumen.</p>
      <div style="display:grid;grid-template-columns:430px 1fr 120px 120px;gap:20px;margin-bottom:14px;">
        <div class="t-micro" style="color:var(--n-500);font-weight:700;letter-spacing:0.08em;text-transform:uppercase;">Narrativa</div>
        <div></div>
        <div class="t-micro" style="text-align:right;color:var(--n-500);font-weight:700;letter-spacing:0.08em;text-transform:uppercase;">Menciones</div>
        <div class="t-micro" style="text-align:right;color:var(--n-500);font-weight:700;letter-spacing:0.08em;text-transform:uppercase;">Engagement</div>
      </div>
      <div class="col gap-4">{nrows}</div>
      <p class="t-micro" style="margin-top:20px;color:var(--n-400);">Etiquetado temático por palabras clave sobre la base completa (166 467 registros). Los temas no son mutuamente excluyentes: una misma mención puede tocar más de una narrativa.</p>
    </div>
    {FOOT}
  </div>
</section>
'''

chap07 = div07+s71+s72+s73+s74+s75
open(f"{SC}/chap07.html","w",encoding="utf-8").write(chap07)
print("Capítulo 07 construido:", chap07.count("<section"), "slides")
