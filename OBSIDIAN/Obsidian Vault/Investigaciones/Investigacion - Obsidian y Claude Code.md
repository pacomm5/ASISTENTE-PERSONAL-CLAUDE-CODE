---
title: Investigación — Obsidian y Claude Code
type: research
status: en curso
tags:
  - investigacion
  - obsidian
  - claude-code
  - sistemas
created: 2026-04-05
updated: 2026-04-05
---

# Obsidian y Claude Code como sistema de conocimiento

## Pregunta principal

¿Cómo combinar Obsidian y Claude Code para construir un sistema de conocimiento y trabajo que sea útil en el día a día, no solo en teoría?

---

## Contexto

Este vault existe precisamente para responder a esta pregunta. La investigación documenta lo que se aprende sobre el flujo, las ventajas reales, los límites y las ideas de mejora a medida que el sistema evoluciona.

---

## Resumen

Obsidian actúa como el repositorio persistente: captura, organiza y conecta conocimiento que sobrevive entre conversaciones y proyectos. Claude Code actúa como el asistente activo: lee el contexto, ayuda a estructurar, genera contenido y ejecuta tareas. La combinación es potente cuando el contexto (archivos, CLAUDE.md) está bien definido.

---

## Hallazgos clave

- **El valor de Obsidian no está en las notas individuales, sino en las conexiones.** Un wikilink entre una investigación y un proyecto activo es más útil que la nota más completa sin conexiones.

- **Claude Code lee el contexto del CLAUDE.md y de los archivos que se le indican.** Cuanto mejor estructurado esté ese contexto, mejores serán las respuestas. El CLAUDE.md de este vault es el punto de partida.

- **Las skills de Obsidian instaladas en `.claude/skills/` dan a Claude Code instrucciones específicas** sobre cómo trabajar con wikilinks, callouts, propiedades, bases y canvas. Esto mejora la calidad del output sin necesidad de explicarlo cada vez.

- **La nota diaria es el pegamento del sistema.** Conecta el foco del día con proyectos, ideas y aprendizajes. Sin ella, el sistema tiende a ser reactivo.

- **La revisión semanal es lo que mantiene vivo el sistema.** Sin revisión, el inbox se acumula y los proyectos pierden vigencia.

---

## Cómo capturar prompts, decisiones y snippets útiles

- Los prompts que funcionan bien merecen guardarse en `Recursos/` para reutilizarlos
- Las decisiones técnicas tomadas con Claude Code deben documentarse en la nota del proyecto o área correspondiente, no solo quedar en el chat
- Los snippets de código útiles pueden ir a `Investigaciones/` o a `Recursos/` con contexto de cuándo y para qué usarlos

---

## Flujo práctico diario propuesto

1. Abrir la nota diaria (o crearla desde la plantilla)
2. Definir el foco del día y las 3 tareas clave
3. Trabajar con Claude Code en tareas concretas, documentando decisiones en sus notas
4. Al final del día: apuntar aprendizajes en la nota diaria
5. Si algo merece profundidad: crear una investigación o actualizar una existente

---

## Ventajas del sistema

- El conocimiento persiste entre conversaciones gracias a los archivos
- Claude Code puede orientarse rápidamente leyendo el CLAUDE.md y los archivos de contexto
- La combinación reduce la carga cognitiva: no hay que explicar el contexto desde cero cada vez
- Las skills de Obsidian mejoran la calidad del markdown generado

---

## Límites del sistema

- Claude Code no puede leer archivos que no se le proporcionen explícitamente
- El CLAUDE.md tiene un límite de tamaño útil: si crece demasiado, pierde efectividad
- La bóveda no es en tiempo real: los cambios en proyectos hay que actualizarlos manualmente
- No hay integración directa con herramientas externas (DMS, Power BI) sin MCP o scripts

---

## Ideas accionables

- [ ] Crear un flujo de captura de prompts útiles en `Recursos/Prompts utiles/`
- [ ] Documentar el uso de cada skill de Obsidian con un ejemplo real
- [ ] Explorar la posibilidad de conectar Claude Code con Notion via MCP cuando esté disponible

---

## Preguntas abiertas

- ¿Cómo gestionar el crecimiento de la bóveda sin que se vuelva difícil de navegar?
- ¿Tiene sentido automatizar la creación de notas diarias desde un script?
- ¿Qué partes del flujo se pueden delegar completamente a Claude Code?

---

## Herramientas o fuentes

| Nombre | Tipo | Utilidad |
|---|---|---|
| Obsidian | App | Sistema de notas y conocimiento |
| Claude Code | Asistente | Desarrollo y segundo cerebro |
| kepano/obsidian-skills | Repositorio | Skills para Claude Code específicas de Obsidian |
| CLAUDE.md | Archivo de contexto | Instrucciones para Claude Code en este vault |

---

## Enlaces relacionados

- [[Sistema/Como usar esta boveda|Cómo usar esta bóveda]]
- [[Ideas/Idea - Sistema de conocimiento personal con IA|Idea: Sistema de conocimiento personal con IA]]
- [[Areas/Programacion/Area - Programacion|Area - Programación]]
- [[MOC - Aprendizaje]]
