# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:39:34 2025

@author: GIOVANNI ESCOBAR OCAMPO
"""

# Importar las librerias
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Deifinimos los parametros

config = {
        "user": "root",
        "password":"root"
        }
conn= mysql.connect(**config)

#Definimos el cursor
cursor= conn.cursor()

#Crear base de datos

db_nombre="clientes"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_nombre}")

#Verificar 

dbs = pd.read_sql(sql="SHOW DATABASES", con=conn)
if  any(dbs.isin([db_nombre])):
    print("Base de datos creada: ", db_nombre)
    
# Usar las base de datos 
cursor.execute(f"USE {db_nombre}")

tabla_nombre= "agenda_contacto"
query = f"""
    CREATE TABLE IF NOT EXISTS {tabla_nombre} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Nombre VARCHAR(50) NOT NULL COMMENT 'Nombre del contacto',
        Apellido VARCHAR(50)NOT NULL COMMENT 'Apellido del Contacto',
        Telefono VARCHAR(25)NOT NULL UNIQUE COMMENT 'Numero de telefono',
        Email VARCHAR(100) UNIQUE COMMENT 'Correo electronico del contacto',
        Direccion VARCHAR(255) COMMENT 'Dirrecion del Contacto',
        Ciudad VARCHAR(50) COMMENT 'Cuidad del Contacto',
        Estado VARCHAR(50) COMMENT 'Estado del Contacto',
        Codido_Postal VARCHAR(10) COMMENT 'Codigo postal del Contacto',
        Fecha_Nacimiento DATE COMMENT 'Fecha de nacimento del Contacto',
        Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro',
        Notas TEXT COMMENT 'Notas Adicionales',
        Foto LONGBLOB COMMENT 'Fotografia del contacto'
        )

"""
cursor.execute(query)
#Verificar
tablas=pd.read_sql(sql=f"SHOW TABLES FROM {db_nombre}", con=conn)
if  any(dbs.isin([tabla_nombre])):
    print("Table creada: ", tabla_nombre)

#Ver la estrutura de nuestro agenda
estrutura=pd.read_sql_query(sql="DESCRIBE clientes.agenda_contacto", con=conn)

#ver la es

    