import pyautogui
import time

imgVolver= 'volver.png'
tempsEspera = 120

for segundos_restantes in range(tempsEspera, 0, -1):
    print(f"Comprobando... Tiempo restante: {segundos_restantes}s")

    try:
        ubicacion = pyautogui.locateCenterOnScreen(imgVolver, confidence=0.8)
    except pyautogui.ImageNotFoundException:
        ubicacion = None  # No se encontró, continuar normalmente

    if ubicacion:
        print("Imagen detectada. Pulsando el botón...")
        pyautogui.click(ubicacion)
        break
    else:
        time.sleep(1)
else:
    print("Tiempo agotado, continuando de todos modos.")
    pyautogui.leftClick(111,850)
    time.sleep(0.5)
    pyautogui.leftClick(1132,665)
    time.sleep(1)
    pyautogui.leftClick(953,916)
    time.sleep(2)
