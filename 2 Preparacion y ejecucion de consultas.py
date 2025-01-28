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
    
    Config ={
        
        "user":usuario
        "password":contraseña
        "datanase":base_datos
        "port":puerto
        }
    
    #Establecer conexion
    
    conn=mysql.connect(**config)
    
    return conn
#Verificamos connexion 
conn=establecer_conexion(usuario="root", contraseña:"root", host:"localhost", base_datos=None)
print("Estatudo de la conexion: ",conn.is_connected())
cursor=conn.cursor()
    