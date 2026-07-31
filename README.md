# Reporte de Social Listening · Rayados de Monterrey (Q2–Q3 2026)

Deck ejecutivo HTML (1920×1080, design system Artool) sobre la conversación digital del **Club de Fútbol Monterrey (Rayados)** entre el **28 de abril y el 28 de julio de 2026**.

Archivo principal: **`Rayados_Social_Listening_Q2-Q3_2026.html`** (autocontenido; se abre en cualquier navegador y se puede exportar a PDF/PPTX).

## Base de datos

- **166 467 registros** (menciones y posts), una sola tabla.
- Columnas: `published`, `content`, `source_type`, `extra_author_attributes.name`, `engagement`, `Visualizaciones TikTok`.
- Fuente vigente: `09541295-Descarga_Rayados_mejorada1.xlsx` (base "mejorada": mismos 166 467 registros que la original, con los nombres de autor calificados por plataforma, p. ej. `Rayados (Instagram)`).
- Todos los cálculos numéricos se hacen sobre la **base completa** (sin muestreo ni estimaciones).

## Estructura (6 capítulos + índice)

01 Resumen ejecutivo · 02 Volumen, dinámica e hitos · 03 Plataformas y autores (incl. own vs earned) · 04 Narrativas y sentimiento · 05 Rayados como institución · 06 Estrategia de monitoreo.

