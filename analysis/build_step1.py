# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/rayados_report.html",encoding="utf-8").read()
orig_sections = html.count("<section")
print("secciones originales:", orig_sections)

# ============================================================
# (A) CORRECCIONES DE CONTENIDO (valores con base total)
# ============================================================

# A1 — Eliminar MEDIANA en 3.1 y recalcular top-3 días (10,1% -> 10,4%)
old = ('<p class="t-small" style="color:var(--n-500);">Promedio diario: <strong style="color:var(--ink);">1 810 publicaciones</strong> &nbsp;·&nbsp; Mediana diaria: <strong style="color:var(--ink);">1 437 publicaciones</strong> &nbsp;·&nbsp; El top-3 de días concentra el <strong style="color:var(--ink);">10,1%</strong> del volumen total.</p>')
new = ('<p class="t-small" style="color:var(--n-500);">Promedio diario: <strong style="color:var(--ink);">1 809 publicaciones</strong> &nbsp;·&nbsp; El top-3 de días concentra el <strong style="color:var(--ink);">10,4%</strong> del volumen total &nbsp;·&nbsp; base: 166 467 registros del período.</p>')
assert old in html, "A1 no encontrado"
html=html.replace(old,new)

# A2 — Eliminar MEDIANA del corpus en 4.2
old=('<p class="t-small">Engagement promedio por publicación en X: <strong style="color:var(--ink);">moderado</strong> · Mediana del corpus completo = 0 interacciones (la mayoría son menciones sin traction).</p>')
new=('<p class="t-small">Engagement promedio por publicación en X: <strong style="color:var(--ink);">≈ 33 interacciones</strong> por pieza sobre la base completa (3,78 M de interacciones en 115 072 tweets).</p>')
assert old in html, "A2 no encontrado"
html=html.replace(old,new)

# A3 — Multiplicador del peak 4,2x -> 3,8x (2 ocurrencias)
old='6 939 menciones — 4,2× el promedio diario del trimestre. Peak asociado al anuncio mundialista.'
new='6 939 menciones — 3,8× el promedio diario del trimestre. Peak asociado al anuncio mundialista.'
assert old in html; html=html.replace(old,new)
old='Publicaciones el <strong>28 de abril</strong> — 4,2× el promedio diario del período.'
new='Publicaciones el <strong>28 de abril</strong> — 3,8× el promedio diario del período.'
assert old in html; html=html.replace(old,new)

# A4 — 4.1 nota al pie (engagement SÍ disponible; referencia cap. 07)
old='Podcast, Bluesky, LinkedIn, Newsletters y otros suman el 1,8% restante · Engagement no disponible desagregado por plataforma en el export.'
new='Podcast, Bluesky, LinkedIn, Newsletters y otros suman el 1,3% restante · El detalle de engagement por plataforma se analiza sobre la base completa en el capítulo 07 (Own &amp; Earned Media).'
assert old in html; html=html.replace(old,new)
# 4.1 ajustar Noticias online y Resto para consistencia con la base total
html=html.replace('<td class="num tabular">25 571</td>','<td class="num tabular">26 337</td>')
html=html.replace('<td class="num tabular">15,4%</td>','<td class="num tabular">15,8%</td>')
html=html.replace('<td class="num tabular" style="color:var(--n-400);">2 934</td>','<td class="num tabular" style="color:var(--n-400);">2 168</td>')
html=html.replace('<td class="num tabular" style="color:var(--n-400);">1,8%</td>','<td class="num tabular" style="color:var(--n-400);">1,3%</td>')

# ============================================================
# (B) RECALCULAR 5.1 CONCENTRACIÓN (base total)
# ============================================================
# donut arc 75% -> 66,2%  (0.662*879.6 = 582.3)
html=html.replace('stroke-dasharray="659.7 879.6"','stroke-dasharray="582.3 879.6"')
html=html.replace('font-size="80" fill="#0A0A0A" letter-spacing="-2">75%</text>','font-size="80" fill="#0A0A0A" letter-spacing="-2">66%</text>')
html=html.replace('<!-- 30 autores / 166 467 menciones. Top 30 generan ~75% del engagement total -->',
                  '<!-- 30 autores / 166 467 menciones. Top 30 generan 66,2% del engagement total (base completa) -->')
