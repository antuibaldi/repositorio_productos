lista = []
salir_del_programa = False

while not salir_del_programa:
    print("Menú de opciones:")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        contador=0
        while contador < 10:
            nombre_producto = input("Dame tu producto: ")
            encontro_producto=False
            for producto in lista:
                if producto[0]==nombre_producto:
                    encontro_producto=True
                    break
            if encontro_producto==False:
                nombre_cliente = input("Dame tu nombre: ")
                producto_precio = int(input("Dame el precio del producto: "))
                variables = [nombre_producto, nombre_cliente, producto_precio]
                lista.append(variables)
                print("Producto agregado.\n")
            else:
                print("Ese producto ya esta en stoock no se puede agregar")
                contado=contador-1
                
            contador=contador+1
        if contador > 10:
            print("Ya se han cargado 10 productos.\n")
    
    elif opcion == 2:
        if not lista:
            print("No se puede mostrar lista no a cargado ningun producto")
        else:
            print("\nLista completa de productos:")
            for item in lista:
                print(f"Producto: {item[0]}, Cliente: {item[1]}, Precio: ${item[2]}")
    
    elif opcion == 3:
        nombre_buscar = input("Dame el nombre del producto a buscar: ")
        encontrado = False
        for item in lista:
            if item[0] == nombre_buscar:
                print(f"Producto: {item[0]}, Cliente: {item[1]}, Precio: ${item[2]}")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún producto con ese nombre.")
    
    elif opcion == 4:
        nombre_eliminar = input("Ingresa el nombre del producto a eliminar: ")
        eliminados = 0
        lista_filtrada = []
        for item in lista:
            if item[0] != nombre_eliminar:
                lista_filtrada.append(item)
            else:
                eliminados=eliminados+1
        lista = lista_filtrada
        if eliminados > 0:
            print(f"{eliminados} producto(s) eliminado(s).")
        else:
            print("No se encontró ningún producto con ese nombre para eliminar.")
    
    elif opcion == 5:
        salir_del_programa = True
        print("Saliendo del programa. ¡Hasta luego!")
    
    else:
        print("Opción no válida. Intenta nuevamente.")












    
