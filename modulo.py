

# ---------- VALIDACIONES ----------

def validar_codigo(codigo, productos):
    codigo = codigo.strip().upper()

    if codigo == "":
        return False

    if " " in codigo:
        return False

    if codigo in productos:
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


# ---------- FUNCIONES DEL SISTEMA ----------

def buscar_codigo(codigo, productos):
    codigo = codigo.strip().upper()

    if codigo in productos:
        return True

    return False


def stock_categoria(categoria, productos, inventario):
    categoria = categoria.strip().lower()
    stock_total = 0
    encontrados = 0

    for codigo in productos:
        categoria_producto = productos[codigo][1].lower()

        if categoria_producto == categoria:
            stock_total += inventario[codigo][0]
            encontrados += 1

    if encontrados == 0:
        print("No existen productos en esa categoría")
    else:
        print(f"Stock total de la categoría {categoria}: {stock_total}")


def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []

    for codigo in productos:
        nombre = productos[codigo][0]
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio >= precio_min and precio <= precio_max and stock > 0:
            resultados.append([nombre, codigo])

    resultados.sort()

    if len(resultados) == 0:
        print("No se encontraron productos en ese rango de precio")
    else:
        for producto in resultados:
            print(f"{producto[0]}--{producto[1]}")


def actualizar_precio(codigo, nuevo_precio, productos):
    codigo = codigo.strip().upper()

    if codigo not in productos:
        return False

    productos[codigo][2] = nuevo_precio
    return True


def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    codigo = codigo.strip().upper()

    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]

    return True


def eliminar_producto(codigo, productos, inventario):
    codigo = codigo.strip().upper()

    if codigo not in productos:
        return False

    del productos[codigo]
    del inventario[codigo]

    return True


def mostrar_productos(productos, inventario):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    for codigo in productos:
        print(f"CODIGO: {codigo}")
        print("--------------------------")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoría: {productos[codigo][1]}")
        print(f"Precio: ${productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")
        print("--------------------------")