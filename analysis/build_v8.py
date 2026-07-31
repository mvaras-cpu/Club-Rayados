# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v7.html",encoding="utf-8").read()
v4=open(f"{SC}/Rayados_Social_Listening_v4.html",encoding="utf-8").read()
def sec(doc,label):
    s=doc.index(f'<section data-label="{label}">'); e=doc.index('</section>',s)+10; return s,e
LOGO='<span class="right"><span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span></span>'
FOOT4=f'<footer class="slide-footer"><span>04 · Narrativas y sentimiento</span>{LOGO}</footer>'

# ---------- extraer secciones v7 ----------
s_est,e_est=sec(html,"04.1 Estructura: futbolística vs no-futbolística"); EST=html[s_est:e_est]
s_alm,e_alm=sec(html,"04.2 Almeyda y jugadores"); ALM=html[s_alm:e_alm]
s_sen,e_sen=sec(html,"04.3 Distribución de sentimiento")   # se reconstruye entera

# ---------- NEW_SEN (4.1) 3-way 7/75/18 ----------
NEW_SEN=f'''<section data-label="04.1 Distribución de sentimiento">
  <div class="slide">
    <header class="slide-header"><div class="eyebrow">04 · Narrativas y sentimiento</div><div class="crumb"><span>4.1</span><span class="dot">·</span><b>Distribución de sentimiento</b></div></header>
    <div class="frame" style="padding-top:50px;gap:36px;">
      <div class="row" style="align-items:flex-start;gap:48px;margin-bottom:6px;">
        <div class="col gap-3">
          <p class="t-eyebrow">Sentimiento · conversación de terceros · clasificación por léxico explícito</p>
          <p class="t-title" style="font-size:52px;max-width:1080px;">El tono es sobre todo neutro o positivo; la crítica explícita al club es minoritaria.</p>
        </div>
        <div style="flex-shrink:0;padding-top:6px;"><span class="pill pill--neu" style="font-size:15px;">Base: menciones de terceros · el export no trae campo de sentimiento</span></div>
      </div>
      <div style="display:flex;height:84px;border:1px solid var(--n-200);margin-top:6px;">
        <div style="background:#B5251D;width:7%;display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-display);font-weight:900;font-size:24px;letter-spacing:-0.02em;">7%</div>
        <div style="background:#EAEAE8;width:75%;display:flex;align-items:center;justify-content:center;color:#0A0A0A;font-family:var(--font-display);font-weight:900;font-size:40px;letter-spacing:-0.02em;">75%</div>
        <div style="background:#1B9E4B;width:18%;display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-display);font-weight:900;font-size:32px;letter-spacing:-0.02em;">18%</div>
      </div>
      <div class="row gap-7" style="margin-top:18px;">
        <div class="col gap-4 fill">
          <div style="display:flex;align-items:center;gap:12px;"><div style="width:16px;height:16px;background:#B5251D;flex-shrink:0;"></div><span style="font-weight:700;font-size:18px;letter-spacing:.06em;text-transform:uppercase;color:#B5251D;">Negativo · 7%</span></div>
          <p style="font-size:20px;line-height:1.45;color:var(--n-600);">Crítica explícita a Rayados: <strong>dirigencia y gestión, sequía y reacción a derrotas (5,5%)</strong> más la <strong>rivalidad hostil</strong> que sí ataca al club (1,4%). Bajo volumen y baja tracción (~60 de eng/pieza).</p>
        </div>
        <div class="col gap-4 fill">
          <div style="display:flex;align-items:center;gap:12px;"><div style="width:16px;height:16px;background:#EAEAE8;border:1px solid var(--n-300);flex-shrink:0;"></div><span style="font-weight:700;font-size:18px;letter-spacing:.06em;text-transform:uppercase;color:var(--n-500);">Neutro · 75%</span></div>
          <p style="font-size:20px;line-height:1.45;color:var(--n-600);">Cobertura informativa, fichajes y retransmisión, y la <strong>rivalidad sin carga clara</strong> (notas, fixtures, comparaciones). El grueso de la conversación no expresa sentimiento explícito.</p>
        </div>
        <div class="col gap-4 fill">
          <div style="display:flex;align-items:center;gap:12px;"><div style="width:16px;height:16px;background:#1B9E4B;flex-shrink:0;"></div><span style="font-weight:700;font-size:18px;letter-spacing:.06em;text-transform:uppercase;color:#0F6B33;">Positivo · 18%</span></div>
          <p style="font-size:20px;line-height:1.45;color:var(--n-600);">Orgullo y porras, celebración de goles y fichajes, ilusión por la «nueva era» de Almeyda. Aspiracional, con alta tracción y potencial viral.</p>
        </div>
      </div>
      <p class="t-micro" style="color:var(--n-400);margin-top:4px;">Clasificación por léxico explícito sobre la base completa. Lo que no expresa sentimiento claro se cuenta como <strong>neutro</strong>; la rivalidad se cuenta como <strong>negativa solo cuando incluye crítica o mofa hacia Rayados</strong> (1,4% de terceros), y como neutra el resto (7,4%).</p>
    </div>
    {FOOT4}
  </div>
</section>'''

