import pandas as pd

# Carga del CSV en el dataframe

df = pd.read_csv("data/raw/GlobalLandTemperaturesByCity.csv")

# Número de filas y columnas
print("Dimensiones del CSV:", df.shape)

# Nombres de las columnas
print("\nColumnas:", df.columns.tolist())

# Tipos de datos de cada columna
print("\nTipos de datos:")
print(df.dtypes)

# Cuántos valores nulos hay en cada columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Rango de fechas
print("\nFecha más antigua:", df["dt"].min())
print("\nFecha mas reciente:", df["dt"].max())

# Primeras 5 filas
print("\nPrimeras filas:")
print(df.head())