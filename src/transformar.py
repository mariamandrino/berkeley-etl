import pandas as pd

#Carga de datos limpias
df = pd.read_csv("data/processed/temperaturas_limpias.csv")

#Conversión de formato de dt a tipo fecha
df["dt"] = pd.to_datetime(df["dt"])

#Extracción del año de la columna dt en una columna NUEVA llamada "year"
df["year"] = df["dt"].dt.year

print("Columnas disponibles:", df.columns.tolist())
print("Ejemplo:")
print(df[["dt", "year", "City", "AverageTemperature"]].head())