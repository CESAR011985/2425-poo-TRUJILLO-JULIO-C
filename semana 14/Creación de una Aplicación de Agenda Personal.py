import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitarás instalar tkcalendar: pip install tkcalendar

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")  # Tamaño inicial de la ventana

        # Estilos
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=("Arial", 10))
        self.style.configure("TLabel", font=("Arial", 10))
        self.style.configure("Treeview", font=("Arial", 10))

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10, fill=tk.X)

        # Campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(padx=10, pady=10, fill=tk.X)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    def validar_hora(self, hora):
        """Valida que la hora esté en formato HH:MM."""
        try:
            horas, minutos = map(int, hora.split(':'))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return True
            return False
        except ValueError:
            return False

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validaciones
        if not (fecha and hora and descripcion):
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        if not self.validar_hora(hora):
            messagebox.showwarning("Hora Inválida", "Por favor, ingrese una hora válida en formato HH:MM.")
            return

        # Verificar duplicados
        for item in self.tree.get_children():
            if self.tree.item(item, "values") == (fecha, hora, descripcion):
                messagebox.showwarning("Evento Duplicado", "Este evento ya existe en la lista.")
                return

        # Agregar evento al Treeview
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Nada Seleccionado", "Por favor, seleccione un evento para eliminar.")

    def limpiar_campos(self):
        """Limpia los campos de entrada."""
        self.fecha_entry.set_date(None)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()