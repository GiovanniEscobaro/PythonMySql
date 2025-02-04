# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:23:49 2025

@author: Giovanni Escoba Ocampo
"""

import mysql.connector as mysql
#Definir Conexion

conn = mysql.connect (
        user="root",
        password="root",
        host="localhost"
        )

print("Estatos", conn.is_connected())

#Definir Cursor
cursor=conn.cursor()

#Definir la base de Datos
bd="clientes"

cursor.execute(f"USE {bd}")
#Modificar la base de datos
Nombre_Viejo="agenda_contacto"
Nombre_Nuevo="Contactos"
query= f"ALTER TABLE {Nombre_Viejo} RENAME TO {Nombre_Nuevo}"
cursor.execute(query)

# Verificar Cambio

cursor.execute("SHOW TABLES")
print(list(cursor))
# Cambiar el nombre a Dato Original

query= f"ALTER TABLE {Nombre_Nuevo} RENAME TO {Nombre_Viejo}"
cursor.execute(query)

# Verificar Cambio

cursor.execute("SHOW TABLES")
print(list(cursor))


# Como renombra un table
