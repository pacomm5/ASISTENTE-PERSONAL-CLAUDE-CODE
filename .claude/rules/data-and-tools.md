# Datos y herramientas

## Stack de trabajo de Paco

- **DMS:** Quiter (sistema principal del concesionario, fuente de datos de negocio)
- **Reporting:** Power BI (accesible por todo el equipo)
- **Análisis:** Excel y Python (VS Code)
- **Cloud:** Google Cloud + Railway
- **IA:** OpenAI, Gemini, Claude Code
- **Organización:** Notion

## Cómo trabajar con datos

- Cuando Paco pida extraer, transformar o analizar datos, asumir que el destino habitual es Power BI o Excel.
- Los scripts de Python son la herramienta preferida para automatizaciones y procesamiento de datos.
- Si hay que conectar con una base de datos, Railway es el entorno habitual para proyectos propios (PlayersHubs).

## MCP / Integraciones

| Servidor MCP | Estado | Propósito |
|---|---|---|
| `mcp__notion__*` | Conectado | API oficial de Notion — leer y escribir páginas, bases de datos y bloques del workspace "Notion de Paco Martin" |
| `mcp__claude_ai_Notion__*` | Conectado | Integración nativa de Claude.ai con Notion |
| `mcp__google-calendar__*` | Conectado | Google Calendar vía `@cocal/google-calendar-mcp` — leer, crear, editar y borrar eventos en todos los calendarios de pacomm5@gmail.com |
