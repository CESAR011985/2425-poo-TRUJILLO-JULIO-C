import tkinter as tk
from tkinter import messagebox, ttk
import os

ARCHIVO_TAREAS = "tasks.txt"

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            for linea in f:
                lista_tareas.insert(tk.END, linea.strip())

def guardar_tareas():
    with open(ARCHIVO_TAREAS, "w") as f:
        for i in range(lista_tareas.size()):
            f.write(lista_tareas.get(i) + "\n")

def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
        guardar_tareas()
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar una tarea.")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, f"✔ {tarea}")
            guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta tarea?"):
            lista_tareas.delete(indice)
            guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

def editar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        entrada_tarea.delete(0, tk.END)
        entrada_tarea.insert(0, tarea.replace("✔ ", ""))
        lista_tareas.delete(indice)
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para editar.")

def ordenar_tareas():
    tareas = list(lista_tareas.get(0, tk.END))
    tareas.sort(key=lambda x: (not x.startswith("✔ "), x))
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)
    guardar_tareas()
# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("450x450")

# Campo de entrada
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = ttk.Button(frame_botones, text="Añadir", command=agregar_tarea)
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_completar = ttk.Button(frame_botones, text="Completar", command=marcar_completada)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_editar = ttk.Button(frame_botones, text="Editar", command=editar_tarea)
btn_editar.pack(side=tk.LEFT, padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)

btn_ordenar = ttk.Button(frame_botones, text="Ordenar", command=ordenar_tareas)
btn_ordenar.pack(side=tk.LEFT, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=60, height=15)
lista_tareas.pack(pady=10)

# Atajos de teclado
root.bind("<Control-a>", lambda e: agregar_tarea())
root.bind("<Control-m>", lambda e: marcar_completada())
root.bind("<Control-d>", lambda e: eliminar_tarea())
root.bind("<Control-o>", lambda e: ordenar_tareas())

# Cargar tareas al iniciar
cargar_tareas()

# Iniciar la aplicación
root.mainloop()