# ---------- NEW_QF (4.2) desde v4 ----------
s,e=sec(v4,"04.1 Qué funciona own vs terceros"); NEW_QF=v4[s:e]
NEW_QF=NEW_QF.replace('data-label="04.1 Qué funciona own vs terceros"','data-label="04.2 Narrativas: qué funciona"')
NEW_QF=NEW_QF.replace('<div class="crumb"><span>4.1</span>','<div class="crumb"><span>4.2</span>')

# ---------- NEW_EST (4.3) ----------
NEW_EST=EST.replace('data-label="04.1 Estructura: futbolística vs no-futbolística"','data-label="04.3 Estructura de la conversación"')
NEW_EST=NEW_EST.replace('<div class="crumb"><span>4.1</span>','<div class="crumb"><span>4.3</span>')
old_call='El <strong>28% de tono crítico</strong> se concentra en la dimensión institucional: la narrativa <strong>«directiva / plantel caro que no gana»</strong> es negativa en ~53%. Conviven un <strong>equity de marca positivo</strong> (mística «La Pandilla», historia, orgullo mundialista) con ese frente negativo dirigido a la gestión — y una <strong>RSE casi invisible</strong> para terceros (oportunidad de amplificación).'
new_call='La <strong>crítica dura al club es minoritaria (~5,5% de terceros)</strong> y de baja tracción: se concentra en la dimensión institucional (dirigencia y gestión) y en la reacción a resultados. Conviven un <strong>equity de marca positivo</strong> (mística «La Pandilla», historia, orgullo mundialista) con ese frente crítico acotado — y una <strong>RSE casi invisible</strong> para terceros (oportunidad de amplificación).'
assert old_call in NEW_EST,"callout no encontrado"
NEW_EST=NEW_EST.replace(old_call,new_call)

# ---------- NEW_ALM (4.4) ----------
NEW_ALM=ALM.replace('data-label="04.2 Almeyda y jugadores"','data-label="04.4 Almeyda y jugadores"')
NEW_ALM=NEW_ALM.replace('<div class="crumb"><span>4.2</span>','<div class="crumb"><span>4.4</span>')

# ---------- reensamblar cap 04 (bloque EST..SEN) ----------
block_new=NEW_SEN+"\n"+NEW_QF+"\n"+NEW_EST+"\n"+NEW_ALM
html=html[:s_est]+block_new+html[e_sen:]

