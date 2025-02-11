# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:39:40 2025

@author: Giovanni Escobar
"""
# Importar librerias
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Hacemos conexion 
conn=mysql.connect(user="root",password="root", host="localhost",port="3306")
print("Estatp conexion; ", conn.is_connected())
print("Base de datos: ", conn.database)
#cursor
cursor=conn.cursor()

#Defenimos la consulta

db="clientes"
tabla="agenda_contacto"
columna="Licenciatura"
query=f"ALTER TABLE {db}.{tabla} DROP COLUMN {columna}"


#Veridficar la estructura de la tabla

estructura= pd.read_sql(sql=f"DESCRIBE {db}.{tabla}", con=conn)
print("La columnas son:", estructura.shape[0])

#Ejecutar la consulta

cursor.execute(query)

#Veridficar la estructura de la tabla
estructura= pd.read_sql(sql=f"DESCRIBE {db}.{tabla}", con=conn)
print("La columnas son:", estructura.shape[0])

#Eliminarda Nuevamente que erro nos da

try:
    cursor.execute(query)
except Exception as error:
    print(error)
    
#validar existencia
query=f"SHOW COLUMNS FROM {db}.{tabla}"
columnas=pd.read_sql_query(sql=query, con=conn)

print(columnas)

if columna is columnas["Field"]:
    query= f"ALTER TABLA {db}.{tabla} DROP COLUMN{columna}"
    cursor(query)
else:
    print("La columno se ha eliminado")
    
    
