# Definimos la clase base "Empleado"
class Empleado:
    """
    Clase base que representa a un empleado.
    Demuestra encapsulación mediante atributos protegidos.
    """
    def __init__(self, nombre, salario):
        self._nombre = nombre  # Atributo protegido
        self._salario = salario  # Atributo protegido

    def mostrar_informacion(self):
        """Método para mostrar información del empleado."""
        print(f"Nombre: {self._nombre}, Salario: {self._salario}")

    def calcular_bono(self):
        """Método base para calcular un bono."""
        return self._salario * 0.10


# Definimos la clase derivada "Gerente"
class Gerente(Empleado):
    """
    Clase derivada que representa a un gerente.
    Extiende la funcionalidad de la clase base Empleado.
    """
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llamamos al constructor de la clase base
        self.departamento = departamento  # Atributo adicional de la clase derivada

    def mostrar_informacion(self):
        """Método sobrescrito para incluir el departamento."""
        super().mostrar_informacion()  # Llamamos al método de la clase base
        print(f"Departamento: {self.departamento}")

    def calcular_bono(self):
        """Sobrescribimos el método para calcular un bono mayor para los gerentes."""
        return self._salario * 0.20


# Ejemplo de polimorfismo mediante una función externa
def mostrar_bono(empleado):
    """
    Funciona con cualquier objeto que sea de la clase Empleado o sus derivadas,
    demostrando polimorfismo.
    """
    print(f"El bono de {empleado._nombre} es: {empleado.calcular_bono()}")


# Bloque principal
if __name__ == "__main__":
    # Crear una instancia de la clase base
    empleado1 = Empleado("Julio", 600)
    empleado1.mostrar_informacion()
    mostrar_bono(empleado1)

    print("-" * 30)

    # Crear una instancia de la clase derivada
    gerente1 = Gerente("Rouse", 400, "Ventas")
    gerente1.mostrar_informacion()
    mostrar_bono(gerente1)
