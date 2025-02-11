# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:02:47 2025

@author: Giovanni Escobar Ocampo

"""

import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Conexion

conn=mysql.connect(user="root", password="root", database="clientes")

cursor= conn.cursor()

# Columnas actules

tabla="agenda_contacto"
columnas=pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)
columnas= columnas["Field"]

#Modificaremois el nombre del columna
nombre_viejo="Email"
nombre_nuevo="correo_electronico"
query=f"ALTER TABLE {tabla} RENAME COLUMN {nombre_viejo} TO {nombre_nuevo}"
cursor.execute(query)

nueva_columnas=pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)
nueva_columnas= nueva_columnas["Field"]


query=f"ALTER TABLE {tabla} RENAME COLUMN {nombre_nuevo} TO {nombre_viejo}"
cursor.execute(query)

columnas_incial= pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)["Field"]
if all(columnas_incial== columnas):
    print("Columna Origina")