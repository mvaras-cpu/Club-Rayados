# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v3.html",encoding="utf-8").read()

HEAD=html[:html.index('<section data-label="Portada"')]
TAIL=html[html.index('</section>', html.index('data-label="Cierre"'))+len('</section>'):]

def sec(label):
    s=html.index(f'<section data-label="{label}">'); e=html.index('</section>',s)+len('</section>')
    return html[s:e]

def rewrite(block, new_label, new_sub, new_dl):
    m=re.search(r'<div class="eyebrow">([^<]+)</div>', block)
    if m: block=block.replace(m.group(1), new_label)
    block=re.sub(r'<span>[0-9]+\.[0-9]+</span>', f'<span>{new_sub}</span>', block, count=1)
    block=re.sub(r'data-label="[^"]*"', f'data-label="{new_dl}"', block, count=1)
    return block

ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'
def footer(lbl): return f'<footer class="slide-footer"><span>{lbl}</span><span class="right">{ART}</span></footer>'

def divider(num, eyebrow, title_html, desc):
    return f'''<section data-label="{num} {eyebrow} — Divider">
  <div class="slide dark">
    <div class="divider">
      <div class="top-row">
        <span class="ch-eyebrow">{num} · {eyebrow}</span>
        <span style="font-family:var(--font-display);font-weight:900;font-size:28px;color:rgba(255,255,255,.45);letter-spacing:0.06em;">RAYADOS · 2026</span>
      </div>
      <div>
        <div class="ch-num" style="opacity:.12;position:absolute;right:72px;bottom:60px;font-size:480px;line-height:0.8;pointer-events:none;user-select:none;">{num}</div>
        <p class="ch-title">{title_html}</p>
        <p class="ch-desc">{desc}</p>
      </div>
    </div>
  </div>
</section>'''

# ===================== ÍNDICE (6 capítulos) =====================
def idx_item(num, title, desc):
    return f'''        <div style="display:grid;grid-template-columns:74px 1fr;gap:24px;align-items:baseline;border-top:2px solid var(--n-200);padding-top:16px;">
          <span style="font-family:var(--font-display);font-weight:900;font-size:44px;letter-spacing:-0.02em;color:var(--ink);">{num}</span>
          <div>
            <h4 style="font-family:var(--font-display);font-weight:900;font-size:28px;line-height:1.05;margin:0 0 4px;color:var(--ink);">{title}</h4>
            <p style="font-size:18px;color:var(--n-500);margin:0;line-height:1.3;">{desc}</p>
          </div>
        </div>'''
indice=f'''<section data-label="Índice">
  <div class="slide">
    <header class="slide-header">
      <div class="eyebrow">Rayados · Social Listening Q2–Q3 2026</div>
      <div class="crumb"><b>Índice</b></div>
    </header>
    <div class="frame" style="padding-top:52px;padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Contenido del reporte</p>
      <h2 class="t-h2" style="font-size:56px;margin-bottom:44px;">Seis capítulos.</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px 80px;">
{idx_item("01","Resumen ejecutivo","Cinco lecturas y la magnitud del trimestre")}
{idx_item("02","Volumen, dinámica e hitos","166 467 menciones, sus peaks y los hitos que los detonaron")}
{idx_item("03","Plataformas y autores","Dónde se habla, quién habla y own vs earned media")}
{idx_item("04","Narrativas y sentimiento","Qué temas mueven la conversación y qué funciona")}
{idx_item("05","Rayados como institución","FEMSA, Dennis te Kloese y responsabilidad social")}
{idx_item("06","Recomendaciones","Vigilancia, monitoreo y lineamientos estratégicos")}
      </div>
    </div>
    {footer("Índice")}
  </div>
</section>'''

# ===================== NEW 3.1 · PLATAFORMAS (total) =====================
EY3='<div class="eyebrow">03 · Plataformas y autores</div>'
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
prows=""
for p,mn,pv,eg,epp,dest,acc in plat:
    st=' style="color:var(--accent);font-weight:700;"' if acc else ''
    prows+=f'<tr><td class="strong"{st}>{p}</td><td class="num tabular"{st}>{mn}</td><td class="num tabular">{pv}</td><td class="num tabular"{st}>{eg}</td><td class="num tabular">{epp}</td><td style="color:var(--n-600);font-size:18px;">{dest}</td></tr>'
