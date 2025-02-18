# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:38:53 2025

@author: ADMIN
"""

import mysql.connector as mysql
import pandas as pd
from warnings  import filterwarnings
filterwarnings("ignore")

# Conexion
conn= mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="world",
    port=3306
    )
print("Estado de la conexion: ", conn.is_connected())
print("Base de datos: ", conn.database)

# Definir el cursor
cursor=conn.cursor()

# Seleciona Tablar
cursor.execute("SHOW TABLES")
tablas=cursor.fetchall()
print(tablas)

#Traes datas y almacernarlos

datos={}
for i  in tablas:
    df=pd.read_sql(sql=f"SELECT * FROM {i[0]}", con=conn)
    #Alamacenar datos
    datos[i[0]]=df
print (datos)

#Extreer subconojunto de nuestra dase de datos
sub_conjuntos={}

for i in tablas :
    #Usaremos las dos primeras Columnas
    cursor.execute(F"DESCRIBE {i[0]}")
    columnas_info=cursor.fetchall()
    cols=[columnas_info[0][0],columnas_info[1][0]]
    print("estas" ,cols)
    cols_formateo= ", ".join(cols)
    #Realizar la consulta
    df=pd.read_sql(sql=f"SELECT {cols_formateo} FROM {i[0]}", con=conn)
    sub_conjuntos[i[0]]=df
print(sub_conjuntos)

# Imprimer las dimensiones de la tabla

for i in tablas:
    print("Tabla: ", i[0],  "- Dimension: ", datos[i[0]].shape)
    print("Subconjuntos ", i[0], "-Deminsiones",sub_conjuntos[i[0]].shape)




















    