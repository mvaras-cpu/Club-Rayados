# Reporte de Social Listening · Rayados de Monterrey (Q2–Q3 2026)

Deck ejecutivo HTML (1920×1080, design system Artool) sobre la conversación digital del **Club de Fútbol Monterrey (Rayados)** entre el **28 de abril y el 28 de julio de 2026**.

Archivo principal: **`Rayados_Social_Listening_Q2-Q3_2026.html`** (autocontenido; se abre en cualquier navegador y se puede exportar a PDF/PPTX).

## Base de datos

- **166 467 registros** (menciones y posts), una sola tabla.
- Columnas: `published`, `content`, `source_type`, `extra_author_attributes.name`, `engagement`, `Visualizaciones TikTok`.
- Fuente vigente: `09541295-Descarga_Rayados_mejorada1.xlsx` (base "mejorada": mismos 166 467 registros que la original, con los nombres de autor calificados por plataforma, p. ej. `Rayados (Instagram)`).
- Todos los cálculos numéricos se hacen sobre la **base completa** (sin muestreo ni estimaciones).

## Estructura (9 capítulos + índice)

01 Resumen ejecutivo · 02 Volumen y dinámica temporal · 03 Plataformas y distribución · 04 Autores y tipologías · 05 Narrativas y sentimiento · 06 Hitos del período · **07 Own & Earned Media** · **08 Rayados como institución** · 09 Recomendaciones.

## Own media · listado oficial (8 cuentas)

Para todo análisis de cuentas propias / own media se usa este listado (nombre exacto en la base):

- `Club de Futbol Monterrey Rayados (Linkedin)`
- `Rayados (Facebook)`
- `Rayados (Instagram)`
- `Rayados (TikTok)`
- `Rayados (X)`
- `rayados_fb (Instagram)`
- `Tienda Rayados (Instagram)`
- `wearerayados (instagram)`

Todo lo demás es **earned media** (terceros).

## Metodología de las métricas

- **Plataformas:** derivadas de `source_type`; engagement = suma real de la columna `engagement`.
- **Tipologías (4.3):** own = listado de 8 cuentas; el resto se clasifica por patrones de nombre de autor + tipo de fuente. Suma de engagement por categoría sobre la base completa.
- **Sentimiento (5.1):** clasificación editorial de terceros heredada del pipeline original (excluye cuentas propias). No hay campo de sentimiento en el export, por lo que se conserva sin recomputar.
- **Narrativas (7.3) y temas corporativos (cap. 08):** etiquetado por palabras clave sobre el texto de la base completa; los temas no son mutuamente excluyentes.

## Cifras clave (base completa · listado de 8 cuentas)

| Métrica | Valor |
|---|---|
| Menciones totales | 166 467 |
| Interacciones totales | 20 632 584 (20,6 M) |
| Autores únicos | 49 495 |
| Own media | 1 720 menciones (1,0 %) · 9,5 M eng (46,0 %) · 8 cuentas |
| Earned media | 164 747 menciones (99,0 %) · 11,1 M eng (54,0 %) · 49 487 autores |
| Top-30 autores | 65,4 % del engagement |
| Cuenta #1 | Rayados en Instagram · 5,4 M (26,2 %) |
| Tres handles oficiales (IG + FB + wearerayados) | 38,6 % del engagement |
| Own media por plataforma | Instagram 707 posts / 6,38 M · Facebook 513 / 1,95 M · X 440 / 413 K · TikTok 43 / 741 K · LinkedIn 17 / 3 K |
| FEMSA | 842 menciones |
| Dennis te Kloese | 1 360 menciones · peak en mayo |
| Responsabilidad social | 2 354 menciones |

## Changelog

**Iteración 3 (re-anclaje de hitos + narrativas por fuente):**
- Re-anclada la narrativa de peaks/hitos con las fechas reales de la base: **28 abr** salida de Canales · **7 may** llegada de te Kloese · **21 may** anuncio de Almeyda como DT · **8 jul** fichaje de Rossi · **18–19 jul** Cuypers/Orbelín · **26 jul** debut en el Apertura. Corregidas las slides 2.2, 2.3, el divider del capítulo 02 y el capítulo 6 (6.1, 6.4). El anuncio de Almeyda estaba mal fechado (figuraba el 8 jul; fue el 21 may).
- Slide 6.2: curva re-graficada con los 92 valores diarios reales; las anotaciones caen sobre los peaks verdaderos.
- 4.1: los tres handles pasan a ser los de mayor engagement (Rayados en Instagram + Facebook + TikTok = **39,3 %**).
- Añadidas dos slides al capítulo 07: **7.4 Narrativas · cuentas oficiales** (qué publica el club y qué le rinde) y **7.5 Narrativas · terceros** (qué amplifican y qué resuena), con análisis de tracción (engagement por pieza).

**Iteración 2 (base mejorada + listado oficial de 8 cuentas):**
- Own media redefinido al listado de 8 cuentas; recalculados 7.1 (volumen), 7.2 (ahora "own media por plataforma"), 4.1 (concentración), 4.2 (top autores, con `Rayados` desglosado por plataforma), 4.3 (tipologías) y 4.4 (hallazgos).
- 4.1: se especifican las redes de los tres handles oficiales.
- Eliminadas las slides 7.3 (top autores own+earned, redundante con 4.2) y 7.4 (sentimiento own vs earned, inconsistente con 5.1); la narrativa pasó a ser 7.3.
- 8.3: se quitó la mención a "Fundación Rayados".

**Iteración 1:** capítulos 07 (Own & Earned) y 08 (Institucional) nuevos; índice; numeración consecutiva; eliminación de medianas; "pico"→"peak"; recálculo de tipologías y top autores.

## Reproducibilidad

`analysis/` contiene los scripts de transformación (`build_step*.py`, `build_final.py`, `build_v3.py`) y los agregados calculados (`analisisA.json`, `analisisB.json`, `tipologias.json`, `newbase.json`, `tip_new.json`). El archivo de datos crudo (Excel) no se versiona.