new31=f'''<section data-label="03.1 Plataformas">
  <div class="slide">
    <header class="slide-header">{EY3}<div class="crumb"><span>3.1</span><span class="dot">·</span><b>Distribución por plataforma</b></div></header>
    <div class="frame" style="padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Menciones y engagement por plataforma · base completa · ordenado por menciones</p>
      <p class="t-h3" style="margin-bottom:18px;">X domina el volumen; Instagram y Facebook concentran el engagement.</p>
      <table class="tbl" style="font-size:20px;table-layout:fixed;">
        <colgroup><col style="width:250px;"><col style="width:160px;"><col style="width:110px;"><col style="width:160px;"><col style="width:140px;"><col style="width:560px;"></colgroup>
        <thead><tr><th>Plataforma</th><th class="num">Menciones</th><th class="num">% vol</th><th class="num">Engagement</th><th class="num">Eng/pieza</th><th>En qué destaca</th></tr></thead>
        <tbody>{prows}</tbody>
      </table>
      <div style="margin-top:14px;padding:16px 24px;background:var(--n-50);border-left:3px solid var(--accent);">
        <p class="t-small">X aporta el 69&nbsp;% de las menciones pero solo el 18&nbsp;% del engagement: es la plaza del debate. Instagram (47&nbsp;% del engagement) y Facebook (19&nbsp;%) concentran la tracción porque ahí publican las cuentas propias; TikTok rinde altísimo por pieza con poco volumen. El club publica 1 720 piezas propias, sobre todo en Instagram.</p>
      </div>
    </div>
    {footer("03 · Plataformas y autores")}
  </div>
</section>'''

# ===================== NEW 3.2 · CONCENTRACIÓN + OWN vs EARNED =====================
new32=f'''<section data-label="03.2 Concentración y own vs earned">
  <div class="slide">
    <header class="slide-header">{EY3}<div class="crumb"><span>3.2</span><span class="dot">·</span><b>Concentración · own vs earned</b></div></header>
    <div class="frame" style="flex-direction:row;gap:64px;align-items:center;padding-bottom:120px;">
      <div class="col gap-5" style="align-items:center;flex-shrink:0;">
        <svg viewBox="0 0 360 360" style="width:340px;height:340px;">
          <circle cx="180" cy="180" r="140" fill="none" stroke="#EAEAE8" stroke-width="64"/>
          <circle cx="180" cy="180" r="140" fill="none" stroke="#0A0A0A" stroke-width="64" stroke-dasharray="575.3 879.6" transform="rotate(-90 180 180)"/>
          <text x="180" y="164" text-anchor="middle" font-family="'Visby CF','Inter',system-ui" font-weight="900" font-size="80" fill="#0A0A0A" letter-spacing="-2">65%</text>
          <text x="180" y="202" text-anchor="middle" font-family="Inter,system-ui" font-weight="700" font-size="13" fill="#5C5C59" letter-spacing="2">DEL ENGAGEMENT</text>
          <text x="180" y="222" text-anchor="middle" font-family="Inter,system-ui" font-weight="600" font-size="12" fill="#8B8B87" letter-spacing="1.5">EN 30 CUENTAS</text>
        </svg>
        <p class="t-micro" style="text-align:center;max-width:320px;color:var(--n-400);">49 495 autores únicos · 20,6 M interacciones · 166 467 menciones</p>
      </div>
      <div class="col gap-5 fill">
        <p class="t-eyebrow">La conversación es masiva en volumen, muy estrecha en influencia</p>
        <p class="t-title" style="font-size:44px;max-width:940px;">Pocas cuentas concentran el engagement — y el club domina.</p>
        <div class="row" style="gap:32px;margin-top:8px;">
          <div style="flex:1;border-top:4px solid var(--accent);padding-top:18px;">
            <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:10px;">Own media · 8 cuentas propias</p>
            <div class="row" style="gap:24px;">
              <div><div class="bignum small" style="font-size:52px;">1,0%</div><p class="t-micro" style="margin-top:2px;">del volumen (1 720 posts)</p></div>
              <div><div class="bignum small accent-color" style="font-size:52px;">46,0%</div><p class="t-micro" style="margin-top:2px;">del engagement (9,5 M)</p></div>
            </div>
          </div>
          <div style="flex:1;border-top:4px solid var(--ink);padding-top:18px;">
            <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);margin-bottom:10px;">Earned media · terceros</p>
            <div class="row" style="gap:24px;">
              <div><div class="bignum small" style="font-size:52px;">99,0%</div><p class="t-micro" style="margin-top:2px;">del volumen (164 747)</p></div>
              <div><div class="bignum small" style="font-size:52px;">54,0%</div><p class="t-micro" style="margin-top:2px;">del engagement (11,1 M)</p></div>
            </div>
          </div>
        </div>
        <p class="t-small t-body--muted" style="margin-top:14px;">Los tres handles oficiales de mayor engagement —Rayados en Instagram, Facebook y TikTok— concentran el <strong>39,3&nbsp;%</strong> del engagement total; la cuenta #1 (Rayados en Instagram) suma 5,4&nbsp;M (26&nbsp;%). El ecosistema de terceros compite sobre una base ya dominada por el owned.</p>
      </div>
    </div>
    {footer("03 · Plataformas y autores")}
  </div>
</section>'''

