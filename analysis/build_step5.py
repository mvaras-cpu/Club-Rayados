# -*- coding: utf-8 -*-
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'
EY='<div class="eyebrow">08 · Rayados como institución</div>'
FOOT='<footer class="slide-footer"><span>08 · Rayados como institución</span><span class="right">'+ART+'</span></footer>'

def quote(txt, src, date):
    return f'''<div style="border-left:3px solid var(--accent);padding:14px 22px;background:var(--n-50);">
        <p style="font-size:19px;line-height:1.4;color:var(--ink);">“{txt}”</p>
        <p style="font-size:14px;letter-spacing:0.06em;text-transform:uppercase;color:var(--n-500);margin-top:8px;font-weight:600;">{src} · {date}</p>
      </div>'''

def stat(label,val,sub,accent=False):
    c='accent-color' if accent else ''
    return f'''<div class="stat" style="flex:1;">
          <span class="label">{label}</span>
          <span class="value tabular {c}" style="font-size:52px;">{val}</span>
          <span class="sub">{sub}</span>
        </div>'''

# ---------- DIVIDER 08 ----------
div08='''<section data-label="08 Rayados como institución — Divider">
  <div class="slide dark">
    <div class="divider">
      <div class="top-row">
        <span class="ch-eyebrow">08 · Rayados como institución</span>
        <span style="font-family:var(--font-display);font-weight:900;font-size:28px;color:rgba(255,255,255,.45);letter-spacing:0.06em;">RAYADOS · 2026</span>
      </div>
      <div>
        <div class="ch-num" style="opacity:.12;position:absolute;right:72px;bottom:60px;font-size:480px;line-height:0.8;pointer-events:none;user-select:none;">08</div>
        <p class="ch-title">Rayados como<br>institución.</p>
        <p class="ch-desc">Más allá del equipo de fútbol: cómo aparece Rayados en su dimensión corporativa. FEMSA como propietario, Dennis te Kloese como presidente deportivo, la responsabilidad social del club y otros temas institucionales — rastreados en el texto de la base completa.</p>
      </div>
    </div>
  </div>
</section>
'''

# ---------- 8.1 FEMSA ----------
femsa_bars=""
for k,v,mx in [('ABR',25,361),('MAY',210,361),('JUN',246,361),('JUL',361,361)]:
    h=round(v/mx*150)
    femsa_bars+=f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;justify-content:flex-end;"><div style="font-weight:700;font-size:16px;">{v}</div><div style="width:54px;height:{h}px;background:var(--ink);"></div><div style="font-size:13px;font-weight:700;letter-spacing:0.08em;color:var(--n-500);">{k}</div></div>'

