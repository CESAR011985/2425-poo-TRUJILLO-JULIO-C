class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio por unidad

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

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
    def __init__(self):
        self.productos = []  # Lista de productos en el inventario

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        return self.productos


def ejecutar_pruebas():
    inventario = Inventario()
    inventario.agregar_producto(Producto(1, "Tubo Negro Redondo 4 pulgadas", 15, 50))
    inventario.agregar_producto(Producto(2, "Tubo Cuadrado 2 pulgadas", 40, 30))

    print("\nInventario Inicial:")
    for producto in inventario.mostrar_productos():
        print(producto)

    print("\nEliminando producto con ID 1...")
    inventario.eliminar_producto(1)
    for producto in inventario.mostrar_productos():
        print(producto)

    print("\nActualizando precio del producto con ID 2 a 35...")
    inventario.actualizar_producto(2, nuevo_precio=35)
    for producto in inventario.mostrar_productos():
        print(producto)

    print("\nBuscando productos con 'Cuadrado':")
    resultados = inventario.buscar_producto("Cuadrado")
    for producto in resultados:
        print(producto)


if __name__ == "__main__":
    ejecutar_pruebas()