# ===================== NEW 4.1 · QUÉ FUNCIONA (own vs terceros) =====================
EY4='<div class="eyebrow">04 · Narrativas y sentimiento</div>'
def minitab(rows, maxep):
    body=""
    for nar,vol,ep,tag in rows:
        w=round(int(ep.replace(" ",""))/maxep*100,1)
        col='var(--accent)' if tag=='up' else ('#B5251D' if tag=='down' else 'var(--ink)')
        body+=f'<tr><td class="strong" style="font-size:17px;">{nar}</td><td class="num tabular" style="font-size:16px;color:var(--n-500);">{vol}</td><td class="num tabular strong" style="font-size:17px;">{ep}</td><td style="width:110px;"><div class="barbar" style="height:12px;"><i style="width:{w}%;background:{col};"></i></div></td></tr>'
    return f'<table class="tbl tqf" style="font-size:17px;"><colgroup><col style="width:250px;"><col style="width:90px;"><col style="width:100px;"><col style="width:120px;"></colgroup><thead><tr><th>Narrativa</th><th class="num">Vol.</th><th class="num">Eng/pza</th><th></th></tr></thead><tbody>{body}</tbody></table>'
own_r=[("Salida de Canales","7","54 885","up"),("Era Almeyda","27","14 471","up"),("Fichajes y refuerzos","140","11 686","up"),("Casa Mundialista","299","7 894",""),("Apertura · partidos","293","5 848",""),("Rivalidad Tigres/Japón","45","5 025",""),("Responsabilidad social","33","3 488","down"),("Rayadas · femenil","42","1 339","down")]
earn_r=[("Rayadas · femenil","2 186","177","up"),("Casa Mundialista","14 158","175","up"),("Era Almeyda","13 738","146","up"),("Rivalidad Tigres/Japón","18 415","108",""),("Apertura · partidos","18 169","102",""),("Fichajes y refuerzos","16 631","93",""),("Responsabilidad social","334","70","down"),("Crítica directiva/sequía","5 110","46","down")]
new41=f'''<section data-label="04.1 Qué funciona own vs terceros">
  <div class="slide">
    <style>.tqf td,.tqf th{{padding:8px 12px;}}</style>
    <header class="slide-header">{EY4}<div class="crumb"><span>4.1</span><span class="dot">·</span><b>Narrativas: qué funciona</b></div></header>
    <div class="frame" style="padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Principales narrativas y su tracción · own vs terceros · ordenado por engagement por pieza</p>
      <p class="t-h3" style="margin-bottom:20px;">Lo que el club publica y lo que la afición amplifica no coinciden en lo que rinde.</p>
      <div class="row" style="gap:56px;align-items:flex-start;">
        <div style="flex:1;min-width:0;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:10px;">Own media · cuentas oficiales (1 720 posts)</p>
          {minitab(own_r, 54885)}
          <p class="t-micro" style="margin-top:10px;color:var(--n-500);"><strong style="color:var(--ink);">Rinden</strong> las despedidas y los hitos institucionales (Canales, Almeyda, fichajes). <strong style="color:var(--ink);">Rinden poco</strong> el femenil y la RSE pese a publicarse seguido.</p>
        </div>
        <div style="flex:1;min-width:0;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);margin-bottom:10px;">Earned media · terceros (164 747 menciones)</p>
          {minitab(earn_r, 177)}
          <p class="t-micro" style="margin-top:10px;color:var(--n-500);"><strong style="color:var(--ink);">Resuena</strong> lo aspiracional (Mundial, Almeyda, femenil). La <strong style="color:var(--ink);">crítica</strong> es ruido de alto volumen y baja tracción; la RSE casi no la recogen terceros.</p>
        </div>
      </div>
      <p class="t-micro" style="margin-top:12px;color:var(--n-400);">El engagement por pieza del own media (miles) es de otro orden que el de terceros (decenas–cientos). Etiquetado por palabras clave sobre la base completa; temas no excluyentes.</p>
    </div>
    {footer("04 · Narrativas y sentimiento")}
  </div>
</section>'''

