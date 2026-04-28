# Berkeley Earth ETL

Pipeline ETL sobre datos de temperatura superficial de Berkeley Earth.
Incluye limpieza, transformación con propagación de errores, exportación 
a GeoJSON para visualización en QGIS y carga en base de datos SQLite.

## Fuente de datos
[Berkeley Earth en Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)

Descargar `GlobalLandTemperaturesByCity.csv` y colocar en `data/raw/`.

## Estructura del proyecto

```
berkeley-etl/
├── data/
│   ├── raw/          ← datos originales, nunca se modifican
│   └── processed/    ← datos limpios generados por el código
├── src/
│   ├── explorar.py         ← análisis inicial del dataset
│   ├── limpiar.py          ← limpieza y corrección de tipos
│   ├── transformar.py      ← agregación por períodos y propagación de errores
│   ├── exportar_geojson.py ← exportación a GeoJSON para QGIS
│   └── consultar_sqlite.py ← consultas SQL sobre la base de datos
│   └── cargar_sqlite.py    ← carga SQL sobre la base de datos
├── output/
│   ├── temperaturas.geojson  ← para visualización en QGIS
│   └── temperaturas.db       ← base de datos SQLite
└── README.md
```

## Pipeline ETL

Los scripts se ejecutan en orden desde la raíz del proyecto:

```bash
python src/explorar.py
python src/limpiar.py
python src/transformar.py
python src/exportar_geojson.py
python src/cargar_sqlite.py
python src/consultar_sqlite.py
```

## Metodología

### Períodos de análisis
- **Histórico:** 1900-1979
- **Reciente:** 1980-2013

### Transformaciones aplicadas
- Eliminación de valores nulos en temperatura
- Conversión de fechas a tipo datetime
- Conversión de coordenadas de formato texto (57.05N) a decimal (57.05)
- Temperatura media por ciudad en cada período
- Propagación de errores estándar sobre la incertidumbre en la medida de la temperatura
- Diferencia de temperaturas entre períodos con incertidumbre propagada

### Propagación de errores
La incertidumbre de la media se calcula como:

σ_media = sqrt(Σσᵢ²) / N

La incertidumbre de la diferencia entre dos períodos:

σ_diferencia = sqrt(σ_historico² + σ_reciente²)

## Resultados destacados
- 3.510 ciudades analizadas en 159 países
- Las ciudades con mayor calentamiento están en Siberia y Asia Central (>1.3°C)
- Las ciudades con menor calentamiento están en el suroeste de China (~0.18°C)
- Los países con mayor calentamiento medio son Mongolia, Kazajistán y Turkmenistán

## Estado del proyecto
- [x] Exploración del dataset
- [x] Limpieza de datos (nulos, tipos, coordenadas)
- [x] Transformación con propagación de errores
- [x] Exportación a GeoJSON
- [x] Carga en SQLite
- [ ] Visualización en QGIS

## Tecnologías
- Python 3.14
- pandas
- SQLite
- QGIS (visualización geoespacial, pendiente)# Berkeley Earth ETL