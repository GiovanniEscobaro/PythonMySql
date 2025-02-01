# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:19:36 2025

@author: Giovanni Escobar Ocampo
"""

import mysql.connector as mysql
import pandas as pd
#Definimos la conexion
conn= mysql.connect (
    user="root",
    password="root",
    host="localhost"
    )

cursor=conn.cursor()
#Estable  que base de datos es

cursor.execute("USE clientes")
#Creamos un tabla
cursor.execute("""
               
               CREATE TABLE IF NOT EXISTS tabla_eliminacion
               (
                Id INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(100) NOT NULL
                   )
               """)
#Verificar la existencia
cursor.execute("SHOW TABLES")
print(list(cursor))

#Eliminar Tabla

query="DROP TABLE IF EXISTS tabla_eliminacion"
cursor.execute(query)

#Validar si esta

cursor.execute("SHOW TABLES")
tablas_existente=[i[0]for i in cursor]
if "tabla_eliminacion" not in tablas_existente:
    print("la tabla se elimino")
else:
    raise ValueError("La tabla se elimino")

cursor.execute("SHOW TABLES")
print(list(cursor))


# Como si elimina una tabla 