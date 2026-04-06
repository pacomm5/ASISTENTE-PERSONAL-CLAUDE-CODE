---
title: Presentación Data Science — Guion Oral
type: guion
status: en preparación
tags:
  - proyecto
  - trabajo
  - presentacion
  - guion
created: 2026-04-05
updated: 2026-04-05
fecha-limite: 2026-04-22
---

# Guion Oral — Presentación Data Science

Duración objetivo: 20 minutos
Slides: 15
Referencia: [[Proyectos/Presentacion Data Science]]

---

## Antes de salir al escenario

> [!tip] Reencuadre mental
> No pienses "voy a hablar delante de mucha gente".
> Piensa:
> "Voy a contar algo que ya hago todos los días."
> "No voy a impresionar. Voy a explicar algo que ya hago todos los días."
> "No soy el ponente. Soy el que sabe de esto."

Tienes negocio real, datos reales, visión y conexión con IA. Eso no lo tiene casi nadie junto en este tipo de charlas.

---

## Cuando te presenten o estés a punto de empezar

- Mira a 2-3 personas concretas, no a toda la sala.
- Empieza hablándoles a ellas.
- Tu cerebro lo convierte en conversación, no en exposición.

---

## Introducción — Las tres personalidades

"Yo siempre digo que tengo como tres personalidades en el trabajo.

Está el Paco friki… que le encantan los sistemas, el software… y automatizar todo lo que se mueve.

Luego está el Paco de datos… que es un obsesionado de los patrones, de buscar oportunidades… y que cada vez que oye la palabra 'potencial'… sabe que viene lío. Quien inventaría esta palabra, si alguna vez la escucháis, tened seguro que alguien va a sufrir…"

*(pequeña pausa, tono cómplice)*

"Y luego está el Paco director de posventa… que es el que tiene que hacer que todo eso funcione…
y que es el que sufre a los otros dos todos los días."

*(transición)*

"Y al final, lo interesante es que estos tres perfiles conviven en algo que todos tenemos en común…
que es cómo usamos el dato para tomar decisiones de verdad…
no en PowerPoint… sino en el día a día del taller."

---

## Slide 1 — El problema no es la falta de datos

"Quiero empezar con una idea muy simple: en postventa no nos faltan datos, nos falta conexión entre ellos. Trabajamos mucho, generamos actividad constantemente, pero ese esfuerzo no siempre se transforma en el resultado que realmente podríamos conseguir. Mi propuesta hoy es ver cómo la arquitectura de datos y el gobierno de procesos pueden convertir esa complejidad en ventaja competitiva."

---

## Slide 2 — La tormenta perfecta: entorno vs. gestión

"El entorno se ha vuelto mucho más exigente: más canales, más sistemas, más presión sobre la rentabilidad y clientes con expectativas más altas, y muchos más puntos de contacto. El problema es que muchas veces nuestros esquemas de gestión no han evolucionado al mismo ritmo. Y ahí aparece la brecha: no entre lo que queremos hacer y lo que hacemos, sino entre la complejidad que vivimos y nuestra capacidad real para ordenarla y decidir bien."

---

## Slide 3 — Abundancia de herramientas, escasez de lógica común

"La mayoría de organizaciones no tienen escasez de información; al contrario, tienen demasiadas piezas sueltas. DMS, CRM, agendas, históricos, encuestas… todo existe, pero no convive. Y cuando el dato no convive, no genera inteligencia.

Os pongo un ejemplo muy concreto: imagina que lanzamos hoy una campaña de descuento en pastillas de freno. Si los sistemas no conviven, ese descuento llega a un cliente al que le cambiamos las pastillas ayer. O peor: a un cliente que puso una reclamación ayer. Eso no es un fallo tecnológico. Es un fallo de estructura.

Por eso el problema no es tecnológico: es de estructura, de criterio y de gobierno. Cuando no hay lógica común, cada departamento termina trabajando en su propia realidad, y así es muy difícil alinear el negocio."

---

## Slide 4 — El coste de la desconexión

"Cuando los datos no están conectados, el esfuerzo operativo se fuga por muchas grietas invisibles. Aparecen duplicidades, interpretaciones distintas, trazabilidad incompleta y campañas que fallan no por falta de trabajo, sino por falta de conexión. En otras palabras: muchas pérdidas de negocio no vienen de hacer poco, sino de no hacer de forma coordinada."

---

## Slide 5 — Definición: arquitectura de datos

"Para mí, arquitectura de datos significa algo muy práctico: decidir cómo convertimos actividad en valor. La actividad genera datos, los datos solo valen si les damos contexto, y el contexto solo importa si desemboca en una decisión mejor. Es decir, no hablamos de almacenar información, sino de diseñar un sistema que transforme operación en negocio."

---

## Slide 6 — Gobierno no es burocracia

"Aquí conviene desmontar un mito: gobernar no es burocratizar. Gobierno no significa capas innecesarias ni rigidez administrativa; significa tener responsables claros, reglas de juego comunes y capacidad de mejora con criterio. Porque cuando no hay gobierno, cada equipo acaba construyendo su propia versión de la realidad, y así es imposible escalar."

---

## Slide 7 — El doble viaje: cliente y dato

