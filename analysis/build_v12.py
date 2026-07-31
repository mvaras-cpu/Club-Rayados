# -*- coding: utf-8 -*-
# Iteración 12: corrige el «20% del volumen» de «Era Almeyda» en la slide 1.1.
# Era una cifra legacy inflada; el conteo real de la narrativa es ~8-10% del volumen.
# Se usa 8,3% para dejarla consistente con las slides 4.2 (earned 13 738) y 4.4 (Almeyda 13 765 = 8,3%).
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
h=open(f"{SC}/Rayados_Social_Listening_v11.html",encoding="utf-8").read()
a='Con el 20&nbsp;% del volumen, la narrativa "Era Almeyda"'
b='Con el 8,3&nbsp;% del volumen, la narrativa "Era Almeyda"'
assert a in h,"NO encontrado"
h=h.replace(a,b,1)
open(f"{SC}/Rayados_Social_Listening_v12.html","w",encoding="utf-8").write(h)
print("ok · 20% restante:", h.count("Con el 20&nbsp;%"), "| 8,3% nuevo:", h.count("Con el 8,3&nbsp;%"))
