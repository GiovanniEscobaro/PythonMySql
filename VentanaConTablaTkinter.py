# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:27:19 2025

@author: ADMIN
"""

from tkinter import ttk
import tkinter as tk

ventana = tk.Tk()
ventana.title("Tabla en Tkinter")

# Crear tabla (Treeview)
columnas = ("ID", "Nombre", "Edad")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

# Configurar encabezados
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.pack()

# Insertar datos
datos = [(1, "Ana", 25), (2, "Carlos", 30), (3, "María", 22)]
for fila in datos:
    tabla.insert("", "end", values=fila)

ventana.mainloop()