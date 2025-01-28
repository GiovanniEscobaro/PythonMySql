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

#Consulta su existencia
cursor.execute("SHOW DATABASES")
dbs=cursor.fetchall()
print(dbs)

try:
    cursor.execute(query)
except Exception as error:
    print("No se puede crear la base de datos por el Siquiete error: ", error)
query=f"CREATE DATABASE IF NOt EXISTS {nombre}"
cursor.execute(query)

# Se puede crear bases de datos y veirficar si no existen