Archivos:
- `Rayados_Social_Listening_Q2-Q3_2026.html` — **versión concisa** (6 capítulos, 28 slides).
- `Rayados_Social_Listening_Q2-Q3_2026_extendido.html` — versión extendida (9 capítulos, 40 slides) como respaldo; misma información, más granular.

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
- **Tipologías:** own = listado de 8 cuentas; el resto se clasifica por patrones de nombre de autor + tipo de fuente. Suma de engagement por categoría sobre la base completa.
- **Sentimiento (4.1):** el export **no trae campo de sentimiento**, por lo que se clasifica por **léxico explícito** sobre los terceros. Tres categorías: negativo (crítica explícita al club — dirigencia/gestión, sequía, reacción a derrotas — más rivalidad hostil que ataca a Rayados), positivo (orgullo, porras, celebración) y neutro (todo lo que no expresa sentimiento claro, incluida la rivalidad sin carga). Resultado: **Negativo 7 % · Neutro 75 % · Positivo 18 %**.
- **Percepción de FEMSA / te Kloese (5.2, 5.3):** split promotor/neutro/detractor de la conversación earned por léxico; para FEMSA se suma, en lente aparte, el análisis de comentarios en las publicaciones propias.
- **Narrativas y temas corporativos:** etiquetado por palabras clave sobre el texto de la base completa; los temas no son mutuamente excluyentes.

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
| FEMSA | 842 menciones (0,51% del corpus) · 99,5% earned / 0,5% own |
| Dennis te Kloese | 1 360 menciones (0,82%) · 100% earned · peak en mayo |
| Sentimiento (terceros, léxico explícito) | Negativo 7 % (crítica al club 5,5 % + rivalidad hostil 1,4 %) · Neutro 75 % · Positivo 18 % |
| Responsabilidad social | 163 menciones de programas concretos: Medio ambiente 35 (Megalimpieza) · Deporte y niñez 61 (Escuelas Rayados) · Comunidad/legado 39 (The World's Pitch) · Infancia 28 (UNICEF) |
| Almeyda (DT) | 13 765 menciones (8,3% del corpus) |

## Changelog

**Iteración 12 (corrige el «20 %» de «Era Almeyda» en el resumen ejecutivo):**
- **Slide 1.1 (tarjeta B):** el «20 % del volumen» de la narrativa «Era Almeyda» era una cifra legacy inflada (el conteo real es ~8–10 % del volumen / ~13 % de interacciones; ni el alcance más amplio llega a 20 %). Se corrigió a **8,3 %**, dejándola consistente con las slides 4.2 (earned 13 738) y 4.4 (Almeyda 13 765 = 8,3 %).

**Iteración 11 (slide 4.3 recalculada con criterio corregido):**
- Se corrigió la clasificación **futbolística vs no-futbolística**: el contenido de equipo, porras, goles y **mística/identidad** ahora cuenta como **futbolística** (antes inflaba la dimensión de marca). Nueva estructura: **~93 % futbolística / ~7 % no-futbolística** (antes ~85 / 15).
- La tabla de sub-temas institucionales queda solo con lo **corporativo/off-pitch**: Patrocinio 3,4 % · Dirigencia 2,2 % · Estadio-sede 1,2 % · Aniversario 0,2 % · RSE 0,2 % (se retiran «Mística» e «Historia», que pasan a futbolística).
- **Nota del own corregida:** own institucional **~18 % vs terceros ~6,5 %** (own ≈ 3× más institucional; es la principal fuente de la marca positiva), en lugar del erróneo «~31 %, casi a la par de lo futbolístico» de la iteración 9.

**Iteración 10 (corrección del «26 %» en el resumen ejecutivo):**
- **Slide 1.1 (tarjeta A):** se corrigió el rótulo de la narrativa Mundial/estadio. El «26 % del corpus» era el **share de interacciones** mal etiquetado como volumen. Ahora dice «~11 % del volumen, pero moviliza ~1 de cada 4 interacciones (~24 %)», y se alinea el nombre con «Mundial · estadio sede» (4.2). Cierra el pendiente A.

**Iteración 9 (pendientes resueltos y ajustes de rótulos):**
- **Capítulo 06 renombrado** de «Estrategia» a **«Estrategia de monitoreo»** (índice, divider, encabezados y pies).
- **Slide 4.1:** se retiran las menciones a la metodología en pantalla (el eyebrow queda «Sentimiento · conversación de terceros», el pill «Base: menciones de terceros») y se elimina la nota al pie sobre la clasificación por léxico. La metodología se conserva documentada en este README.
- **Etiqueta «Casa Mundialista» alineada** (pendiente B): en 4.2 la narrativa pasa a **«Mundial · estadio sede»** (14 158 earned); en 4.3 el sub-tema pasa a **«Estadio como marca»** (1 249 / 0,8 %). Así una misma etiqueta deja de designar dos universos distintos.
- **Own en la dimensión de marca** (pendiente C, versión completa): en 4.3 el encabezado de la tabla se aclara a «Sub-tema de marca · resonancia en terceros» y se añade la nota «Qué empuja el own en esta dimensión» (RSE, aniversario, patrocinios, mística; ~31 % de lo que publica el club es institucional).
- Queda anotado en `PENDIENTES.md` un hallazgo nuevo por confirmar: la slide 1.1 afirma «Casa Mundialista 26 % del corpus», cifra legacy que no cuadra con la base.

**Iteración 8 (sentimiento recomputado, cap. 04 reordenado y percepción earned):**
- **Sentimiento recomputado por léxico explícito** (antes 28/47/25 editorial, inconsistente): el 28 % negativo estaba sobreestimado. La crítica dura dirigida al club es **5,5 %** (dirigencia/gestión, sequía, reacción a derrotas) y, sumando la rivalidad hostil que sí ataca a Rayados (1,4 %), el negativo real es **7 %**. La rivalidad sin carga clara pasa a neutro. Nueva distribución: **Negativo 7 · Neutro 75 · Positivo 18**. Se corrigió el callout de la slide de estructura para que sea coherente.
- **Capítulo 04 reordenado** a: 4.1 Distribución de sentimiento · 4.2 Narrativas: qué funciona (**re-agregada**) · 4.3 Estructura de la conversación · 4.4 Almeyda y jugadores.
- **FEMSA (5.2):** se añade la lente de **conversación abierta / earned** (Promotor 23 · Neutro 70 · Detractor 7; 99 % de las menciones de FEMSA son en relación a Rayados) separada de la lente de **comentarios** (Promotor 64 · Condicional 21 · Detractor 14).
- **te Kloese (5.3):** se añade la lente de percepción earned (Promotor 47 · Neutro 50 · Detractor 3).
- **RSE (5.4):** el total pasa de 168 a **163** para cuadrar con la suma de los cuatro criterios (35 + 61 + 39 + 28). Deck en **28 slides**.

**Iteración 7 (ajustes finales de formato y capítulo 06):**
- Slide 3.3: los dos valores de engagement ≥ 1 M pasan de K a M (`5 406 K → 5,4 M`, `1 953 K → 1,9 M`); el resto de la columna se mantiene en K.
- Se retiran las notas al pie del ranking de jugadores (4.2) y de la percepción de FEMSA (5.2), y se recorta la nota de RSE (5.4) dejando solo «Medido por programas concretos (Megalimpieza, Escuelas Rayados, The World's Pitch, UNICEF)».
- Slide 5.4: la tarjeta **Infancia** cambia el símbolo «+» por su volumen real, **28 menciones** (alianza UNICEF). Las cuatro tarjetas (35 · 61 · 39 · 28) suman 163, coherente con el titular de 168.
- Capítulo **06 «Recomendaciones» renombrado a «Estrategia»** en índice, divider, encabezados y pies (6.1 y 6.2).

**Iteración 6 (percepción de FEMSA en la audiencia):**
- Nueva slide **5.2 «FEMSA · percepción de la audiencia»**, insertada tras 5.1. Analiza los comentarios de las publicaciones de @rayados sobre la Megalimpieza del Río La Silla (iniciativa FEMSA): 14 comentarios de audiencia clasificados en **Promotor (64%) · Promotor condicional (21%) · Detractor (14%)**. Hallazgo: la audiencia percibe a FEMSA como promotor y **ninguna crítica ataca a FEMSA como propietario** — el malestar se redirige al plantel (deportivo) o al Estado (impuestos); el único frente a gestionar es la continuidad de la labor social. Fuentes: `Comentarios_1.xlsx` y `Comentarios_2.xlsx` (exports de comentarios; muestra cualitativa/direccional, no estadística).
- Renumeración de capítulo 05: te Kloese pasa a **5.3** y Responsabilidad social a **5.4**. El deck queda en **27 slides**.

**Iteración 5 (marca, jugadores y consistencia institucional):**
- **Cap. 04 reordenado a 3 slides.** Nueva **4.1 «Estructura: futbolística vs no-futbolística»**: la conversación es ~85% futbolística y ~15% de marca/institución; se abre la dimensión de marca en sub-temas (Dirigencia 8 142 · Patrocinio 5 718 · Mística 4 995 · Historia 4 684 · Estadio 1 249 · RSE ~170) con su tono, y se marca que el frente negativo vive en lo institucional («directiva / plantel caro que no gana»). Reemplaza la antigua «qué funciona: own vs terceros».
- Nueva **4.2 «Almeyda y jugadores»**: desglose de la conversación sobre Almeyda (DT, 13 765 menciones / 8,3%, con veta escéptica del 9%) y ranking de jugadores por volumen (Canales, Orbelín, Cuypers, Andrada, Rossi, Ocampos, Óliver Torres, Ambriz). Excluye al DT, a quienes ya no juegan en Rayados y a los nombres de mercado/rumor.
- **Sentimiento → 4.3.** El segmento del 28% se re-etiqueta **«Crítico / no-positivo»** (agrupa crítica al club y rivalidad bidireccional); se aclara que el negativo estructural dirigido al club es **~3–4%** y de baja tracción (49 de eng/pieza vs 175 de lo aspiracional): el 28% estaba sobre-representando el peso real del descontento.
- **FEMSA (5.1):** se agrega lectura de corpus — 0,51% del total, **99,5% earned / 0,5% own** (99 pts de diferencia), con narrativas por segmento.
- **te Kloese (5.2):** 0,82% del corpus, **100% earned** (0% own), con las tres narrativas dominantes (nueva era / arquitecto de Almeyda / despedida del Feyenoord).
- **RSE (5.3) corregida:** la cifra pasa de **2 354 → 168** menciones de programas concretos (Megalimpieza, Escuelas Rayados, The World's Pitch, UNICEF), **excluyendo el hashtag** general #EnLaVidaYEnLaCancha (usado en +2 000 posts, que inflaba el conteo). La conversación amplia de comunidad llega a ~450 menciones, impulsada por las cuentas propias.

**Iteración 4 (reestructura a 6 capítulos):**
- Deck consolidado de 40 → 25 slides y de 9 → 6 capítulos, sin perder información. Se eliminaron las repeticiones: la curva diaria duplicada, los 3 detalles de hito redundantes, el recap de autores (4.4), la narrativa total (7.3) y los solapes de own vs earned.
- Fusiones: Volumen+Hitos → cap. 02; Plataformas+Autores+own/earned → cap. 03 (nuevas slides "plataformas total" y "concentración · own vs earned"); Narrativas+Sentimiento → cap. 04 (nueva slide "qué funciona: own vs terceros"); FEMSA/te Kloese/RSE+otros → cap. 05.
- La versión extendida de 40 slides queda como respaldo.

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
