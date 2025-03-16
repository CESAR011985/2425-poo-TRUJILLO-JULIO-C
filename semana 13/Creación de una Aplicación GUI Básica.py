import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato.strip():  # Verifica que no esté vacío
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese un dato antes de agregar.")
print("se imprimio un mensaje en pantalla")

# Función para limpiar el campo de texto y/o la lista
def limpiar_datos():
    seleccion = lista_datos.curselection()
    if seleccion:  # Si hay un ítem seleccionado, lo elimina
        lista_datos.delete(seleccion)
    else:
        # Si no hay selección, preguntar si desea limpiar toda la lista
        confirmar = messagebox.askyesno("Limpiar Todo", "¿Desea limpiar toda la lista?")
        if confirmar:
            lista_datos.delete(0, tk.END)
    entrada_texto.delete(0, tk.END)  # Limpia el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos Básico")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, width=15, bg="lightblue")
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos, width=15, bg="lightcoral")
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

