---
title: Proyecto - Chatbot Dudas Técnicas
date: 2026-04-13
tags:
  - jarmauto
  - proyecto
  - ia
status: pendiente de arrancar
---

# Chatbot Dudas Técnicas

Chatbot interno con RAG (Retrieval-Augmented Generation) para resolver dudas técnicas en tiempo real. Actúa de forma diferente según el perfil del usuario que pregunta.

---

## Usuarios y modos de uso

| Perfil | Contexto | Cómo responde el chatbot |
|---|---|---|
| Call center | Está hablando con un cliente por teléfono | Lenguaje accesible, orientado a trasladar la información al cliente |
| Asesor de servicio | Necesita información técnica para gestionar la OR | Lenguaje técnico, orientado a la reparación |
| Técnico | Tiene una duda durante la reparación | Lenguaje técnico, detalle de procedimiento |

---

## Base de conocimiento (RAG)

| Fuente | Formato | Estado |
|---|---|---|
| Documentación técnica de reparaciones | PDF y HTML en carpetas | Disponible, pendiente de indexar |
| Comentarios del cliente en apertura de OT | Datos del DMS (Quiter/ONE) | Por definir cómo extraerlos |

---

## Decisiones técnicas pendientes

- [ ] Definir modelo de lenguaje (OpenAI, Claude, modelo local...)
- [ ] Definir stack del RAG (LangChain, LlamaIndex, otra solución...)
- [ ] Definir dónde se aloja (servidor propio de Jarmauto)
- [ ] Definir cómo se indexa la documentación técnica (PDF y HTML)
- [ ] Definir cómo se conecta con ONE/Quiter para obtener los comentarios de apertura de OR
- [ ] Definir la interfaz de usuario (web interna, integración en ONE, app...)

---

## Por qué se hace

- Los asesores y el call center pierden tiempo buscando información técnica dispersa en carpetas.
- La documentación existe pero no es accesible de forma rápida durante la atención al cliente o la reparación.
- Mejorar la calidad de la información que llega al cliente reduce reclamaciones y mejora la experiencia.

---

## Próximos pasos

- [ ] Inicio de investigación: semana del 20 de abril de 2026
- [ ] Decidir tecnología y arquitectura
- [ ] Inventariar la documentación técnica disponible (volumen, idiomas, formatos)
- [ ] Definir cómo se distingue el perfil del usuario (call center vs. técnico)
- [ ] Hacer una prueba de concepto con un subconjunto de documentación
