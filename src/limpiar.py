import pandas as pd

# carga del CSV
df = pd.read_csv("data/raw/GlobalLandTemperaturesByCity.csv")

print("Filas originales:", len(df))

# PASO 1: Eliminación de filas sin temperatura
df = df.dropna(subset=["AverageTemperature", "AverageTemperatureUncertainty"])

print("Filas tras eliminar valores nulos de temperatura:", len(df))

# PASO 2: Convertir dt a formato fecha
df["dt"] = pd.to_datetime(df["dt"])

print("\nTipo de dt antes:", "str")
print("Tipo de dt ahora:", df["dt"].dtype)
print("Ejemplo:", df["dt"].iloc[0])

# PASO 3: Convertir coordenadas a números decimales
# N y E > 0, S y W < 0

def convertir_coordenada(valor):
    #La letra que representa N, S, E u W se encuentra al final de cada valor
    letra = valor[-1]
    numero = float(valor[:-1])

    #S y W son coordenadas negativas
    if letra in ["S", "W"]:
        numero = -numero
    return numero

df["Latitude"] = df["Latitude"].apply(convertir_coordenada)
df["Longitude"] = df["Longitude"].apply(convertir_coordenada)

print("\nEjemplo de coordenadas convertidas:")
print(df[["City", "Latitude", "Longitude"]].head())

# PASO 4: Guardar los datos procesados
df.to_csv("data/processed/temperaturas_limpias.csv", index = False)

print("\nArchivo guardado en carpeta processed")
print("Dimensiones finales:", df.shape)