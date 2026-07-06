# ARCHIVO CON DEF PARA EL FUNCIONAMIENTO DE LA APP


# ---- Validaciones 


def validar_codigo(codigo, productos):
    if codigo.strip() == "":
        return False
    elif codigo in productos:
        return False
    
    return True

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def validar_categoria(categoria):
    if categoria.strip() == "":
        return False
    return True

def validar_precio(precio):
    if precio <= 0:
        return False
    return True
    

def validar_disponible(opcion):
    opcion = opcion.strip().lower()
    if opcion == "s" or opcion == "n":
        if opcion == "s":
            disponible = True
        elif opcion == "n":
            disponible = False
        return True
    return False
    
def validar_stock(stock):
    if stock < 0:
        return False
    return True
    

def validar_vendidos(vendidos):
    if vendidos < 0:
        return False
    return True


    

