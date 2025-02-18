# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:35:38 2025

@author: Giovanni Escobar Ocampo
"""
#Importar Librerias
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Conexion
conn= mysql.connect(user="root", password= "root", database="clientes")
#Cursor
cursor = conn.cursor()

#Obtener las Columnas

query="SHOW COLUMNS FROM agenda_contacto"
estrutura=pd.read_sql(sql=query, con=conn)
#Nueva Estrutura de clave primaria

query="ALTER TABLE agenda_contacto ADD COLUMN Identificardor INT AUTO_INCREMENT PRIMARY KEY" 
# Eliminar la clave  primaria Existente
query_eliminar="ALTER TABLE agenda_contacto DROP COLUMN Id "

#Para eliminar la clavi primaria
cursor.execute(query_eliminar)
#Se crea la nueva clave primara
cursor.execute(query)

#Valida 
contacto= pd.read_sql(sql="SHOW COLUMNS FROM agenda_contacto", con=conn)

# Clave primaria original
query="ALTER TABLE agenda_contacto RENAME COLUMN Identificardor TO Id"
cursor.execute(query)
#Verificar 
query="SHOW COLUMNS FROM agenda_contacto"
estrutura_original = pd.read_sql(sql=query, con=conn)
if all (estrutura_original.sort_values(by="Field")["Field"].values == estrutura.sort_values(by="Field")["Field"].values):
    print("Clave  primara Original !!!!")
                                                                                 
