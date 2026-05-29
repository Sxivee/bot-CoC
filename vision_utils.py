import pyautogui
import time
import random
from matplotlib.path import Path

def esperar_y_clicar_imagen(ruta_imagen, confianza=0.8, timeout=10, retardo_post_clic=0.5):
    """Busca una imagen y hace clic si la encuentra antes de que acabe el timeout."""
    tiempo_inicio = time.time()
    while (time.time() - tiempo_inicio) < timeout:
        try:
            ubicacion = pyautogui.locateCenterOnScreen(ruta_imagen, confidence=confianza)
            if ubicacion:
                pyautogui.click(ubicacion)
                print(f"[+] Clic realizado en: {ruta_imagen}")
                time.sleep(retardo_post_clic)
                return True
        except pyautogui.ImageNotFoundException:
            pass # Ignoramos el error hasta que aparezca la imagen
        time.sleep(0.5)
        
    print(f"[-] No se encontró {ruta_imagen} tras {timeout}s.")
    return False

def get_random_point_in_polygon(polygon_array):
    """Devuelve un punto aleatorio dentro de un polígono definido por coordenadas."""
    path = Path(polygon_array)
    x_min, y_min = polygon_array.min(axis=0)
    x_max, y_max = polygon_array.max(axis=0)
    
    while True:
        x_rand = random.uniform(x_min, x_max)
        y_rand = random.uniform(y_min, y_max)
        if path.contains_point((x_rand, y_rand)):
            return int(x_rand), int(y_rand)

def desplegar_heroes(num_heroes):
    """Despliega hasta 4 héroes sin tener que repetir código."""
    if num_heroes <= 0:
        return
    
    num_heroes = min(num_heroes, 4) # Máximo 4
    # Coordenadas X de los héroes en la barra (asumiendo tu configuración original)
    coords_x_heroes = [604, 722, 845, 957]
    x_mapa, y_mapa = 1424, 220
    
    for i in range(num_heroes):
        pyautogui.leftClick(coords_x_heroes[i], 1000) # Selecciona héroe
        time.sleep(0.1)
        pyautogui.leftClick(x_mapa, y_mapa)           # Lo suelta en el mapa
        time.sleep(0.1)
        print(f"    - Héroe {i+1} desplegado.")

def activar_habilidades_heroes(num_heroes):
    """Vuelve a pulsar sobre los héroes para activar sus habilidades."""
    if num_heroes <= 0:
        return
        
    num_heroes = min(num_heroes, 4)
    coords_x_heroes = [604, 722, 845, 957]
    
    for i in range(num_heroes):
        pyautogui.leftClick(coords_x_heroes[i], 1000)
        time.sleep(0.1)
    print("    - Habilidades activadas.")

import pyautogui
import time

def desplegar_heroes_por_imagen(lista_imagenes_heroes, x_despliegue=1424, y_despliegue=220):
    """
    Busca las imágenes de los héroes en la barra inferior y los despliega en el mapa.
    """
    print("[*] Iniciando despliegue de Héroes mediante visión artificial...")
    
    for imagen_heroe in lista_imagenes_heroes:
        # 1. Buscamos y seleccionamos la carta del héroe (timeout corto de 2 segs)
        # Usamos una confianza del 0.7 por si hay ligeros cambios de iluminación
        ha_encontrado = esperar_y_clicar_imagen(imagen_heroe, confianza=0.7, timeout=2, retardo_post_clic=0.1)
        
        if ha_encontrado:
            # 2. Desplegamos el héroe en la coordenada estática del mapa
            pyautogui.leftClick(x_despliegue, y_despliegue)
            time.sleep(0.1)
            print(f"    [+] {imagen_heroe} desplegado.")
        else:
            print(f"    [-] No se detectó {imagen_heroe} en pantalla. Saltando...")

def activar_habilidades_por_imagen(lista_imagenes_habilidades):
    """
    Busca los iconos específicos de las habilidades (ej. hab_rey.png) para activarlas.
    """
    print("[*] Buscando los iconos de habilidad para activarlas...")
    
    for imagen_habilidad in lista_imagenes_habilidades:
        # Buscamos el icono de la habilidad activa
        ha_encontrado = esperar_y_clicar_imagen(imagen_habilidad, confianza=0.7, timeout=2, retardo_post_clic=0.1)
        
        if ha_encontrado:
            print(f"    [+] Clic en {imagen_habilidad} (Habilidad activada).")
        else:
            print(f"    [-] {imagen_habilidad} no detectado (quizás ya se usó o el héroe cayó).")