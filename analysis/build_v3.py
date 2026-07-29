# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v2.html",encoding="utf-8").read()

def repl(old,new,n=1):
    global html
    assert old in html, "NO ENCONTRADO: "+old[:80]
    html=html.replace(old,new,n)

def get_section(label):
    s=html.index(f'<section data-label="{label}">')
    e=html.index('</section>',s)+len('</section>')
    return s,e
def replace_section(label,new):
    global html
    s,e=get_section(label); html=html[:s]+new.rstrip("\n")+html[e:]
def delete_section(label):
    global html
    s,e=get_section(label)
    if html[e:e+1]=="\n": e+=1
    html=html[:s]+html[e:]

ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'
EY7='<div class="eyebrow">07 · Own &amp; Earned Media</div>'
FOOT7='<footer class="slide-footer"><span>07 · Own &amp; Earned Media</span><span class="right">'+ART+'</span></footer>'

# ============================================================
# 4.1 CONCENTRACIÓN (nueva base + listado 8)
# ============================================================
repl('>49 493<', '>49 495<')
repl('letter-spacing="-2">66%</text>', 'letter-spacing="-2">65%</text>')
repl('stroke-dasharray="582.3 879.6"', 'stroke-dasharray="575.3 879.6"')
repl('56px;">66%</span>', '56px;">65%</span>')
repl('>29%</span>\n            <span class="sub">solo <span class="mono" style="font-size:16px;">@rayados</span> acumula 6 M interacciones</span>',
     '>26%</span>\n            <span class="sub"><span class="mono" style="font-size:16px;">Rayados</span> en Instagram acumula 5,4 M interacciones</span>')
repl('Tres handles oficiales del club (rayados · Rayados · wearerayados) concentran ',
     'Tres handles oficiales del club —Rayados en Instagram, Rayados en Facebook y Rayados en TikTok— concentran ')
repl('<strong>44%</strong> del engagement total', '<strong>39,3&nbsp;%</strong> del engagement total')

# ============================================================
# 4.3 TIPOLOGÍAS (nueva base + listado 8) — reemplazar tabla completa
# ============================================================
tip_new='''<table class="tbl" style="font-size:21px;">
        <colgroup>
          <col style="width:300px;">
          <col style="width:120px;">
          <col style="width:240px;">
          <col style="width:150px;">
          <col style="width:150px;">
          <col style="width:300px;">
        </colgroup>
        <thead>
          <tr>
            <th>Tipología</th>
            <th class="num">Engagement</th>
            <th></th>
            <th class="num">% eng.</th>
            <th class="num">% menc.</th>
            <th>Rol en la conversación</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="strong">Cuentas propias del club</td>
            <td class="num tabular">9,5 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:100%;background:var(--accent);"></i></div></td>
            <td class="num tabular"><strong>46,0%</strong></td>
            <td class="num tabular">1,0%</td>
            <td style="color:var(--n-600);font-size:18px;">Concentran el engagement con volumen mínimo: fichajes, Mundial, Almeyda, RSE</td>
          </tr>
          <tr>
            <td class="strong">Ciudadanía / individuales</td>
            <td class="num tabular">5,8 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:61%;"></i></div></td>
            <td class="num tabular">28,1%</td>
            <td class="num tabular">66,5%</td>
            <td style="color:var(--n-600);font-size:18px;">Principal voz de crítica, rivalidad y celebración espontánea</td>
          </tr>
          <tr>
            <td class="strong">Medios y prensa deportiva</td>
            <td class="num tabular">3,0 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:31%;"></i></div></td>
            <td class="num tabular">14,4%</td>
            <td class="num tabular">27,1%</td>
            <td style="color:var(--n-600);font-size:18px;">Amplifican hitos y fichajes (Fox, Récord, Multimedios, ESPN…)</td>
          </tr>
          <tr>
            <td class="strong">Fan accounts / comunidad rayada</td>
            <td class="num tabular">2,1 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:22%;"></i></div></td>
            <td class="num tabular">10,1%</td>
            <td class="num tabular">5,1%</td>
            <td style="color:var(--n-600);font-size:18px;">Viralizan contenido emocional (delapandilla…, somosinvictos, zonarayada)</td>
          </tr>
          <tr>
            <td class="strong">Organismos / internacional</td>
            <td class="num tabular">0,3 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:3%;"></i></div></td>
            <td class="num tabular">1,4%</td>
            <td class="num tabular">0,3%</td>
            <td style="color:var(--n-600);font-size:18px;">FIFA, Liga MX, UNICEF, SportBible — tracción Mundial / Almeyda</td>
          </tr>
          <tr style="background:var(--n-50);">
            <td colspan="6" style="font-size:17px;color:var(--n-400);font-style:italic;padding:14px 20px;">
              Cálculo sobre la base completa (166 467 registros): suma de engagement por categoría. Las cuentas propias corresponden al listado oficial de 8 cuentas del club; el resto se deriva del nombre de autor y el tipo de fuente.
            </td>
          </tr>
        </tbody>
      </table>'''
