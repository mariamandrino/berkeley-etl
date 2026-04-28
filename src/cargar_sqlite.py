import pandas as pd
import sqlite3

#Carga del CSV limpio y transformado
df = pd.read_csv("data/processed/temperaturas_transformadas.csv")

#Conectamos con la base de datos
conn = sqlite3.connect("output/temperaturas.db")

#Cargamos el DataFrame en una tabla SQL
df.to_sql("temperaturas", conn, if_exists="replace", index=False)

print("Base de datos creada en output/temperaturas.db")
print(len(df), "filas cargadas en la tabla 'temperaturas'")

conn.close()