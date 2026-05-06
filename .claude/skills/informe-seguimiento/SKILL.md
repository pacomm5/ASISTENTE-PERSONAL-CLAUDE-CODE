---
name: informe-seguimiento
description: Genera informes de seguimiento en formato Word (.docx) para asesores de servicio e instalaciones (jefes de taller) de Jarmauto. Incluye datos de rankings de desgaste, Iron Man e ICC por sección. Activar cuando el usuario pida un informe de seguimiento, un Word de seguimiento, o informe de instalación/persona. También genera la versión HTML a partir del Word ya generado.
---

# Skill: Informe de Seguimiento (Word + HTML)

Genera documentos Word (.docx) estructurados para hacer seguimiento de instalaciones y asesores en Jarmauto. Usa `python-docx` para construir el documento.

## Flujo obligatorio Word → HTML / Excel

El Word es siempre el documento de trabajo. El HTML y el Excel son siempre derivados del Word, nunca al revés.

1. **Generar el Word** con los datos de rankings del vault.
2. **El usuario revisa y completa el Word**: tareas pendientes, grado de cumplimiento, notas específicas.
3. **Generar el HTML y/o Excel** leyendo el Word ya cerrado con `python-docx` como única fuente de datos.

No generar HTML ni Excel antes de que el Word esté revisado y cerrado. Si el usuario pide HTML o Excel sin haber generado el Word antes, avisar y generar primero el Word.

**Ejecutable Python obligatorio:** `/opt/homebrew/bin/python3` (el Python de sistema 3.9 no tiene acceso al módulo docx aunque esté instalado).

**Ruta de salida por defecto:** `/Users/franciscomartin/Documents/ASISTENTE PERSONAL DE CLAUDE CODE/informes/`

**Naming:** `informe_seguimiento_{nombre}_{instalacion}_{periodo}.docx` (ejemplo: `informe_seguimiento_emilio_rivas_audi_2026-03.docx`)

---

## Fuentes de datos

Los rankings de referencia están guardados en el vault en `Areas/Trabajo Postventa/`:

| Archivo | Contenido |
|---|---|
| `Ranking Desgaste Asesores - {periodo}.md` | Desgaste por categoría de los 18 asesores activos |
| `Ranking Desgaste Instalaciones - {periodo}.md` | Desgaste por categoría de las 7 instalaciones de mecánica |
| `Ranking Iron Man Asesores - {periodo}.md` | Full/Long Drive, CAL1SEM, Fidelidad, Horch Lauden de asesores |
| `Ranking Iron Man Jefes Taller - {periodo}.md` | ICC puesto, CAL1SEM, Productividad, Var Rec, Var MO, Horch Lauden de instalaciones |
| `Ranking ICC Instalaciones - {periodo}.md` | Todos los módulos ICC (Proactividad, Digital, Carrocería, Calidad, Recursos, Personas) por instalación |

---

## Tipos de informe

### A) Informe de Asesor de Servicio

**Secciones (9):**

1. **Proactividad comercial** — Desgaste total (posición ranking + detalle por categoría vs media equipo) + Full/Long Drive (vs media 8.39) + Fidelidad (vs media 63.48%)
2. **Digital** — Sin datos (dejar vacío salvo que el usuario aporte información)
3. **Calidad** — CAL1SEM con escala de puntos Iron Man (<4→0, 4-<5→10, 5-<6→20, 6-7→30, >7→50)
4. **Procesos** — Sin datos (dejar vacío salvo que el usuario aporte información)
5. **Recursos generales** — Sin datos (dejar vacío salvo que el usuario aporte información)
6. **Horch Lauden** — Posición en la competición de marca (menor = mejor). Sección propia porque el sentido es inverso al resto.
7. **Cuadro de Calidad CX 2026** — KPIs de remuneración CX de la instalación asignada, con puntuación obtenida, umbrales de referencia y clasificación positivo/mejorar. Fuente: `Ranking CX Instalaciones - AAAA-MM.md`
8. **ONE KVPS** — Score SEM, Service CAM Acum., Diferidos Acum., Multimedia Acum. con clasificación positivo/mejorar
9. **Tareas pendientes** — Tabla con columnas: Tarea, Responsable, Fecha límite

**Clasificación positivo/mejorar (asesores):**
- Desgaste total: por debajo de 200 pts → mejorar (seguimiento prioritario)
- Desgaste por categoría: comparar con media del equipo
- Full/Long Drive: media equipo = 8.39 operaciones
- Fidelidad: media equipo = 63.48% (N/A para Estefanía, Juan, Dennis, Jon, Nuria)
- CAL1SEM >= 5 → positivo; < 5 → mejorar
- Horch Lauden: <= 20 destacado, <= 50 aceptable, > 50 requiere atención

