import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_inventario(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as f:
                data = json.load(f)
                self.productos = {k: Producto(**v) for k, v in data.items()}
        except FileNotFoundError:
            self.productos = {}


def menu(entrada_usuario=None):
    inventario = Inventario()

    # Actualización de productos específicos
    inventario.actualizar_producto("cafe", 25, 1.50)
    inventario.actualizar_producto("azucar", 50, 1.20)
    inventario.actualizar_producto("leche", 15, 1.00)

    opciones = ["1", "2", "3", "4", "5", "6"]
    index = 0

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        if entrada_usuario:
            if index >= len(entrada_usuario):
                break
            opcion = entrada_usuario[index]
            index += 1
        else:
            print("Error: No se puede leer la entrada en este entorno.")
            break

        if opcion == "1":
            id_producto, nombre, cantidad, precio = entrada_usuario[index:index + 4]
            index += 4
            inventario.agregar_producto(Producto(id_producto, nombre, int(cantidad), float(precio)))
        elif opcion == "2":
            id_producto = entrada_usuario[index]
            index += 1
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto, cantidad, precio = entrada_usuario[index:index + 3]
            index += 3
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = entrada_usuario[index]
            index += 1
            print(inventario.buscar_producto(nombre))
        elif opcion == "5":
            print(inventario.mostrar_inventario())
        elif opcion == "6":
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    datos_prueba = ["1", "201", "Arroz", "20", "35.00", "1", "202", "Aceite", "10", "25.00", "5", "6"]
    menu(datos_prueba)
