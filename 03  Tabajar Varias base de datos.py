

#Importar librerias
import mysql.connector as mysql

#Defini parametros de conecion

config= {
    "user": "root",
    "password":"root",
    "database":None
     }

conn = mysql.connect(**config)
print("La conexion en correcta: ", conn.is_connected())

 #Definir cursor
cursor=conn.cursor()

#Seleccinar una Base
query="SHOW DATABASES"
cursor.execute(query)
BaseDeDatos=list(cursor)


# Metodo 1: Intentar cambiar el paramento interno
conn.database=BaseDeDatos[-1][0]
print("Base de datos actual es: " , conn.database)

#Metodo 2: Mediante consultas
query=f"USE {BaseDeDatos[-2][0]}"
cursor.execute(query)
print("Base de datos actual es: " , conn.database)

# Metodo 3 Establecer una conexion(Ineficiente)

config= {
    "user": "root",
    "password":"root",
    "database":BaseDeDatos[-3][0]
     }
conn = mysql.connect(**config)
print("Base de datos actual es: " , conn.database)
conn.close()

# - Permite el cambio de basa de datos para nuestro Proyectos

