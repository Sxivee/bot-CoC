import pyautogui
import time
import random
import sys
from matplotlib.path import Path
import numpy as np


reps=int(input("Cuants d'atacs vols fer?"))
i=1
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
    time.sleep(5)

#Seleccionar Duendes
    pyautogui.leftClick(472, 997)
    time.sleep(0.1)

#Tirar duendes 1
    pyautogui.leftClick(1736,535)
    time.sleep(0.2)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left') 
#Tirar duendes 2
    pyautogui.leftClick(1400,879)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 3
    pyautogui.leftClick(1534,409)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 4
    pyautogui.leftClick(1134,114)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 5
    pyautogui.leftClick(558,162)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 6
    pyautogui.leftClick(422,727)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 7
    pyautogui.leftClick(558,162)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 8
    pyautogui.leftClick(1736,535)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 9
    pyautogui.leftClick(422,727)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
#Tirar duendes 10
    pyautogui.leftClick(1534,409)
    pyautogui.mouseDown(button='left')
    time.sleep(3)
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
    time.sleep(2)
    i+=1
