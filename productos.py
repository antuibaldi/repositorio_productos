from datos import lista, guardar_lista

def mostrar_productos():
    if not lista:
        print("No hay productos cargados.")
    for i, (nombre, cliente, precio) in enumerate(lista, 1):
        print(f"{i}. Producto: {nombre}, Cliente: {cliente}, Precio: ${precio}")

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    for producto in lista:
        if producto[0].lower() == nombre.lower():
            print(f"Encontrado: {producto}")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in lista:
        if producto[0].lower() == nombre.lower():
            lista.remove(producto)
            guardar_lista(lista)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")
