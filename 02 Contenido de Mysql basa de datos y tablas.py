# Importa liberias
import mysql.connector as mysql


#Establecer conexion
conn= mysql.connect(user="root", password="root", host="localhost")
print("Estado de la conexion: ", conn.is_connected())


# Difinor cursor

cursor= conn.cursor()


#Declara el nombre de la basa de datos

nombre ="base_datos_prueba"
query= f"CREATE DATABASE {nombre}"
cursor.execute(query)