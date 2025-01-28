import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Establecer parametros


config ={
        
        "user":"root",
        "password":"root",
        "host":"localhost",
        "database":"world",
        "port":3306
        
        }
#Conexion Base de datos

conn = mysql.connect(**config)
print("Estatus conexion : ", conn.is_connected())
# Defnir cursor

cursor=conn.cursor()

#Mostremos las tablas
# Extracion1 Iterar sobre los resultados
cursor.execute("SHOW TABLES")

for i in cursor:
    print(f"Tabla {i[0]}")
    
    
# Estraccion 2: Extraer la consulta de un lista    
cursor.execute("SHOW TABLES")
tablas= list(cursor)
print(tablas)

#Extracion 3 : Metodo Fetchall del curso
cursor.execute("SHOW TABLES")
tablas_fetchall=cursor.fetchall()
print(tablas_fetchall)

#Extraccion 4:  Usuando pandas

tablas_pd=pd.read_sql_query(sql="SHOW TABLES", con=conn)
print(tablas_pd)

#Recordatorio
#  El tratamiendo de los datas que depende de la necisioda de la programcaion.