s81=f'''<section data-label="08.1 FEMSA — propietario">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>8.1</span><span class="dot">·</span><b>FEMSA · el propietario</b></div></header>
    <div class="frame" style="padding-top:44px;padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Menciones que refieren a FEMSA, dueño de Rayados</p>
      <p class="t-h3" style="margin-bottom:26px;max-width:1250px;">FEMSA aparece como ciudadano corporativo, no como objeto de debate.</p>
      <div class="row" style="gap:48px;align-items:flex-start;">
        <div class="col fill" style="gap:22px;">
          <div class="row" style="gap:0;">
            {stat("Menciones","842","con referencia explícita a FEMSA")}
            <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
            {stat("Interacciones","20,9 K","engagement acumulado",True)}
            <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
            {stat("Tendencia","▲ 14×","de 25 (abr) a 361 (jul)")}
          </div>
          <p class="t-small" style="color:var(--n-600);margin-top:8px;">El grupo controlador se menciona sobre todo por su rol en <strong>iniciativas de comunidad y sustentabilidad</strong> (voluntariado en la Megalimpieza del Río La Silla) y en <strong>alianzas de negocio</strong> (activación del 81 aniversario, acuerdo con WOBI). Casi no figura en la conversación crítica sobre el equipo: la propiedad no es un frente reputacional activo en el período.</p>
          <p class="t-eyebrow" style="margin-top:10px;">Menciones por mes</p>
          <div class="chart-wrap" style="padding:20px 28px 14px;"><div style="display:flex;gap:18px;height:180px;align-items:flex-end;">{femsa_bars}</div></div>
        </div>
        <div class="col fill" style="gap:16px;">
          {quote("¡Familia Rayada! Está todo listo para iniciar con la Megalimpieza del Río La Silla. Un gran partido que jugaremos entre Club, Aficionados, Voluntarios de FEMSA y parte de la comunidad.","@rayados","13 jun 2026")}
          {quote("El deporte también transforma los espacios y conecta a las personas. El Club de Futbol Monterrey celebró su 81 aniversario con la activación The World's Pitch, llevando el fútbol al corazón de la ciudad.","FEMSA","3 jul 2026")}
          {quote("La innovación también nace de las grandes alianzas. El Club de Futbol Monterrey y WOBI anunciaron una alianza estratégica que conecta el liderazgo empresarial con el deporte.","FEMSA","25 jul 2026")}
        </div>
      </div>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 8.2 TE KLOESE ----------
s82=f'''<section data-label="08.2 Dennis te Kloese">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>8.2</span><span class="dot">·</span><b>Dennis te Kloese · presidente deportivo</b></div></header>
    <div class="frame" style="padding-top:44px;padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Referencias al presidente deportivo del club</p>
      <p class="t-h3" style="margin-bottom:26px;max-width:1250px;">te Kloese: el arquitecto de la "nueva era" que trajo a Almeyda.</p>
      <div class="row" style="gap:48px;align-items:flex-start;">
        <div class="col fill" style="gap:22px;">
          <div class="row" style="gap:0;">
            {stat("Menciones","1 360","refieren a Dennis te Kloese")}
            <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
            {stat("Interacciones","133 K","engagement acumulado",True)}
            <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
            {stat("Peak","mayo","963 menciones · llegada")}
          </div>
          <p class="t-small" style="color:var(--n-600);margin-top:8px;">Su llegada (procedente del Feyenoord) concentró el peak de conversación en <strong>mayo</strong> y quedó ligada de inmediato a la promesa de <strong>"borrar a Tigres"</strong> y a la contratación de Matías Almeyda. Es una figura de <strong>tono mayoritariamente positivo y aspiracional</strong>, amplificada tanto por medios deportivos como por fan accounts.</p>
          <p class="t-eyebrow" style="margin-top:10px;">Quién lo amplifica</p>
          <p class="t-small" style="color:var(--n-500);">RG La Deportiva · delapandillatodalavida · Récord · TyC Sports · futboltotal_mx — mezcla de prensa deportiva regional/nacional y comunidad rayada.</p>
        </div>
        <div class="col fill" style="gap:16px;">
          {quote("Hoy comienza la nueva era exitosa del Monterrey. La misión fundamental de Dennis te Kloese es borrar del mapa a Tigres.","RG La Deportiva","7 may 2026")}
          {quote("Con lágrimas y siendo aplaudido por la afición, Dennis te Kloese se despide del Feyenoord. En las próximas semanas estará reportando con el Club de Fútbol Monterrey.","Prensa deportiva","may 2026")}
          {quote("Con la llegada de Dennis te Kloese, ya se rumora que tanto Matías Almeyda como Robin van Persie podrían llegar a Monterrey.","record_mexico","7 may 2026")}
        </div>
      </div>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 8.3 RSE ----------
def prog(icon,title,txt,num):
    return f'''<div style="border-top:3px solid var(--accent);padding-top:14px;">
          <div style="font-family:var(--font-display);font-weight:900;font-size:34px;color:var(--ink);">{num}</div>
          <h4 style="font-family:var(--font-display);font-weight:900;font-size:21px;margin:6px 0 4px;">{icon} {title}</h4>
          <p style="font-size:16px;color:var(--n-600);line-height:1.35;">{txt}</p>
        </div>'''