s=html.index('<table class="tbl" style="font-size:21px;">'); e=html.index('</table>',s)+len('</table>')
html=html[:s]+tip_new+html[e:]

# ============================================================
# 4.4 HALLAZGO A
# ============================================================
repl('Las cuentas oficiales (rayados, wearerayados, rayadostv, rayados_fb, tiendarayados) acumulan ~49% del engagement total. Ningún tercero supera en tracción a las cuentas propias.',
     'Las ocho cuentas oficiales del club (Rayados en X, Facebook, Instagram y TikTok; wearerayados; rayados_fb; Tienda Rayados; y CFM Rayados en LinkedIn) acumulan el 46% del engagement total. Ningún tercero supera en tracción a las cuentas propias.')

# ============================================================
# DIVIDER 07 desc
# ============================================================
repl('Las 12 cuentas propias del club generan apenas el 1,4&nbsp;% del volumen, pero el 48,9&nbsp;% del engagement. Este capítulo separa el contenido que Rayados produce (own media) de lo que la conversación dice sobre él (earned media): volumen, plataformas, autores, sentimiento y narrativas — calculado sobre la base completa de 166 467 registros.',
     'Las 8 cuentas propias del club generan apenas el 1,0&nbsp;% del volumen, pero el 46,0&nbsp;% del engagement. Este capítulo separa el contenido que Rayados produce (own media) de lo que la conversación dice sobre él (earned media): volumen, plataformas y narrativas — calculado sobre la base completa de 166 467 registros.')

# ============================================================
# 8.3 quitar hallazgo Fundación + cláusula del título
# ============================================================
repl('La labor social se comunica bajo el sello #EnLaVidaYEnLaCancha, no como "Fundación Rayados".',
     'La labor social se comunica bajo el sello #EnLaVidaYEnLaCancha.')
repl('Hallazgo: la marca "Fundación Rayados" casi no aparece nominalmente en la conversación (1 mención directa). La RSE del club circula bajo programas concretos',
     'La RSE del club circula bajo programas concretos')

# ============================================================
# Corrección atribución del peak del 28 abr (era "Estadio sede
# mundialista"; los datos muestran que fue la salida de Canales)
# ============================================================
repl('<p class="t-h3" style="margin-bottom:16px;">Estadio sede mundialista</p>',
     '<p class="t-h3" style="margin-bottom:16px;">Salida de Sergio Canales</p>')
repl('Confirmación del Estadio Monterrey como venue del Mundial 2026 detona orgullo institucional y cobertura internacional. La narrativa «Casa Mundialista» captura el 26% del período.',
     'El anuncio oficial de la baja de Sergio Canales concentra el 60&nbsp;% de las menciones del día y las publicaciones de mayor engagement (despedidas del club y del jugador). Es el mayor peak de volumen del período.')
repl('Peak asociado al anuncio mundialista.',
     'Peak asociado al anuncio de la salida de Sergio Canales.')
