# Reporte de Social Listening · Rayados de Monterrey (Q2–Q3 2026)

Deck ejecutivo HTML (1920×1080, design system Artool) sobre la conversación digital del **Club de Fútbol Monterrey (Rayados)** entre el **28 de abril y el 28 de julio de 2026**.

Archivo principal: **`Rayados_Social_Listening_Q2-Q3_2026.html`** (autocontenido; se abre en cualquier navegador y se puede exportar a PDF/PPTX).

## Base de datos

- **166 467 registros** (menciones y posts), una sola tabla.
- Columnas: `published`, `content`, `source_type`, `extra_author_attributes.name`, `engagement`, `Visualizaciones TikTok`.
- Todos los cálculos numéricos se hicieron sobre la **base completa** (sin muestreo ni estimaciones).

## Cambios respecto a la versión anterior

### Capítulos nuevos
- **07 · Own & Earned Media** — profundización en el contenido propio del club (own) vs las menciones de terceros (earned):
  1. Volumen total, timeline por mes y autores.
  2. Distribución por plataforma (menciones + engagement + en qué destaca cada una), ordenada por menciones.
  3. Principales autores por engagement (own + earned).
  4. Distribución de sentimiento (own vs earned).
  5. Principales narrativas ordenadas por volumen de menciones.
- **08 · Rayados como institución** — dimensión corporativa:
  1. FEMSA (propietario).
  2. Dennis te Kloese (presidente deportivo).
  3. Responsabilidad social (Megalimpieza Río La Silla, Escuelas Rayados y clínicas para la niñez, The World's Pitch, alianza con UNICEF).
  4. Otros temas institucionales (Estadio Monterrey como sede mundialista, patrocinio BBVA, 81 aniversario, alianza WOBI).

### Correcciones
1. **Estimaciones → base total.** La slide de tipologías (4.3) se recalculó sobre los 166 467 registros (se eliminó la nota "Estimaciones basadas en el top 30 de autores").
2. **Sin medianas.** Se eliminaron los cálculos de mediana ("Mediana diaria" en 2.1 y "Mediana del corpus completo = 0 interacciones" en 3.2).
3. **"pico/picos" → "peak/peaks"** en todo el deck.
4. **Top autores por engagement (4.2)** recalculado sobre la base (los valores coincidían con la base; se confirmaron).

### Estructura
- Se agregó un **índice** con los 9 capítulos.
- Numeración **consecutiva y ascendente desde 1** (antes iniciaba en 02 y saltaba el 08). El índice no cuenta como capítulo.

## Metodología de las nuevas métricas

- **Own media (cuentas propias del club, 12):** `rayados`, `Rayados`, `wearerayados`, `rayadostv`, `rayados_fb`, `tiendarayados`, `rayadas`, `Rayadas`, `Rayados English`, `Club de Futbol Monterrey`, `Club de Futbol Monterrey Rayados`, `Rayados Fuerzas Básicas`. **Earned media:** el resto de autores (49 481 cuentas).
- **Plataformas:** derivadas de `source_type`; engagement por plataforma = suma real de la columna `engagement`.
- **Tipologías (4.3):** clasificación de todos los autores por patrones de nombre + tipo de fuente; suma de engagement por categoría.
- **Sentimiento (7.4):** clasificación léxica automatizada (léxico positivo/negativo en español) sobre el 100 % de los registros. Complementa la lectura editorial de terceros del capítulo 05.
- **Narrativas (7.5) y temas corporativos (cap. 08):** etiquetado por palabras clave sobre el texto de la base completa; los temas no son mutuamente excluyentes.

## Cifras clave (base completa)

| Métrica | Valor |
|---|---|
| Menciones totales | 166 467 |
| Interacciones totales | 20 632 584 (20,6 M) |
| Autores únicos | 49 493 |
| Own media | 2 319 menciones (1,4 %) · 10,1 M eng (48,9 %) |
| Earned media | 164 148 menciones (98,6 %) · 10,6 M eng (51,1 %) |
| Top-30 autores | 66,2 % del engagement |
| Peak de volumen | 28 abr · 6 939 menciones (3,8× el promedio diario) |
| FEMSA | 842 menciones |
| Dennis te Kloese | 1 360 menciones · peak en mayo |
| Responsabilidad social | 2 354 menciones |

## Reproducibilidad

La carpeta `analysis/` contiene los scripts de transformación (`build_step1.py` … `build_final.py`) y los agregados calculados (`analisisA.json`, `analisisB.json`, `tipologias.json`). El archivo de datos crudo (Excel) no se versiona.
