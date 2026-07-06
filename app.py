# aplicación principal,
from modulo import leer_opcion
from modulo import validar_codigo, validar_nombre, validar_categoria
from modulo import validar_precio, validar_disponible
from modulo import validar_stock, validar_vendidos
from modulo import buscar_codigo, stock_categoria, buscar_precio
from modulo import actualizar_precio, agregar_producto
from modulo import eliminar_producto, mostrar_productos


def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================
""")
    

def pedir_entero(mensaje, funcion_validar, mensaje_error):
    while True:
        try:
            numero = int(input(mensaje))

            if funcion_validar(numero):
                return numero
            else:
                print(mensaje_error)

        except ValueError:
            print("Debe ingresar un número entero")


def pedir_codigo_nuevo(productos):
    while True:
        codigo = input("Ingrese código del producto: ").strip().upper()

        if validar_codigo(codigo, productos):
            return codigo
        else:
            print("Código inválido o ya existente")


def pedir_nombre():
    while True:
        nombre = input("Ingrese nombre del producto: ").strip()

        if validar_nombre(nombre):
            return nombre
        else:
            print("Nombre inválido")


def pedir_categoria():
    while True:
        categoria = input("Ingrese categoría del producto: ").strip()

        if validar_categoria(categoria):
            return categoria
        else:
            print("Categoría inválida")


def pedir_disponible():
    while True:
        opcion = input("¿Está disponible? s/n: ").strip().lower()

        if validar_disponible(opcion):
            disponible = opcion == "s"
            return disponible
        else:
            print("Debe ingresar s o n")


def opcion_stock_categoria(productos, inventario):
    categoria = input("Ingrese categoría a buscar: ").strip()

    if validar_categoria(categoria):
        stock_categoria(categoria, productos, inventario)
    else:
        print("Categoría inválida")


def opcion_buscar_precio(productos, inventario):
    precio_min = pedir_entero(
        "Ingrese precio mínimo: ",
        validar_stock,
        "El precio mínimo debe ser mayor o igual a cero"
    )

    while True:
        precio_max = pedir_entero(
            "Ingrese precio máximo: ",
            validar_stock,
            "El precio máximo debe ser mayor o igual a cero"
        )

        if precio_max >= precio_min:
            break
        else:
            print("El precio máximo debe ser mayor o igual al precio mínimo")

    buscar_precio(precio_min, precio_max, productos, inventario)


def opcion_actualizar_precio(productos):
    while True:
        codigo = input("Ingrese código del producto: ").strip().upper()

        if buscar_codigo(codigo, productos):
            nuevo_precio = pedir_entero(
                "Ingrese nuevo precio: ",
                validar_precio,
                "El precio debe ser mayor que cero"
            )

            actualizado = actualizar_precio(codigo, nuevo_precio, productos)

            if actualizado:
                print("Precio actualizado correctamente")
            else:
                print("No se pudo actualizar el precio")

        else:
            print("Código inexistente")

        continuar = input("¿Desea actualizar otro precio? s/n: ").strip().lower()

        if continuar != "s":
            break


def opcion_agregar_producto(productos, inventario):
    codigo = pedir_codigo_nuevo(productos)
    nombre = pedir_nombre()
    categoria = pedir_categoria()

    precio = pedir_entero(
        "Ingrese precio del producto: ",
        validar_precio,
        "El precio debe ser mayor que cero"
    )

    disponible = pedir_disponible()

    stock = pedir_entero(
        "Ingrese stock: ",
        validar_stock,
        "El stock debe ser mayor o igual a cero"
    )

    vendidos = pedir_entero(
        "Ingrese cantidad vendida: ",
        validar_vendidos,
        "Los vendidos deben ser mayor o igual a cero"
    )

    agregado = agregar_producto(
        codigo,
        nombre,
        categoria,
        precio,
        disponible,
        stock,
        vendidos,
        productos,
        inventario
    )

    if agregado:
        print("Producto agregado correctamente")
    else:
        print("No se pudo agregar el producto")


def opcion_eliminar_producto(productos, inventario):
    codigo = input("Ingrese código del producto a eliminar: ").strip().upper()

    eliminado = eliminar_producto(codigo, productos, inventario)

    if eliminado:
        print("Producto eliminado correctamente")
    else:
        print("Código inexistente")


def main():
    productos = {}
    inventario = {}

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            opcion_stock_categoria(productos, inventario)

        elif opcion == 2:
            opcion_buscar_precio(productos, inventario)

        elif opcion == 3:
            opcion_actualizar_precio(productos)

        elif opcion == 4:
            opcion_agregar_producto(productos, inventario)

        elif opcion == 5:
            opcion_eliminar_producto(productos, inventario)

        elif opcion == 6:
            mostrar_productos(productos, inventario)

        elif opcion == 7:
            print("Programa finalizado")
            break


main()