repl('Tres peaks definen el período: el anuncio del Estadio como sede mundialista, el debut de Almeyda y el inicio del Mundial. Cada uno responde a un motor distinto.',
     'Tres peaks definen el período: la salida de Sergio Canales, el anuncio de Almeyda como DT y los refuerzos y debut rumbo al Apertura. El Mundial fue una narrativa sostenida, no un peak de un solo día.')

# ============================================================
# Re-anclaje de fechas de hitos (base: 28 abr Canales · 21 may Almeyda ·
# 8 jul fichaje Rossi · 18–26 jul refuerzos y debut)
# ============================================================
# 2.3 Peak 02: 21 may era "Japón rechaza a Tigres" -> anuncio de Almeyda
repl('<p class="t-h3" style="margin-bottom:16px;">Japón rechaza a Tigres</p>',
     '<p class="t-h3" style="margin-bottom:16px;">Almeyda es nuevo DT</p>')
repl('La Selección Japonesa abandona las instalaciones de Tigres y entrena en el Barrial de Rayados. El episodio activa rivalidad local y amplificación masiva de aficionados.',
     'Rayados oficializa a Matías Almeyda como DT. Los posts de bienvenida del club (123 K y 91 K de engagement) reencuadran la conversación de la crítica hacia la expectativa.')
# 2.3 Peak 03
repl('<p class="t-h3" style="margin-bottom:16px;">Debut Almeyda + Mundial arranca</p>',
     '<p class="t-h3" style="margin-bottom:16px;">Refuerzos + debut de Almeyda</p>')
repl('Doble spike en 9 días: presentación oficial de Almeyda y primer partido del Mundial en Estadio Monterrey. La conversación institucional y la global se superponen por primera vez.',
     'Doble spike en la recta final: presentación de refuerzos (Cuypers y Orbelín, 18–19 jul) y debut de Almeyda en el Apertura 2026 (26 jul), con la expectativa deportiva al máximo.')

# 6.1: tarjeta Almeyda 8 JUL -> 21 MAY
repl('color:var(--n-400);">8 JUL</span>\n          <span style="font-family:var(--font-display);font-weight:900;font-size:38px;line-height:0.95;letter-spacing:-0.02em;color:var(--ink);">Llega<br>Almeyda</span>',
     'color:var(--n-400);">21 MAY</span>\n          <span style="font-family:var(--font-display);font-weight:900;font-size:38px;line-height:0.95;letter-spacing:-0.02em;color:var(--ink);">Llega<br>Almeyda</span>')
# 6.4 header + stats
repl('8 de julio · Anuncio de Almeyda como DT', '21 de mayo · Anuncio de Almeyda como DT')
repl('menciones · 8 jul</div>', 'menciones · 21 may</div>')
repl('<div class="label">Jul 9 (día siguiente)</div>\n              <div class="value" style="font-size:44px;">2 131</div>',
     '<div class="label">22 may (día siguiente)</div>\n              <div class="value" style="font-size:44px;">1 335</div>')
# resto de "3 893" (tarjeta y stat de 6.1) -> 4 253
html=html.replace('3 893','4 253')
# 6.2 curva: re-graficada con los 92 valores diarios reales (incluye anotaciones correctas)
svg62=open(f"{SC}/svg62_new.html",encoding="utf-8").read()
_s6=html.index('data-label="06.2'); _sv0=html.index('<svg',_s6); _sv1=html.index('</svg>',_sv0)+6
html=html[:_sv0]+svg62+html[_sv1:]

print("Parte A (ediciones puntuales) OK")

