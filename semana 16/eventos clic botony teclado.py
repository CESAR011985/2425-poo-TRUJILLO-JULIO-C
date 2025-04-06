import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea
def añadir_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar como completada
def marcar_completada(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        texto = lista_tareas.get(seleccion)
        if not texto.startswith("✓ "):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, "✓ " + texto)
    except IndexError:
        messagebox.showinfo("Info", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def eliminar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

# Cerrar la app con Escape
def cerrar_aplicacion(event=None):
    root.destroy()

# --- Configuración de la ventana ---
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Título del proyecto, clase y nombre
header = tk.Label(root, text="Aplicación GUI para Gestión de Tareas\n16 - Última clase del Semestre\nJulio Cesar Trujillo",
                  font=("Arial", 16), justify=tk.CENTER)
header.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)
entrada.focus_set()

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_añadir = tk.Button(frame_botones, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar Completada", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
lista_tareas.pack(pady=10, fill=tk.BOTH, expand=True)

# --- Atajos de teclado ---
root.bind("<Return>", añadir_tarea)        # Enter para añadir
root.bind("<c>", marcar_completada)        # C para completar
root.bind("<d>", eliminar_tarea)           # D para eliminar
root.bind("<Delete>", eliminar_tarea)      # Tecla Suprimir también elimina
root.bind("<Escape>", cerrar_aplicacion)   # Escape para salir

root.mainloop()
