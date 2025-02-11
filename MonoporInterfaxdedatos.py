# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:41:48 2025

@author: ADMIN
"""
import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk

# Conectar a MySQL (cambia los valores según tu configuración)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",       # Reemplaza con tu usuario de MySQL
    password="root",       # Reemplaza con tu contraseña
    database="usuarios_db"
)
cursor = conexion.cursor()

# Crear base de datos y tabla si no existen
cursor.execute("CREATE DATABASE IF NOT EXISTS usuarios_db")
cursor.execute("USE usuarios_db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT
    )
""")

# Función para insertar usuario
def insertar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    if nombre and edad.isdigit():
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, int(edad)))
        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        mostrar_usuarios()
    else:
        messagebox.showwarning("Error", "Por favor ingrese datos válidos.")

# Función para mostrar usuarios en la tabla
def mostrar_usuarios():
    for row in tabla.get_children():
        tabla.delete(row)

    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        tabla.insert("", "end", values=usuario)

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("400x400")

# Crear etiquetas y entradas
tk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

tk.Label(root, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(root)
entry_edad.pack(pady=5)

# Botón para agregar usuario
btn_agregar = tk.Button(root, text="Agregar Usuario", command=insertar_usuario)
btn_agregar.pack(pady=10)

# Tabla para mostrar usuarios
tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Edad"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.pack(pady=10)

mostrar_usuarios()

# Iniciar la interfaz gráfica
root.mainloop()

# Cerrar la conexión al cerrar la app
cursor.close()
conexion.close()