# ============================================================
# 4.2 TOP 30 AUTORES (nueva base) — rebuild sección completa
# ============================================================
TOP=[
 (1,"Rayados (Instagram)","Cuenta oficial · Instagram",5405745,True),
 (2,"Rayados (Facebook)","Cuenta oficial · Facebook",1953363,True),
 (3,"Rayados (TikTok)","Cuenta oficial · TikTok",740795,True),
 (4,"wearerayados (instagram)","Cuenta oficial · Instagram",596494,True),
 (5,"RG La Deportiva","Medio deportivo · regional",454789,False),
 (6,"Rayados (X)","Cuenta oficial · X",412772,True),
 (7,"delapandillatodalavida","Fan account · TikTok",365568,False),
 (8,"diegobonti","Periodista · fichajes",342390,False),
 (9,"rayadostv","Rayados TV · TikTok",333559,False),
 (10,"rayadoos_","Fan influencer · TikTok",258229,False),
 (11,"rayados_fb (Instagram)","Cuenta oficial · Instagram",214724,True),
 (12,"Multimedios Deportes","Medio deportivo · regional",203344,False),
 (13,"FOX Sports MX","Medio deportivo · nacional",188469,False),
 (14,"record_mexico","Medio deportivo · nacional",177388,False),
 (15,"somosinvictos","Fan account · X",161431,False),
 (16,"Tienda Rayados (Instagram)","Cuenta oficial · tienda",160634,True),
 (17,"El Tigre Francés","Fan influencer · X",129894,False),
 (18,"mediotiempocom","Medio deportivo · nacional",128662,False),
 (19,"latinus_us","Medio noticias · internacional",125654,False),
 (20,"rayadas4life4","Fan influencer · TikTok",125142,False),
 (21,"fifa","Organismo · FIFA oficial",122110,False),
 (22,"sportbible","Medio deportivo · global",111326,False),
 (23,"rayadas","Cuenta femenil · Rayadas",107518,False),
 (24,"tycsports","Medio deportivo · argentina",107261,False),
 (25,"diario.ole","Medio deportivo · argentina",103386,False),
 (26,"Rayadas","Cuenta femenil · Rayadas",98261,False),
 (27,"foxsportsmx","Medio deportivo · nacional",94326,False),
 (28,"sergiocanalesoficial","Jugador · despedida",92017,False),
 (29,"raya2dcorazon","Fan account · TikTok",91633,False),
 (30,"scespn","Medio deportivo · ESPN",91599,False),
]
MAXE=5405745
def engK(e): return f"{round(e/1000):,} K".replace(","," ")
def disp(n):
    for suf in [" (Instagram)"," (instagram)"," (Facebook)"," (TikTok)"," (X)"]:
        if n.endswith(suf): return n[:-len(suf)]
    return n
def namecell(n):
    d=disp(n)
    if " " in d: return f'<td class="strong">{d}</td>'
    return f'<td class="strong"><span class="mono" style="font-size:15px;">{d}</span></td>'
def toprow(rk,n,tip,e,own):
    w=round(e/MAXE*100,1)
    bar='var(--accent)' if own else 'var(--ink)'
    return f'''<tr>
                <td class="t-micro" style="color:var(--n-400);">{rk}</td>
                {namecell(n)}
                <td style="color:var(--n-500);font-size:16px;white-space:nowrap;">{tip}</td>
                <td class="num tabular">{engK(e)}</td>
                <td><div class="barbar" style="height:13px;"><i style="width:{w}%;background:{bar};"></i></div></td>
              </tr>'''
def toptable(rows):
    body="".join(toprow(*r) for r in rows)
    return f'''<table class="tbl t42" style="font-size:18px;">
            <colgroup><col style="width:40px;"><col style="width:180px;"><col style="width:220px;"><col style="width:110px;"><col style="width:80px;"></colgroup>
            <thead><tr><th>#</th><th>Autor</th><th>Tipología</th><th class="num">Engagement</th><th></th></tr></thead>
            <tbody>{body}</tbody>
          </table>'''
