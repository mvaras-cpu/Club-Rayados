# -*- coding: utf-8 -*-
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v10.html",encoding="utf-8").read()

rows=[
 ("Patrocinio / comercial","5 585","3,4%","Neutro","var(--n-500)","BBVA, tienda, jerseys, abonos"),
 ("Dirigencia / gestión","3 554","2,2%","⚠️ Negativo","#B5251D","«plantel caro que no gana», directiva"),
 ("Estadio como sede / marca","1 940","1,2%","✅ Positivo","#0F6B33","Casa Mundialista, Gigante de Acero"),
 ("Aniversario / efeméride","398","0,2%","✅ Positivo","#0F6B33","81 años, efemérides"),
 ("RSE / comunidad","393","0,2%","⚪ Invisible","var(--n-400)","Megalimpieza, Escuelas, UNICEF"),
]
trows=""
for t,v,p,tag,col,desc in rows:
    trows+=f'''<tr>
            <td class="strong" style="font-size:18px;">{t}</td>
            <td class="num tabular" style="font-size:18px;">{v}</td>
            <td class="num tabular" style="font-size:15px;color:var(--n-500);">{p}</td>
            <td style="font-size:15px;font-weight:700;color:{col};">{tag}</td>
            <td style="font-size:15px;color:var(--n-600);">{desc}</td>
          </tr>'''

new43=f'''<section data-label="04.3 Estructura de la conversación">
  <div class="slide">
    <style>.tbrand td,.tbrand th{{padding:9px 14px;}}</style>
    <header class="slide-header"><div class="eyebrow">04 · Narrativas y sentimiento</div><div class="crumb"><span>4.3</span><span class="dot">·</span><b>Estructura de la conversación</b></div></header>
    <div class="frame" style="padding-bottom:120px;">
      <p class="t-eyebrow" style="margin-bottom:8px;">Sobre qué se habla · futbolística vs no-futbolística · own y terceros</p>
      <p class="t-h3" style="margin-bottom:20px;max-width:1350px;">La conversación es casi toda futbolística; lo institucional y de marca es una minoría —y ahí se concentra lo negativo.</p>
      <div class="row" style="gap:40px;align-items:stretch;">
        <div style="flex:0 0 360px;border-top:4px solid var(--ink);padding-top:20px;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--n-500);">Futbolística</p>
          <div class="bignum small" style="font-size:72px;margin:6px 0;">~93%</div>
          <p class="t-small" style="color:var(--n-600);">Resultados y partidos, fichajes, DT y jugadores —e incluye la <strong>identidad y las porras</strong> de la afición (mística «La Pandilla», orgullo, leyendas): cultura de equipo, no gestión. El <strong>own</strong> la genera; los <strong>terceros</strong> la amplifican.</p>
        </div>
        <div class="fill" style="border-top:4px solid var(--accent);padding-top:20px;min-width:0;">
          <p style="font-weight:700;font-size:15px;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);">No futbolística · marca e institución &nbsp;·&nbsp; ~7%</p>
          <table class="tbl tbrand" style="font-size:18px;margin-top:8px;">
            <colgroup><col style="width:280px;"><col style="width:100px;"><col style="width:90px;"><col style="width:130px;"><col style="width:360px;"></colgroup>
            <thead><tr><th>Sub-tema institucional · resonancia en terceros</th><th class="num">Menc.</th><th class="num">% earn</th><th>Tono</th><th>Qué contiene</th></tr></thead>
            <tbody>{trows}</tbody>
          </table>
          <p class="t-micro" style="margin-top:8px;color:var(--n-400);">Solo lo corporativo/off-pitch. La mística, las porras y las leyendas se cuentan como futbolística (identidad de equipo).</p>
        </div>
      </div>
      <div style="margin-top:14px;padding:14px 24px;background:#EEF6F0;border-left:3px solid #1B9E4B;">
        <p class="t-small"><strong>Qué empuja el own en esta dimensión:</strong> el grueso de lo que publica el club también es sobre el equipo (~82&nbsp;%). Pero en lo institucional el <strong>own pesa ~3× los terceros (~18&nbsp;% de sus posts vs ~6,5&nbsp;%)</strong>: es la principal fuente de la marca positiva —patrocinios, estadio y aniversario, RSE—. La tabla de arriba muestra cómo esa marca <strong>resuena y se critica en terceros</strong>.</p>
      </div>
      <div style="margin-top:14px;padding:14px 24px;background:#FBEEEC;border-left:3px solid #B5251D;">
        <p class="t-small">Dentro de lo institucional, lo negativo se concentra en la <strong>dirigencia y gestión</strong> («plantel caro que no gana»), pero es una <strong>crítica minoritaria (~2,2&nbsp;% de terceros) y de baja tracción</strong>. El resto de la dimensión es neutral o positivo (patrocinios, estadio mundialista, aniversario) y la <strong>RSE casi invisible</strong> para terceros (oportunidad de amplificación).</p>
      </div>
    </div>
    <footer class="slide-footer"><span>04 · Narrativas y sentimiento</span><span class="right"><span style="font-size:20px;font-weight:900;font-family:var(--font-display);letter-spacing:-0.02em;">artool.</span></span></footer>
  </div>
</section>'''

s=html.index('<section data-label="04.3 Estructura de la conversación">'); e=html.index('</section>',s)+10
html=html[:s]+new43+html[e:]
open(f"{SC}/Rayados_Social_Listening_v11.html","w",encoding="utf-8").write(html)
print("31% restante:", html.count("31&nbsp;% de lo que publica"), "| ~93% presente:", ">~93%<" in html)
print("Mística en tabla:", html.count("Mística / identidad"), "| filas nuevas ok:", html.count("Estadio como sede / marca"))
print("div bal:", html.count("<div")==html.count("</div>"),"| sec bal:", html.count("<section")==html.count("</section>"))
