# Vault de Obsidian — Paco

Este vault es el segundo cerebro de Paco, Director de Postventa en Jarmauto y desarrollador de PlayersHubs. Aquí se centraliza el conocimiento personal y profesional: notas de trabajo, proyectos, referencias, ideas y diario.

---

## Contexto personal

**Quién es Paco:**
- Director de Postventa en Jarmauto (concesionario Audi, Volkswagen y Volkswagen Industriales)
- Desarrollador de PlayersHubs: app de deportes para organizar quedadas de fútbol, gestionar equipos y conectar jugadores
- Familia: mujer e hijo
- Zona horaria: Europe/Madrid (CET/CEST)
- Perfil tecnológico avanzado: Python, VS Code, Google Cloud, Railway, OpenAI/Gemini/Claude Code
- Apasionado del Machine Learning y la Inteligencia Artificial aplicada al negocio y la productividad

**Jarmauto — datos clave:**

| Indicador | Dato |
|---|---|
| Marcas | Audi, Volkswagen, Volkswagen Industriales |
| Instalaciones | 6 |
| Entradas diarias de vehículos | ~120 |
| Facturación recambios (anual) | ~11 M€ |
| Facturación mano de obra (anual) | ~8 M€ |
| Personas en postventa | 150 |

**Equipo:**
- 150 personas: asesores de servicio, mecánicos, técnicos de chapa y pintura, personal de recambios
- Punto de dolor principal: adherencia a procedimientos
- Seguimiento activo: asesores de servicio con bajo rendimiento en ventas de desgaste (neumáticos, frenos)

**Herramientas del día a día:**
DMS Quiter · Power BI · Excel · Python/VS Code · Notion · Google Cloud · Railway · OpenAI/Gemini/Claude Code · Webs internas propias

---

## Prioridades y proyectos activos

| Proyecto / Foco | Estado | Fecha clave |
|---|---|---|
| Presentación Data Science ante sector automoción | En preparación | 22 abril 2026 |
| PlayersHubs — reconstrucción desde cero | En curso | Sin fecha fija |
| Campaña fidelización Q2 2026 (Jarmauto) | Activo | Q2 2026 |
| Asesores de servicio — ventas de desgaste | Seguimiento mensual | Continuo |

**Contexto de la presentación (22 abril):**
- Audiencia: ~100 personas del sector de automoción
- Rol esperado: experto en aplicación de datos e IA en postventa
- Pendiente: confirmar que Diego (ELO) envía la presentación para poder ensayarla
- Tono objetivo: natural y cercano, credibilidad de negocio + claridad técnica, sin jerga

---

## Propósito del vault

- Capturar y organizar el conocimiento de trabajo (Jarmauto, PlayersHubs)
- Servir como base de referencia para decisiones y proyectos
- Funcionar como diario y registro de aprendizajes

---

## Convenciones

### Nombres de archivo

- Diario: único archivo `Diario/Diario.md` (no hay archivos por fecha)
- Notas de proyecto: nombre descriptivo en minúsculas con guiones (ejemplo: `estrategia-postventa-q2.md`)
- Sin caracteres especiales en nombres de archivo

### Frontmatter

Toda nota debe incluir como mínimo:

```yaml
---
title: Título de la nota
date: AAAA-MM-DD
tags:
  - categoria
---
```

### Wikilinks

Usar siempre `[[wikilinks]]` para enlaces internos entre notas del vault. Reservar `[texto](url)` para URLs externas.

### Etiquetas

Jerarquía recomendada:

- `#jarmauto` — trabajo en el concesionario
- `#playershubs` — proyecto de la app
- `#ia` — inteligencia artificial y machine learning
- `#decision` — decisiones importantes
- `#referencia` — material de consulta
- `#diario` — notas del día a día

---

## Skills disponibles

Las skills están en `.claude/skills/` y se cargan automáticamente. Son instrucciones especializadas que Claude Code usa al trabajar con este vault.

