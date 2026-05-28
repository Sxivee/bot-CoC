import pyautogui
import time


boton = pyautogui.locateOnScreen('donar.png', confidence=0.8)

pyautogui.leftClick(boton)


dragonelectrico=pyautogui.locateOnScreen('dragonelectrico.png', confidence=0.8)
globos=pyautogui.locateOnScreen('globos.png', confidence=0.8)
if dragonelectrico :
    pyautogui.leftClick(dragonelectrico)
    pyautogui.leftClick(globos)


