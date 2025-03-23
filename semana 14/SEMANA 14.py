import tkinter as tk
from tkinter import messagebox, Menu, scrolledtext

# Función que se ejecuta al presionar el botón
def boton_accion():
    messagebox.showinfo("Nuevo Mensaje", "Has presionado el botón con un nuevo mensaje")

# Función para el menú desplegable
def menu_accion():
    messagebox.showinfo("Nuevo Menú", "Has seleccionado una nueva opción del menú")

# Función para mostrar la selección de los Radio Buttons
def mostrar_seleccion():
    messagebox.showinfo("Nueva Selección", f"Has seleccionado: {var_radio.get()}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Componentes GUI Comunes Personalizados")
root.geometry("500x500")

# Etiqueta
etiqueta = tk.Label(root, text="Esta es una nueva etiqueta")
etiqueta.pack()

# Campo de Texto
campo_texto = tk.Entry(root)
campo_texto.pack()

# Botón
boton = tk.Button(root, text="Nuevo Botón", command=boton_accion)
boton.pack()

# Casilla de Verificación
var_check = tk.IntVar()
casilla_verificacion = tk.Checkbutton(root, text="Nueva Casilla de Verificación", variable=var_check)
casilla_verificacion.pack()

# Lista Desplegable
opciones = ["Nueva Opción 1", "Nueva Opción 2", "Nueva Opción 3"]
variable_seleccionada = tk.StringVar(root)
variable_seleccionada.set(opciones[0])
lista_desplegable = tk.OptionMenu(root, variable_seleccionada, *opciones)
lista_desplegable.pack()

# Botones de Radio
var_radio = tk.StringVar()
var_radio.set("Opción A")  # Inicializa con la primera opción
radio1 = tk.Radiobutton(root, text="Nueva Opción A", variable=var_radio, value="Opción A", command=mostrar_seleccion)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Nueva Opción B", variable=var_radio, value="Opción B", command=mostrar_seleccion)
radio2.pack()
radio3 = tk.Radiobutton(root, text="Nueva Opción C", variable=var_radio, value="Opción C", command=mostrar_seleccion)
radio3.pack()

# Área de Texto (Text Widget)
area_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
area_texto.pack()

# Nuevo Área de Texto
nueva_area_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=5)
nueva_area_texto.pack()

# Menú
barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo Abrir", command=menu_accion)
menu_archivo.add_command(label="Nuevo Guardar", command=menu_accion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Nuevo Menú
menu_edicion = Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=lambda: messagebox.showinfo("Edición", "Cortar seleccionado"))
menu_edicion.add_command(label="Copiar", command=lambda: messagebox.showinfo("Edición", "Copiar seleccionado"))
barra_menu.add_cascade(label="Edición", menu=menu_edicion)

root.config(menu=barra_menu)
root.mainloop()