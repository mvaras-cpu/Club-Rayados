# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v5.html",encoding="utf-8").read()

def sec_slice(label):
    s=html.index(f'<section data-label="{label}">'); e=html.index('</section>',s)+len('</section>'); return s,e

# ---- 1) Renumerar RSE 5.3 -> 5.4 (dentro de su seccion) ----
s,e=sec_slice("05.3 Responsabilidad social"); seg=html[s:e]
seg=seg.replace('data-label="05.3 Responsabilidad social"','data-label="05.4 Responsabilidad social"')
seg=seg.replace('<span>5.3</span>','<span>5.4</span>')
html=html[:s]+seg+html[e:]

# ---- 2) Renumerar te Kloese 5.2 -> 5.3 (dentro de su seccion) ----
s,e=sec_slice("05.2 Dennis te Kloese"); seg=html[s:e]
seg=seg.replace('data-label="05.2 Dennis te Kloese"','data-label="05.3 Dennis te Kloese"')
seg=seg.replace('<span>5.2</span>','<span>5.3</span>')
html=html[:s]+seg+html[e:]

# ---- 3) Nueva slide 5.2 · FEMSA · percepcion de la audiencia ----
FOOT='<footer class="slide-footer"><span>05 · Rayados como institución</span><span class="right"><span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span></span></footer>'
HEAD='<header class="slide-header"><div class="eyebrow">05 · Rayados como institución</div><div class="crumb"><span>5.2</span><span class="dot">·</span><b>FEMSA · percepción de la audiencia</b></div></header>'

focos=[
 ("#1B9E4B","#0F6B33","Promotor · apoyo a la acción","9 · 64%","Promueve a FEMSA",
  "«Gracias por construir juntos una cultura en gestión de residuos y cuidado de la Tierra, en la cancha y afuera de ella 🌎⚽🙌»",
  "@ciclica_mex · 13 jun",
  "Aplausos (👏, «Son los mejores 🙌») y aliados ambientales que agradecen y suman. La iniciativa se lee como algo bueno del club y de FEMSA."),
 ("#C9922B","#8A6410","Promotor condicional · continuidad","3 · 21%","Apoya, pero condiciona",
  "«Sigamos limpiando aunque no sea el mundial… buscamos crear una comunidad consciente» · «el chiste es mantenerlo así»",
  "@riovivomx · @marco_hernandezz94",
  "Apoyan la causa pero piden que sea sostenida y no oportunismo por el Mundial 2026. Es respaldo con una reserva de continuidad."),
 ("#B5251D","#B5251D","Detractor · malestar redirigido","2 · 14%","No apunta a FEMSA",
  "«También sería bueno limpiar el plantel de tanto jugador mediocre…» · «Cosas que debería hacer el gobierno con nuestros impuestos»",
  "@bychrxsoff · @dantebaresi",
  "La única crítica no ataca a FEMSA como propietario: se desvía al plantel (malestar deportivo) o al rol del Estado (impuestos)."),
]
cards=""
for bar,txt,label,cnt,tag,quote,author,gloss in focos:
    cards+=f'''<div class="fill" style="min-width:0;border-top:4px solid {bar};padding-top:14px;">
        <div style="display:flex;justify-content:space-between;align-items:baseline;gap:10px;">
          <span style="font-weight:700;font-size:14px;letter-spacing:.07em;text-transform:uppercase;color:{txt};line-height:1.2;">{label}</span>
          <span class="mono" style="font-size:15px;font-weight:700;color:{txt};white-space:nowrap;">{cnt}</span>
        </div>
        <p style="font-size:15px;font-weight:700;color:var(--n-500);margin-top:6px;letter-spacing:.02em;">{tag}</p>
        <div style="border-left:3px solid {bar};padding:11px 16px;background:var(--n-50);margin-top:10px;">
          <p style="font-size:16px;line-height:1.42;color:var(--ink);">{quote}</p>
          <p style="font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--n-500);margin-top:8px;font-weight:600;">{author}</p>
        </div>
        <p class="t-micro" style="margin-top:10px;color:var(--n-600);line-height:1.4;">{gloss}</p>
      </div>'''

new52=f'''<section data-label="05.2 FEMSA · percepción de la audiencia">
  <div class="slide">
    {HEAD}
    <div class="frame" style="padding-top:40px;padding-bottom:118px;">
      <div class="row" style="align-items:flex-start;gap:40px;margin-bottom:16px;">
        <div style="min-width:0;">
          <p class="t-eyebrow" style="margin-bottom:8px;">Comentarios en los posts de @rayados sobre la Megalimpieza del Río La Silla (iniciativa FEMSA) · jun 2026</p>
          <p class="t-h3" style="max-width:1250px;">La audiencia percibe a FEMSA como <strong>promotor</strong>; el malestar que existe no apunta a FEMSA, se redirige.</p>
        </div>
        <div style="flex-shrink:0;padding-top:4px;"><span class="pill pill--neu" style="font-size:14px;">14 comentarios de audiencia · lectura cualitativa</span></div>
      </div>
      <!-- barra promotor / condicional / detractor -->
      <div style="display:flex;height:64px;border:1px solid var(--n-200);margin-bottom:8px;">
        <div style="background:#1B9E4B;width:64.3%;display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-display);font-weight:900;font-size:26px;letter-spacing:-0.02em;">Promotor · 64%</div>
        <div style="background:#E7C877;width:21.4%;display:flex;align-items:center;justify-content:center;color:#5A420A;font-family:var(--font-display);font-weight:900;font-size:22px;letter-spacing:-0.02em;">Condic. · 21%</div>
        <div style="background:#B5251D;width:14.3%;display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-display);font-weight:900;font-size:20px;letter-spacing:-0.02em;">14%</div>
      </div>
      <p class="t-micro" style="color:var(--n-400);margin-bottom:20px;">Foco de los comentarios · postura frente a FEMSA / la iniciativa</p>
      <div class="row" style="gap:32px;align-items:stretch;">{cards}</div>
      <div style="margin-top:20px;padding:15px 24px;background:#EEF6F0;border-left:3px solid #1B9E4B;">
        <p class="t-small"><strong>Percepción neta promotora:</strong> 12 de 14 comentarios apoyan la iniciativa y <strong>ninguna crítica ataca a FEMSA como propietario</strong>. La narrativa de «trabajar en conjunto» la refuerzan los aliados ambientales y la propia FEMSA en respuesta («Una muestra clara del impacto que logramos cuando trabajamos en conjunto» —@femsa_oficial). El único frente a gestionar es la <strong>continuidad</strong>: sostener la labor social evita el reproche de oportunismo.</p>
      </div>
      <p class="t-micro" style="margin-top:12px;color:var(--n-400);">Muestra cualitativa y direccional (no estadística): 16 comentarios exportados de 2 publicaciones de la Megalimpieza; se excluyen la respuesta de la propia FEMSA y un duplicado de exportación → 14 comentarios de audiencia.</p>
    </div>
    {FOOT}
  </div>
</section>'''

s,e=sec_slice("05.1 FEMSA · el propietario"); html=html[:e]+"\n"+new52+html[e:]

open(f"{SC}/Rayados_Social_Listening_v6.html","w",encoding="utf-8").write(html)
print("sections:", html.count("<section"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', html))
print("div bal:", html.count("<div")==html.count("</div>"), "| sec bal:", html.count("<section")==html.count("</section>"))
