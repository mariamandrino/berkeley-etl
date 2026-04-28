import pandas as pd
import json

#Cargamos el rersultado transformado
df = pd.read_csv("data/processed/temperaturas_transformadas.csv")

print("Número de filas:", len(df))
print("Número de columnas:", df.columns.tolist())


#Construimos el GeoJSON
features = []

for _, fila in df.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [fila["Longitude"], fila["Latitude"]]
        },
        "properties": {
            "city": fila["City"],
            "country": fila["Country"],
            "temp_historico": round(fila["temp_historico"], 4),
            "temp_reciente": round(fila["temp_reciente"], 4),
            "diferencia": round(fila["diferencia"], 4),
            "incert_diferencia": round(fila["incert_diferencia"], 4)
        }
    }
    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

#Guardamos en output
with open("output/temperaturas.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

print(f"GeoJSON generado con {len(features)} ciudades")
print("Guardado en output/temperaturas.geojson")