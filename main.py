from menu import mostrar_menu
from agrega import agregar_productos
from productos import mostrar_productos, buscar_producto, eliminar_producto

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_productos()
            case "2":
                mostrar_productos()
            case "3":
                buscar_producto()
            case "4":
                eliminar_producto()
            case "5":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
