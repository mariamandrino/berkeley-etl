# Berkeley Earth ETL

Pipeline ETL sobre datos de temperatura superficial de Berkeley Earth.
Incluye limpieza, transformación y exportación a GeoJSON para visualización en QGIS.

## Fuente de datos
[Berkeley Earth en Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)

Descargar `GlobalLandTemperaturesByCity.csv` y colocar en `data/raw/`.

## Estructura del proyecto
berkeley-etl/
├── data/
│   ├── raw/          ← datos originales, nunca se modifican
│   └── processed/    ← datos limpios generados por el código
├── src/              ← código Python
├── output/           ← archivos finales (GeoJSON para QGIS)
└── README.md

## Tecnologías
- Python + pandas
- QGIS (visualización geoespacial)