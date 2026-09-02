import random


def extrarMuestra(poblacion: list[int], tamanio: int) -> list[int]:
    return random.sample(poblacion, tamanio)


# poblacion: porcentaje de uso de cpu
poblacion_cpu: list[int] = [45, 55, 89, 21, 12, 99, 40, 60]

# muestra: seleccionamos 3 peticiones al azar para analizar los tiempos
muestra: list[int] = extrarMuestra(poblacion_cpu, 3)

print("Poblacion de porcentajes de uso de cpu:\n", poblacion_cpu)
print("Datos de la muestra extraida: \n", muestra)