s83=f'''<section data-label="08.3 Responsabilidad social / Fundación">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>8.3</span><span class="dot">·</span><b>Responsabilidad social</b></div></header>
    <div class="frame" style="padding-top:44px;padding-bottom:130px;">
      <p class="t-eyebrow" style="margin-bottom:10px;">Comunidad · salud · educación · deporte para la niñez</p>
      <p class="t-h3" style="margin-bottom:24px;max-width:1300px;">La labor social se comunica bajo el sello #EnLaVidaYEnLaCancha, no como "Fundación Rayados".</p>
      <div class="row" style="gap:0;margin-bottom:22px;">
        {stat("Menciones RSE","2 354","labor comunitaria en la base")}
        <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
        {stat("Interacciones","1,56 M","engagement acumulado",True)}
        <div style="width:1px;background:var(--n-100);margin:0 28px;"></div>
        {stat("Impulsor","Own","impulsado por cuentas propias")}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:32px;margin-bottom:22px;">
        {prog("🌳","Medio ambiente","Megalimpieza del Río La Silla: 3,5 toneladas de residuos y +200 voluntarios (Club, afición, FEMSA, Cíclica, Municipio).","35")}
        {prog("⚽","Deporte y niñez","Escuelas Rayados y clínicas con +40 niñas y niños, con leyendas del club (Magdaleno Cano, Ignacio Jáuregui).","61")}
        {prog("🏙️","Comunidad / legado","The World's Pitch en Plaza Hidalgo: cancha pública inaugurada por el 81 aniversario, «de Monterrey para el Mundo».","39")}
        {prog("🧒","Infancia","Alianza con UNICEF México en torno a la infancia, con jugadores de Rayados como voceros.","+")}
      </div>
      <div class="row" style="gap:16px;">
        <div class="fill">{quote("La Megalimpieza Rayada logró recolectar 3,5 toneladas de residuos gracias al compromiso de más de 200 voluntarios que se sumaron a esta gran causa.","@rayados","13 jun 2026")}</div>
        <div class="fill">{quote("Magdaleno Cano e Ignacio Jáuregui compartieron una clínica de futbol con más de 40 niñas y niños de Escuelas Rayados. #EnLaVidaYEnLaCancha","@rayados","17 jul 2026")}</div>
      </div>
      <p class="t-micro" style="margin-top:14px;color:var(--n-400);">Hallazgo: la marca "Fundación Rayados" casi no aparece nominalmente en la conversación (1 mención directa). La RSE del club circula bajo programas concretos y el hashtag institucional #EnLaVidaYEnLaCancha — una oportunidad para dar nombre y continuidad narrativa a la labor social.</p>
    </div>
    {FOOT}
  </div>
</section>
'''

# ---------- 8.4 OTROS ----------
def card(num,title,txt):
    return f'''<div class="item" style="display:grid;grid-template-columns:70px 1fr;gap:22px;align-items:start;">
          <span class="num">{num}</span>
          <div><h4>{title}</h4><p>{txt}</p></div>
        </div>'''

s84=f'''<section data-label="08.4 Otros temas institucionales">
  <div class="slide">
    <header class="slide-header">{EY}<div class="crumb"><span>8.4</span><span class="dot">·</span><b>Otros temas institucionales</b></div></header>
    <div class="frame" style="padding-top:50px;">
      <p class="t-eyebrow" style="margin-bottom:20px;">Temas corporativos relevantes más allá de la propiedad y la dirección</p>
      <div class="numlist" style="display:grid;grid-template-columns:1fr 1fr;gap:40px 80px;">
        {card("A","Estadio Monterrey · activo mundialista","1 034 menciones y 930 K de engagement posicionan al Estadio Monterrey como sede del Mundial 2026 — el mayor activo reputacional institucional del período, más allá del rendimiento deportivo.")}
        {card("B","Patrocinio y marca BBVA","1 903 menciones ligan al club con BBVA (estadio y patrocinio), el sello comercial más presente en la conversación institucional.")}
        {card("C","81 aniversario del club","390 menciones alrededor de los 81 años de historia (fundación en 1945), eje del relato de tradición e identidad regiomontana comunicado en canales corporativos (LinkedIn incluido).")}
        {card("D","Alianzas estratégicas","Acuerdos como el de WOBI (World of Business Ideas) proyectan a Rayados como plataforma de liderazgo empresarial, conectando deporte y negocio desde la voz de FEMSA.")}
      </div>
      <div style="margin-top:36px;padding:22px 28px;border-left:4px solid var(--accent);background:var(--n-50);">
        <p style="font-family:var(--font-display);font-weight:900;font-size:23px;line-height:1.25;color:var(--ink);">La dimensión institucional de Rayados —Mundial, sustentabilidad, aniversario y alianzas— genera conversación positiva y de bajo riesgo, pero está fragmentada: falta un relato corporativo unificado que la capitalice.</p>
      </div>
    </div>
    {FOOT}
  </div>
</section>
'''

chap08 = div08+s81+s82+s83+s84
open(f"{SC}/chap08.html","w",encoding="utf-8").write(chap08)
print("Capítulo 08 construido:", chap08.count("<section"), "slides")
