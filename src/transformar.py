import pandas as pd

# --- PASO 1: Carga de datos limpios ---
df = pd.read_csv("data/processed/temperaturas_limpias.csv")

#Conversión de formato de dt a tipo fecha
df["dt"] = pd.to_datetime(df["dt"])

#Extracción del año de la columna dt en una columna NUEVA llamada "year"
df["year"] = df["dt"].dt.year

print("Columnas disponibles:", df.columns.tolist())
print("Ejemplo:")
print(df[["dt", "year", "City", "AverageTemperature"]].head())

# --- PASO 2: Filtrado por periodos ---
historico = df[(df["year"] >= 1900) & (df["year"] <= 1979)]
reciente = df[(df["year"] >= 1980) & (df["year"] <= 2013)]

print("\nFilas periodo histórico", len(historico))
print("Filas periodo reciente", len(reciente))

# --- PASO 3: Temperatura media e incertidumbre por ciudad en cada periodo ---
def incertidumbre_media(x):
    # Propagación de errores: sqrt(suma de cuadrados) / N
    return (x ** 2).sum() ** 0.5 / len(x)

media_historico = historico.groupby(["City", "Country", "Latitude", "Longitude"])["AverageTemperature"].mean()
media_reciente = reciente.groupby(["City", "Country", "Latitude", "Longitude"])["AverageTemperature"].mean()

incert_historico = historico.groupby(["City", "Country", "Latitude", "Longitude"])["AverageTemperatureUncertainty"].agg(incertidumbre_media)
incert_reciente = reciente.groupby(["City", "Country", "Latitude", "Longitude"])["AverageTemperatureUncertainty"].agg(incertidumbre_media)


print("\nEjemplo media histórica:")
print(media_historico.head())

# --- PASO 4: Combinar periodos y calcular diferencia ---
df_final = pd.DataFrame({
    "temp_historico" : media_historico,
    "temp_reciente" : media_reciente,
    "incert_historica": incert_historico,
    "incert_reciente": incert_reciente
}).reset_index()

#Diferencia entre periodos
df_final["diferencia"] = df_final["temp_reciente"] - df_final["temp_historico"]

#Prpagacion de errores de la diferencia
df_final["incert_diferencia"] = (
    df_final["incert_historica"] ** 2 + df_final["incert_reciente"] ** 2
) ** 0.5

df_final = df_final.dropna()

print("\nResultado final:")
print(df_final.head(10))
print("\nDimensiones:", df_final.shape)

# --- PASO 5: Guardado del resultado final ---
df_final.to_csv("data/processed/temperaturas_transformadas.csv")
print("Archivo guardado correctamente en data/processed/temperaturas_transformadas.csv")