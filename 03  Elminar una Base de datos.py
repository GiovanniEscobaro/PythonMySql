# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:15:14 2024

@author: GIOVANNI ESCOBAR OCAMPO
"""

import mysql.connector as mysql
import time

# Definir nuestra conexion

config = {
        "user": "root",
        "password":"root",
        "host":"localhost",
        "port":3306,
        "database": None
        }
conn=mysql.connect(**config)
print("Estado de la conexion:" , conn.is_connected())

#Definir cursor
cursor=conn.cursor()

#Crear base de datos
db_nombre="base_datos_prueba"
query= f"CREATE DATABASE IF NOT EXISTS {db_nombre}"
cursor.execute(query)
#verificar
cursor.execute("SHOW DATABASES")
print("Bases de datos : ", list(cursor))


#Elemina base de datos
print("!Cuidado! Esta por elinminar una base da datos con nombre", db_nombre)
time.sleep(5)
query=f"DROP DATABASE {db_nombre}"
cursor.execute(query)
print("Base de datos fue elimana ", db_nombre)
#verificar
cursor.execute("SHOW DATABASES")
print("Bases de datos : ", list(cursor))


try:
    query=f"DROP DATABASE {db_nombre}"
    cursor.execute(query)
except Exception as error:
    print("Error:" ,error)

query= f"DROP DATABASE IF EXISTS {db_nombre}"
cursor.execute(query)

# Eliminar de una base de datos







