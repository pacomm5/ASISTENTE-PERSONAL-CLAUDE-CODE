---
title: Captura rápida
type: inbox
tags:
  - inbox
created: 2026-04-05
updated: 2026-04-05
---

# Captura rápida

Esta es la zona de entrada. Todo lo que aparece y no tienes tiempo de clasificar va aquí: ideas, tareas, referencias, observaciones, pendientes.

**Reglas:**
- Captura rápido, sin estructura
- No te preocupes por el formato
- Vacía esto en cada revisión (diaria o semanal)
- Cada elemento clasificado se mueve a su lugar y se elimina de aquí

---

## Entradas sin procesar

_(Añade aquí lo que vaya apareciendo. Vacía esto regularmente.)_

- Bienvenido al sistema. Este es tu punto de entrada. [[Sistema/Flujo de captura y procesado|Ver cómo procesarlo.]]
- preparacion cita3 es el excel para preparar la cita (esta en datos maestros) contraseña desgaste. luego tengo un script para analizar potenciales se llama PREPARARCITA se abre con visual studio code. la carpeta es PREPARARCITA y el cuaderno se llama igual. esta dentro de presentacion segmentacion
- Afianzar el informe de seguimiento para todo el personal
	- El mes que viene solo tienes que decirme "genera los informes de seguimiento de abril" y yo leo el SOP, leo los rankings del vault del periodo anterior para comparar, y ejecuto. Si me pasas los nuevos rankings antes, mejor; si no, te lo pido.
	- Sí. El flujo será:

		1. Me pasas los rankings actualizados (Desgaste Asesores, Desgaste Instalaciones, Iron Man Asesores, Iron Man Jefes de Taller, ICC Instalaciones)
		2. Los guardo en el vault como archivos de referencia con el nuevo periodo (por ejemplo `- 2026-04.md`)
		3. Genero todos los informes Word con los datos nuevos, mostrando la evolución respecto a los de marzo donde corresponda
		4. La tarea "Utilizar el Laser de desgaste" va incluida de serie en todos los informes
	1. Sí. El flujo está completamente documentado en el SKILL.md y el SOP, y las reglas clave están en la memoria persistente.

	Lo único que necesitaré el mes que viene es que me pases los rankings nuevos (tal como indica el SOP Paso 1): los 5 rankings mensuales + los 2 rankings ONE de la semana de referencia. Con eso:

	1. Los guardo en el vault
	2. Leo los informes de marzo para arrastrar las tareas con Grado de cumplimentación < 100%
	3. Genero los 30 informes con los datos nuevos, incluyendo la sección ONE clasificada con las medias recalculadas del nuevo periodo

	La única cosa que no puedo hacer solo es acceder al DMS o al sistema ONE directamente. Los datos los tienes que exportar tú.

	Lo único que necesito que me confirmes en ese momento es si hay cambios en el equipo (altas, bajas, cambios de instalación) o si quieres añadir alguna tarea nueva fija. El resto lo ejecuto directamente.
- posibles mecánico prácticas. 
	- tres en rivas audi

---

## Cómo procesar cada entrada

¿Qué es esto?

| Si es...                   | Va a...                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------- |
| Una tarea concreta         | Nota del proyecto o nota diaria                                                         |
| Un proyecto nuevo          | `Proyectos/` con [[Templates/Template - Proyecto\|Template - Proyecto]]                 |
| Conocimiento o aprendizaje | `Investigaciones/` con [[Templates/Template - Investigacion\|Template - Investigación]] |
| Una idea sin desarrollar   | `Ideas/` con [[Templates/Template - Idea\|Template - Idea]]                             |
| Un contacto relevante      | `Personas/` con [[Templates/Template - Persona\|Template - Persona]]                    |
| Referencia o documentación | `Recursos/`                                                                             |
| No vale nada ahora         | Eliminar                                                                                |
