from dataclasses import dataclass
from datetime import datetime
from time import time

#Esta función toma el tiempo de ejecución de un programa
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print("Pasaron " + str(time_elapse.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre = "David"):
    print("Hola", nombre)

random_func()
suma(10, 150)
saludo()