# ARCHIVO CON DEF PARA EL FUNCIONAMIENTO DE LA APP


# ---- Validaciones 


def validar_codigo(codigo, productos):
    codigo = codigo.strip().upper()
    if codigo == "":
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


    
# ---- librerías

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    codigo = codigo.strip().upper()

    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]

    return True

# ---------- MENÚ ----------

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")