'''
Programa de aprendizaje
'''

# Importacion de bibliotecas

import platform   # funciones para extraer datos del sistema operativo
import os         # contiene la funcion para la limpieza de pantalla
import time       # funciones de tiempo. Ej. tiempo de epera

def limpiar_pantalla():
    time.sleep(2)

    if platform.system() == "Windows":
       os.system('cls')
    else:
        os.system('clear')
if __name__ == "__main__":
    limpiar_pantalla()