# ===================== FEMSA 5.2 (dos lentes) =====================
s,e=sec(html,"05.2 FEMSA · percepción de la audiencia")
NEW_F='''<section data-label="05.2 FEMSA · percepción de la audiencia">
  <div class="slide">
    <header class="slide-header"><div class="eyebrow">05 · Rayados como institución</div><div class="crumb"><span>5.2</span><span class="dot">·</span><b>FEMSA · percepción de la audiencia</b></div></header>
    <div class="frame" style="padding-top:38px;padding-bottom:104px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Cómo se percibe a FEMSA · dos señales independientes (conversación abierta y comentarios)</p>
      <p class="t-h3" style="max-width:1320px;margin-bottom:22px;">FEMSA se percibe como promotor por dos vías distintas; ninguna crítica la ataca como propietaria.</p>
      <!-- A: earned -->
      <div style="border-top:3px solid var(--ink);padding-top:12px;margin-bottom:24px;">
        <div class="row" style="justify-content:space-between;align-items:baseline;margin-bottom:9px;"><span style="font-weight:700;font-size:15px;letter-spacing:.09em;text-transform:uppercase;">A · Conversación abierta · earned</span><span class="t-micro" style="color:var(--n-500);">860 menciones en relación a Rayados · 99% del total FEMSA</span></div>
        <div style="display:flex;height:46px;border:1px solid var(--n-200);">
          <div style="background:#1B9E4B;width:23%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;">Promotor 23%</div>
          <div style="background:#EAEAE8;width:70%;display:flex;align-items:center;justify-content:center;color:#0A0A0A;font-weight:800;font-size:15px;">Neutro 70%</div>
          <div style="background:#B5251D;width:7%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:13px;">7%</div>
        </div>
        <p class="t-small" style="color:var(--n-600);margin-top:10px;">Dominan el <strong>respaldo económico para fichajes</strong> («echar la casa por la ventana», 18%) y la comunicación de <strong>RSE, 81 aniversario y alianza WOBI</strong>. La crítica (precios, «solo negocio») es <strong>7%</strong> y no cuestiona la propiedad del club.</p>
      </div>
      <!-- B: comentarios -->
      <div style="border-top:3px solid var(--accent);padding-top:12px;">
        <div class="row" style="justify-content:space-between;align-items:baseline;margin-bottom:9px;"><span style="font-weight:700;font-size:15px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);">B · Comentarios en publicaciones propias</span><span class="t-micro" style="color:var(--n-500);">14 comentarios · posts de la Megalimpieza (jun 2026)</span></div>
        <div style="display:flex;height:46px;border:1px solid var(--n-200);">
          <div style="background:#1B9E4B;width:64.3%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;">Promotor 64%</div>
          <div style="background:#E7C877;width:21.4%;display:flex;align-items:center;justify-content:center;color:#5A420A;font-weight:800;font-size:15px;">Condic. 21%</div>
          <div style="background:#B5251D;width:14.3%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:14px;">14%</div>
        </div>
        <div class="row" style="gap:30px;margin-top:12px;align-items:flex-start;">
          <div class="fill" style="min-width:0;"><p style="font-weight:700;font-size:13px;color:#0F6B33;text-transform:uppercase;letter-spacing:.06em;">Promotor · 64%</p><p class="t-small" style="color:var(--n-600);margin-top:3px;">Aplausos y aliados que agradecen y co-construyen («Gracias por construir juntos una cultura…» —@ciclica_mex).</p></div>
          <div class="fill" style="min-width:0;"><p style="font-weight:700;font-size:13px;color:#8A6410;text-transform:uppercase;letter-spacing:.06em;">Condicional · 21%</p><p class="t-small" style="color:var(--n-600);margin-top:3px;">Apoyan, pero piden continuidad («aunque no sea el mundial», «el chiste es mantenerlo así»).</p></div>
          <div class="fill" style="min-width:0;"><p style="font-weight:700;font-size:13px;color:#B5251D;text-transform:uppercase;letter-spacing:.06em;">Detractor · 14%</p><p class="t-small" style="color:var(--n-600);margin-top:3px;">Malestar que no apunta a FEMSA: se redirige al plantel (deportivo) o al Estado (impuestos).</p></div>
        </div>
      </div>
      <div style="margin-top:18px;padding:13px 22px;background:#EEF6F0;border-left:3px solid #1B9E4B;">
        <p class="t-small"><strong>Convergen las dos señales:</strong> en la conversación abierta (23% promotor, 7% crítica) y en los comentarios (86% de apoyo), FEMSA se lee como ciudadano corporativo. <strong>Ninguna crítica la ataca como propietaria</strong>; el único frente a gestionar es la continuidad de la labor social.</p>
      </div>
    </div>
    <footer class="slide-footer"><span>05 · Rayados como institución</span>''' + LOGO + '''</footer>
  </div>
</section>'''
html=html[:s]+NEW_F+html[e:]

# ===================== te Kloese 5.3 · lente earned (en columna derecha, bajo las citas) =====================
qkey='record_mexico · 7 may 2026</p>'
qi=html.index(qkey); qdiv=html.index('</div>',qi)+len('</div>')   # cierre del div de la 3ª cita
tk_bar='''
          <p class="t-eyebrow" style="margin-top:22px;">Percepción · conversación earned</p>
          <div style="display:flex;height:40px;border:1px solid var(--n-200);margin-top:8px;">
            <div style="background:#1B9E4B;width:47%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:15px;">Promotor 47%</div>
            <div style="background:#EAEAE8;width:50%;display:flex;align-items:center;justify-content:center;color:#0A0A0A;font-weight:800;font-size:15px;">Neutro 50%</div>
            <div style="background:#B5251D;width:3%;"></div>
          </div>
          <p class="t-micro" style="color:var(--n-500);margin-top:8px;">Detractor 3%. Promueven al <strong>«arquitecto» que trajo a Almeyda</strong> (26%), la despedida del Feyenoord y la «nueva era»; la crítica o duda es marginal.</p>'''
html=html[:qdiv]+tk_bar+html[qdiv:]

# ===================== RSE 168 -> 163 =====================
assert '<span class="value tabular " style="font-size:52px;">168</span>' in html,"168 no encontrado"
html=html.replace('<span class="value tabular " style="font-size:52px;">168</span>','<span class="value tabular " style="font-size:52px;">163</span>')

open(f"{SC}/Rayados_Social_Listening_v8.html","w",encoding="utf-8").write(html)
print("sections:", html.count("<section"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', html))
print("div bal:", html.count("<div")==html.count("</div>"),"| sec bal:", html.count("<section")==html.count("</section>"))
print("28% restante:", html.count("28%"), "| 168 restante:", html.count(">168<"), "| 163:", html.count(">163<"))
print("qué funciona presente:", 'Narrativas: qué funciona' in html)
