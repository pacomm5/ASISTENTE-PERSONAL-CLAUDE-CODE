# SOP: Actualización mensual de datos

**Frecuencia:** Día 1 de cada mes
**Entorno:** Google Colab + Google Drive + OneDrive local
**Antes de empezar:** Busca la palabra `REVISAR` en el script principal y actualiza las fechas y rangos (especialmente el del RFM).

---

## Paso 1 — Archivo U239 (Fidelidad / base principal)

**Origen:** Archivo local `U239_IMPORTADO.xlsx`
**Ubicación:** Machine Learning (local), sincronizado en Google Drive

1. Actualizar el archivo `U239_IMPORTADO.xlsx` en el ordenador antes de ejecutar nada.
2. En el script, se carga así:
   ```python
   xlsx = pd.ExcelFile("/content/U239_IMPORTADO.xlsx")
   df_U239 = pd.read_excel(xlsx, "U239_IMPORTADO")
   ```
3. El archivo está guardado en Google Drive para evitar cargarlo manualmente cada vez.

---

## Paso 2 — Recambios

**Listado de Quiter:** `U5701298`
**Archivo base:** `recambios_2022.xlsx` (con datos hasta diciembre 2022)

1. En Quiter, sacar el listado `U5701298` y guardarlo como **archivo con separadores** (TXT).
2. Abrir el Excel `recambios_2022` e importar el TXT generado. Nombrar la pestaña con el nombre del mes.
3. Los archivos históricos ya están guardados como pickle y se cargan directamente:
   ```python
   total_recambios_final_2022 = pd.read_pickle("/content/drive/MyDrive/Colab Notebooks/total_recambios_final_2022_pickle")
   total_recambios_2023 = pd.read_pickle("/content/drive/MyDrive/Colab Notebooks/total_recambios_2023_pickle")
   ```

---

## Paso 3 — Piloto Telemarketing

**Listado de Quiter:** `U5661298`
**Carpeta local:** `Documentos/2022/Piloto Telemarketing/`

1. Sacar el listado `U5661298` del mes en Quiter. Guardarlo en la carpeta `piloto_telemarketing` como `base_datos`.
2. Abrir `base_datos_piloto_1` (en `2022/Piloto Telemarketing/`) y actualizar con los nuevos datos.
3. Copiar los datos en la pestaña `base_piloto_2` y actualizar la consulta dentro de esa misma pestaña.
4. Abrir `consulta_pilot_call` del mismo directorio y actualizar.
5. Actualizar `IMP_BASE_PILOTO_2` en Machine Learning:
   - Ruta: `/content/onedrive/Documentos/2018/POWER BI INFORMES/DATOS MAESTROS/MACHINE LEARNING/IMP_BASE_PILOTO_2.xlsx`
   - Siempre actualizar en local antes de importar en Colab.

---

## Paso 4 — Datos del conductor

**Listado de Quiter:** `U5891298`
**Archivo destino:** `datos_del_conductor.xlsx` — carpeta `Machine Learning/Datos del Conductor/`

1. Sacar el listado `U5891298` del mes en Quiter (solo el mes en curso).
2. Abrir el TXT exportado y **ordenar por cuenta de cliente** antes de copiar (el teléfono sale en línea diferente y hay que eliminar vacíos).
3. Pegar los datos al final del archivo `datos_del_conductor.xlsx`.

---

## Paso 5 — Archivos de fidelidad (post-ejecución del script)

Después de ejecutar el script principal:

1. Descargar en local (carpeta Machine Learning) los dos archivos de salida:
   - `u239_fidelidad_1`
   - `u239_fidelidad_2`
2. Crear una consulta Power Query para cada uno (nombrarlas igual con sufijo `_consulta`).
3. Fusionar ambas consultas en un archivo llamado `fusion_fidelidad`.
4. `fusion_fidelidad` es el archivo que se lleva a Power BI.

---

## Resumen de listados de Quiter

| Listado | Uso |
|---|---|
| U239_IMPORTADO | Base principal de fidelidad |
| U5701298 | Recambios del mes |
| U5661298 | Piloto Telemarketing |
| U5891298 | Datos del conductor |

## Archivos clave

| Archivo | Ubicación | Notas |
|---|---|---|
| `U239_IMPORTADO.xlsx` | Machine Learning (local) + Google Drive | Actualizar en local antes de ejecutar |
| `recambios_2022.xlsx` | Google Drive / Colab | Añadir pestaña con nombre del mes |
| `base_datos_piloto_1` | `Documentos/2022/Piloto Telemarketing/` | |
| `IMP_BASE_PILOTO_2.xlsx` | `POWER BI INFORMES/DATOS MAESTROS/MACHINE LEARNING/` | Actualizar en local primero |
| `datos_del_conductor.xlsx` | `Machine Learning/Datos del Conductor/` | Ordenar por cuenta de cliente al pegar |
| `fusion_fidelidad` | Local / Machine Learning | Output final para Power BI |
