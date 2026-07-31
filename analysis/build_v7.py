# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v6.html",encoding="utf-8").read()
def repl(a,b,n=1):
    global html; assert a in html,"NO: "+a[:80]; html=html.replace(a,b,n)

# 1) Slide 3.3 · K -> M en los dos valores >= 1 M
repl('<td class="num tabular">5 406 K</td>','<td class="num tabular">5,4 M</td>')
repl('<td class="num tabular">1 953 K</td>','<td class="num tabular">1,9 M</td>')

# 2) Eliminar nota al pie del ranking de jugadores (4.2)
repl('<p class="t-micro" style="margin-top:12px;color:var(--n-400);">Jugadores actuales de Rayados. Excluye al DT (Almeyda, arriba) y los nombres de mercado/rumores (Erik Lira, Quiñones). Andrada destaca por su sanción en España más que por su juego.</p>','')

# 3) Eliminar nota al pie de percepción FEMSA (5.2)
repl('<p class="t-micro" style="margin-top:12px;color:var(--n-400);">Muestra cualitativa y direccional (no estadística): 16 comentarios exportados de 2 publicaciones de la Megalimpieza; se excluyen la respuesta de la propia FEMSA y un duplicado de exportación → 14 comentarios de audiencia.</p>','')

# 4) RSE (5.4) · recortar la nota al pie tras "UNICEF)"
before=html
html=re.sub(r', excluyendo el hashtag general #EnLaVidaYEnLaCancha.*?amplificar la labor social\.', '.', html, count=1, flags=re.S)
assert html!=before, "NO: recorte RSE no aplicado"

# 5) RSE (5.4) · Infancia: "+" -> volumen real (UNICEF = 28 menciones)
repl('font-size:34px;color:var(--ink);">+</div>','font-size:34px;color:var(--ink);">28</div>')

# 6) "Recomendaciones" -> "Estrategia" (capítulo 06, todas las apariciones)
html=html.replace('Recomendaciones','Estrategia')

open(f"{SC}/Rayados_Social_Listening_v7.html","w",encoding="utf-8").write(html)
print("Recomendaciones restante:", html.count("Recomendaciones"), "| Estrategia:", html.count("Estrategia"))
print("5 406 K:", html.count("5 406 K"), "| 1 953 K:", html.count("1 953 K"), "| 5,4 M:", html.count("5,4 M"), "| 1,9 M:", html.count("1,9 M"))
print("infancia + :", '">+</div>' in html, "| 28 card:", 'font-size:34px;color:var(--ink);">28</div>' in html)
print("hashtag rest:", html.count("#EnLaVidaYEnLaCancha"), "| ~450 rest:", html.count("~450"))
print("footnotes removed:", html.count("Jugadores actuales de Rayados"), html.count("Muestra cualitativa"))
print("sections:", html.count("<section"), "| div bal:", html.count("<div")==html.count("</div>"),"| sec bal:", html.count("<section")==html.count("</section>"))
print("crumbs:", re.findall(r'<span>([0-9]+\.[0-9]+)</span>', html))
# show RSE footnote result
i=html.find("Medido por programas concretos"); print("RSE footnote:", html[i:i+120])
