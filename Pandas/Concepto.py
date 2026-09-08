import numpy as np
import pandas as pd

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

print(tabla_edades)
