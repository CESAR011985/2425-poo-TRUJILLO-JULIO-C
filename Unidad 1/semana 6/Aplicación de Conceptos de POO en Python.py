#  clase base "Persona"
class Persona:
    """
    Clase base que representa a una persona.
    Demuestra el uso de encapsulación al hacer privados algunos atributos.
    """
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad      # Atributo encapsulado

    def mostrar_informacion(self):
        """Método público para mostrar información de la persona."""
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")

    def hablar(self):
        """Ejemplo de método para ser sobrescrito (polimorfismo)."""
        print(f"{self._nombre} dice: ¡Hola!")

# Definimos la clase derivada "Estudiante"
class Estudiante(Persona):
    """
    Clase derivada que hereda de la clase base Persona.
    Representa a un estudiante, extendiendo la funcionalidad de Persona.
    """
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.grado = grado  # Atributo adicional de la clase derivada

    # Sobrescribimos el método hablar para demostrar polimorfismo
    def hablar(self):
        print(f"{self._nombre} dice: Estoy estudiando en el grado {self.grado}.")

    def mostrar_informacion(self):
        """Método sobrescrito para incluir la información adicional."""
        super().mostrar_informacion()  # Llamamos al método de la clase base
        print(f"Grado: {self.grado}")

# Ejemplo de uso de polimorfismo mediante métodos y herencia
def saludar(persona):
    """
    Función que demuestra polimorfismo al aceptar tanto objetos Persona como Estudiante.
    """
    persona.hablar()

# Bloque principal
if __name__ == "__main__":
    # Crear una instancia de la clase base
    persona1 = Persona("Rouse", 54)
    persona1.mostrar_informacion()
    saludar(persona1)

    print("-" * 30)

    # Crear una instancia de la clase derivada
    estudiante1 = Estudiante("Julio", 39, "Universidad")
    estudiante1.mostrar_informacion()
    saludar(estudiante1)