# ===================== NEW 5.3 · RSE + OTROS =====================
def prog(icon,title,txt,num):
    return f'''<div style="border-top:3px solid var(--accent);padding-top:12px;">
          <div style="font-family:var(--font-display);font-weight:900;font-size:30px;color:var(--ink);">{num}</div>
          <h4 style="font-family:var(--font-display);font-weight:900;font-size:19px;margin:5px 0 3px;">{icon} {title}</h4>
          <p style="font-size:15px;color:var(--n-600);line-height:1.3;">{txt}</p>
        </div>'''
def otro(letter,title,txt):
    return f'<div style="display:grid;grid-template-columns:34px 1fr;gap:12px;align-items:start;"><span style="font-family:var(--font-display);font-weight:900;font-size:24px;color:var(--accent);">{letter}</span><div><h4 style="font-family:var(--font-display);font-weight:900;font-size:17px;margin:0 0 2px;">{title}</h4><p style="font-size:14px;color:var(--n-600);line-height:1.3;">{txt}</p></div></div>'
new53=f'''<section data-label="05.3 Responsabilidad social y otros temas">
  <div class="slide">
    <header class="slide-header"><div class="eyebrow">05 · Rayados como institución</div><div class="crumb"><span>5.3</span><span class="dot">·</span><b>Responsabilidad social y otros temas</b></div></header>
    <div class="frame" style="padding-top:40px;padding-bottom:110px;">
      <p class="t-eyebrow" style="margin-bottom:6px;">Comunidad · salud · educación · deporte para la niñez — bajo el sello #EnLaVidaYEnLaCancha</p>
      <p class="t-h3" style="margin-bottom:16px;">Responsabilidad social (2 354 menciones · 1,56 M eng · impulsada por cuentas propias).</p>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:26px;margin-bottom:22px;">
        {prog("🌳","Medio ambiente","Megalimpieza del Río La Silla: 3,5 t de residuos y +200 voluntarios (Club, afición, FEMSA, Cíclica, Municipio).","35")}
        {prog("⚽","Deporte y niñez","Escuelas Rayados y clínicas con +40 niñas y niños, con leyendas del club.","61")}
        {prog("🏙️","Comunidad / legado","The World's Pitch en Plaza Hidalgo: cancha pública abierta en el 81 aniversario.","39")}
        {prog("🧒","Infancia","Alianza con UNICEF México en torno a la infancia, con jugadores como voceros.","+")}
      </div>
      <p class="t-eyebrow" style="margin-bottom:12px;">Otros temas institucionales</p>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:26px;">
        {otro("A","Estadio Monterrey · sede","1 034 menciones y 930 K de engagement: el estadio del club como sede del Mundial 2026, mayor activo institucional del período.")}
        {otro("B","Patrocinio BBVA","1 903 menciones ligan al club con BBVA (estadio y patrocinio), el sello comercial más presente.")}
        {otro("C","81 aniversario","390 menciones alrededor de los 81 años (fundación en 1945): relato de tradición e identidad regiomontana.")}
        {otro("D","Alianzas estratégicas","Acuerdos como WOBI proyectan a Rayados como plataforma de liderazgo empresarial (voz de FEMSA).")}
      </div>
    </div>
    {footer("05 · Rayados como institución")}
  </div>
</section>'''

