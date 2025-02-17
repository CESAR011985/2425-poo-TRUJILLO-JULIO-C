import json
import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un producto con su ID, nombre, cantidad y precio."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Representación en texto del producto."""
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

    def to_dict(self):
        """Convierte el producto en un diccionario para almacenamiento."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(data['id_producto'], data['nombre'], data['cantidad'], data['precio'])

    # Métodos Getters y Setters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        """Inicializa el inventario y carga los productos desde el archivo."""
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.archivo):
            print("📁 No se encontró el archivo de inventario. Se creará uno nuevo.")
            return []

        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
                return [Producto.from_dict(p) for p in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ Error: Archivo de inventario corrupto o inexistente. Se iniciará un nuevo inventario.")
            return []
        except Exception as e:
            print(f"❌ Error inesperado al cargar el inventario: {e}")
            return []

    def guardar_inventario(self):
        """Guarda el inventario en un archivo JSON."""
        try:
            with open(self.archivo, 'w') as file:
                json.dump([p.to_dict() for p in self.productos], file, indent=4)
            print("💾 Inventario guardado exitosamente.")
        except PermissionError:
            print("❌ Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Añade un producto al inventario si el ID no existe."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("⚠️ Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"✅ Producto '{producto.get_nombre()}' agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if not any(p.get_id() == id_producto for p in self.productos):
            print(f"⚠️ Error: No se encontró un producto con ID {id_producto}.")
            return
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_inventario()
        print(f"🗑️ Producto con ID {id_producto} eliminado correctamente.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad y/o precio de un producto existente."""
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_inventario()
                print(f"🔄 Producto '{p.get_nombre()}' actualizado correctamente.")
                return
        print(f"⚠️ Error: Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos cuyo nombre contenga la palabra ingresada."""
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for producto in self.productos:
                print(producto)


def ejecutar_pruebas():
    """Ejecuta pruebas para verificar el correcto funcionamiento del inventario."""
    inventario = Inventario()

    print("\n➡️ Agregando productos...")
    inventario.agregar_producto(Producto(1, "Tubo Negro Redondo 4 pulgadas", 15, 50))
    inventario.agregar_producto(Producto(2, "Tubo Cuadrado 2 pulgadas", 40, 30))

    print("\n📌 Inventario Inicial:")
    inventario.mostrar_productos()

    print("\n➡️ Intentando agregar un producto con ID repetido...")
    inventario.agregar_producto(Producto(1, "Repetido", 10, 20))  # Debe mostrar error

    print("\n➡️ Eliminando producto con ID 1...")
    inventario.eliminar_producto(1)
    inventario.mostrar_productos()

    print("\n➡️ Intentando eliminar un producto inexistente...")
    inventario.eliminar_producto(99)  # No debe existir

    print("\n➡️ Actualizando precio del producto con ID 2 a 35...")
    inventario.actualizar_producto(2, nuevo_precio=35)
    inventario.mostrar_productos()

    print("\n➡️ Buscando productos con 'Cuadrado'...")
    resultados = inventario.buscar_producto("Cuadrado")
    for producto in resultados:
        print(producto)

    print("\n➡️ Buscando un producto inexistente...")
    resultados = inventario.buscar_producto("Inexistente")
    if not resultados:
        print("⚠️ No se encontraron productos con ese nombre.")


if __name__ == "__main__":
    ejecutar_pruebas()