sec42=f'''<section data-label="04.2 Top 30 autores — tabla doble">
  <div class="slide">
    <style>.t42 td,.t42 th{{padding:10px 14px;}}</style>
    <header class="slide-header">
      <div class="eyebrow">04 · Autores y tipologías</div>
      <div class="crumb"><span>4.2</span><span class="dot">·</span><b>Top autores por engagement</b></div>
    </header>
    <div class="frame" style="padding-top:40px;padding-bottom:120px;">
      <div class="row gap-7" style="align-items:flex-start;">
        <div style="flex:1;min-width:0;">{toptable(TOP[:15])}</div>
        <div style="flex:1;min-width:0;">{toptable(TOP[15:])}
          <p style="font-size:16px;color:var(--n-400);margin-top:12px;font-style:italic;">
            * Engagement en interacciones (likes, RT, comentarios, shares) sobre la base completa. Las cuentas propias (naranja) aparecen desglosadas por plataforma.
          </p>
        </div>
      </div>
    </div>
    <footer class="slide-footer">
      <span>04 · Autores y tipologías</span>
      <span class="right"><span style="font-size:13px;letter-spacing:.12em;color:var(--n-400);">ARTOOL</span></span>
    </footer>
  </div>
</section>'''
replace_section("04.2 Top 30 autores — tabla doble", sec42)

# ============================================================
# 7.1 VOLUMEN own vs earned + timeline (nueva base + listado 8)
# ============================================================
mm={'ABR':12272,'MAY':49772,'JUN':41778,'JUL':62645}
share={'ABR':'37,6%','MAY':'27,0%','JUN':'52,4%','JUL':'50,8%'}
maxm=62645; bars=""
for k,v in mm.items():
    h=round(v/maxm*200); vs=f"{v:,}".replace(","," ")
    bars+=f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;justify-content:flex-end;">
            <div style="font-family:var(--font-display);font-weight:900;font-size:23px;color:var(--ink);">{vs}</div>
            <div style="width:78px;height:{h}px;background:var(--ink);"></div>
            <div style="font-weight:700;font-size:16px;letter-spacing:0.1em;color:var(--n-500);">{k}</div>
            <div class="pill" style="font-size:13px;padding:3px 10px;">own eng {share[k]}</div>
          </div>'''
sec71=f'''<section data-label="07.1 Volumen own vs earned + timeline">
  <div class="slide">
    <header class="slide-header">{EY7}<div class="crumb"><span>7.1</span><span class="dot">·</span><b>Volumen total y timeline</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Conversación total · 28 abr – 28 jul 2026</p>
      <p class="t-h3" style="margin-bottom:28px;max-width:1150px;">Own media es el 1,0&nbsp;% de las menciones, pero casi la mitad del engagement.</p>
      <div class="row" style="gap:40px;align-items:stretch;">
        <div style="flex:1;border-top:4px solid var(--accent);padding-top:24px;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:14px;">Own media · cuentas propias</p>
          <div class="row" style="gap:36px;">
            <div><div class="bignum small" style="font-size:64px;">1 720</div><p class="t-micro" style="margin-top:4px;">menciones · 1,0&nbsp;%</p></div>
            <div><div class="bignum small accent-color" style="font-size:64px;">9,5 M</div><p class="t-micro" style="margin-top:4px;">interacciones · 46,0&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">8</div><p class="t-micro" style="margin-top:4px;">cuentas oficiales</p></div>
          </div>
        </div>
        <div style="width:1px;background:var(--n-100);"></div>
        <div style="flex:1;border-top:4px solid var(--ink);padding-top:24px;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);margin-bottom:14px;">Earned media · terceros</p>
          <div class="row" style="gap:36px;">
            <div><div class="bignum small" style="font-size:64px;">164 747</div><p class="t-micro" style="margin-top:4px;">menciones · 99,0&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">11,1 M</div><p class="t-micro" style="margin-top:4px;">interacciones · 54,0&nbsp;%</p></div>
            <div><div class="bignum small" style="font-size:64px;">49 487</div><p class="t-micro" style="margin-top:4px;">autores únicos</p></div>
          </div>
        </div>
      </div>
      <p class="t-eyebrow" style="margin:28px 0 6px;">Timeline por mes · menciones totales</p>
      <div class="chart-wrap" style="height:300px;padding:22px 40px 18px;">
        <div style="display:flex;gap:24px;height:100%;align-items:flex-end;">
          {bars}
        </div>
      </div>
      <p class="t-micro" style="margin-top:12px;color:var(--n-400);">La etiqueta "own eng" indica la proporción del engagement del mes generada por las cuentas propias: sube del 27–38&nbsp;% en abril–mayo a más del 50&nbsp;% en junio–julio, cuando el club domina la conversación con fichajes y Mundial. Abril cubre solo 3 días (28–30).</p>
    </div>
    {FOOT7}
  </div>
