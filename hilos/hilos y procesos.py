import threading
import time

# Definir una función para la primera tarea
def tarea1():
    for i in range(5):
        time.sleep(1)
        print(f"Tarea 1 - Iteración {i+1}")

# Definir una función para la segunda tarea
def tarea2():
    for i in range(5):
        time.sleep(1.5)
        print(f"Tarea 2 - Iteración {i+1}")

# Crear los hilos
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ejecución finalizada")


