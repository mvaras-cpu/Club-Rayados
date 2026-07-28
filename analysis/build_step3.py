# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/step2.html",encoding="utf-8").read()

FOOT_ART='<span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span>'

# =====================================================================
#  ÍNDICE
# =====================================================================
def idx_item(num, title, desc, accent=False):
    col = "var(--accent)" if accent else "var(--ink)"
    bt  = "var(--accent)" if accent else "var(--n-200)"
    return f'''        <div style="display:grid;grid-template-columns:74px 1fr;gap:24px;align-items:baseline;border-top:2px solid {bt};padding-top:14px;">
          <span style="font-family:var(--font-display);font-weight:900;font-size:44px;letter-spacing:-0.02em;color:{col};">{num}</span>
          <div>
            <h4 style="font-family:var(--font-display);font-weight:900;font-size:27px;line-height:1.05;margin:0 0 3px;color:var(--ink);">{title}</h4>
            <p style="font-size:17px;color:var(--n-500);margin:0;line-height:1.3;">{desc}</p>
          </div>
        </div>'''

indice = f'''<section data-label="Índice">
  <div class="slide">
    <header class="slide-header">
      <div class="eyebrow">Rayados · Social Listening Q2–Q3 2026</div>
      <div class="crumb"><b>Índice</b></div>
    </header>
    <div class="frame" style="padding-top:44px;padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Contenido del reporte</p>
      <h2 class="t-h2" style="font-size:54px;margin-bottom:38px;">Nueve capítulos.</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px 80px;">
{idx_item("01","Resumen ejecutivo","Cinco lecturas y la magnitud del trimestre")}
{idx_item("02","Volumen y dinámica temporal","166 467 menciones en 92 días y sus peaks")}
{idx_item("03","Plataformas y distribución","Dónde se habla y dónde impacta la conversación")}
{idx_item("04","Autores y tipologías","Concentración del engagement y voceros clave")}
{idx_item("05","Narrativas y sentimiento","Marcos de conversación y tono de terceros")}
{idx_item("06","Hitos del período","Cinco momentos que estructuraron la agenda")}
{idx_item("07","Own &amp; Earned Media","Contenido propio del club vs menciones de terceros", accent=True)}
{idx_item("08","Rayados como institución","FEMSA, Dennis te Kloese y responsabilidad social", accent=True)}
{idx_item("09","Recomendaciones","Vigilancia, monitoreo y lineamientos estratégicos")}
      </div>
    </div>
    <footer class="slide-footer">
      <span>Índice</span>
      <span class="right">{FOOT_ART}</span>
    </footer>
  </div>
</section>
'''

# insertar índice antes del divider del capítulo 01
marker='<section data-label="01 Resumen ejecutivo — divider">'
assert marker in html, "marker indice no encontrado"
html=html.replace(marker, indice+marker, 1)

open(f"{SC}/step3a.html","w",encoding="utf-8").write(html)
print("Índice insertado. secciones:", html.count("<section"))