"En postventa solemos mirar muy bien el viaje del cliente, pero no siempre miramos con la misma atención el viaje del dato. Cada cita, cada recepción, cada entrega, cada seguimiento deja una huella digital. Si no entendemos ambos viajes a la vez, la experiencia del cliente y la trazabilidad de la información, estamos viendo solo la mitad del negocio."

---

## Slide 8 — El análisis de brechas

"La eficiencia real de una organización no depende solo de cómo funciona cada pieza por separado, sino de cómo se conectan entre sí. Por eso las brechas críticas no suelen estar dentro de un área, sino entre áreas: entre marketing y recepción, entre la cita y la entrada real, o entre una operación realizada y la siguiente oportunidad comercial.

Un ejemplo muy práctico: cuando un cliente llama para saber cómo va su coche, o cuándo le van a entregar el vehículo, ¿quién puede responderle? Si la información de la reparación, del estado del taller y de la cita prometida está en un mismo sitio, cualquier persona de la empresa puede dar esa respuesta en tiempo y forma. Si no lo está, el cliente habla con tres personas y recibe tres respuestas distintas. Ahí se fuga la confianza, y con ella, la fidelidad."

---

## Slide 9 — El modelo de arquitectura de 4 capas

"Para ordenar todo esto, propongo un modelo de cuatro capas. Primero, las fuentes, hoy día casi todo es computable; después, la integración; encima, la lógica de negocio; y por último, la explotación en dashboards, campañas y CRM.

Un ejemplo del día a día: si tenemos actualizado el trabajo en curso en el taller, y además sabemos cuál es la capacidad productiva real de ese día, tenemos un dato muy sencillo pero muy valioso: cuándo es el día adecuado para dar la siguiente cita. No prometemos lo que no podemos cumplir, y no perdemos huecos por no tenerlos visibles. Eso es lo que hace una arquitectura bien construida: convertir operación en decisión."

---

## Slide 10 — La visión única: de registro a inteligencia

"El objetivo final es construir una visión única de cliente y vehículo. No solo un histórico, sino una lectura completa que combine frecuencia, momento de ciclo, valor de vida y riesgo de fuga.

En Jarmauto tenemos clasificados todos los clientes con el sistema RFM. Lo interesante no es solo tenerlo, sino que cuando un cliente llama, el call center sabe qué tipo de cliente es. Lo sabe el asesor, lo sabe el mecánico, lo sabe recambios. El grado de fidelidad es el mismo para marketing que para postventa. Todo el mundo trabaja con la misma verdad.

Y esto conecta con algo que creo que es clave: la visión única es al dato lo que la cultura es a una empresa. Si conviven verdades distintas, es muy difícil escalar. Muy difícil girar el volante y que la organización gire con él. Sin una visión única, cada área optimiza la suya, y el negocio pierde el conjunto."

---

## Slide 11 — La tecnología no sustituye al gobierno

"La tecnología es importante, pero no sustituye el orden, no hace milagros. Hace falta alguien que defina reglas, valide calidad, corrija desviaciones y asegure coherencia: en definitiva, un dueño del proceso. Porque la tecnología amplifica lo que ya somos; si tenemos orden, lo multiplica, y si tenemos desorden, también."

---

## Slide 12 — Impacto en negocio: el ROI

"Todo esto no es un ejercicio teórico, tiene un impacto directo en negocio. El salto es pasar de una postventa reactiva a una que anticipa.

Un ejemplo concreto: cuando tenemos la ficha de cliente actualizada, con su historial completo de servicios, sabemos cuándo cambió las pastillas, cuándo fue el último mantenimiento, si tiene neumáticos próximos a cambio. Con eso podemos hacer marketing predictivo: sabemos qué va a necesitar ese cliente antes de que él lo sepa. Y además podemos medir el potencial de cada visita: qué hay activable, qué está dormido. Eso transforma una visita de mantenimiento en una oportunidad de negocio gestionada. No en una casualidad. Estamos hablando de palancas del negocio."

---

## Slide 13 — Nuevos KPIs: medir la salud

"Normalmente medimos muy bien el resultado final: facturación, conversión, volumen. Pero si solo miramos eso, estamos llegando tarde. Las organizaciones maduras también miden la salud del sistema que produce ese resultado: calidad del dato, completitud, trazabilidad y consistencia. Porque si el sistema está enfermo, el resultado acabará resintiéndose."

---

## Slide 14 — Hoja de ruta: empezar con foco

"La transformación no empieza intentando arreglarlo todo a la vez. Empieza con foco: elegir procesos críticos, identificar puntos de fricción, construir un modelo mínimo común y, solo después, escalar. La credibilidad del cambio no la da el discurso; la da demostrar, en pequeño primero, que el modelo funciona y genera resultado."

---

## Slide 15 — Cierre / manifiesto final

"Y cierro con esta idea: la postventa no necesita solo más datos; necesita datos conectados a procesos bien gobernados. Porque cuando la información está bien estructurada, se convierte en decisión; la decisión mejora el proceso; y el proceso mejora el resultado. En ese punto, la organización deja de reaccionar y empieza a anticipar."

---

## Notas de ensayo

- Los slides 3, 10 y 12 son los más cargados de contenido: practicarlos primero.
- El ejemplo de las pastillas (slide 3) y el RFM (slide 10) son los que más van a resonar con la audiencia.
- Permitir silencio después de la frase del manifiesto final. No añadir nada después.
- La intro de las tres personalidades marca el tono de toda la charla: si sale natural, el resto fluye.
