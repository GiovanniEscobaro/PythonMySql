# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:18:58 2025

@author: Giovanni Escobar

Label: Muestra texto.
Entry: Permite ingresar texto.
Button: Ejecuta una función cuando se presiona (command=mostrar_texto).
Ventana con Múltiples Widgets

"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Completo")

# Etiqueta
label = tk.Label(ventana, text="Introduce tu nombre:")
label.pack()

# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Botón para mostrar mensaje
def mostrar_mensaje():
    nombre = entrada.get()
    resultado.config(text=f"¡Hola, {nombre}!")

boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack()

# Etiqueta de resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()