# ===================== ENSAMBLE =====================
body=[]
body.append(sec("Portada"))
body.append(indice)
# Cap 1
body.append(divider("01","Resumen ejecutivo","Resumen<br>ejecutivo.","Las cinco lecturas que el equipo directivo necesita para entender qué dijo la conversación digital sobre Rayados entre abril y julio de 2026, y qué conviene hacer al respecto."))
body.append(sec("01.1 Resumen ejecutivo — cinco lecturas clave"))
body.append(sec("01.2 Resumen ejecutivo — cifra tesis"))
# Cap 2
body.append(divider("02","Volumen, dinámica e hitos","Volumen, dinámica<br>e hitos.","166 467 publicaciones en 92 días. Los peaks responden a decisiones institucionales —salida de Canales, llegada de Almeyda, refuerzos— más que a resultados deportivos; el Mundial fue una narrativa sostenida, no un peak de un día."))
body.append(rewrite(sec("02.1 Stats globales del período"),"02 · Volumen, dinámica e hitos","2.1","02.1 Métricas del período"))
body.append(rewrite(sec("06.2 Hitos — curva con anotaciones"),"02 · Volumen, dinámica e hitos","2.2","02.2 Curva diaria anotada"))
body.append(rewrite(sec("02.3 Qué detonó cada peak"),"02 · Volumen, dinámica e hitos","2.3","02.3 Motor de cada peak"))
# Cap 3
body.append(divider("03","Plataformas y autores","Plataformas<br>y autores.","Dónde se habla y quién habla. X domina el volumen, pero el engagement se concentra en Instagram y Facebook y en un puñado de cuentas: las 8 propias del club generan casi la mitad de las interacciones."))
body.append(new31)
body.append(new32)
body.append(rewrite(sec("04.2 Top 30 autores — tabla doble"),"03 · Plataformas y autores","3.3","03.3 Top autores por engagement"))
body.append(rewrite(sec("04.3 Tipologías de actores"),"03 · Plataformas y autores","3.4","03.4 Tipologías de actores"))
# Cap 4
body.append(divider("04","Narrativas y sentimiento","Narrativas<br>y sentimiento.","Qué temas mueven la conversación y con qué tono. Lo que el club publica y lo que amplifican los terceros no siempre coincide en lo que funciona."))
body.append(new41)
body.append(rewrite(sec("05.1 Sentimiento global de terceros"),"04 · Narrativas y sentimiento","4.2","04.2 Distribución de sentimiento"))
# Cap 5
body.append(divider("05","Rayados como institución","Rayados como<br>institución.","Más allá del equipo de fútbol: FEMSA como propietario, Dennis te Kloese en la dirección deportiva y la responsabilidad social del club."))
body.append(rewrite(sec("08.1 FEMSA — propietario"),"05 · Rayados como institución","5.1","05.1 FEMSA · el propietario"))
body.append(rewrite(sec("08.2 Dennis te Kloese"),"05 · Rayados como institución","5.2","05.2 Dennis te Kloese"))
body.append(new53)
# Cap 6
body.append(divider("06","Recomendaciones","Recomendaciones.","Lineamientos estratégicos de comunicación y monitoreo derivados de los hallazgos del trimestre: Mundial, era Almeyda y tensiones narrativas con la afición."))
body.append(rewrite(sec("09.1 Recomendaciones — Vigilancia y monitoreo"),"06 · Recomendaciones","6.1","06.1 Vigilancia y monitoreo"))
body.append(rewrite(sec("09.2 Recomendaciones — Lineamientos estratégicos"),"06 · Recomendaciones","6.2","06.2 Lineamientos estratégicos"))
body.append(sec("Cierre"))

out=HEAD+"\n".join(body)+"\n"+TAIL
open(f"{SC}/Rayados_Social_Listening_v4.html","w",encoding="utf-8").write(out)

# validación
print("sections:", out.count("<section"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', out))
print("ch-eyebrows:", re.findall(r'class="ch-eyebrow">([^<]+)', out))
print("div balance:", out.count("<div")==out.count("</div>"), "| sec balance:", out.count("<section")==out.count("</section>"))
print("dup eyebrow check (should be no 07/08/09 refs):", [x for x in re.findall(r'<div class="eyebrow">([^<]+)</div>', out) if x[:2] in ('07','08','09')][:5])
