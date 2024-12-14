# Programa para calcular el promedio semanal de temperaturas usando Programación Orientada a Objetos

class DiaClima:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def __str__(self):
        return f"Día {self.dia}: {self.temperatura} °C"

class ClimaSemanal:
    def __init__(self):
        # Atributo privado para almacenar la información diaria del clima
        self.__dias_clima = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        print("Introduce las temperaturas diarias (7 días):")
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Día {i + 1}: "))
                    dia_clima = DiaClima(dia=i + 1, temperatura=temp)
                    self.__dias_clima.append(dia_clima)
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")

    # Método para calcular el promedio semanal de temperaturas
    def calcular_promedio(self):
        if not self.__dias_clima:
            print("No se han ingresado temperaturas.")
            return None
        suma = sum(dia.temperatura for dia in self.__dias_clima)
        promedio = suma / len(self.__dias_clima)
        return promedio

    # Método para mostrar el resumen semanal
    def mostrar_resumen(self):
        if not self.__dias_clima:
            print("No se ha ingresado información del clima.")
            return
        print("\nResumen semanal:")
        for dia in self.__dias_clima:
            print(dia)
        promedio = self.calcular_promedio()
        if promedio is not None:
            print(f"\nPromedio semanal: {promedio:.2f} °C")

# Función principal para organizar el flujo del programa
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resumen()

# Ejecución del programa
if __name__ == "__main__":
    main()
