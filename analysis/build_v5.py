# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v4.html",encoding="utf-8").read()
def repl(a,b,n=1):
    global html; assert a in html,"NO: "+a[:70]; html=html.replace(a,b,n)
def get(label):
    s=html.index(f'<section data-label="{label}">'); e=html.index('</section>',s)+len('</section>'); return s,e

ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'
def foot(l): return f'<footer class="slide-footer"><span>{l}</span><span class="right">{ART}</span></footer>'
EY4='<div class="eyebrow">04 · Narrativas y sentimiento</div>'

# ============================================================
# (1+2) NUEVA 4.1 — Futbolística vs No-futbolística + marca + negativos
# ============================================================
brand=[
 ("Dirigencia / institución","8 142","4,9%","⚠️ Negativo","#B5251D","«plantel caro que no gana», directiva"),
 ("Patrocinio / comercial","5 718","3,5%","Neutro","var(--n-500)","BBVA, tienda, marca"),
 ("Mística / identidad","4 995","3,0%","✅ Positivo","#0F6B33","«La Pandilla», orgullo, pasión, colores"),
 ("Historia / tradición","4 684","2,8%","✅ Positivo","#0F6B33","81 años, 1945, leyendas"),
 ("Estadio como marca / sede","1 249","0,8%","✅ Positivo","#0F6B33","Casa Mundialista"),
 ("Responsabilidad social","~170","0,1%","⚪ Invisible","var(--n-400)","comunidad, niñez — poco recogida"),
]
brows=""
for t,v,p,tag,col,desc in brand:
    brows+=f'''<tr>
            <td class="strong" style="font-size:18px;">{t}</td>
            <td class="num tabular" style="font-size:18px;">{v}</td>
            <td class="num tabular" style="font-size:15px;color:var(--n-500);">{p}</td>
            <td style="font-size:15px;font-weight:700;color:{col};">{tag}</td>
            <td style="font-size:15px;color:var(--n-600);">{desc}</td>
          </tr>'''
new41=f'''<section data-label="04.1 Estructura: futbolística vs no-futbolística">
  <div class="slide">
    <style>.tbrand td,.tbrand th{{padding:9px 14px;}}</style>
    <header class="slide-header">{EY4}<div class="crumb"><span>4.1</span><span class="dot">·</span><b>Estructura de la conversación</b></div></header>
    <div class="frame" style="padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Sobre qué se habla · futbolística vs no-futbolística · own y terceros</p>
      <p class="t-h3" style="margin-bottom:20px;max-width:1350px;">La conversación es sobre todo futbolística; lo institucional y de marca es minoría —y ahí vive lo negativo.</p>
      <div class="row" style="gap:40px;align-items:stretch;">
        <div style="flex:0 0 360px;border-top:4px solid var(--ink);padding-top:20px;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);">Futbolística</p>
          <div class="bignum small" style="font-size:72px;margin:6px 0;">~85%</div>
          <p class="t-small" style="color:var(--n-600);">Resultados y partidos, fichajes y refuerzos, DT y jugadores. El <strong>own</strong> la genera (bienvenidas, hitos); los <strong>terceros</strong> la amplifican (opinión, rumores, resultados). Aquí lo negativo es <strong>reacción a resultados</strong> y escepticismo de fichajes.</p>
        </div>
        <div class="fill" style="border-top:4px solid var(--accent);padding-top:20px;min-width:0;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);">No futbolística · marca e institución &nbsp;·&nbsp; ~15%</p>
          <table class="tbl tbrand" style="font-size:18px;margin-top:8px;">
            <colgroup><col style="width:280px;"><col style="width:100px;"><col style="width:90px;"><col style="width:130px;"><col style="width:360px;"></colgroup>
            <thead><tr><th>Sub-tema de marca (terceros)</th><th class="num">Menc.</th><th class="num">% earn</th><th>Tono</th><th>Qué contiene</th></tr></thead>
            <tbody>{brows}</tbody>
          </table>
        </div>
      </div>
      <div style="margin-top:18px;padding:16px 24px;background:#FBEEEC;border-left:3px solid #B5251D;">
        <p class="t-small">El <strong>28% de tono crítico</strong> se concentra en la dimensión institucional: la narrativa <strong>«directiva / plantel caro que no gana»</strong> es negativa en ~53%. Conviven un <strong>equity de marca positivo</strong> (mística «La Pandilla», historia, orgullo mundialista) con ese frente negativo dirigido a la gestión — y una <strong>RSE casi invisible</strong> para terceros (oportunidad de amplificación).</p>
      </div>
    </div>
    {foot("04 · Narrativas y sentimiento")}
  </div>
</section>'''
s,e=get("04.1 Qué funciona own vs terceros"); html=html[:s]+new41+html[e:]

