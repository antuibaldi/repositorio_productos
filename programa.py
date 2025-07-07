lista = []

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar")
    print("5. Salir")

def agregar_productos():
    contador = 0
    while contador < 10:
        nombre_producto = input("Dame tu producto: ")
        if not producto_existe(nombre_producto):
            nombre_cliente = input("Dame tu nombre: ")
            try:
                producto_precio = int(input("Dame el precio del producto: "))
            except ValueError:
                print("Precio inválido. Intenta de nuevo.")
                continue
            variables = [nombre_producto, nombre_cliente, producto_precio]
            lista.append(variables)
            print("Producto agregado.\n")
        else:
            print("Ese producto ya está en stock, no se puede agregar.")

        contador += 1

    if contador >= 10:
        print("Ya se han cargado 10 productos.\n")

def producto_existe(nombre):
    for producto in lista:
        if producto[0] == nombre:
            return True
    return False

def mostrar_productos():
    if not lista:
        print("No se puede mostrar la lista. No ha cargado ningún producto.")
    else:
        print("\nLista completa de productos:")
        for idx, item in enumerate(lista):
            print(f"{idx}. Producto: {item[0]}, Cliente: {item[1]}, Precio: ${item[2]}")

def buscar_producto():
    nombre_buscar = input("Dame el nombre del producto a buscar: ")
    encontrado = False
    for item in lista:
        if item[0] == nombre_buscar:
            print(f"Producto: {item[0]}, Cliente: {item[1]}, Precio: ${item[2]}")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún producto con ese nombre.")

def eliminar_producto():
    if not lista:
        print("No hay productos para eliminar.")
        return

    mostrar_productos()  # Mostramos los productos con índice
    try:
        indice = int(input("Ingresa el número del producto a eliminar: "))
        if 0 <= indice < len(lista):
            eliminado = lista.pop(indice)
            print(f"Producto '{eliminado[0]}' eliminado correctamente.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")



def main():
    salir = False
    while not salir:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada no válida. Ingresa un número del 1 al 5.")
            continue
        match opcion:

            case "1":
                agregar_productos()
            case"2":
                mostrar_productos()
            case"3":
                buscar_producto()
            case"4":
                eliminar_producto()
            case"5":
                salir = True
                print("Saliendo del programa. ¡Hasta luego!")
            case _:
                print("Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
main()