</section>'''
replace_section("07.1 Volumen own vs earned + timeline", sec71)

# ============================================================
# 7.2 OWN MEDIA por plataforma (nueva base + listado 8)
# ============================================================
opl=[
 ("Instagram","707","6,38 M","9 021","Núcleo del own media: más publicaciones y engagement",True),
 ("Facebook","513","1,95 M","3 808","Alcance masivo y comunidad",False),
 ("X (Twitter)","440","413 K","938","Tiempo real y servicio informativo",False),
 ("TikTok","43","741 K","17 228","Máximo engagement por pieza (video / viralidad)",False),
 ("LinkedIn","17","3 K","197","Comunicación corporativa / institucional",False),
]
orows=""
for p,mn,eg,epp,dest,acc in opl:
    st=' style="color:var(--accent);font-weight:700;"' if acc else ''
    orows+=f'''<tr>
            <td class="strong"{st}>{p}</td>
            <td class="num tabular"{st}>{mn}</td>
            <td class="num tabular"{st}>{eg}</td>
            <td class="num tabular">{epp}</td>
            <td style="color:var(--n-600);font-size:18px;">{dest}</td>
          </tr>'''
sec72=f'''<section data-label="07.2 Own media por plataforma">
  <div class="slide">
    <header class="slide-header">{EY7}<div class="crumb"><span>7.2</span><span class="dot">·</span><b>Own media por plataforma</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Publicaciones de las cuentas propias por plataforma · ordenado por menciones</p>
      <p class="t-h3" style="margin-bottom:18px;max-width:1250px;">El own media vive en Instagram; TikTok rinde el mayor engagement por pieza.</p>
      <table class="tbl" style="font-size:21px;table-layout:fixed;">
        <colgroup><col style="width:260px;"><col style="width:200px;"><col style="width:200px;"><col style="width:180px;"><col style="width:640px;"></colgroup>
        <thead><tr><th>Plataforma</th><th class="num">Publicaciones</th><th class="num">Engagement</th><th class="num">Eng/pieza</th><th>En qué destaca</th></tr></thead>
        <tbody>{orows}</tbody>
      </table>
      <div style="margin-top:16px;padding:16px 24px;background:var(--n-50);border-left:3px solid var(--accent);">
        <p class="t-small">Las 8 cuentas oficiales publicaron <strong>1 720 piezas</strong> en el trimestre, con <strong>9,5&nbsp;M de interacciones</strong>. Instagram concentra tanto el volumen (707 posts) como el engagement (6,4&nbsp;M). TikTok, con solo 43 publicaciones, logra el mayor engagement por pieza (17 228). LinkedIn opera como canal corporativo/institucional.</p>
      </div>
    </div>
    {FOOT7}
  </div>
