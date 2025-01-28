import mysql.connector as mysql
import json

#Realizar nuestar conexion

conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )
#print("Conexion: ", conn.is_connected())
# Definir en curso
cursor= conn.cursor()
# Informacion de mysql
print("Usuario: ",conn.user)
print("Version: ",conn.get_server_version())
print("Host: ",conn.server_host)
print("Puerto: ",conn.server_port)

# Consutar las base de datos exitentes

query=  "SHOW DATABASES"
cursor.execute(query)
dbs= cursor.fetchall()
print("Base de datos: ", dbs)

# Consutal tablas en cada base
db_muestra="world"
query=f"SHOW TABLES FROM {db_muestra}"
cursor.execute(query)
tablas_world= cursor.fetchall()
#print(tablas_world)
#Describir cada tabla

query="DESCRIBE {base_datos}.{tabla}".format(base_datos=db_muestra, tabla=tablas_world[0][0])
cursor.execute(query)
contenido_tabla=cursor.fetchall()
#print(contenido_tabla)

def obtener_MySql_info():
    
    """
    Obtiene la informacion exostete dentro de MySql
    salida
    ------
          Dicionario con la inforamcion de nuesras base de datos dento de MySql.
    """ 

    #Almacenar
    db_info= {
        "MySQL": {
            "Server": conn.get_server_info(),
            "Host": conn.server_host,
            "Port": conn.server_port,
            "DBs":{}    
            }
        }

    #Obtener base de Datos
    
    cursor.execute("SHOW DATABASES")
    for i in cursor:
        db_info["MySQL"]["DBs"][i[0]] = {}
        #print(i)
    
    #Consultas las tablas
    for i in db_info["MySQL"]["DBs"]:
        query = f"SHOW TABLES FROM {i}"
        #print(db_info["MySQL"]["DBs"])
        cursor.execute(query)
        tablas= cursor.fetchall()
        #print(1)
        for t in tablas:
            cursor.execute(f"DESCRIBE {i}.{t[0]}")
            estructura_tabla=cursor.fetchall()
            db_info["MySQL"]["DBs"][i][t[0]] =estructura_tabla
            #print(tablas)
    return db_info
    
#Recuperar Información
mysql_info=obtener_MySql_info()
print("Informacion general d MySql: \n", json.dumps(mysql_info,indent=4))

#Recordotorio
# Podemos mirar tadas las base de datos y sus tablas en MYSQL desde python




