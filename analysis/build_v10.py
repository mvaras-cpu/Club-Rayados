# -*- coding: utf-8 -*-
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/Rayados_Social_Listening_v9.html",encoding="utf-8").read()
def repl(a,b):
    global html; assert a in html,"NO: "+a[:80]; html=html.replace(a,b,1)

# Pendiente A: slide 1.1 — el 26% era share de interacciones mal rotulado como «del corpus».
# Se corrige el rótulo (volumen vs interacciones) y se alinea el nombre con 4.2.
old='La narrativa "Casa Mundialista" concentra el 26&nbsp;% del corpus y movilizó la mayor proporción de interacciones positivas. El campo desbordó al equipo en relevancia global durante semanas.'
new='La narrativa «Mundial&nbsp;· estadio sede» es ~11&nbsp;% del volumen, pero moviliza <strong>~1 de cada 4 interacciones (~24&nbsp;%)</strong>, en su mayoría positivas: pega muy por encima de su peso. El campo desbordó al equipo en relevancia global durante semanas.'
repl(old,new)

open(f"{SC}/Rayados_Social_Listening_v10.html","w",encoding="utf-8").write(html)
print("26% restante:", html.count("26&nbsp;% del corpus"), "| Casa Mundialista restante:", html.count("Casa Mundialista"))
print("nuevo rótulo presente:", "~1 de cada 4 interacciones" in html)
print("div bal:", html.count("<div")==html.count("</div>"),"| sec bal:", html.count("<section")==html.count("</section>"))
