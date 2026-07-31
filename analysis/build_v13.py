# -*- coding: utf-8 -*-
# Iteración 13: reconcilia las cifras del resumen ejecutivo (1.1) con los capítulos de detalle.
# Misma estructura, mismos titulares, mismo sentiment y narrativas — solo se corrigen números.
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
h=open(f"{SC}/Rayados_Social_Listening_v12.html",encoding="utf-8").read()
def repl(a,b):
    global h; assert a in h,"NO: "+a[:70]; h=h.replace(a,b,1)

# A · quitar los ~ (cifras ya correctas: 11% vol / 24% inter., consistentes con 4.2-4.3)
repl('es ~11&nbsp;% del volumen, pero moviliza <strong>~1 de cada 4 interacciones (~24&nbsp;%)</strong>',
     'es 11&nbsp;% del volumen, pero moviliza <strong>1 de cada 4 interacciones (24&nbsp;%)</strong>')

# C · 18% -> 13% (unión real de los 4 jugadores de la slide 4.4)
repl('Almeyda, Rossi, Orbelín y Cuypers suman el 18&nbsp;% del corpus',
     'Almeyda, Rossi, Orbelín y Cuypers suman el 13&nbsp;% del corpus')

# D · mantiene el 14% pero reencuadrado a "la rivalidad completa" (evita el "parte > todo" vs 4.2)
repl('La historia de Japón abandonando el Volcán para entrenar en el Barrial de Rayados (14&nbsp;% del corpus) circuló viralmente entre audiencias no-aficionadas.',
     'La rivalidad con Tigres —con la historia de Japón entrenando en el Barrial de Rayados como chispa viral— movió cerca del 14&nbsp;% de la conversación y circuló entre audiencias no-aficionadas.')

# E · 15%+7%=22% -> 7% (tope del tono negativo, consistente con 4.1); conserva las 2 narrativas y el sentimiento
repl('Las narrativas "Mercenarios / directiva mediocre" (15&nbsp;%) y "Sequía de títulos" (7&nbsp;%) muestran que la desconfianza es recurrente e independiente del momentum positivo. Juntas representan el 22&nbsp;% del corpus.',
     'Las narrativas "Mercenarios / directiva mediocre" y "Sequía de títulos" concentran el grueso del 7&nbsp;% de tono negativo del período: minoritarias pero recurrentes y de baja tracción, e independientes del momentum positivo.')

open(f"{SC}/Rayados_Social_Listening_v13.html","w",encoding="utf-8").write(h)
import re
print("chequeos:")
print("  '18% del corpus':", h.count("suman el 18&nbsp;%"), "-> '13%':", h.count("suman el 13&nbsp;%"))
print("  '22% del corpus':", h.count("22&nbsp;% del corpus"), "| '15&nbsp;%' resto:", h.count("(15&nbsp;%)"))
print("  '~11'/'~24' resto:", h.count("~11")+h.count("~24")+h.count("~1 de cada"))
print("  '14&nbsp;% de la conversación':", h.count("14&nbsp;% de la conversación"))
print("  div bal:", h.count("<div")==h.count("</div>"), "| sec bal:", h.count("<section")==h.count("</section>"))
