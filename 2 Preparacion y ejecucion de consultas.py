# Importa librerias
import mysql.connector as mysql 
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Definir funciones

def establecer_conexion(usuario: str, contraseña: str, host:str,base_datos= str,puerto: int=3306):
    
    """
    Establece una conexio a MySql
    
    Parametros
    ---------
    usuario(str):
        Nombre del Usuario de Mysql
    contraseña(str):
        contraseña de Mysql
    host(str):
        Dirrecion del hots
    base_datos(str):
        Base de datos donde nos queremos conetar
    Puerto(str):
        Numero de puerto Mysql, por defecto es 3306 pero es mejor investagrlo
    Salisa
    -----------
    return. objeto de la canexion
    """
    #Estabecer los Parametros
    
    config = {
        
        "user":usuario,
        "password":contraseña,
        "host":host,
        "database":base_datos,
        "port":puerto
        }
    
    #Establecer conexion
    
    conn=mysql.connect(**config)
    
    return conn
# Conexion
conn=establecer_conexion(usuario="root", contraseña="root", host="localhost", base_datos=None)
print("Estatudo de la conexion: ",conn.is_connected())
#Cursor
cursor = conn.cursor()


def ejecutar_consulta(consulta:str):
    
    """
    Ejecutar consulta de la base de datos
    
    Args:
        consulta (str): Consulta SQL a ejecutar
    Salidad:
        Cusor que contine los recustaldos de la consulta
    """
 
    # Ejecutar
    cursor.execute(consulta)
    return cursor
    



# Distitas consultas

query="SHOW DATABASES"
db_existentes = ejecutar_consulta(query)
for n, i in enumerate(db_existentes):
    print(f"Base de datos No. {n}: {i[0]}")

#Ralizar para Pandas

db_existentes_pd= pd.read_sql_query(sql=query, con=conn)
print(db_existentes_pd)

#Usar Base de datos
db_usar=db_existentes_pd.iloc[-1,0] 
print(db_usar)
ejecutar_consulta(f"USE {db_usar}")
print("trabajando con la Bases de datos :", conn.database)


# Ralaizar con pandas
try:
    pd.read_sql_query(sql= f"USE {db_usar}", con= conn)
except Exception as error:
    print("No se puedo ejecutar con error; ", error)
    
    # El resutado de la condulta essta alameciadano dento del mismo cursor. Debemos eztraer dicho 
    # contenido para poder trabajar con la informacion.