**Equivalencias de nombres DMS → nombre real:**
- EUGENIO T. → Taboada
- F.J. RODRIGUEZ → Javier Pina
- CARLOS AYALA → Carlos Aguilar
- JON2 → Jon
- JORGE → ya no trabaja (no generar informe)

---

### B) Informe de Jefe de Taller (instalación)

**Secciones (11):**

1. **Proactividad comercial** — Datos Iron Man (desgaste + variaciones) + datos ICC módulo Proactividad
2. **Digital** — Datos ICC módulo Digital
3. **Calidad** — CAL1SEM Iron Man + datos ICC módulo Calidad
4. **Procesos** — Productividad vs objetivo específico por instalación
5. **Recursos generales** — Datos ICC módulo Recursos Generales
6. **Carrocería** — Datos ICC módulo Carrocería
7. **Personas** — Datos ICC módulo Personas
8. **Rankings de marca** — Posición global ICC + Iron Man ICC puesto + Horch Lauden
9. **Cuadro de Calidad CX 2026** — KPIs de remuneración CX de la instalación, con puntuación obtenida, umbrales de referencia y clasificación positivo/mejorar. Fuente: `Ranking CX Instalaciones - AAAA-MM.md`
10. **ONE KVPS** — Score SEM, Service CAM Acum., Diferidos Acum., Multimedia Acum. con clasificación positivo/mejorar
11. **Tareas pendientes** — Tabla con columnas: Tarea, Responsable, Fecha límite

**Detalle sección Proactividad comercial:**
- Instalaciones de **mecánica** (Rivas Audi, Moncloa VW, Moncloa Audi, Ayala, Vara, Canarias, Rivas VW): desgaste total con posición ranking (referencia: <220% es seguimiento prioritario) + detalle por categoría + Var Rec 2A + Var MO 2A + indicadores ICC
- Instalaciones de **chapa** (Rivas A Chapa, Rivas W Chapa, Canarias Chapa, Vara Chapa): sin desgaste propio, solo Var Rec 2A + Var MO 2A + indicadores ICC

**Objetivos de productividad por instalación:**
- Ayala: 105%
- Rivas VW (mecánica): 89%
- Chapa (Rivas A, Rivas W, Canarias, Vara): 120%
- Resto (Rivas Audi, Moncloa VW, Moncloa Audi, Vara, Canarias): 93%

**Clasificación positivo/mejorar ICC:** usar los iconos del propio informe ICC (check verde → positivo, cruz roja → mejorar). Cada punto ICC lleva el prefijo "ICC -" y la primera viñeta de cada sección es la referencia de módulo con posición y puntuación.

**Mapeo instalación → código ICC:**
- Rivas Audi → 51AQ1 AU
- Ayala → 51AQ2 AU
- Canarias → 51AQ3 AU
- Moncloa Audi → 31523 AU
- Rivas VW + Rivas W Chapa → 30070 VW
- Vara + Vara Chapa → 0311Q VW
- Moncloa VW → 31523 VW
- Industriales → 30070 LCV

**Caso especial — Industriales (Fernando):** solo datos ICC, sin datos Iron Man. Procesos y Rankings de marca vacíos.

---

## ONE KVPS

Sistema de seguimiento semanal de satisfacción del cliente. Se incluye como sección propia en todos los informes mensuales, antes de Tareas pendientes.

**Fuentes de datos:**
- `Areas/Trabajo Postventa/Ranking ONE Instalaciones - AAAA-SNN.md`
- `Areas/Trabajo Postventa/Ranking ONE Asesores - AAAA-SNN.md`

**KPIs incluidos (4):** Score SEM, Service CAM Acum., Diferidos Acum., Multimedia Acum.

**Umbrales de clasificación:**

| KPI | Positivo | Regular (mejorar) | Mejorar |
|---|---|---|---|
| Score SEM | Por encima de la media del equipo | — | Por debajo de la media |
| Service CAM Acum. | ≥8% | 5-8% | <5% |
| Diferidos Acum. | ≥8% | 5-8% | <5% |
| Multimedia Acum. | ≥5 | 3-5 | <3 |

Cada bullet incluye el valor, la media del equipo y la descripción del rango.

