import pyautogui
import random
from matplotlib.path import Path
import numpy as np

# Coordenadas del paralelogramo(ÁREA ATAQUE)
x1, y1 = 1224, 104
x2, y2 = 1359, 104
x3, y3 = 1416, 284
x4, y4 = 1532, 271

# vértices
polygon = np.array([
    [x1, y1],
    [x2, y2],
    [x4, y4],
    [x3, y3]
])

# Crear el Path para verificar si un punto está dentro
path = Path(polygon)

# Bounding box del área
x_min, y_min = polygon.min(axis=0)
x_max, y_max = polygon.max(axis=0)

# Función para obtener un punto válido
def get_random_point_in_polygon(path, x_min, x_max, y_min, y_max):
    while True:
        x_rand = random.uniform(x_min, x_max)
        y_rand = random.uniform(y_min, y_max)
        if path.contains_point((x_rand, y_rand)):
            return int(x_rand), int(y_rand)

# Obtener punto y hacer clic
x, y = get_random_point_in_polygon(path, x_min, x_max, y_min, y_max)
print(f"Clic en: {x}, {y}")
pyautogui.moveTo(x, y)
pyautogui.click()