# stat "≈ 52 K" -> 49 493 ; "75%" (top30) -> 66%
html=html.replace('<span class="value tabular" style="font-size:56px;">≈ 52 K</span>','<span class="value tabular" style="font-size:56px;">49 493</span>')
html=html.replace('<span class="value tabular" style="font-size:56px;">75%</span>','<span class="value tabular" style="font-size:56px;">66%</span>')
# nota de pie 5.1: mantener 44% (top-3 oficiales) — correcto; ajustar texto "≈ 52 K" no aplica
html=html.replace('emisores distintos en el período','autores únicos en el período (base completa)')

# ============================================================
# (C) RECALCULAR 5.3 TIPOLOGÍAS (base total, sin estimación)
# ============================================================
tip_old_start = html.index('<table class="tbl" style="font-size:21px;">')
tip_old_end = html.index('</table>', tip_old_start)+len('</table>')
tip_block = '''<table class="tbl" style="font-size:21px;">
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
            <td class="num tabular">10,1 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:100%;background:var(--accent);"></i></div></td>
            <td class="num tabular"><strong>48,9%</strong></td>
            <td class="num tabular">1,4%</td>
            <td style="color:var(--n-600);font-size:18px;">Concentran el engagement con volumen mínimo: fichajes, Mundial, Almeyda, RSE</td>
          </tr>
          <tr>
            <td class="strong">Ciudadanía / individuales</td>
            <td class="num tabular">5,8 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:57%;"></i></div></td>
            <td class="num tabular">28,1%</td>
            <td class="num tabular">66,5%</td>
            <td style="color:var(--n-600);font-size:18px;">Principal voz de crítica, rivalidad y celebración espontánea</td>
          </tr>
          <tr>
            <td class="strong">Medios y prensa deportiva</td>
            <td class="num tabular">2,9 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:29%;"></i></div></td>
            <td class="num tabular">14,3%</td>
            <td class="num tabular">27,0%</td>
            <td style="color:var(--n-600);font-size:18px;">Amplifican hitos y fichajes (Fox, Récord, Multimedios, ESPN…)</td>
          </tr>
          <tr>
            <td class="strong">Fan accounts / comunidad rayada</td>
            <td class="num tabular">1,5 M</td>
            <td><div class="barbar" style="height:16px;"><i style="width:15%;"></i></div></td>
            <td class="num tabular">7,3%</td>
            <td class="num tabular">4,7%</td>
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
              Cálculo sobre la base completa (166 467 registros): suma de engagement por categoría. Tipologías derivadas del nombre de autor y el tipo de fuente; las cuentas propias corresponden al listado oficial del club.
            </td>
          </tr>
        </tbody>
      </table>'''
html = html[:tip_old_start]+tip_block+html[tip_old_end:]
# título 5.3 ajuste
html=html.replace('Cinco tipos de actor concentran el debate. Las cuentas propias y los medios dominan el engagement; la afición produce el volumen.',
                  'Cinco tipos de actor concentran el debate. Las cuentas propias dominan el engagement; la ciudadanía y los medios producen el volumen.')

# ============================================================
# (D) pico/picos -> peak/peaks (respetando mayúsculas, palabra completa)
# ============================================================
html=re.sub(r'\bpicos\b','peaks',html)
html=re.sub(r'\bPicos\b','Peaks',html)
html=re.sub(r'\bpico\b','peak',html)
html=re.sub(r'\bPico\b','Peak',html)
html=re.sub(r'\bPICO\b','PEAK',html)
html=re.sub(r'\bPICOS\b','PEAKS',html)

open(f"{SC}/step1.html","w",encoding="utf-8").write(html)
print("Paso 1 OK. pico/picos restantes:", len(re.findall(r'\bpicos?\b',html,re.I)))
print("mediana restantes:", len(re.findall(r'mediana',html,re.I)))
print("estimac restantes:", len(re.findall(r'estimac',html,re.I)))
