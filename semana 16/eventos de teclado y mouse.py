import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - Julio Cesar Trujillo - Semana 16")
        self.root.geometry("750x350")
        self.root.resizable(False, False)

        # Configuración de estilos
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("Completed.TLabel", foreground="gray", font=("Arial", 10, "overstrike"))

        # Variables
        self.tasks = []

        # Crear widgets
        self.create_header()
        self.create_task_input()
        self.create_task_list()
        self.setup_keyboard_shortcuts()

    def create_header(self):
        """Crea el encabezado con información personal"""
        header_frame = ttk.Frame(self.root, padding=(10, 5))
        header_frame.pack(fill=tk.X)

        ttk.Label(
            header_frame,
            text="Aplicación GUI para Gestión de Tareas con Atajos de Teclado",
            font=("Arial", 12, "bold")
        ).pack(side=tk.LEFT)

        ttk.Label(
            header_frame,
            text="Julio Cesar Trujillo - Semana 16",
            font=("Arial", 10)
        ).pack(side=tk.RIGHT)

    def create_task_input(self):
        """Crea el área de entrada de tareas"""
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.pack(fill=tk.X)

        ttk.Label(input_frame, text="Nueva Tarea:").grid(row=0, column=0, sticky=tk.W)
        self.task_entry = ttk.Entry(input_frame, width=50)
        self.task_entry.grid(row=0, column=1, padx=5)
        self.task_entry.focus()

        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=0, column=2, padx=(10, 0))

        self.add_btn = ttk.Button(button_frame, text="Añadir (Enter)", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=2)

        self.complete_btn = ttk.Button(button_frame, text="Completar (C)", command=self.mark_completed)
        self.complete_btn.pack(side=tk.LEFT, padx=2)

        self.delete_btn = ttk.Button(button_frame, text="Eliminar (D)", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT)

    def create_task_list(self):
        """Crea la lista visual de tareas"""
        list_frame = ttk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        # Treeview para mostrar tareas
        self.task_tree = ttk.Treeview(
            list_frame,
            columns=("status", "task"),
            show="headings",
            height=15,
            selectmode="browse"
        )

        # Configurar columnas
        self.task_tree.heading("status", text="Estado", anchor=tk.CENTER)
        self.task_tree.heading("task", text="Tarea", anchor=tk.W)
        self.task_tree.column("status", width=80, anchor=tk.CENTER)
        self.task_tree.column("task", width=450, anchor=tk.W)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        self.task_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Estilo para tareas completadas
        self.task_tree.tag_configure("completed", foreground="gray", font=("Arial", 10, "overstrike"))

    def setup_keyboard_shortcuts(self):
        """Configura los atajos de teclado"""
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        self.root.bind("<c>", lambda e: self.mark_completed())
        self.root.bind("<d>", lambda e: self.delete_task())
        self.root.bind("<Delete>", lambda e: self.delete_task())
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def add_task(self):
        """Añade una nueva tarea a la lista"""
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self):
        """Marca/desmarca la tarea seleccionada como completada"""
        selected = self.task_tree.selection()
        if selected:
            index = self.task_tree.index(selected[0])
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    def delete_task(self):
        """Elimina la tarea seleccionada"""
        selected = self.task_tree.selection()
        if selected:
            index = self.task_tree.index(selected[0])
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        """Actualiza la visualización de la lista de tareas"""
        self.task_tree.delete(*self.task_tree.get_children())
        for task in self.tasks:
            status = "✓" if task["completed"] else ""
            tags = ("completed",) if task["completed"] else ()
            self.task_tree.insert("", tk.END, values=(status, task["text"]), tags=tags)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()