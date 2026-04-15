---
name: informe-cex
description: Genera el Informe de Seguimiento CEX, un documento Word único con todas las instalaciones de Jarmauto. Incluye Calidad ICC (con media y Top20 de red), CEM Carrocería y Cuadro de Calidad CX 2026 por instalación. Activar cuando el usuario pida el informe CEX, informe de calidad global o informe CX consolidado.
---

# Skill: Informe de Seguimiento CEX (Word)

Genera un único documento Word (.docx) con el seguimiento de calidad de todas las instalaciones de Jarmauto. Es un informe consolidado, no individual.

**Ejecutable Python obligatorio:** `/opt/homebrew/bin/python3`

**Ruta de salida:** `/Users/franciscomartin/Documents/ASISTENTE PERSONAL DE CLAUDE CODE/informes/`

**Naming:** `informe_seguimiento_CEX_{periodo}.docx` (ejemplo: `informe_seguimiento_CEX_2026-03.docx`)

**Script de referencia:** `/tmp/generar_informe_cex.py` (generado en sesión 2026-04-08, válido como base para periodos futuros)

---

## Fuentes de datos

| Archivo | Contenido |
|---|---|
| `Areas/Trabajo Postventa/Ranking ICC Instalaciones - {periodo}.md` | Posiciones, puntuaciones y detalle por módulo de cada instalación |
| `Areas/Trabajo Postventa/Ranking CX Instalaciones - {periodo}.md` | KPIs CX por instalación con puntuación y umbrales |
| Informes individuales `.docx` del periodo | Fuente de los valores de media y Top20 de red por indicador ICC |

Los valores de **media y Top20 de red** no están en el ranking ICC del vault. Se extraen de los informes individuales de jefes de taller:

| Instalación referencia | Red |
|---|---|
| `informe_seguimiento_izquierdo_canarias_{periodo}.docx` | Audi (143 instalaciones) |
| `informe_seguimiento_carlos_vara_{periodo}.docx` | VW Turismos (166 instalaciones) |
| `informe_seguimiento_fernando_industriales_{periodo}.docx` | VW Comerciales / LCV (121 instalaciones) |

Para extraerlos automáticamente usar `python-docx` buscando párrafos con "ICC -" y "media" en la sección Calidad de cada informe.

---

## Estructura del documento

Un documento único con 8 instalaciones. Cada instalación ocupa una página propia (salto de página al final, excepto la última).

### Orden de instalaciones

1. Rivas VW (30070 VW) — Volkswagen Turismos
2. Vara (0311Q VW) — Volkswagen Turismos
3. Moncloa VW (31523 VW) — Volkswagen Turismos
4. Industriales (30070 LCV) — VW Vehículos Comerciales
5. Canarias (51AQ3 AU) — Audi
6. Rivas Audi (51AQ1 AU) — Audi
7. Ayala (51AQ2 AU) — Audi
8. Moncloa Audi (31523 AU) — Audi

### Secciones por instalación (3)

#### 1. Calidad ICC

Encabezado: `ICC Calidad — Posición X/Y | Puntuación X,XX`

Clasificación positivo/mejorar usando los iconos del ranking ICC (check verde ✅ → positivo, cruz roja ❌ → mejorar). Cada línea incluye valor, media de red y Top20:

```
ICC - Nombre indicador: valor (media X,XX, Top20 X,XX). Comentario.
```

Indicadores por red:

**Audi (instalaciones 51AQ1, 51AQ2, 51AQ3, 31523 AU):**
- CEM Satisfacción General (media 4,69, Top20 5,0)
- Audi Move (media 56,2%, Top20 92,5%)
- ICT Incidencias (media 0,6%, Top20 0%)
- Contacto Proceso AU (media 74,1%, Top20 96,3%)
- Escalaciones (media 4,67%, Top20 0%)
- Transporte Alternativo (media 56,1%, sin Top20 documentado)
- MyAudi&Me (media 25,9%, Top20 52,9%)
- Cita Online (media 18,1%, Top20 47,6%)

