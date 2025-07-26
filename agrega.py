from helpers import producto_existe
from datos import lista, guardar_lista

def agregar_productos():
    contador = 0
    while contador < 10:
        nombre = input("Dame tu producto: ").strip()
        if not producto_existe(nombre):
            cliente = input("Dame tu nombre: ").strip()
            try:
                precio = int(input("Dame el precio del producto: "))
            except ValueError:
                print("Precio inválido. Intenta de nuevo.")
                continue
            lista.append([nombre, cliente, precio])
            guardar_lista(lista)
            print("Producto agregado.\n")
        else:
            print("Ese producto ya está en stock, no se puede agregar.")
        contador += 1

    print("Ya se han cargado 10 productos.\n")
