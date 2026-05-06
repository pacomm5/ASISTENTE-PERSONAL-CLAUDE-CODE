#!/usr/bin/env /opt/homebrew/bin/python3
"""
Genera HTML y Excel para todos los informes de seguimiento Word (.docx).
Lee cada Word, parsea su estructura y produce archivos .html y .xlsx con el mismo nombre.
"""

import glob
import os
import re
import datetime
from docx import Document
from docx.oxml.ns import qn

# ── openpyxl ──────────────────────────────────────────────────────────────────
from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter

# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTES DE ESTILO
# ══════════════════════════════════════════════════════════════════════════════
COLOR_HEADER   = "#1A2B4A"
COLOR_VERDE    = "#1A7A3C"
COLOR_ROJO     = "#C0392B"
COLOR_AMARILLO = "#FFD700"
COLOR_GRIS     = "#F5F5F5"

# ══════════════════════════════════════════════════════════════════════════════
# PARSER DEL WORD
# ══════════════════════════════════════════════════════════════════════════════

ICC_MOD_RE = re.compile(
    r"ICC\s+M[oó]dulo\s+(.+?)\s*[—\-]\s*Posici[oó]n\s+(\d+)\s+de\s+(\d+)"
    r"(?:\s*\|\s*Puntuaci[oó]n del m[oó]dulo:\s*([\d,\.]+))?",
    re.I
)

def parse_word(path):
    doc = Document(path)

    meta = {"titulo": "", "subtitulo": "", "fecha": ""}
    sections = []
    cur_sec = None
    bloque = None

    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if not txt:
            continue

        sname = p.style.name

        if sname == "Title" or (i == 0 and not meta["titulo"]):
            meta["titulo"] = txt
        elif sname == "Normal" and i == 1 and not meta["subtitulo"]:
            meta["subtitulo"] = txt
        elif sname == "Normal" and txt.startswith("Fecha:") and not meta["fecha"]:
            meta["fecha"] = txt
        elif sname == "Heading 1":
            cur_sec = {"nombre": txt, "positivo": [], "mejorar": [], "neutro": []}
            sections.append(cur_sec)
            bloque = None
        elif txt == "Puntos positivos":
            bloque = "positivo"
        elif txt == "Puntos a mejorar":
            bloque = "mejorar"
        elif txt == "Sin datos registrados":
            if cur_sec is not None:
                cur_sec["sin_datos"] = True
        elif cur_sec is not None and bloque and sname in ("List Bullet", "List Paragraph", "Normal"):
            cur_sec[bloque].append(txt)

    # Tareas (tabla Word)
    tabla_tareas = None
    for tbl in doc.tables:
        filas = [[c.text.strip() for c in row.cells] for row in tbl.rows]
        if filas and "Tarea" in filas[0]:
            tabla_tareas = filas
            break

    return meta, sections, tabla_tareas


def parse_icc_bullet(txt):
    """
    Parsea bullets con formato:
      ICC - Indicador: valor (media X, Top20 Y). Comentario.
    Devuelve (indicador, valor, media, top20, comentario) o None.
    """
    if not re.match(r'^ICC\s*-\s*', txt, re.I):
        return None

    # Quitar prefijo "ICC - "
    rest = re.sub(r'^ICC\s*-\s*', '', txt, flags=re.I).strip()

    # Separar indicador en el primer ":"
    colon = rest.find(':')
    if colon == -1:
        return None
    indicador = rest[:colon].strip()
    after = rest[colon + 1:].strip()

    # Buscar "(media "
    m_media = re.search(r'\(media\s+', after, re.I)
    if m_media:
        valor = after[:m_media.start()].strip()
        inner_start = m_media.end()
        # Primer ")" que cierra el paréntesis de media
        close = after.find(')', inner_start)
        if close == -1:
            close = len(after)
        inner = after[inner_start:close]

        # Separar media de Top20 (si existe)
        m_top = re.search(r',\s*Top20\s+', inner, re.I)
        if m_top:
            media = inner[:m_top.start()].strip()
            top20 = inner[m_top.end():].strip()
        else:
            media = inner.strip()
            top20 = ""

        # Comentario es lo que queda tras el ")"
        comment = after[close + 1:].strip().lstrip('.')
    else:
        valor = after
        media = ""
        top20 = ""
        comment = ""

    return indicador, valor, media, top20, comment


