import pyautogui
import time
import random
import sys
from matplotlib.path import Path
import numpy as np

#Variables per FINALITZAR PARTIDA
imgVolver= 'volver.png'
tempsEspera = 120

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

def get_random_point_in_polygon(path, x_min, x_max, y_min, y_max):
    while True:
        x_rand = random.uniform(x_min, x_max)
        y_rand = random.uniform(y_min, y_max)
        if path.contains_point((x_rand, y_rand)):
            return int(x_rand), int(y_rand)

i=1

print("Preparate un ejército con SOLO Dragones électricos. Quan ho tenguis, dim el seüent: ")
reps=int(input("Cuants d'atacs vols fer? "))
heroes=int(input("Cuants de héroes tens actius? [0]/[1]/[2]/[3]/[4]: "))

if heroes>=5:
        print("No és possible tenir més de 4 héroes actius.")
        sys.exit
else:
    while i <= reps:
        print("Atac numero %d" % i)
        
        time.sleep(0.2)
        pyautogui.moveTo(100, 1000)
        time.sleep(0.1)
        pyautogui.leftClick()
        time.sleep(0.1)
        pyautogui.moveTo(1380, 668)
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(5)
        pyautogui.leftClick(472, 997)
        time.sleep(0.1)
#Tirar Dragpones 1
        x, y = get_random_point_in_polygon(path, x_min, x_max, y_min, y_max)
        pyautogui.leftClick(x,y)
        time.sleep(0.1)
        pyautogui.mouseDown(button='left')
        time.sleep(0.8)
        pyautogui.mouseUp(button='left')

    #Tirar Dragpones 2
        pyautogui.leftClick(604,1000)
        time.sleep(0.1)
        pyautogui.mouseDown(button='left')
        time.sleep(1.2)
        pyautogui.mouseUp(button='left')

#Tirar Héroes
        z=1
        xHeores, yHeroes=(604,1000)
        while z<=heroes:
            print(z)
            pyautogui.leftClick(xHeores,yHeroes)
            time.sleep(0.1)

            pyautogui.leftClick(1424,220)
            time.sleep(0.1)
            xHeores+=120
            z+=1

#Tirar Habilidades Héroes
        q=1
        xHabilidadesHeores, yHeroes=(604,1000)
        while q<=heroes:
            print(q)
            pyautogui.leftClick(xHabilidadesHeores,yHeroes)
            time.sleep(0.1)

            xHabilidadesHeores+=120
            q+=1

#SI TENIM 0 HÉROES
#Seleccionar i Tirar Hechizo 1
        if heroes==0:
            pyautogui.leftClick(604,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1082,268)
            time.sleep(0.1)
            pyautogui.leftClick(1254,378)

#Seleccionar i Tirar Hechizo 2
        
            pyautogui.leftClick(722,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1049,262)
            time.sleep(0.1)
            pyautogui.leftClick(1175,340)
            time.sleep(0.1)
            pyautogui.leftClick(1277,433)



#SI TENIM 1 HÉROES
#Seleccionar i Tirar Hechizo 1
        if heroes==1:
            pyautogui.leftClick(722,1000)
            time.sleep(0.1)
            pyautogui.leftClick(1082,268)
            time.sleep(0.1)
            pyautogui.leftClick(1254,378)

#Seleccionar i Tirar Hechizo 2
        
            pyautogui.leftClick(845,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1049,262)
            time.sleep(0.1)
            pyautogui.leftClick(1175,340)
            time.sleep(0.1)
            pyautogui.leftClick(1277,433)



#SI TENIM 2 HÉROES
#Seleccionar i Tirar Hechizo 1
        elif heroes==2:
            pyautogui.leftClick(845,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1082,268)
            time.sleep(0.1)
            pyautogui.leftClick(1254,378)

#Seleccionar i Tirar Hechizo 2
        
            pyautogui.leftClick(957,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1049,262)
            time.sleep(0.1)
            pyautogui.leftClick(1175,340)
            time.sleep(0.1)
            pyautogui.leftClick(1277,433)


#SI TENIM 3 HÉROES
#Seleccionar i Tirar Hechizo 1
        elif heroes==3:
            pyautogui.leftClick(957,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1082,268)
            time.sleep(0.1)
            pyautogui.leftClick(1254,378)

#Seleccionar i Tirar Hechizo 2
        
            pyautogui.leftClick(1094,1000)
            time.sleep(0.1)
            pyautogui.leftClick(1049,262)
            time.sleep(0.1)
            pyautogui.leftClick(1175,340)
            time.sleep(0.1)
            pyautogui.leftClick(1277,433)

#SI TENIM 4 HÉROES
#Seleccionar i Tirar Hechizo 1
        elif heroes==4:
            pyautogui.leftClick(1094,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1082,268)
            time.sleep(0.1)
            pyautogui.leftClick(1254,378)

#Seleccionar i Tirar Hechizo 2
        
            pyautogui.leftClick(1213,1000)
            time.sleep(0.1)

            pyautogui.leftClick(1049,262)
            time.sleep(0.1)
            pyautogui.leftClick(1175,340)
            time.sleep(0.1)
            pyautogui.leftClick(1277,433)
        
        else: 
            print("No és poden tenir més de 5 héroes actius")

        print("Esperant 2 minuts o a que acabi la batalla.")

        for segundos_restantes in range(tempsEspera, 0, -1):
            try:
                ubicacion = pyautogui.locateCenterOnScreen(imgVolver, confidence=0.8)
            except pyautogui.ImageNotFoundException:
                ubicacion = None  # No se encontró, continuar normalmente

            if ubicacion:
                pyautogui.click(ubicacion)
                time.sleep(1)
                break
            else:
                time.sleep(1)
        else:
            print("Temps acabat, abandonant.")
            pyautogui.leftClick(111,850)
            time.sleep(0.5)
            pyautogui.leftClick(1132,665)
            time.sleep(1)
            pyautogui.leftClick(953,916)
            time.sleep(2)
        i+=1
