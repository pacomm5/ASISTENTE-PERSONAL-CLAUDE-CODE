---
title: SOP — Informes de Seguimiento Mensual
type: sop
tags:
  - jarmauto
  - informes
  - seguimiento
  - sop
created: 2026-04-06
updated: 2026-04-06
---

# SOP: Generación de Informes de Seguimiento Mensual

Este documento describe el proceso completo para generar los informes de seguimiento mensuales de asesores de servicio y jefes de taller en Jarmauto.

---

## Cuándo ejecutarlo

Una vez al mes, después de tener los datos cerrados del periodo anterior.

---

## Paso 1 — Rankigs que hay que pasar a Claude

Pasar los siguientes rankings en este orden:

| Ranking | Quién afecta | Dónde se guarda en el vault |
|---|---|---|
| Ranking Desgaste Asesores | 18 asesores activos | `Areas/Trabajo Postventa/Ranking Desgaste Asesores - AAAA-MM.md` |
| Ranking Desgaste Instalaciones | 7 instalaciones mecánica | `Areas/Trabajo Postventa/Ranking Desgaste Instalaciones - AAAA-MM.md` |
| Ranking Iron Man Asesores | 18 asesores activos | `Areas/Trabajo Postventa/Ranking Iron Man Asesores - AAAA-MM.md` |
| Ranking Iron Man Jefes Taller | 11 instalaciones | `Areas/Trabajo Postventa/Ranking Iron Man Jefes Taller - AAAA-MM.md` |
| Ranking ICC Instalaciones | 8 instalaciones (incluye Industriales) | `Areas/Trabajo Postventa/Ranking ICC Instalaciones - AAAA-MM.md` |

Claude guardará cada ranking en el vault antes de generar los informes.

---

## Paso 2 — Informar de cambios en el equipo

Antes de generar, confirmar si hay:
- Nuevas incorporaciones
- Bajas
- Cambios de instalación

Si no hay cambios, decir "sin cambios en el equipo".

---

## Paso 3 — Tareas pendientes del mes anterior

Revisar los informes del mes anterior. La tabla de tareas pendientes tiene una columna "Grado de cumplimentación".

- Tareas con **Grado de cumplimentación < 100%** (o vacío) → Claude las arrastra automáticamente al nuevo informe.
- Tareas con **Grado de cumplimentación = 100%** → completadas, no se incluyen en el nuevo informe.

Si es la primera vez, este paso no aplica.

---

## Paso 4 — Ejecutar

Decir: **"Genera los informes de seguimiento de [periodo]"**

Claude generará:
- 18 informes de asesores de servicio
- 11 informes de jefes de taller (instalaciones)
- 1 informe de Fernando Industriales (solo ICC)

Total: 30 archivos `.docx` en `/Users/franciscomartin/Documents/ASISTENTE PERSONAL DE CLAUDE CODE/informes/`

---

## Estructura de los informes

### Asesores de servicio

| Sección | Fuente de datos |
|---|---|
| Proactividad comercial | Ranking Desgaste Asesores + Iron Man (Full/Long Drive + Fidelidad) |
| Digital | Sin datos salvo que se aporten |
| Calidad | Iron Man CAL1SEM |
| Procesos | Sin datos salvo que se aporten |
| Recursos generales | Sin datos salvo que se aporten |
| Horch Lauden | Iron Man Horch Lauden |
| Tareas pendientes | Arrastradas del periodo anterior si no tienen check |

### Jefes de taller

| Sección | Fuente de datos |
|---|---|
| Proactividad comercial | Ranking Desgaste Instalaciones + Iron Man Var Rec/MO + ICC módulo Proactividad |
| Digital | ICC módulo Digital |
| Calidad | Iron Man CAL1SEM + ICC módulo Calidad |
| Procesos | Iron Man Productividad vs objetivo |
| Recursos generales | ICC módulo Recursos Generales |
| Carrocería | ICC módulo Carrocería |
| Personas | ICC módulo Personas |
| Rankings de marca | Posición global ICC + Iron Man ICC puesto + Horch Lauden |
| Tareas pendientes | Arrastradas del periodo anterior si no tienen check |

---

## Instalaciones y responsables

### Asesores activos (18)

Guillermo, Alvaro, Estefanía, Magán, Javier Díaz Mesa, Alberto Martínez, José María Vázquez, Taboada (DMS: EUGENIO T.), Alejandro, Javier Pina (DMS: F.J. RODRIGUEZ), Juan, Raúl Muñoz, José María, Carlos Aguilar (DMS: CARLOS AYALA), Alex Codru, Dennis, Jon (DMS: JON2), Nuria.

JORGE no trabaja en la empresa, no generar informe.

### Instalaciones (12 informes)

| Instalación | Jefe | Tipo | Objetivo Productividad | Código ICC |
|---|---|---|---|---|
| Rivas Audi | Emilio | Mecánica | 93% | 51AQ1 AU |
| Rivas Audi Chapa | Luis Ramos | Chapa | 120% | 51AQ1 AU |
| Moncloa VW | José María Campos | Mecánica | 93% | 31523 VW |
| Moncloa Audi | José María Campos | Mecánica | 93% | 31523 AU |
| Ayala | Alberto Martínez | Ayala | 105% | 51AQ2 AU |
| Vara | Carlos | Mecánica | 93% | 0311Q VW |
| Canarias | Izquierdo | Mecánica | 93% | 51AQ3 AU |
| Canarias Chapa | Pericles | Chapa | 120% | 51AQ3 AU |
| Rivas VW | Fernando | Rivas VW | 89% | 30070 VW |
| Rivas VW Chapa | Luis Ramos | Chapa | 120% | 30070 VW |
| Vara Chapa | Pericles | Chapa | 120% | 0311Q VW |
| Industriales | Fernando | Solo ICC | — | 30070 LCV |

---

## Notas importantes

- Ejecutable Python: `/opt/homebrew/bin/python3` (no usar el de sistema)
- Parabrisas 0% en Moncloa VW, Ayala y Moncloa Audi es normal (lunas en talleres de carrocería)
- Las instalaciones de chapa no tienen desgaste propio en Proactividad comercial
- Industriales solo tiene datos ICC, sin Iron Man
- Los datos ICC de una instalación aplican tanto al informe de mecánica como al de chapa de esa misma instalación
