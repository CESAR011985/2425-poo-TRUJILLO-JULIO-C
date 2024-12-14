def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana (7 días):")
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    Recibe una lista de temperaturas y retorna el promedio.
    """
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """
    Función para mostrar el resultado del promedio.
    Recibe el promedio calculado y lo imprime en pantalla.
    """
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()

