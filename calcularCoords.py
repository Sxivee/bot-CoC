import pyautogui
import time
import sys

def calibrar_zona():
    print("\n--- HERRAMIENTA DE CALIBRACIÓN DE OCR ---")
    print("Abre Clash of Clans y ponlo en pantalla completa (o en el tamaño que vayas a usar siempre).")
    time.sleep(3)
    
    # 1. Obtener X e Y (Esquina superior izquierda)
    print("\n[Paso 1] Mueve el cursor a la esquina SUPERIOR IZQUIERDA del texto de tu oro.")
    print("Tienes 5 segundos...")
    time.sleep(5)
    x1, y1 = pyautogui.position()
    print(f"-> Guardado: Esquina superior izquierda en X: {x1}, Y: {y1}")
    
    # 2. Obtener Ancho y Alto (Esquina inferior derecha)
    print("\n[Paso 2] Mueve el cursor a la esquina INFERIOR DERECHA del texto de tu oro.")
    print("Tienes 5 segundos...")
    time.sleep(5)
    x2, y2 = pyautogui.position()
    print(f"-> Guardado: Esquina inferior derecha en X: {x2}, Y: {y2}")
    
    # 3. Calcular la región matemática
    ancho = x2 - x1
    alto = y2 - y1
    
    if ancho <= 0 or alto <= 0:
        print("\n[-] Error: Has movido el ratón en la dirección incorrecta. El ancho y alto deben ser positivos.")
        sys.exit()
        
    tupla_region = (x1, y1, ancho, alto)
    print(f"\n[+] CALIBRACIÓN COMPLETADA")
    print(f"Tu línea de código exacta debe ser: zona_oro = {tupla_region}")
    
    # 4. Prueba visual
    print("\n[*] Tomando una captura de prueba de esa región...")
    captura = pyautogui.screenshot(region=tupla_region)
    nombre_archivo = 'prueba_recorte_oro.png'
    captura.save(nombre_archivo)
    
    print(f"[+] Captura guardada como '{nombre_archivo}' en esta carpeta.")
    print("Ábrela. Si en la imagen se ve EXCLUSIVAMENTE el número de tu oro, el OCR no fallará.")

if __name__ == "__main__":
    calibrar_zona()