| Skill | Cuándo se activa |
|---|---|
| `obsidian-markdown` | Al crear o editar notas `.md` con sintaxis Obsidian (wikilinks, callouts, embeds, propiedades) |
| `obsidian-bases` | Al trabajar con archivos `.base` para crear vistas de base de datos sobre las notas |
| `json-canvas` | Al crear o editar archivos `.canvas` (mapas visuales, diagramas, mind maps) |
| `obsidian-cli` | Al interactuar con el vault desde la terminal (leer, crear, buscar, gestionar tareas) |
| `defuddle` | Al extraer contenido limpio de una URL para guardarlo como nota |

---

## Estructura del vault

Estructura activa a fecha 2026-04-05:

```
/
├── CLAUDE.md                        — Este archivo (contexto para Claude Code)
├── INDEX.md                         — Índice general navegable
├── README.md                        — Descripción y flujos del vault
├── MOC - Inicio.md                  — Mapa maestro: foco diario, proyectos, áreas
├── MOC - Trabajo.md                 — Postventa, datos, automatizaciones
├── MOC - PlayersHubs.md             — Todo sobre el proyecto PlayersHubs
├── MOC - Aprendizaje.md             — Programación, herramientas, aprendizaje
├── MOC - Personal.md                — Mapa de notas personales
├── .claude/skills/                  — Skills de Claude Code (obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle)
├── Diario/                          — Diario único (Diario.md)
├── Proyectos/                       — Proyectos activos
│   ├── PlayersHubs.md
│   ├── Presentacion Data Science.md — Urgente: 22 abril 2026
│   └── Proyecto - Campana Fidelizacion Q2 2026.md
├── Areas/                           — Áreas estables de responsabilidad (una subcarpeta por área)
│   ├── Trabajo Postventa/
│   ├── Data y Automatizacion/
│   ├── Programacion/
│   ├── PlayersHubs/
│   ├── Aprendizaje/
│   └── Personal/
├── Investigaciones/                 — Análisis en profundidad
│   ├── Investigacion - Segmentacion RFM postventa.md
│   ├── Investigacion - Arquitectura Docker para apps.md
│   └── Investigacion - Obsidian y Claude Code.md
├── Ideas/                           — Ideas sin desarrollar
│   ├── Idea - Automatizacion avanzada de postventa.md
│   ├── Idea - Sistema de conocimiento personal con IA.md
│   └── Idea - Dashboard rendimiento postventa.md
├── Recursos/                        — Referencias reutilizables (guías, prompts, snippets, checklists)
│   └── README.md
├── PERSONAL/                        — Espacio personal (salud, trámites, viajes, familia)
│   ├── README.md
│   ├── Personal - Salud.md
│   ├── Personal - Tramites.md
│   └── Personal - Viajes.md
├── Personas/                        — Contactos clave
├── Inbox/                           — Captura rápida sin procesar
│   └── Captura rapida.md
├── Templates/                       — Plantillas reutilizables (8 templates)
├── Sistema/                         — Cómo funciona la bóveda (5 notas de sistema)
└── Archivos/                        — Lo que ya no está activo (no borrar, solo mover aquí)
```

---

## Cómo trabajar con Claude Code aquí

- Para crear una nota nueva: describe el contenido y Claude Code la estructura con el frontmatter correcto, wikilinks y callouts adecuados.
- Para crear un canvas visual: describe los nodos y relaciones, Claude Code genera el `.canvas` válido.
- Para crear una vista de base de datos: describe qué notas quieres ver y con qué filtros, Claude Code genera el `.base`.
- Para guardar contenido de una URL: proporciona la URL y Claude Code usa `defuddle` para extraerlo como markdown limpio.
- Para operar con el vault desde la terminal: Claude Code usará la `obsidian-cli` si Obsidian está abierto.

---

## Reglas generales

- No borrar notas: moverlas a `Archivos/` con la fecha si ya no están activas.
- Mantener el frontmatter completo en todas las notas.
- Priorizar wikilinks sobre texto plano para conectar ideas.
- Las notas de decisiones importantes deben llevar el tag `#decision` y una sección de razonamiento.