def parse_icc_module_header(txt):
    """Devuelve (modulo, pos, total, puntuacion) o None."""
    m = ICC_MOD_RE.match(txt)
    if not m:
        return None
    mod  = m.group(1).strip()
    pos  = m.group(2)
    tot  = m.group(3)
    pts  = (m.group(4) or "").strip()
    return mod, pos, tot, pts




# ══════════════════════════════════════════════════════════════════════════════
# GENERADOR HTML
# ══════════════════════════════════════════════════════════════════════════════

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: #F0F2F5; color: #222; }
.page { max-width: 900px; margin: 0 auto; background: #fff; box-shadow: 0 2px 12px rgba(0,0,0,.15); }
.header { background: #1A2B4A; color: #fff; padding: 36px 40px 28px; }
.header h1 { font-size: 22px; font-weight: 700; letter-spacing: .5px; margin-bottom: 6px; }
.header .sub { font-size: 14px; color: #A8B8D0; }
.header .fecha { font-size: 12px; color: #7A90B0; margin-top: 4px; }
.body { padding: 32px 40px; }
.section { margin-bottom: 28px; border-radius: 8px; border: 1px solid #E5E8EE; overflow: hidden; }
.section-title { background: #1A2B4A; color: #fff; padding: 10px 18px; font-size: 14px; font-weight: 700; letter-spacing: .3px; }
.section-body { padding: 14px 18px; }
.bloque-label { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; margin: 10px 0 6px; }
.label-positivo { color: #1A7A3C; }
.label-mejorar  { color: #C0392B; }
ul.bullets { margin-left: 18px; }
ul.bullets li { font-size: 13px; margin-bottom: 4px; line-height: 1.5; }
.sin-datos { color: #888; font-style: italic; font-size: 13px; }
/* Tabla ICC */
.tbl-icc { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.tbl-icc th { background: #1A2B4A; color: #fff; padding: 7px 10px; text-align: left; font-weight: 600; }
.tbl-icc td { padding: 6px 10px; border-bottom: 1px solid #EEE; vertical-align: top; }
.tbl-icc tr:last-child td { border-bottom: none; }
.tbl-icc tr:nth-child(even) td { background: #F9FAFB; }
.badge { display: inline-block; border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 700; }
.badge-pos  { background: #D4EDDA; color: #1A7A3C; }
.badge-mej  { background: #FADBD8; color: #C0392B; }
.badge-top  { background: #FFD700; color: #333; }
.badge-mod  { background: #E8ECF5; color: #1A2B4A; font-size: 11px; }
/* Tabla tareas */
.tbl-tareas { width: 100%; border-collapse: collapse; font-size: 12.5px; margin-top: 6px; }
.tbl-tareas th { background: #1A2B4A; color: #fff; padding: 8px 12px; text-align: left; }
.tbl-tareas td { padding: 7px 12px; border-bottom: 1px solid #EEE; vertical-align: top; }
.tbl-tareas tr:nth-child(even) td { background: #F5F5F5; }
"""

def estado_badge(estado):
    if estado == "positivo":
        return '<span class="badge badge-pos">Positivo</span>'
    if estado == "mejorar":
        return '<span class="badge badge-mej">Mejorar</span>'
    return ""

def render_bullets_html(bullets, bloque_class):
    """Renderiza bullets de una sección como tabla ICC o lista."""
    rows_icc = []     # (ind, val, media, top20, comt)
    rows_text = []    # texto plano
    icc_mod_header = None

    for txt in bullets:
        parsed = parse_icc_bullet(txt)
        if parsed:
            rows_icc.append(parsed)
        else:
            mod = parse_icc_module_header(txt)
            if mod:
                icc_mod_header = mod
            else:
                rows_text.append(txt)

    html = ""

    # Cabecera de módulo ICC
    if icc_mod_header:
        mod, pos, tot, pts = icc_mod_header
        pts_str = f" | Puntuación: {pts}" if pts else ""
        html += f'<p class="badge badge-mod" style="margin-bottom:8px;">ICC Módulo {mod} — Posición {pos} de {tot}{pts_str}</p>\n'

    # Tabla ICC
    if rows_icc:
        html += '<table class="tbl-icc"><thead><tr>'
        html += '<th>Indicador</th><th>Valor</th><th>Media red</th><th>Top 20</th><th>Estado</th>'
        html += '</tr></thead><tbody>\n'
        for ind, val, media, top20, comt in rows_icc:
            top20_cell = f'<span class="badge badge-top">{top20}</span>' if top20 else ""
            est_badge = estado_badge(bloque_class)
            html += f"<tr><td>{ind}</td><td>{val}</td><td>{media}</td><td>{top20_cell}</td><td>{est_badge}</td></tr>\n"
        html += "</tbody></table>\n"

    # Bullets de texto
    if rows_text:
        html += '<ul class="bullets">\n'
        for t in rows_text:
            html += f"<li>{t}</li>\n"
        html += "</ul>\n"

    return html


def gen_html(meta, sections, tabla_tareas, output_path):
    titulo   = meta["titulo"]
    subtitulo = meta["subtitulo"]
    fecha    = meta["fecha"]

    lines = [
        "<!DOCTYPE html>",
        '<html lang="es"><head>',
        '<meta charset="UTF-8">',
        f'<title>{titulo}</title>',
        f'<style>{CSS}</style>',
        "</head><body>",
        '<div class="page">',
        '<div class="header">',
        f'<h1>{titulo}</h1>',
        f'<div class="sub">{subtitulo}</div>',
        f'<div class="fecha">{fecha}</div>',
        "</div>",  # header
        '<div class="body">',
    ]

    for sec in sections:
        nombre = sec["nombre"]
        positivos = sec.get("positivo", [])
        mejoras   = sec.get("mejorar", [])
        sin_datos = sec.get("sin_datos", False)

        lines.append('<div class="section">')
        lines.append(f'<div class="section-title">{nombre}</div>')
        lines.append('<div class="section-body">')

        if nombre == "Tareas pendientes" and tabla_tareas:
            lines.append('<table class="tbl-tareas"><thead><tr>')
            for col in tabla_tareas[0]:
                lines.append(f"<th>{col}</th>")
            lines.append("</tr></thead><tbody>")
            for fila in tabla_tareas[1:]:
                lines.append("<tr>")
                for celda in fila:
                    lines.append(f"<td>{celda}</td>")
                lines.append("</tr>")
            lines.append("</tbody></table>")
        else:
            if not positivos and not mejoras:
                lines.append('<p class="sin-datos">Sin datos registrados</p>')
            else:
                if positivos:
                    lines.append('<p class="bloque-label label-positivo">Puntos positivos</p>')
                    lines.append(render_bullets_html(positivos, "positivo"))
                if mejoras:
                    lines.append('<p class="bloque-label label-mejorar">Puntos a mejorar</p>')
                    lines.append(render_bullets_html(mejoras, "mejorar"))

        lines.append("</div>")  # section-body
        lines.append("</div>")  # section

    lines.append("</div>")  # body
    lines.append("</div>")  # page
    lines.append("</body></html>")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════════════════════════
# GENERADOR EXCEL
# ══════════════════════════════════════════════════════════════════════════════

FILL_HEADER  = PatternFill("solid", fgColor="1A2B4A")
FILL_SEC_HDR = PatternFill("solid", fgColor="1A2B4A")
FILL_TBL_HDR = PatternFill("solid", fgColor="2C3E6B")
FILL_POS     = PatternFill("solid", fgColor="D4EDDA")
FILL_MEJ     = PatternFill("solid", fgColor="FADBD8")
FILL_TOP     = PatternFill("solid", fgColor="FFD700")
FILL_ALT     = PatternFill("solid", fgColor="F9FAFB")
FILL_EMPTY   = PatternFill("solid", fgColor="F5F5F5")

FONT_WHITE_BOLD = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
FONT_WHITE      = Font(name="Calibri", color="FFFFFF", size=10)
FONT_DARK_BOLD  = Font(name="Calibri", bold=True, color="1A2B4A", size=10)
FONT_DARK       = Font(name="Calibri", color="222222", size=10)
FONT_POS        = Font(name="Calibri", bold=True, color="1A7A3C", size=10)
FONT_MEJ        = Font(name="Calibri", bold=True, color="C0392B", size=10)
FONT_ITALIC     = Font(name="Calibri", italic=True, color="888888", size=10)

THIN  = Side(border_style="thin",   color="DDDDDD")
THICK = Side(border_style="medium", color="AAAAAA")
BORDER_THIN = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

def xl_write(ws, row, col, value, fill=None, font=None, align=None, border=None, wrap=False):
    c = ws.cell(row=row, column=col, value=value)
    if fill:   c.fill = fill
    if font:   c.font = font
    if align:  c.alignment = align
    if border: c.border = border
    if wrap:   c.alignment = Alignment(wrap_text=True, vertical="top")
    return c

def xl_merge_write(ws, row, col1, col2, value, fill=None, font=None):
    ws.merge_cells(start_row=row, start_column=col1, end_row=row, end_column=col2)
    c = ws.cell(row=row, column=col1, value=value)
    if fill: c.fill = fill
    if font: c.font = font
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    return c

NCOLS = 6  # A:num B:indicador C:valor D:media E:top20 F:estado

def gen_excel(meta, sections, tabla_tareas, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Informe"

    # Anchos
    ws.column_dimensions["A"].width = 4
    ws.column_dimensions["B"].width = 40
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["D"].width = 16
    ws.column_dimensions["E"].width = 14
    ws.column_dimensions["F"].width = 14

    row = 1

    # Cabecera
    ws.row_dimensions[row].height = 30
    xl_merge_write(ws, row, 1, NCOLS, meta["titulo"], fill=FILL_HEADER,
                   font=Font(name="Calibri", bold=True, color="FFFFFF", size=14))
    row += 1

    ws.row_dimensions[row].height = 18
    xl_merge_write(ws, row, 1, NCOLS, meta["subtitulo"], fill=FILL_HEADER,
                   font=Font(name="Calibri", color="A8B8D0", size=11))
    row += 1

    ws.row_dimensions[row].height = 16
    xl_merge_write(ws, row, 1, NCOLS, meta["fecha"], fill=FILL_HEADER,
                   font=Font(name="Calibri", color="7A90B0", size=10))
    row += 1
    row += 1  # espacio

    sec_num = 0
    for sec in sections:
        nombre    = sec["nombre"]
        positivos = sec.get("positivo", [])
        mejoras   = sec.get("mejorar", [])
        sin_datos = sec.get("sin_datos", False)
        sec_num += 1

        # Título sección
        ws.row_dimensions[row].height = 20
        xl_merge_write(ws, row, 1, NCOLS, f"{sec_num}. {nombre}",
                       fill=FILL_SEC_HDR,
                       font=Font(name="Calibri", bold=True, color="FFFFFF", size=11))
        row += 1

        if nombre == "Tareas pendientes" and tabla_tareas:
            # Cabecera tabla
            ws.row_dimensions[row].height = 18
            cols_t = tabla_tareas[0]
            for ci, col_name in enumerate(cols_t):
                xl_write(ws, row, ci + 1, col_name, fill=FILL_TBL_HDR,
                         font=FONT_WHITE_BOLD, border=BORDER_THIN,
                         align=Alignment(horizontal="center", vertical="center"))
            row += 1
            for fi, fila in enumerate(tabla_tareas[1:]):
                ws.row_dimensions[row].height = 30
                fill_row = FILL_ALT if fi % 2 == 1 else None
                for ci, celda in enumerate(fila):
                    xl_write(ws, row, ci + 1, celda, fill=fill_row,
                             font=FONT_DARK, border=BORDER_THIN, wrap=True)
                row += 1
        elif not positivos and not mejoras:
            ws.row_dimensions[row].height = 16
            xl_merge_write(ws, row, 1, NCOLS, "Sin datos registrados",
                           font=FONT_ITALIC)
            row += 1
        else:
            for bloque_key, bloque_name, bloque_font, bloque_fill in [
                ("positivo", "Puntos positivos", FONT_POS, FILL_POS),
                ("mejorar",  "Puntos a mejorar", FONT_MEJ, FILL_MEJ),
            ]:
                bullets = sec.get(bloque_key, [])
                if not bullets:
                    continue

                # Etiqueta bloque
                ws.row_dimensions[row].height = 16
                xl_merge_write(ws, row, 1, NCOLS, bloque_name.upper(),
                               font=bloque_font)
                row += 1

                # Separar ICC module header, ICC bullets, texto
                rows_icc = []
                icc_header = None
                text_bullets = []

                for txt in bullets:
                    parsed = parse_icc_bullet(txt)
                    if parsed:
                        rows_icc.append(parsed)
                    else:
                        mod = parse_icc_module_header(txt)
                        if mod:
                            icc_header = mod
                        else:
                            text_bullets.append(txt)

                if icc_header:
                    mod, pos, tot, pts = icc_header
                    pts_str = f" | Puntuación: {pts}" if pts else ""
                    ws.row_dimensions[row].height = 16
                    xl_merge_write(ws, row, 1, NCOLS,
                                   f"ICC Módulo {mod} — Posición {pos} de {tot}{pts_str}",
                                   fill=PatternFill("solid", fgColor="E8ECF5"),
                                   font=Font(name="Calibri", bold=True, color="1A2B4A", size=10))
                    row += 1

                if rows_icc:
                    # Cabecera tabla ICC
                    ws.row_dimensions[row].height = 16
                    for ci, hdr in enumerate(["#", "Indicador", "Valor", "Media red", "Top 20", "Estado"], 1):
                        xl_write(ws, row, ci, hdr, fill=FILL_TBL_HDR,
                                 font=FONT_WHITE_BOLD, border=BORDER_THIN,
                                 align=Alignment(horizontal="center", vertical="center"))
                    row += 1

                    for ri, (ind, val, media, top20, comt) in enumerate(rows_icc):
                        ws.row_dimensions[row].height = 28
                        fill_row = FILL_ALT if ri % 2 == 1 else None
                        xl_write(ws, row, 1, ri + 1, fill=fill_row,
                                 font=FONT_DARK, border=BORDER_THIN,
                                 align=Alignment(horizontal="center", vertical="top"))
                        xl_write(ws, row, 2, ind, fill=fill_row,
                                 font=FONT_DARK, border=BORDER_THIN, wrap=True)
                        xl_write(ws, row, 3, val, fill=fill_row,
                                 font=FONT_DARK, border=BORDER_THIN, wrap=True)
                        xl_write(ws, row, 4, media, fill=fill_row,
                                 font=FONT_DARK, border=BORDER_THIN, wrap=True)
                        top20_val = top20 if top20 else ""
                        xl_write(ws, row, 5, top20_val,
                                 fill=FILL_TOP if top20 else fill_row,
                                 font=Font(name="Calibri", bold=True, color="333333", size=10) if top20 else FONT_DARK,
                                 border=BORDER_THIN,
                                 align=Alignment(horizontal="center", vertical="top"))
                        if bloque_key == "positivo":
                            xl_write(ws, row, 6, "Positivo", fill=FILL_POS,
                                     font=FONT_POS, border=BORDER_THIN,
                                     align=Alignment(horizontal="center", vertical="top"))
                        else:
                            xl_write(ws, row, 6, "Mejorar", fill=FILL_MEJ,
                                     font=FONT_MEJ, border=BORDER_THIN,
                                     align=Alignment(horizontal="center", vertical="top"))
                        row += 1

                if text_bullets:
                    for ti, txt in enumerate(text_bullets):
                        ws.row_dimensions[row].height = 28
                        fill_row = FILL_ALT if ti % 2 == 1 else None
                        xl_write(ws, row, 1, "•", fill=fill_row, font=FONT_DARK,
                                 align=Alignment(horizontal="center", vertical="top"))
                        c = ws.cell(row=row, column=2, value=txt)
                        c.fill = fill_row or PatternFill()
                        c.font = FONT_DARK
                        c.alignment = Alignment(wrap_text=True, vertical="top")
                        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=NCOLS)
                        row += 1

        row += 1  # espacio entre secciones

    wb.save(output_path)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    pattern = os.path.join(base, "informe_seguimiento_*.docx")
    files = sorted(glob.glob(pattern))

    # Excluir CEX y archivos temporales
    files = [f for f in files if
             not os.path.basename(f).startswith("~") and
             "_CEX_" not in os.path.basename(f)]

    print(f"Encontrados {len(files)} informes Word.\n")

    ok = 0
    errors = []

    for docx_path in files:
        name = os.path.splitext(os.path.basename(docx_path))[0]
        html_path  = os.path.join(base, name + ".html")
        excel_path = os.path.join(base, name + ".xlsx")

        try:
            meta, sections, tabla_tareas = parse_word(docx_path)
            gen_html(meta, sections, tabla_tareas, html_path)
            gen_excel(meta, sections, tabla_tareas, excel_path)
            print(f"  OK  {name}")
            ok += 1
        except Exception as e:
            print(f"  ERR {name}: {e}")
            errors.append((name, str(e)))

    print(f"\nGenerados: {ok}/{len(files)}")
    if errors:
        print("\nErrores:")
        for n, e in errors:
            print(f"  {n}: {e}")


if __name__ == "__main__":
    main()