</section>'''
replace_section("07.2 Distribución por plataforma", sec72)

# ============================================================
# Borrar 7.3 y 7.4 ; renumerar 7.5 -> 7.3
# ============================================================
delete_section("07.3 Top autores por engagement (own+earned)")
delete_section("07.4 Distribución de sentimiento own vs earned")
# renumerar narrativas 7.5 -> 7.3
s,e=get_section("07.5 Narrativas por volumen")
seg=html[s:e]
seg=seg.replace('data-label="07.5 Narrativas por volumen"','data-label="07.3 Narrativas por volumen"')
seg=seg.replace('<span>7.5</span>','<span>7.3</span>')
html=html[:s]+seg+html[e:]

# ============================================================
# NUEVAS SLIDES 7.4 (narrativas own) y 7.5 (narrativas terceros)
# ============================================================
def insert_after(label, new):
    global html
    s=html.index(f'<section data-label="{label}">')
    e=html.index('</section>',s)+len('</section>')
    html=html[:e]+"\n"+new.rstrip("\n")+html[e:]

def nartable(rows, maxep, volhdr):
    body=""
    for nar,vol,pv,ep,tag in rows:
        w=round(int(ep.replace(" ",""))/maxep*100,1)
        col='var(--accent)' if tag=='up' else ('#B5251D' if tag=='down' else 'var(--ink)')
        tagcell=''
        if tag=='up': tagcell='<span class="pill" style="font-size:12px;padding:2px 9px;color:var(--accent);border-color:var(--accent);background:var(--accent-soft);">FUNCIONA</span>'
        elif tag=='down': tagcell='<span class="pill pill--neg" style="font-size:12px;padding:2px 9px;">BAJO</span>'
        body+=f'''<tr>
            <td class="strong" style="font-size:19px;">{nar}</td>
            <td class="num tabular" style="font-size:19px;">{vol}</td>
            <td class="num tabular" style="font-size:15px;color:var(--n-500);">{pv}</td>
            <td class="num tabular strong" style="font-size:19px;">{ep}</td>
            <td style="width:260px;"><div class="barbar" style="height:14px;"><i style="width:{w}%;background:{col};"></i></div></td>
            <td style="width:120px;">{tagcell}</td>
          </tr>'''
    return f'''<table class="tbl tnar" style="font-size:19px;">
        <colgroup><col style="width:340px;"><col style="width:130px;"><col style="width:80px;"><col style="width:150px;"><col style="width:280px;"><col style="width:120px;"></colgroup>
        <thead><tr><th>Narrativa</th><th class="num">{volhdr}</th><th class="num">%</th><th class="num">Eng/pieza</th><th>Tracción</th><th></th></tr></thead>
        <tbody>{body}</tbody>
      </table>'''

# 7.4 OWN — ordenado por engagement por pieza (qué rinde)
own_rows=[
 ("Salida de Canales","7","0,4%","54 885","up"),
 ("Era Almeyda","27","1,6%","14 471","up"),
 ("Fichajes y refuerzos","140","8,1%","11 686","up"),
 ("Casa Mundialista · Estadio sede","299","17,4%","7 894",""),
 ("Apertura 2026 · partidos","293","17,0%","5 848",""),
 ("Rivalidad Tigres / Japón‑Barrial","45","2,6%","5 025",""),
 ("Responsabilidad social","33","1,9%","3 488","down"),
 ("Rayadas · femenil","42","2,4%","1 339","down"),
]
sec74=f'''<section data-label="07.4 Narrativas desde cuentas oficiales">
  <div class="slide">
    <style>.tnar td,.tnar th{{padding:12px 16px;}}</style>
    <header class="slide-header">{EY7}<div class="crumb"><span>7.4</span><span class="dot">·</span><b>Narrativas · cuentas oficiales</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Narrativas desde las 8 cuentas oficiales (own media) · 1 720 publicaciones</p>
      <p class="t-h3" style="margin-bottom:20px;max-width:1300px;">Qué publica el club y qué le rinde: los hitos emocionales e institucionales mandan.</p>
      {nartable(own_rows, 54885, "Posts")}
      <div class="row" style="gap:24px;margin-top:20px;">
        <div class="fill" style="padding:16px 22px;background:var(--accent-soft);border-left:3px solid var(--accent);">
          <p class="t-small"><strong>Funciona:</strong> despedidas e hitos institucionales — Salida de Canales (54,9 K de engagement por pieza), Era Almeyda (14,5 K) y fichajes (11,7 K) —, más el Mundial/Estadio (7,9 K). Poco volumen, máximo impacto por pieza.</p>
        </div>
        <div class="fill" style="padding:16px 22px;background:#FBEEEC;border-left:3px solid #B5251D;">
          <p class="t-small"><strong>No tanto:</strong> el contenido de Rayadas femenil (1,3 K por pieza) y de responsabilidad social (3,5 K) rinde muy por debajo del resto pese a publicarse con regularidad — conviene revisar formato, timing y narrativa.</p>
        </div>
      </div>
      <p class="t-micro" style="margin-top:14px;color:var(--n-400);">Ordenado por engagement por pieza. Temas no excluyentes; base: 1 720 publicaciones de las cuentas oficiales sobre el corpus completo.</p>
    </div>
    {FOOT7}
  </div>
