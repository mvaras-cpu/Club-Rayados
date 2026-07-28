# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/step3a.html",encoding="utf-8").read()
chap07=open(f"{SC}/chap07.html",encoding="utf-8").read()
chap08=open(f"{SC}/chap08.html",encoding="utf-8").read()

# insertar capítulos 07 y 08 antes del divider de Recomendaciones (09)
marker='<section data-label="09 Recomendaciones — Divider">'
assert marker in html
html=html.replace(marker, chap07+chap08+marker, 1)

# actualizar subtítulo de portada para reflejar los nuevos capítulos
old='Análisis de conversación digital de 92 días: del anuncio mundialista hasta el debut de la era Almeyda. Volumen, narrativas, autores y recomendaciones estratégicas para el equipo directivo.'
new='Análisis de conversación digital de 92 días: del anuncio mundialista al debut de la era Almeyda. Volumen, plataformas, autores, narrativas y sentimiento — con capítulos dedicados a own &amp; earned media y a la dimensión institucional del club (FEMSA, te Kloese, responsabilidad social).'
assert old in html
html=html.replace(old,new)

open(f"{SC}/Rayados_Social_Listening_v2.html","w",encoding="utf-8").write(html)

# ================= VALIDACIONES =================
print("Total <section>:", html.count("<section"))
print("pico/picos:", len(re.findall(r'\bpicos?\b',html,re.I)))
print("mediana   :", len(re.findall(r'mediana',html,re.I)))
print("estimac   :", len(re.findall(r'estimac',html,re.I)))
print("¿índice?  :", 'data-label="Índice"' in html)

print("\n--- Secuencia de capítulos (ch-eyebrow) ---")
for m in re.findall(r'class="ch-eyebrow">([^<]+)', html):
    print("  ", m)
print("\n--- ch-num dividers en orden ---", re.findall(r'class="ch-num"[^>]*>(\d\d)</div>', html))
print("\n--- crumbs en orden ---")
print("  ", re.findall(r'<span>([0-9]\.[0-9])</span>', html))
print("\n--- data-labels (nav) ---")
for m in re.findall(r'data-label="([^"]+)"', html):
    print("  ", m)