**Medias de referencia (actualizables cada semana):**
- Asesores: Score 5,8 | CAM 6% | Diferidos 12% | Multimedia 5,6
- Instalaciones: Score 6,9 | CAM 6% | Diferidos 11% | Multimedia 6,0

**Mapeo instalaciones ONE (códigos KVPS):**
- 31523 → Moncloa (aplica a Moncloa VW y Moncloa Audi)
- 00158 → Rivas Audi (solo informe de Emilio, no chapa)
- 00159 → Ayala
- 00160 → Rivas Canarias (solo informe de Izquierdo, no chapa)
- 00982 → Vara
- 30070 → Industriales + Rivas VW (el mismo código aplica a los dos informes de Fernando)

Las instalaciones de chapa (Luis Ramos, Pericles) no tienen código ONE: sección con "Sin datos registrados".

**José María Campos:** aparece en el ranking ONE de asesores (ASP). Su dato ONE va a su informe de asesor (`informe_seguimiento_jose_maria_AAAA-MM.docx`), no a sus informes de jefe de taller.

---

## Cuadro de Calidad CX 2026

Sistema de remuneración cuatrimestral de marca (Audi, VW Turismos, VW Comerciales). Máximo 8 puntos por instalación. Fuente: `Areas/Trabajo Postventa/Ranking CX Instalaciones - AAAA-MM.md`.

**Clasificación:** 2 pts = positivo; 0 o 1 pt = mejorar. Incluir el valor actual, la puntuación obtenida y los umbrales de referencia en cada línea.

**Para asesores con dos instalaciones** (Guillermo, Javier Pina, Nuria → 30070 VW + 30070 LCV; Raúl Muñoz, José María Campos asesor → 31523 AU + 31523 VW): insertar dos bloques uno debajo del otro, identificados por instalación.

### Umbrales Audi Service

| KPI | 0 pts | 1 pt | 2 pts |
|---|---|---|---|
| CEM Q4 (Satisfacción General) | <4,60 | ≥4,60 | ≥4,80 |
| EC28 (Medidas de Servicio) | >5% | ≤5% | ≤1% |
| Conectividad Posventa (ASR) | <25% | ≥25% | ≥45% |
| TRS / Información Proceso (Encuesta) | <80% | ≥80% | ≥90% |

Remuneración: ≥7pts: 6-7 €/h | 6pts: 5-6 €/h | 5pts: 4-5 €/h | 4pts: 3-4 €/h

### Umbrales VW Turismos

| KPI | 0 pts | 1 pt | 2 pts |
|---|---|---|---|
| Google Business Profile (% Respuestas) | <80% | ≥80% | 100% |
| EC28 (Medidas de Servicio) | >5% | ≤5% | ≤3% |
| Conectividad (ASS Activado) | <25% | ≥25% | ≥40% |
| Club Volkswagen (% Adhesión) | <3% | ≥3% | ≥6% |

Remuneración: ≥7pts: 3-3,5 €/h | 6pts: 2,5-3 €/h | 5pts: 2-2,5 €/h | 4pts: 1,5-2 €/h

### Umbrales VW Vehículos Comerciales

| KPI | 0 pts | 1 pt | 2 pts |
|---|---|---|---|
| Satisfacción General (CEM) | <4,52 | ≥4,52 | ≥4,62 |
| EC28 (Medidas de Servicio) | >5% | ≤5% | ≤3% |
| Conectividad Posventa (ASS) | <10% | ≥10% | ≥25% |
| Servicios Rápidos (en el día) | <40% | ≥40% | ≥45% |

Remuneración: ≥7pts: 6-6,5 €/h | 6pts: 5-5,5 €/h | 5pts: 4-4,5 €/h | 4pts: 3-3,5 €/h

### Mapeo asesor → instalación CX

| Asesor | Código(s) CX |
|---|---|
| Alvaro, Estefanía, Codru, Dennis | 51AQ1 AU |
| Alberto Martínez (asesor), Carlos Aguilar | 51AQ2 AU |
| Magán, Taboada, Alejandro, Jon | 51AQ3 AU |
| Javier Díaz Mesa, José María Vázquez, Juan | 0311Q VW |
| Raúl Muñoz, José María Campos (asesor) | 31523 AU + 31523 VW |
| Guillermo, Javier Pina, Nuria | 30070 VW + 30070 LCV |

### Mapeo jefe de taller → instalación CX

