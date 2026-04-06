---
name: informe-seguimiento
description: Genera un informe de seguimiento en formato Word (.docx) para una instalación, una persona, o un conjunto de ellas. Incluye los capítulos estándar de Jarmauto con puntos positivos y puntos a mejorar por sección. Activar cuando el usuario pida un informe de seguimiento, un Word de seguimiento, o un informe de instalación/persona.
---

# Skill: Informe de Seguimiento (Word)

Genera un documento Word (.docx) estructurado para hacer seguimiento de instalaciones o personas en Jarmauto. Usa `python-docx` para construir el documento.

---

## Cuándo se activa

Cuando el usuario pide:
- "Genera un informe de seguimiento de [instalación/persona]"
- "Crea un Word de seguimiento para [X]"
- "Quiero un informe de [instalación/persona/varias]"

---

## Flujo de trabajo

### 1. Recopilar información antes de generar

Antes de crear el documento, pregunta al usuario por cada capítulo:

| Capítulo | Qué recopilar |
|---|---|
| Proactividad comercial | Acciones de venta activa, propuestas, campañas, resultados |
| Digital | Uso de herramientas digitales, adopción de plataformas, encuestas online |
| Calidad | NPS, reclamaciones, incidencias, auditorías, resultados de calidad |
| Procesos | Adherencia a procedimientos, tiempos, eficiencia operativa |
| Recursos generales | Personal, formación, equipamiento, instalaciones |
| Tareas pendientes | Acciones concretas con responsable y fecha límite |

Para cada sección, recopilar:
- **Puntos positivos** — qué está funcionando bien
- **Puntos a mejorar** — qué hay que corregir o impulsar

Si el usuario ya ha proporcionado la información, no preguntarla de nuevo.

### 2. Generar el script Python

Usa `python-docx` para construir el documento. Estructura del script:

```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import datetime

def crear_informe_seguimiento(titulo, subtitulo, secciones, output_path):
    """
    titulo: str — nombre del informe (ej. "Seguimiento Rivas Audi — Abril 2026")
    subtitulo: str — instalación/persona objeto del seguimiento
    secciones: list de dicts con estructura:
        {
            "nombre": "Proactividad comercial",
            "positivo": ["punto 1", "punto 2"],
            "mejorar": ["punto 1", "punto 2"],
            "tareas": []  # solo para el capítulo de tareas pendientes
        }
    output_path: str — ruta donde guardar el .docx
    """
    doc = Document()

    # Estilo de página
    section = doc.sections[0]
    section.page_width = Inches(8.27)   # A4
    section.page_height = Inches(11.69)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)

    # Cabecera del documento
    titulo_p = doc.add_heading(titulo, level=0)
    titulo_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    sub_p = doc.add_paragraph(subtitulo)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.runs[0].font.size = Pt(12)
    sub_p.runs[0].font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    fecha_p = doc.add_paragraph(f"Fecha: {datetime.date.today().strftime('%d/%m/%Y')}")
    fecha_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fecha_p.runs[0].font.size = Pt(10)
    fecha_p.runs[0].font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    doc.add_paragraph()  # espacio

    # Secciones
    for seccion in secciones:
        doc.add_heading(seccion["nombre"], level=1)

        if seccion.get("positivo"):
            p = doc.add_paragraph()
            run = p.add_run("Puntos positivos")
            run.bold = True
            run.font.color.rgb = RGBColor(0x1A, 0x7A, 0x3C)  # verde
            for punto in seccion["positivo"]:
                doc.add_paragraph(punto, style="List Bullet")

        if seccion.get("mejorar"):
            p = doc.add_paragraph()
            run = p.add_run("Puntos a mejorar")
            run.bold = True
            run.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)  # rojo
            for punto in seccion["mejorar"]:
                doc.add_paragraph(punto, style="List Bullet")

        if seccion.get("tareas"):
            table = doc.add_table(rows=1, cols=3)
            table.style = "Table Grid"
            hdr = table.rows[0].cells
            hdr[0].text = "Tarea"
            hdr[1].text = "Responsable"
            hdr[2].text = "Fecha límite"
            for hc in hdr:
                for run in hc.paragraphs[0].runs:
                    run.bold = True
            for tarea in seccion["tareas"]:
                row = table.add_row().cells
                row[0].text = tarea.get("tarea", "")
                row[1].text = tarea.get("responsable", "")
                row[2].text = tarea.get("fecha", "")

        doc.add_paragraph()  # separador entre secciones

    doc.save(output_path)
    print(f"Informe guardado en: {output_path}")


# --- DATOS DEL INFORME ---
# Rellenar con la información del seguimiento

TITULO = "Seguimiento — [INSTALACIÓN/PERSONA]"
SUBTITULO = "[Instalación o nombre] · [Mes Año]"
OUTPUT = "/Users/franciscomartin/Desktop/informe_seguimiento.docx"

SECCIONES = [
    {
        "nombre": "Proactividad comercial",
        "positivo": [
            # Añadir puntos positivos aquí
        ],
        "mejorar": [
            # Añadir puntos a mejorar aquí
        ]
    },
    {
        "nombre": "Digital",
        "positivo": [],
        "mejorar": []
    },
    {
        "nombre": "Calidad",
        "positivo": [],
        "mejorar": []
    },
    {
        "nombre": "Procesos",
        "positivo": [],
        "mejorar": []
    },
    {
        "nombre": "Recursos generales",
        "positivo": [],
        "mejorar": []
    },
    {
        "nombre": "Tareas pendientes",
        "positivo": [],
        "mejorar": [],
        "tareas": [
            # {"tarea": "Descripción", "responsable": "Nombre", "fecha": "DD/MM/YYYY"}
        ]
    }
]

crear_informe_seguimiento(TITULO, SUBTITULO, SECCIONES, OUTPUT)
```

### 3. Verificar dependencias

Antes de ejecutar, comprobar que `python-docx` está instalado:

```bash
pip show python-docx || pip install python-docx
```

### 4. Ejecutar y entregar

- Ejecutar el script con Python.
- Confirmar al usuario la ruta donde se ha guardado el documento.
- Si hay errores de importación o de ruta, corregirlos antes de reintentar.

---

## Variantes

| Caso | Adaptación |
|---|---|
| Seguimiento de persona | Cambiar título y subtítulo; el resto de secciones es igual |
| Varias instalaciones | Generar un documento por instalación en el mismo script con un bucle |
| Sin datos en una sección | Omitir esa sección del documento o añadir "Sin incidencias" |
| Tareas sin responsable | Dejar la celda en blanco |

---

## Notas

- El documento se guarda por defecto en `/Users/franciscomartin/Documents/ASISTENTE PERSONAL DE CLAUDE CODE/informes/`.
- Si el usuario especifica otra ruta, usarla.
- El formato de colores: verde para positivo, rojo para mejorar. No cambiar salvo que el usuario lo pida.
- La tabla de tareas pendientes solo aparece en el capítulo "Tareas pendientes".