# ============================================================
# (3) NUEVA 4.2 — Almeyda + ranking de jugadores
# ============================================================
alm=[("Bienvenida / nueva era","12%",True),("Proyecto / táctica","10%",False),
     ("Dudas / escepticismo","9%",False),("«Borrar a Tigres»","3%",False),("Salario / negociación","2%",False)]
arows=""
for t,v,acc in alm:
    col='var(--accent)' if acc else 'var(--ink)'
    arows+=f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--n-100);padding:9px 0;"><span style="font-size:20px;color:var(--n-700);">{t}</span><span class="mono" style="font-size:22px;font-weight:700;color:{col};">{v}</span></div>'
players=[(1,"Sergio Canales","6 969","4,2%","Despedida (salida 28 abr)",""),
 (2,"Orbelín Pineda","4 767","2,9%","Bienvenida · liderazgo","up"),
 (3,"Hugo Cuypers","3 085","1,9%","Bienvenida · goleador","up"),
 (4,"Esteban Andrada","2 398","1,4%","Sanción en España","down"),
 (5,"Diego Rossi","2 395","1,4%","Bienvenida · palmarés","up"),
 (6,"Lucas Ocampos","1 513","0,9%","Rendimiento / plantel",""),
 (7,"Óliver Torres","438","0,3%","Plantel",""),
 (8,"Fidel Ambriz","321","0,2%","Plantel","")]
prows=""
for rk,nm,v,pc,tema,tag in players:
    mk='<span style="color:#B5251D;">⚠️ </span>' if tag=='down' else ''
    prows+=f'''<tr>
            <td class="t-micro" style="color:var(--n-400);">{rk}</td>
            <td class="strong" style="font-size:19px;">{nm}</td>
            <td class="num tabular" style="font-size:19px;">{v}</td>
            <td class="num tabular" style="font-size:15px;color:var(--n-500);">{pc}</td>
            <td style="font-size:17px;color:var(--n-600);">{mk}{tema}</td>
          </tr>'''
new42=f'''<section data-label="04.2 Almeyda y jugadores">
  <div class="slide">
    <header class="slide-header">{EY4}<div class="crumb"><span>4.2</span><span class="dot">·</span><b>Almeyda y jugadores</b></div></header>
    <div class="frame" style="padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">De quién se habla · Almeyda y los jugadores de Rayados</p>
      <p class="t-h3" style="margin-bottom:22px;">Almeyda concentra la conversación; los refuerzos y la salida de Canales, el resto.</p>
      <div class="row" style="gap:56px;align-items:flex-start;">
        <div style="flex:0 0 470px;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:6px;">Matías Almeyda · DT</p>
          <div class="row" style="gap:20px;align-items:baseline;margin-bottom:10px;">
            <div class="bignum small" style="font-size:60px;white-space:nowrap;">13 765</div>
            <p class="t-small" style="color:var(--n-500);">menciones · 8,3% del corpus</p>
          </div>
          {arows}
          <p class="t-micro" style="margin-top:12px;color:var(--n-500);">Figura aspiracional con una <strong>veta escéptica clara</strong> (9%): la ilusión de la «nueva era» convive con dudas sobre qué tan real es el proyecto.</p>
        </div>
        <div class="fill" style="min-width:0;">
          <p style="font-weight:700;font-size:16px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);margin-bottom:8px;">Ranking de jugadores por volumen</p>
          <table class="tbl" style="font-size:19px;">
            <colgroup><col style="width:40px;"><col style="width:230px;"><col style="width:110px;"><col style="width:90px;"><col style="width:300px;"></colgroup>
            <thead><tr><th>#</th><th>Jugador</th><th class="num">Menciones</th><th class="num">%</th><th>Tema dominante</th></tr></thead>
            <tbody>{prows}</tbody>
          </table>
          <p class="t-micro" style="margin-top:12px;color:var(--n-400);">Jugadores actuales de Rayados. Excluye al DT (Almeyda, arriba) y los nombres de mercado/rumores (Erik Lira, Quiñones). Andrada destaca por su sanción en España más que por su juego.</p>
        </div>
      </div>
    </div>
    {foot("04 · Narrativas y sentimiento")}
  </div>
</section>'''
# insertar 4.2 justo después de la nueva 4.1
s,e=get("04.1 Estructura: futbolística vs no-futbolística"); html=html[:e]+"\n"+new42+html[e:]