| Jefe | Informe | Código CX |
|---|---|---|
| Emilio | Rivas Audi | 51AQ1 AU |
| Luis Ramos | Rivas Audi Chapa | 51AQ1 AU |
| Luis Ramos | Rivas VW Chapa | 30070 VW |
| Izquierdo | Canarias | 51AQ3 AU |
| Pericles | Canarias Chapa | 51AQ3 AU |
| Pericles | Vara Chapa | 0311Q VW |
| Alberto Martínez | Ayala | 51AQ2 AU |
| Carlos | Vara | 0311Q VW |
| José María Campos | Moncloa VW | 31523 VW |
| José María Campos | Moncloa Audi | 31523 AU |
| Fernando | Rivas VW | 30070 VW |
| Fernando | Industriales | 30070 LCV |

---

## Tareas pendientes

Las tareas **no son fijas**. La tabla tiene 4 columnas: **Tarea**, **Responsable**, **Fecha límite**, **Grado de cumplimentación**.

Funcionan así:

- Al generar un nuevo periodo, leer el informe del periodo anterior.
- Si el **Grado de cumplimentación es 100%** → tarea completada, no arrastrar al nuevo informe.
- Si el **Grado de cumplimentación es inferior a 100%** (o está vacío) → arrastrar al nuevo informe con el grado indicado.
- Si es el primer informe (sin periodo anterior), incluir solo las tareas que indique el usuario.

---

## Personas que comparten instalación ICC

Cuando una instalación tiene mecánica y chapa, los datos ICC del módulo de Carrocería aplican a ambos informes:

| Instalación ICC | Informes afectados |
|---|---|
| 51AQ1 AU (Rivas Audi) | Emilio + Luis Ramos (Rivas A Chapa) |
| 51AQ3 AU (Canarias) | Izquierdo + Pericles (Canarias Chapa) |
| 0311Q VW (Vara) | Carlos + Pericles (Vara Chapa) |
| 30070 VW (Rivas VW) | Fernando + Luis Ramos (Rivas W Chapa) |
| 31523 AU (Moncloa Audi) | José María Campos (Moncloa Audi) |
| 31523 VW (Moncloa VW) | José María Campos (Moncloa VW) |
| 51AQ2 AU (Ayala) | Alberto Martínez |
| 30070 LCV (Industriales) | Fernando (informe separado, solo ICC) |

---

## Flujo de trabajo al generar un nuevo periodo

1. El usuario sube los rankings del nuevo periodo.
2. Guardarlos en el vault como archivos de referencia (`Ranking X - AAAA-MM.md`).
3. Preguntar si hay cambios en el equipo (altas, bajas, cambios de instalación).
4. Leer los informes del periodo anterior para identificar tareas con Grado de cumplimentación inferior a 100%.
5. Generar todos los informes Word con los datos nuevos, mostrando evolución respecto al periodo anterior donde corresponda.
6. Arrastrar solo las tareas con Grado de cumplimentación inferior a 100% (o vacío) al nuevo periodo.
7. El usuario revisa y completa cada Word (tareas pendientes, grado de cumplimiento, notas).
8. Una vez cerrado el Word, generar el HTML y el Excel correspondientes leyendo el Word como fuente de datos.

---

## Generación del HTML y Excel a partir del Word

El HTML y el Excel se generan siempre **después** de que el Word esté revisado y cerrado. Nunca antes. Ambos formatos leen los Word como única fuente de datos.

**Script:** `informes/generar_html_excel.py`. Ejecutar con `/opt/homebrew/bin/python3 generar_html_excel.py`.

### Estructura de salida — multi-pestaña por persona

El script agrupa todos los Word de una misma persona (`informe_seguimiento_{key}_YYYY-MM.docx`) y genera **un único HTML y un único Excel por persona** con las siguientes pestañas/hojas:

| Pestaña | Contenido |
|---|---|
| Una por cada mes (`Mar 2026`, `Abr 2026`...) | Contenido del Word de ese mes (positivos, mejoras, tareas) |
| **Evolución** | Tabla comparativa de métricas clave por mes + columna Objetivo al final |
| **Objetivos** | Tarjeta de umbrales de referencia según el tipo de persona |

La pestaña activa por defecto es el **último mes** disponible.

### Naming

- HTML: `informe_seguimiento_{key}.html` (sin periodo — contiene todos los meses)
- Excel: `informe_seguimiento_{key}.xlsx`

El `key` coincide con el nombre del Word sin el prefijo `informe_seguimiento_` ni el sufijo `_YYYY-MM.docx`. Ejemplos: `alvaro`, `emilio_rivas_audi`, `luis_ramos_rivas_a_chapa`.