**VW Turismos (instalaciones 30070 VW, 0311Q VW, 31523 VW):**
- ICT Incidencias (media 0,5%, Top20 0%)
- Escalaciones At. C. (media 2,4%, Top20 0%)
- Satisfacción General NPS (media 65,4%, Top20 96,2%)
- Google BP (media 97,8%, Top20 100%)
- Recogida y Entrega (media 5,3%–5,85%, Top20 15%)
- ONE Score (media 6,6, Top20 8,8)
- Recovery Conectividad (media 7,72%, Top20 21,47%)
- Serv. Movilidad / Cita Online según instalación

**VW Comerciales (30070 LCV):**
- ICT Incidencias (media 0,9%, Top20 0%)
- Casos Escalados (media 0,0%, Top20 0,0%)
- CEM Satisfacción General (media 4,62, Top20 5,00)
- Servicio Movilidad (media 45,6%, Top20 81,6%)

#### 2. CEM Carrocería

Una sola línea con el dato ICC de CEM Carrocería de la instalación (media y Top20 incluidos). Si la instalación no tiene dato, escribir "Sin datos registrados".

Instalaciones con CEM Carrocería disponible en Marzo 2026:
- Rivas VW: 5,00 (media 4,45, Top20 4,68)
- Industriales: 5,00 (media 4,45, Top20 4,68)
- Rivas Audi: 5,0 (media 4,78, Top20 5,0)
- Ayala: 5,0 (media 4,78, Top20 5,0)

Sin dato: Vara, Moncloa VW, Canarias, Moncloa Audi.

#### 3. Cuadro de Calidad CX 2026

Mismo formato que en los informes individuales. Máximo 8 puntos (4 KPIs × 2 pts), EC28 máximo 1 pt. Clasificación: 2 pts = positivo, <2 pts = mejorar.

Cada línea:
```
Nombre KPI: valor — X/2 pts  |  Referencia: 0pts ... | 1pt ... | 2pts ...
```

Ver `Areas/Trabajo Postventa/Ranking CX Instalaciones - {periodo}.md` para los datos actualizados de cada periodo.

---

## Datos CX Marzo 2026

| Instalación | Total | Código |
|---|---|---|
| Rivas Audi (51AQ1 AU) | 4/8 | `51AQ1_AU` |
| Ayala (51AQ2 AU) | 7/8 | `51AQ2_AU` |
| Canarias (51AQ3 AU) | 5/8 | `51AQ3_AU` |
| Moncloa Audi (31523 AU) | 5/8 | `31523_AU` |
| Moncloa VW (31523 VW) | 4/8 | `31523_VW` |
| Vara (0311Q VW) | 4/8 | `0311Q_VW` |
| Rivas VW (30070 VW) | 5/8 | `30070_VW` |
| Industriales (30070 LCV) | 6/8 | `30070_LCV` |

---

## Flujo de trabajo para un nuevo periodo

1. Recibir el nuevo Ranking ICC Instalaciones y guardarlo en el vault.
2. Recibir el nuevo Ranking CX Instalaciones y guardarlo en el vault.
3. Verificar que los informes individuales del nuevo periodo ya están generados (son la fuente de media y Top20).
4. Extraer media y Top20 de los informes de Izquierdo (Audi), Carlos Vara (VW) y Fernando Industriales (LCV).
5. Actualizar los datos en el script y generar el documento.

---

## Notas

- No usar el Python de sistema (3.9): usar siempre `/opt/homebrew/bin/python3`.
- Vara, Moncloa VW, Canarias y Moncloa Audi no tienen CEM Carrocería: poner "Sin datos registrados".
- Las instalaciones de chapa (Luis Ramos, Pericles) no tienen informe CEX propio: sus datos de calidad van agrupados bajo la instalación mecánica asociada.
- Los colores son fijos: verde `#1A7A3C` para positivos, rojo `#C0392B` para mejorar.
