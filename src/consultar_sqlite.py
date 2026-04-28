import pandas as pd
import sqlite3

#Conexion con la base de datos
conn = sqlite3.connect("output/temperaturas.db")

#Consulta 1: Visionado de las primeras filas
print(" --- Primeras filas --- ")
query1 = "SELECT * FROM temperaturas LIMIT 5"
print(pd.read_sql(query1, conn))

#Consulta 2: Top 10 ciudades más calientes
print("\n --- Top 10 ciudades con mayor calentamiento")
query2 = """
    SELECT city, country, diferencia, incert_diferencia
    FROM temperaturas
    ORDER BY diferencia DESC
    LIMIT 10
"""
print(pd.read_sql(query2, conn))

#Consulta 3: Top bottom ciudades más calientes
print("\n --- Top 10 ciudades con menor calentamiento")
query3 = """
    SELECT city, country, diferencia, incert_diferencia
    FROM temperaturas
    ORDER BY diferencia ASC
    LIMIT 10
"""
print(pd.read_sql(query3, conn))

#Consulta 4: Media de calentamiento por pais
print("\n--- Media de calentamiento por país (top 10) ---")
query4 = """
    SELECT country, 
           ROUND(AVG(diferencia), 4) as calentamiento_medio,
           COUNT(*) as num_ciudades
    FROM temperaturas
    GROUP BY country
    ORDER BY calentamiento_medio DESC
    LIMIT 10
"""
print(pd.read_sql(query4, conn))

conn.close()