import json
import os

ARCHIVO = "productos.json"

def cargar_lista():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    return []

def guardar_lista(lista):
    with open(ARCHIVO, "w") as archivo:
        json.dump(lista, archivo, indent=4)

lista = cargar_lista()
