---
title: Investigación — Segmentación de clientes en postventa
type: research
status: completada
tags:
  - investigacion
  - segmentacion
  - postventa
  - datos
created: 2026-04-05
updated: 2026-04-05
---

# Segmentación de clientes en postventa

> Este archivo es un ejemplo de investigación bien estructurada. Está basado en un tema real y útil para el contexto de trabajo.

## Pregunta principal

¿Cómo segmentar la base de clientes de postventa para identificar oportunidades de fidelización, detección de fuga y comunicación personalizada?

---

## Contexto

El DMS Quiter contiene datos históricos de todos los clientes: visitas, facturación, tipo de trabajo, vehículo, antigüedad. Hasta ahora la comunicación es genérica. Esta investigación explora cómo usar esos datos para ser más precisos.

---

## Resumen

La segmentación RFM (Recencia, Frecuencia, Valor monetario) aplicada a los datos de postventa permite identificar con claridad qué clientes son de alto valor, cuáles están en riesgo de fuga y cuáles llevan demasiado tiempo sin visitar el taller. Cada segmento merece una estrategia de comunicación distinta.

---

## Hallazgos clave

- **La métrica más predictiva de fuga es la recencia.** Un cliente que lleva más de 12 meses sin pasar por el taller tiene una probabilidad alta de no volver sin una acción proactiva.

- **Los clientes de alto valor (top 20%) generan aproximadamente el 60-70% de la facturación de mano de obra.** Perder uno de ellos equivale a perder 5-10 clientes de valor medio.

- **La segmentación por tipo de trabajo (revisión oficial, reparación, neumáticos) permite personalizar la oferta.** No tiene sentido mandar una oferta de revisión a alguien que acaba de hacer la revisión.

- **El mejor momento para contactar es justo antes del vencimiento previsible del siguiente servicio.** Si alguien hace revisiones anuales, contactar a los 10-11 meses tiene mucha más tasa de conversión que una comunicación aleatoria.

---

## Implicaciones

- Se puede crear un sistema de scoring simple con Python sobre datos del DMS
- La comunicación personalizada por segmento requiere plantillas distintas pero se puede automatizar
- Los clientes en riesgo de fuga merecen una llamada personal, no un email automático
- Los datos de neumáticos permiten identificar la ventana estacional óptima para cada cliente

---

## Herramientas o fuentes

| Nombre | Tipo | Utilidad |
|---|---|---|
| DMS Quiter | Fuente de datos | Historial completo de visitas y facturación |
| Python (pandas) | Análisis | Transformación y segmentación |
| Power BI | Visualización | Dashboard de seguimiento de segmentos |
| Excel | Entrega | Listados para el equipo comercial |

---

## Ideas accionables

- [ ] Extraer datos del DMS con historial de los últimos 2 años
- [ ] Implementar scoring RFM básico en Python
- [ ] Crear dashboard en Power BI con los 4 segmentos principales
- [ ] Diseñar plantillas de comunicación para cada segmento

---

## Preguntas abiertas

- ¿Cuál es el umbral óptimo para considerar a un cliente "en riesgo"? ¿6 meses, 9, 12?
- ¿Tiene sentido incluir datos de ventas para enriquecer el perfil del cliente?
- ¿Cómo se automatiza la actualización mensual del scoring?

---

## Segmentos propuestos

| Segmento | Criterio | Acción |
|---|---|---|
| Clientes VIP | Alto valor + alta frecuencia + reciente | Trato preferente, comunicación proactiva |
| En riesgo | Alto valor + sin visita > 9 meses | Llamada personal, oferta especial |
| Regulares activos | Frecuencia media + reciente | Comunicación estándar, recordatorios automáticos |
| Durmientes | Sin visita > 18 meses | Campaña de reactivación o dar de baja |

---

## Enlaces relacionados

- [[Areas/Trabajo Postventa/Area - Trabajo Postventa|Area - Trabajo Postventa]]
- [[Areas/Data y Automatizacion/Area - Data y Automatizacion|Area - Data y Automatización]]
- [[Ideas/Idea - Automatizacion avanzada de postventa|Idea: Automatización avanzada de postventa]]
- [[MOC - Trabajo]]
