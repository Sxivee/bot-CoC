import pyautogui
import time
import random
import sys
from matplotlib.path import Path
import numpy as np

i=1
Mantendre=0
SuperDuendes=int(input("Cuants de super duendes tens? [1]:0-70 / [2]: 70-90 / [3]:90-120: "))

if SuperDuendes== 1:
    Mantendre=0.7
    print("Tens entre 0 i 70")
elif SuperDuendes==2:
    Mantendre=1.1
    print("Tens entre 70 90")
elif SuperDuendes==3:
    Mantendre=1.7
    print("Tens entre 90 i 120")
else:
    print("Opció no disponible")
    sys.exit()

heroes=int(input("Cuants de héroes tens actius? [0]/[1]/[2]/[3]/[4]: "))

if heroes>=5:
        print("No és possible tenir més de 4 héroes actius.")
        sys.exit

reps=int(input("Cuants d'atacs vols fer?"))
print("Tens 10 segons per obrir el joc amb pantalla completa.")
time.sleep(10)
while i <= reps:
    print("Atac numero %d" % i)
    espera=random.randint(1,20)
    time.sleep(0.2)
    pyautogui.moveTo(100, 1000)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(1380, 668)
    time.sleep(0.2)
    pyautogui.leftClick()
    time.sleep(20)

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

#Seleccionar Súper Duendes
    pyautogui.leftClick(472, 997)
    time.sleep(0.1)

#Tirar duendes 1
    pyautogui.leftClick(1736,535)
    time.sleep(0.2)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left') 
#Tirar duendes 2
    pyautogui.leftClick(1400,879)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 3
    pyautogui.leftClick(1534,409)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 4
    pyautogui.leftClick(1134,114)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 5
    pyautogui.leftClick(558,162)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 6
    pyautogui.leftClick(422,727)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 7
    pyautogui.leftClick(558,162)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 8
    pyautogui.leftClick(1736,535)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 9
    pyautogui.leftClick(422,727)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 10
    pyautogui.leftClick(1534,409)
    pyautogui.mouseDown(button='left')
    time.sleep(Mantendre)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Esperar
    print("Esperaré %d segons" % espera)
    time.sleep(espera)
    
    pyautogui.leftClick(111,850)
    time.sleep(0.5)
    pyautogui.leftClick(1132,665)
    time.sleep(1)
    pyautogui.leftClick(953,916)
    time.sleep(5)
    i+=1
