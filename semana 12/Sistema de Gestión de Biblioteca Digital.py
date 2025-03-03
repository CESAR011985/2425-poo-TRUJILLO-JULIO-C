class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # La tupla (autor, titulo) es inmutable
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.categoria}, {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"{libro.titulo} no está prestado a este usuario.")

    def listar_libros_prestados(self):
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = set()  # Conjunto para asegurar IDs únicos de usuarios

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in {u.id_usuario for u in self.usuarios}:
            self.usuarios.add(usuario)
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        usuario_a_borrar = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario_a_borrar:
            self.usuarios.remove(usuario_a_borrar)
        else:
            print("El usuario no existe.")

    def prestar_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = self.libros.get(isbn)

        if usuario and libro:
            if libro not in usuario.libros_prestados:
                usuario.prestar_libro(libro)
                print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = self.libros.get(isbn)

        if usuario and libro:
            usuario.devolver_libro(libro)
            print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def __repr__(self):
        return f"Biblioteca con {len(self.libros)} libros y {len(self.usuarios)} usuarios."


# Prueba del sistema de gestión de la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
libro2 = Libro("El Alquimista", "Paulo Coelho", "Ficción", "978-3-16-148410-1")
libro3 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

# Crear usuarios
usuario1 = Usuario("manuel gomez", "U001")
usuario2 = Usuario("laura cadena", "U002")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "978-3-16-148410-0")
biblioteca.prestar_libro("U002", "978-0-452-28423-4")

# Listar libros prestados
print("Libros prestados por manuel gomez:", usuario1.listar_libros_prestados())
print("Libros prestados por laura cadena:", usuario2.listar_libros_prestados())

# Buscar libros
print("Búsqueda por autor (Gabriel García Márquez):", biblioteca.buscar_libro("autor", "Gabriel García Márquez"))
print("Búsqueda por título (1984):", biblioteca.buscar_libro("titulo", "1984"))

# Devolver libros
biblioteca.devolver_libro("U001", "978-3-16-148410-0")

# Mostrar el estado final de la biblioteca
print(biblioteca)
