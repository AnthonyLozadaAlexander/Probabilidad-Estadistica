import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Edades De La Poblacion
edadPoblacion: list[int] = [18, 22, 25, 30, 19]

edadR: np.ndarray = np.array(edadPoblacion)
edadP: np.ndarray = edadR + 5

# Diccionario De Tabla De Edades
tabla_edades: pd.DataFrame = pd.DataFrame(
    {
        "Edad Actual": edadR,
        "Edad Proyectada En 5 Anios": edadP,
    }
)

# # 'kind=bar' indica que queremos barras verticales
tabla_edades.plot(kind="bar", color=["Blue", "Orange"])

plt.title("Comparacion De Edades Actuales y Proyeccion En 5 Anios")
plt.xlabel("Indice De La Poblacion")
plt.ylabel("Edad")
plt.xticks(rotation=0)  # rota las etiquetas del eje x para que se vean mejor

print(tabla_edades)
plt.show()
