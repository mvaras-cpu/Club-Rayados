# -*- coding: utf-8 -*-
import re
SC="/tmp/claude-0/-home-user-Club-Rayados/462fa5cd-426a-5bf5-985a-b5a484bcce36/scratchpad"
html=open(f"{SC}/step1.html",encoding="utf-8").read()

# Mapa de capítulos: 02..07 bajan 1; 09 se mantiene
def shift(n):  # n es int 2..7
    return f"0{n-1}"

# --- Verificación: mostrar todos los prefijos "0N · " ---
print("=== prefijos '0N · ' encontrados ===")
for m in sorted(set(re.findall(r'0[2-9] · [^<\n]{0,40}', html))):
    print("  ", repr(m[:45]))

# (1) Prefijos de capítulo "0N · Titulo" (eyebrow, ch-eyebrow, footer) -> baja 1 (solo 2..7)
html=re.sub(r'0([2-7]) · ', lambda m: shift(int(m.group(1)))+" · ", html)

# (2) Crumb sub-numeros <span>N.M</span> con N en 2..7 -> N-1
def crumb(m):
    n=int(m.group(1)); return f"<span>{n-1}.{m.group(2)}</span>"
html=re.sub(r'<span>([2-7])\.(\d+)</span>', crumb, html)

# (3) ch-num grande dentro del divider (0N) -> baja 1 (solo 2..7)
def chnum(m):
    return m.group(1)+shift(int(m.group(2)[1]))+m.group(3)
html=re.sub(r'(<div class="ch-num"[^>]*>)(0[2-7])(</div>)', chnum, html)

# (4) data-labels: data-label="0N..." -> baja 1 (solo 2..7); 09 se mantiene
def dlabel(m):
    return 'data-label="'+shift(int(m.group(1)))
html=re.sub(r'data-label="0([2-7])', dlabel, html)
# portada y cierre: quitar numero
html=html.replace('data-label="01 Portada"','data-label="Portada"')
html=html.replace('data-label="10 Cierre"','data-label="Cierre"')

open(f"{SC}/step2.html","w",encoding="utf-8").write(html)

# --- Verificaciones post ---
print("\n=== labels de capitulo tras renumerar ===")
for m in sorted(set(re.findall(r'class="ch-eyebrow">[^<]+', html))):
    print("  ", m.replace('class="ch-eyebrow">',''))
print("\n=== ch-num dividers ===", re.findall(r'class="ch-num"[^>]*>(\d\d)</div>', html))
print("=== crumbs ===", re.findall(r'<div class="crumb"><span>([0-9]\.[0-9])', html) or re.findall(r'<span>([0-9]\.[0-9])</span>', html))
print("=== '2026' intacto? ocurrencias:", html.count("2026"))
print("=== '1080px' intacto? ", html.count("1080px"))
