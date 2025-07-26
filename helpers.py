from datos import lista

def producto_existe(nombre):
    for producto in lista:
        if producto[0].lower() == nombre.lower():
            return True
    return False
