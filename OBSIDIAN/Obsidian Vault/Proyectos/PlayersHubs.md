---
title: PlayersHubs
type: project
status: activo
tags:
  - proyecto
  - playershubs
  - producto
created: 2026-04-05
updated: 2026-04-05
---

# PlayersHubs

## Visión

PlayersHubs es una plataforma digital para organizar partidos de fútbol amateur, gestionar equipos, conectar jugadores y construir comunidad en torno al deporte. El objetivo a largo plazo es crear el espacio de referencia para el fútbol no profesional: desde la quedada semanal hasta ligas organizadas entre amigos, equipos de empresa o comunidades locales.

Lo que distingue PlayersHubs de grupos de WhatsApp o soluciones improvisadas es la estructura: perfiles de jugadores, historial, reputación, y un sistema que reduce la fricción de organizar y mejora la experiencia de jugar.

---

## Qué problema resuelve

- Organizar partidos de fútbol es tedioso: confirmaciones por WhatsApp, listas en notas, cancelaciones de última hora
- No hay un lugar donde encontrar jugadores sueltos para completar un equipo
- Los equipos informales no tienen forma de estructurarse ni de seguir su evolución
- Los organizadores no tienen herramientas para gestionar sus grupos con comodidad
- La experiencia social alrededor del fútbol amateur está muy fragmentada

---

## Posibles líneas funcionales

### Creación y gestión de partidos
- Crear partidos con lugar, fecha, hora y número de jugadores
- Confirmar asistencia e invitar a contactos o jugadores de la plataforma
- Gestionar lista de espera y recordatorios automáticos
- Historial de partidos por jugador y por grupo

### Perfiles y reputación
- Perfil de jugador: posición, nivel, historial, estadísticas básicas
- Sistema de valoraciones entre jugadores (comportamiento, puntualidad, nivel)
- Evolución del perfil a lo largo del tiempo

### Gestión de equipos
- Crear y gestionar un equipo con sus miembros
- Alineaciones, estadísticas por equipo, partidos jugados
- Roles dentro del equipo (capitán, jugador, reserva)

### Búsqueda y comunidad
- Buscar jugadores sueltos para completar un partido
- Buscar partidos abiertos en tu zona
- Descubrir equipos que buscan jugadores

### Ligas y competiciones
- Crear ligas informales con clasificación, jornadas y resultados
- Generación automática de calendario
- Estadísticas de liga: goleadores, porteros menos goleados, asistencias

### Métricas y seguimiento
- Estadísticas personales: partidos jugados, goles, asistencias
- Evolución de nivel y reputación
- Comparativas entre jugadores del mismo equipo

### Contenidos (largo plazo)
- Resúmenes de partido generados automáticamente
- Análisis básico de rendimiento
- Posible integración con vídeo de partidos

---

## Parte técnica

### Frontend
- Framework: React (Next.js para SSR y SEO)
- UI: componentes propios o librería ligera (Tailwind CSS)
- Enfoque mobile-first: la mayoría del uso será desde el móvil

### Backend
- API REST (o GraphQL en fases avanzadas)
- Node.js o Python (FastAPI) — pendiente de decidir
- Autenticación: JWT + posible OAuth social (Google, Apple)
- Notificaciones: email + push (FCM)

### Base de datos
- PostgreSQL para datos relacionales (usuarios, partidos, equipos, ligas)
- Redis para caché de sesiones y datos de alta lectura
- Posible uso de PostGIS para búsquedas geolocalizada de partidos cercanos

### Arquitectura y despliegue
- Arquitectura basada en contenedores Docker
- Entorno de desarrollo reproducible con docker-compose
- Despliegue en Railway (initial) o VPS con Docker
- CI/CD: GitHub Actions

### Estado actual
La app se está rehaciendo desde cero. La arquitectura técnica está en definición.

---

## Decisiones

- `[2026-04-05]` Rehacer la app desde cero en lugar de parchear la versión anterior. Razonamiento: la base de código anterior tenía deuda técnica acumulada y no escalaba bien. Empezar limpio con arquitectura clara es más eficiente a largo plazo.

---

## Próximos pasos

- [ ] Definir y documentar la arquitectura técnica inicial
- [ ] Configurar entorno Docker con frontend, backend y base de datos
- [ ] Diseñar el modelo de datos para usuarios, partidos y equipos
- [ ] Implementar autenticación básica
- [ ] Crear primera versión funcional de creación y gestión de partidos
- [ ] Definir MVP mínimo y sus criterios de éxito

---

## Bloqueos

Ninguno activo. Proyecto en fase de arranque.

---

## Recursos relacionados

- [[Investigaciones/Investigacion - Arquitectura Docker para apps|Arquitectura Docker para apps]]
- [[Investigaciones/Investigacion - Obsidian y Claude Code|Obsidian y Claude Code]] — para documentar decisiones y aprendizajes durante el desarrollo

---

## Enlaces

- [[MOC - PlayersHubs]]
- [[Areas/PlayersHubs/Area - PlayersHubs|Area - PlayersHubs]]
- [[Ideas/Idea - Sistema de conocimiento personal con IA|Sistema de conocimiento personal con IA]]
