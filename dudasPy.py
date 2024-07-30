from PIL import ImageGrab

# Captura de pantalla
screenshot = ImageGrab.grab()
screenshot.save('captura.png')  # Guarda la captura como imagen

from PIL import Image

# Cargar la imagen objetivo
target_image = Image.open('ruta/a/la/imagen_objetivo.png')

import numpy as np

# Convertir imágenes a matrices numpy
screenshot_np = np.array(screenshot)
target_image_np = np.array(target_image)

# Comparar imágenes
difference = np.sum(np.abs(screenshot_np - target_image_np))

# Umbral de diferencia (ajusta según sea necesario)
threshold = 100000

if difference < threshold:
    print("¡La imagen objetivo apareció en la pantalla!")
else:
    print("La imagen objetivo no está presente en la pantalla.")




import os

# Ruta de la carpeta
folder_path = r'C:\Temp\mi_carpeta'  # Cambia esto a la ruta de tu carpeta

# Verificar si la carpeta existe
if os.path.exists(folder_path):
    # Iterar sobre todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Verificar si es un archivo (no un directorio)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Eliminar el archivo
                print(f'Archivo eliminado: {file_path}')
        except Exception as e:
            print(f'Error al eliminar {file_path}: {e}')
else:
    print(f'La carpeta {folder_path} no existe.')


import pyautogui
import time

# Esperar un momento para prepararte (opcional)
time.sleep(5)  # Tienes 5 segundos para preparar la pantalla

# Ruta de la imagen que deseas hacer clic
image_path = r'C:\Temp\imgAuto\mi_imagen.png'  # Cambia esto a la ruta de tu imagen

# Buscar la imagen en la pantalla
location = pyautogui.locateOnScreen(image_path)

if location is not None:
    # Hacer clic en el centro de la imagen encontrada
    pyautogui.click(pyautogui.center(location))
    print('Se hizo clic en la imagen.')

    # Esperar un momento para que el elemento cargue (ajusta según sea necesario)
    time.sleep(1)

    # Escribir texto en el elemento clicado
    text_to_write = "Hola, este es un texto de prueba."
    pyautogui.write(text_to_write)
    print('Texto escrito en el elemento.')
else:
    print('Imagen no encontrada en la pantalla.')