# ============================================================
# (2b) Sentimiento -> 4.3 + re-etiquetado del 28%
# ============================================================
s,e=get("04.2 Distribución de sentimiento"); seg=html[s:e]
seg=seg.replace('data-label="04.2 Distribución de sentimiento"','data-label="04.3 Distribución de sentimiento"')
seg=seg.replace('<span>4.2</span>','<span>4.3</span>')
seg=seg.replace('Negativo · 28%','Crítico / no-positivo · 28%')
seg=seg.replace('Críticas a plantel, directiva y sequía de títulos; rivalidad con Tigres y cuentas de rivalidad. Tono estable, no escala con los hitos positivos.',
 'Agrupa crítica al club (directiva, sequía, resultados) y <strong>rivalidad bidireccional</strong> (Tigres/América). El negativo estructural dirigido al club es ~3–4% y de baja tracción (49 de eng/pieza vs 175 de lo aspiracional).')
html=html[:s]+seg+html[e:]

# ============================================================
# (4) FEMSA (05.1)
# ============================================================
repl('con referencia explícita a FEMSA','0,51% del corpus')
repl('El grupo controlador se menciona sobre todo por su rol en <strong>iniciativas de comunidad y sustentabilidad</strong> (voluntariado en la Megalimpieza del Río La Silla) y en <strong>alianzas de negocio</strong> (activación del 81 aniversario, acuerdo con WOBI). Casi no figura en la conversación crítica sobre el equipo: la propiedad no es un frente reputacional activo en el período.</p>',
 'FEMSA representa el <strong>0,51% del corpus</strong> (842 menciones). La conversación es <strong>99,5% de terceros</strong> (earned) y solo <strong>0,5% del club</strong> (own) —una diferencia de <strong>99 puntos</strong>: FEMSA casi no aparece en los canales propios—. En <strong>earned</strong> dominan el respaldo económico para fichajes («echar la casa por la ventana») y la comunicación de RSE, 81 aniversario y alianza WOBI desde la propia cuenta de FEMSA; en <strong>own</strong>, solo el voluntariado (Megalimpieza). No es un frente reputacional crítico.</p>')

# ============================================================
# (5) te Kloese (05.2)
# ============================================================
repl('Su llegada (procedente del Feyenoord) concentró el peak de conversación en <strong>mayo</strong> y quedó ligada de inmediato a la promesa de <strong>"borrar a Tigres"</strong> y a la contratación de Matías Almeyda. Es una figura de <strong>tono mayoritariamente positivo y aspiracional</strong>, amplificada tanto por medios deportivos como por fan accounts.</p>',
 'te Kloese representa el <strong>0,82% del corpus</strong> (1 360 menciones) y es <strong>100% de terceros</strong> (earned): el club nunca lo nombró en sus cuentas propias (0% own, diferencia de <strong>100 puntos</strong>). Su llegada (procedente del Feyenoord) concentró el peak en <strong>mayo</strong>. En earned dominan tres narrativas: <strong>«nueva era / borrar a Tigres»</strong>, <strong>el arquitecto que trajo a Almeyda</strong> (y el rumor Van Persie) y su <strong>despedida del Feyenoord</strong>. Tono aspiracional/positivo, amplificado por prensa y fan accounts.</p>')

# ============================================================
# (6) RSE (05.3) — cifra corregida + título
# ============================================================
repl('La labor social se comunica bajo el sello #EnLaVidaYEnLaCancha.',
     'Labor social: comunidad, medio ambiente y deporte para la niñez.')
repl('<span class="value tabular " style="font-size:52px;">2 354</span>','<span class="value tabular " style="font-size:52px;">168</span>')
repl('<span class="value tabular accent-color" style="font-size:52px;">1,56 M</span>','<span class="value tabular accent-color" style="font-size:52px;">70 K</span>')
repl('La RSE del club circula bajo programas concretos y el hashtag institucional #EnLaVidaYEnLaCancha — una oportunidad para dar nombre y continuidad narrativa a la labor social.',
 'Medido por programas concretos (Megalimpieza, Escuelas Rayados, The World\'s Pitch, UNICEF), excluyendo el hashtag general #EnLaVidaYEnLaCancha (que se usa en +2 000 posts). La conversación amplia de comunidad y voluntariado llega a ~450 menciones; impulsada por las cuentas propias (75% del engagement). Oportunidad de dar nombre y amplificar la labor social.')

open(f"{SC}/Rayados_Social_Listening_v5.html","w",encoding="utf-8").write(html)
print("sections:", html.count("<section"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', html))
print("div bal:", html.count("<div")==html.count("</div>"), "| sec bal:", html.count("<section")==html.count("</section>"))
print("2 354 restante:", html.count("2 354"), "| 1,56 M:", html.count("1,56 M"))
