# Importadar Librerias
import mysql.connector as mysql

# Estableces parametros de conexion
config = {
    'user':'root',# Nombre Usuario
    'password':'root',# Contaseña
    'host': 'localhost',# Dirrecion del Host de MySOL
    "database": None,# Nombre de la Base de Datos
    'raise_on_warnings':True # Lanzar execiones en casa de Advertencias
         }
#Establecer Conexion
connexion=mysql.connect(**config) 
print("Canexion Exitosas")   
    
#Imprimer inforamacion de la conexion
print("-----Informacion de la connexion-----")
print("Version de Mysql: " , connexion.get_server_info()) 
print("Id de Conexion: ", connexion.connection_id)
print("Servido host: ", connexion.server_host)
print("Puerto de serividor: ", connexion.server_port)
print("base de datos: " ,connexion.database)
print("Usuario: " ,connexion.user)
print("Contaseña: " ,connexion._password)
print("Conexion Activa: " ,connexion.is_connected())
print("Conexion Cerrado: " ,connexion.is_closed())
print("-" *20)


#Definer el curso:
    
cursor =connexion.cursor()
#Identifaicad las base de datos Actuales
cursor.execute("SHOW DATABASES") 
#Extraer todas las Base de datos
for i in cursor:
    print(i)
    
# Cerar Conexion a las Base datos
connexion.close()
print("Conexion Activa: " ,connexion.is_connected())
print("Conexion Cerrado: " ,connexion.is_closed())
   




   
    
    
    
    
    
    
    