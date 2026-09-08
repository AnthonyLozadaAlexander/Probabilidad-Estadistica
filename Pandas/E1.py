"""Enunciado: Imagina que tienes una lista con los salarios de 4 empleados: [1000, 1500, 1200, 2000]."""

""" Sabiendo que NumPy tiene funciones matemáticas directas (como np.average() que vimos previamente) y que Pandas usa diccionarios para armar tablas, ¿cómo escribirías la estructura básica del código para transformar esa lista en un DataFrame de una sola columna llamada "Salarios" y cómo calcularías la media de esos valores usando NumPy? """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salarios_empleados: list[int] = [1000, 1500, 1200, 2000]
nombres_empleados: list[str] = ["Empleado A", "Empleado B", "Empleado C", "Empleado D"]

nombresEmpleados: np.ndarray = np.array(nombres_empleados)
salarios: np.ndarray = np.array(salarios_empleados)
media: float = np.mean(salarios)
tabla: pd.DataFrame = pd.DataFrame(
    {"Empleados": nombresEmpleados, "Salarios": salarios}
)

print("=" * 30)
print("Tabla De Salarios De Empleados")
print("=" * 30)
print(tabla)
print("=" * 30)
print(f"La media es de: {media}")

tabla.plot(kind="bar", color="Orange", x="Empleados", y="Salarios")

plt.title("Salarios De Los Empleados")
plt.xlabel("Empleados")
plt.ylabel("Salarios")
plt.xticks(rotation=0)

plt.show()