</section>'''

# 7.5 EARNED — ordenado por engagement por pieza (qué resuena)
earn_rows=[
 ("Rayadas · femenil","2 186","1,3%","177","up"),
 ("Casa Mundialista · Estadio sede","14 158","8,6%","175","up"),
 ("Era Almeyda","13 738","8,3%","146","up"),
 ("Rivalidad Tigres / Japón‑Barrial","18 415","11,2%","108",""),
 ("Apertura 2026 · partidos","18 169","11,0%","102",""),
 ("te Kloese · dirección","1 360","0,8%","98",""),
 ("Fichajes y refuerzos","16 631","10,1%","93",""),
 ("Responsabilidad social","334","0,2%","70","down"),
 ("Salida de Canales","6 962","4,2%","55","down"),
 ("Crítica directiva / sequía","5 110","3,1%","46","down"),
]
sec75=f'''<section data-label="07.5 Narrativas desde terceros">
  <div class="slide">
    <style>.tnar td,.tnar th{{padding:9px 16px;}}</style>
    <header class="slide-header">{EY7}<div class="crumb"><span>7.5</span><span class="dot">·</span><b>Narrativas · terceros</b></div></header>
    <div class="frame" style="padding-bottom:110px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Narrativas desde terceros (earned media) · 164 747 menciones</p>
      <p class="t-h3" style="margin-bottom:16px;max-width:1300px;">Qué amplifican los terceros y qué resuena: lo aspiracional supera al ruido crítico.</p>
      {nartable(earn_rows, 177, "Menciones")}
      <div class="row" style="gap:24px;margin-top:16px;">
        <div class="fill" style="padding:16px 22px;background:var(--accent-soft);border-left:3px solid var(--accent);">
          <p class="t-small"><strong>Resuena:</strong> las narrativas aspiracionales generan la mayor amplificación por mención — Mundial/Estadio (175), Era Almeyda (146) y el nicho femenil (177, poco volumen pero alta tracción).</p>
        </div>
        <div class="fill" style="padding:16px 22px;background:#FBEEEC;border-left:3px solid #B5251D;">
          <p class="t-small"><strong>Ruido de fondo:</strong> la crítica directiva/sequía es persistente en volumen (5 110 menciones) pero de baja amplificación (46 por pieza); la RSE casi no es recogida por terceros (334 menciones). Oportunidad de amplificar la agenda positiva y la labor social.</p>
        </div>
      </div>
      <p class="t-micro" style="margin-top:10px;color:var(--n-400);">Ordenado por engagement por pieza. El del own media (miles) es de otro orden que el de terceros (decenas–cientos): el club rinde por calidad de cuenta; los terceros, por volumen agregado.</p>
    </div>
    {FOOT7}
  </div>
</section>'''

insert_after("07.3 Narrativas por volumen", sec74+"\n"+sec75)

open(f"{SC}/Rayados_Social_Listening_v3.html","w",encoding="utf-8").write(html)

# ================= VALIDACIONES =================
print("Total <section>:", html.count("<section"))
print("crumbs:", re.findall(r'<span>([0-9]\.[0-9])</span>', html))
print("7.3 old (top autores) presente?:", "07.3 Top autores" in html)
print("7.4 presente?:", "07.4 " in html)
print("narrativas 7.3?:", 'data-label="07.3 Narrativas' in html)
print("49 495?:", "49 495" in html, "| 46,0% en 7.1?:", "46,0&nbsp;%" in html)
print("Fundación en 8.3?:", 'no como "Fundación Rayados"' in html, "| Hallazgo?:", "Hallazgo: la marca" in html)

