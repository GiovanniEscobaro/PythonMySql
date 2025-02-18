# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:12:32 2025

@author: Giovanni Escoba Ocampo
"""

import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Defenir conexion
conn=mysql.connect(user="root", password="root", database="clientes")
cursor=conn.cursor()

# Consutar estruta atual

query="DESCRIBE agenda_contacto"
estru_actual=pd.read_sql(sql=query, con=conn)

# Monificar la Columna Nombre
columna="Nombre"
tabla="agenda_contacto"
nueve_estru_col="VARCHAR(100) NOT NULL"
query=f"ALTER TABLE {tabla} MODIFY COLUMN {columna} {nueve_estru_col} "
cursor.execute(query)


query="DESCRIBE agenda_contacto"
Nueva_estru_actual=pd.read_sql(sql=query, con=conn)


# Modificar la estrutura de una columna 