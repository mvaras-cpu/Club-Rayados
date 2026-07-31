# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v8.html",encoding="utf-8").read()
def repl(a,b,n=1):
    global html; assert a in html,"NO: "+a[:80]; html=html.replace(a,b,n)

# ============ 1) Capítulo 06: Estrategia -> Estrategia de monitoreo ============
repl('06 · Estrategia','06 · Estrategia de monitoreo',5)   # divider eyebrow + 6.1/6.2 eyebrow y footer
repl('>Estrategia</h4>','>Estrategia de monitoreo</h4>')                       # índice
repl('data-label="06 Estrategia — Divider"','data-label="06 Estrategia de monitoreo — Divider"')
repl('<p class="ch-title">Estrategia.</p>','<p class="ch-title">Estrategia de monitoreo.</p>')

# ============ 2) Slide 4.1: quitar menciones a metodología ============
repl('Sentimiento · conversación de terceros · clasificación por léxico explícito','Sentimiento · conversación de terceros')
repl('Base: menciones de terceros · el export no trae campo de sentimiento','Base: menciones de terceros')
# borrar el <p> de nota metodológica completo
i=html.index('Clasificación por léxico explícito sobre la base completa.')
ps=html.rfind('<p',0,i); pe=html.index('</p>',i)+4
# quitar también el salto/espacios previos
pre=html.rfind('\n',0,ps)
html=html[:pre]+html[pe:]

# ============ 3) Pendiente Casa Mundialista: relabel 4.2 y 4.3 ============
# 4.2 (tablas own + earned): "Casa Mundialista" -> "Mundial · estadio sede"
repl('<td class="strong" style="font-size:17px;">Casa Mundialista</td>','<td class="strong" style="font-size:17px;">Mundial · estadio sede</td>',2)
# 4.3 fila de marca: "Estadio como marca / sede" -> "Estadio como marca"
repl('>Estadio como marca / sede</td>','>Estadio como marca</td>')

# ============ 4) Pendiente own·marca (versión completa) en 4.3 ============
# header de la tabla: aclarar alcance
repl('<th>Sub-tema de marca (terceros)</th>','<th>Sub-tema de marca · resonancia en terceros</th>')
# nota "qué empuja el own" antes del callout de crítica
own_note='''<div style="margin-top:16px;padding:14px 24px;background:#EEF6F0;border-left:3px solid #1B9E4B;">
        <p class="t-small"><strong>Qué empuja el own en esta dimensión:</strong> el club es el motor de la marca positiva —RSE (Megalimpieza), 81 aniversario, patrocinios (BBVA, WOBI, VivaAerobus) y mística—. <strong>~31&nbsp;% de lo que publica el club es institucional</strong>, casi a la par de lo futbolístico; la tabla de arriba muestra cómo esa marca <strong>resuena y se critica en terceros</strong>.</p>
      </div>
      '''
anchor='<div style="margin-top:18px;padding:16px 24px;background:#FBEEEC;'
assert anchor in html
html=html.replace(anchor, own_note+anchor,1)

open(f"{SC}/Rayados_Social_Listening_v9.html","w",encoding="utf-8").write(html)
print("Estrategia de monitoreo:", html.count("Estrategia de monitoreo"), "| Estrategia sola restante:", len(re.findall(r'Estrategia(?! de monitoreo)',html)))
print("léxico explícito restante:", html.count("léxico explícito"), "| campo de sentimiento:", html.count("campo de sentimiento"))
print("Casa Mundialista restante:", html.count("Casa Mundialista"))
print("Mundial · estadio sede:", html.count("Mundial · estadio sede"))
print("div bal:", html.count("<div")==html.count("</div>"),"| sec bal:", html.count("<section")==html.count("</section>"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', html))
