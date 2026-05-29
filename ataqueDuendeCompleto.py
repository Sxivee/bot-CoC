import pyautogui
import time
import vision_utils
import sys

def realizar_un_ataque(numero_ataque, total_ataques):
    print(f"\n====================================================")
    print(f"--- INICIANDO ATAQUE {numero_ataque} DE {total_ataques} ---")
    print(f"====================================================")

    # 1. Abrir menú de ataques (esquina inferior izquierda)
    print("[*] Paso 1: Pulsando el botón inicial de espadas...")
    if not vision_utils.esperar_y_clicar_imagen('assets/boton_espadas.png', confianza=0.8, timeout=10):
        print("[-] Error: No se encontró 'assets/boton_espadas.png'. Abortando este ataque.")
        return False

    time.sleep(1.5) 

    # 2. Buscar partida multijugador (botón marrón del mapa)
    print("[*] Paso 2: Pulsando el botón grande de Atacar...")
    if not vision_utils.esperar_y_clicar_imagen('assets/atacar.png', confianza=0.8, timeout=10):
        print("[-] Error: No se encontró 'assets/atacar.png'. Abortando este ataque.")
        return False
        
    time.sleep(1.5) 

    # 3. Confirmar ejército (botón verde)
    print("[*] Paso 3: Confirmando el ejército con el botón VERDE...")
    if not vision_utils.esperar_y_clicar_imagen('assets/atacar_verde.png', confianza=0.8, timeout=10):
        print("[-] Error: No se encontró 'assets/atacar_verde.png'. Abortando este ataque.")
        return False

    print("[*] En las nubes... esperando 7 segundos a que cargue la aldea enemiga.")
    time.sleep(7) 

    # 4. Seleccionar la carta del duende
    print("[*] Paso 4: Seleccionando la carta del duende...")
    if not vision_utils.esperar_y_clicar_imagen('assets/duende.png', confianza=0.7, timeout=15):
        print("[-] Error: No se encontró 'assets/duende.png' en la barra de tropas.")
        # Clic de emergencia para rendirse si no encuentra la tropa
        pyautogui.leftClick(111, 850) 
        time.sleep(1)
        pyautogui.leftClick(1132, 665)
        return False
        
    # 5. Desplegar los duendes
    print("[+] Tropas seleccionadas. ¡Iniciando despliegue de Duendes!")
    
    coordenadas_despliegue = [
        (1736, 535), (1400, 879), (1534, 409), 
        (1134, 114), (558, 162), (422, 727)
    ]
    
    for x, y in coordenadas_despliegue:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')
        time.sleep(2.5) 
        pyautogui.mouseUp(button='left')
        time.sleep(0.2)
        
    print("[+] Todos los duendes desplegados.")

    # 6. Desplegar Héroes y activar habilidades
    print("[*] Paso 5: Despliegue de Héroes...")
    mis_heroes = ['assets/principe.png', 'assets/reina.png', 'assets/centinela.png', 'assets/luchadora.png']
    mis_habilidades = ['assets/hab_principe.png', 'assets/hab_reina.png', 'assets/hab_centinela.png', 'assets/hab_luchadora.png']

    vision_utils.desplegar_heroes_por_imagen(mis_heroes)
    
    print("[*] Esperando 5 segundos para que reciban daño antes de activar poderes...")
    time.sleep(5)
    
    vision_utils.activar_habilidades_por_imagen(mis_habilidades)
    
    # 7. Esperar a que salga el botón volver
    print("[*] Paso 6: Esperando a que termine la batalla (Max 30s antes de rendirse)...")
    
    # Reducimos el timeout de 120 a 30 segundos
    terminado_naturalmente = vision_utils.esperar_y_clicar_imagen('assets/volver.png', confianza=0.8, timeout=30)
    
    if terminado_naturalmente:
        print(f"[+] Batalla {numero_ataque} finalizada naturalmente rápido. Volviendo a la base.")
    else:
        print("[-] Han pasado 30s. Forzando rendición para ahorrar tiempo...")
        
        # 1. Pulsar botón "Rendirse"
        ha_pulsado_rendirse = vision_utils.esperar_y_clicar_imagen('assets/rendirse.png', confianza=0.8, timeout=3)
        if not ha_pulsado_rendirse:
            # Respaldo de seguridad con tus coordenadas originales por si falla la imagen
            pyautogui.leftClick(111, 850) 
            
        time.sleep(1) # Pausa para que salga el cartel de confirmación
        
        # 2. Pulsar botón "Vale"
        ha_pulsado_vale = vision_utils.esperar_y_clicar_imagen('assets/vale.png', confianza=0.8, timeout=3)
        if not ha_pulsado_vale:
            # Respaldo de seguridad con tus coordenadas originales
            pyautogui.leftClick(1132, 665) 
            
        time.sleep(2) # Pausa para que el juego procese la rendición y cargue la pantalla de estadísticas
        
        # 3. Ahora sí, buscar y pulsar el botón de Volver
        print("[*] Buscando el botón Volver tras la pantalla de estadísticas...")
        vision_utils.esperar_y_clicar_imagen('assets/volver.png', confianza=0.8, timeout=10)
        print(f"[+] Batalla {numero_ataque} abortada con éxito. Volviendo a la base.")
        
    # Pausa larga para dejar que la aldea cargue completamente tras la pantalla de carga negra
    time.sleep(8) 
    return True

def iniciar_bot():
    print("\n--- CONFIGURACIÓN DE RUTINA ---")
    try:
        num_ataques = int(input("¿Cuántas partidas seguidas quieres que haga el bot? : "))
    except ValueError:
        print("[-] Debes introducir un número entero. Cerrando programa.")
        sys.exit()

    print(f"\n[*] Entendido. El bot intentará realizar {num_ataques} ataques.")
    print("[*] Tienes 5 segundos para maximizar la ventana del juego y ponerte en la aldea...")
    time.sleep(5)

    for i in range(1, num_ataques + 1):
        realizar_un_ataque(i, num_ataques)
        
        if i < num_ataques:
            print(f"[*] Descanso de 3 segundos antes de iniciar la siguiente búsqueda...")
            time.sleep(3)

    print("\n[+] Tarea finalizada. Se han completado todas las repeticiones.")

# Al importar el archivo desde botatacar.py, esto evita que se ejecute automáticamente
if __name__ == "__main__":
    iniciar_bot()