### Pestaña Evolución — métricas y objetivo

Métricas extraídas por regex de los bullets del Word. La última columna es siempre **Objetivo** (fondo azul oscuro, texto dorado). Métricas por tipo:

| Tipo | Métricas en Evolución |
|---|---|
| Asesor | Desgaste total, Posición ranking, CAL1SEM, Full/Long Drive, Fidelidad, Horch Lauden, Score ONE, Service CAM, Diferidos, Multimedia |
| Jefe mecánica | Desgaste total, Posición ranking, CAL1SEM, Productividad, Var Rec 2A, Var MO 2A, Horch Lauden, Score ONE, Service CAM, Diferidos, Multimedia |
| Jefe chapa | CAL1SEM, Productividad, Var Rec 2A, Var MO 2A, Horch Lauden |
| Industriales | Score ONE, Service CAM, Diferidos, Multimedia |

Los objetivos de productividad específicos por instalación (Ayala 105%, Rivas VW 89%, chapa 120%) se aplican automáticamente a la columna Objetivo.

### Colores fijos

- Verde positivo: `#1A7A3C`
- Rojo mejorar: `#C0392B`
- Azul cabecera: `#1A2B4A`
- Dorado objetivo: `#FFD700` sobre fondo `#1A2B4A`

### Parsing del Word

Usar `python-docx`. Heading 1 = sección, "Puntos positivos" / "Puntos a mejorar" = bloque, List Bullet = bullet. Las tablas Word son las tareas pendientes. Los bullets con patrón `ICC - Indicador: valor (media X, Top20 Y)` se renderizan como tabla de datos; el resto como lista de texto. **No usar regex con `(.*)` al final para parsear ICC** — usar parser paso a paso por `find()` para evitar roturas con coma decimal europea. Ver `parse_icc_bullet()` en el script.

---

## Generación del script Python

```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import datetime

def crear_informe(titulo, subtitulo, secciones, output_path):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.left_margin = section.right_margin = section.top_margin = section.bottom_margin = Inches(1)

    hp = doc.add_heading(titulo, level=0); hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sp = doc.add_paragraph(subtitulo); sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sp.runs[0].font.size = Pt(12); sp.runs[0].font.color.rgb = RGBColor(0x44,0x44,0x44)
    fp = doc.add_paragraph(f"Fecha: {datetime.date.today().strftime('%d/%m/%Y')}"); fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.runs[0].font.size = Pt(10); fp.runs[0].font.color.rgb = RGBColor(0x88,0x88,0x88)
    doc.add_paragraph()

    for s in secciones:
        doc.add_heading(s["nombre"], level=1)
        if s.get("positivo"):
            p = doc.add_paragraph(); r = p.add_run("Puntos positivos")
            r.bold = True; r.font.color.rgb = RGBColor(0x1A,0x7A,0x3C)
            for x in s["positivo"]: doc.add_paragraph(x, style="List Bullet")
        if s.get("mejorar"):
            p = doc.add_paragraph(); r = p.add_run("Puntos a mejorar")
            r.bold = True; r.font.color.rgb = RGBColor(0xC0,0x39,0x2B)
            for x in s["mejorar"]: doc.add_paragraph(x, style="List Bullet")
        if not s.get("positivo") and not s.get("mejorar") and s.get("tareas") is None:
            doc.add_paragraph("Sin datos registrados")
        if s.get("tareas") is not None:
            tbl = doc.add_table(rows=1, cols=3); tbl.style = "Table Grid"
            hdr = tbl.rows[0].cells
            hdr[0].text = "Tarea"; hdr[1].text = "Responsable"; hdr[2].text = "Fecha limite"
            for hc in hdr:
                for r2 in hc.paragraphs[0].runs: r2.bold = True
            for t in s["tareas"]:
                row = tbl.add_row().cells
                row[0].text = t.get("tarea",""); row[1].text = t.get("responsable",""); row[2].text = t.get("fecha","")
        doc.add_paragraph()

    doc.save(output_path)
    print(f"Guardado: {output_path}")
```

---

## Notas

- No cambiar los colores: verde para positivos, rojo para mejorar.
- La tabla de tareas pendientes solo aparece en la sección "Tareas pendientes".
- Si una sección no tiene datos, escribir "Sin datos registrados" (no dejar en blanco).
- Parabrisas con valor 0% en Moncloa VW, Ayala y Moncloa Audi es normal: las lunas se cambian en los talleres de carrocería, no en mecánica.
