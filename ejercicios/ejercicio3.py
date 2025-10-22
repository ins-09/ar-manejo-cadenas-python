"""

Pedir al usuario el nombre de un producto, su precio y la cantidad comprada. Luego, mostrar el total a pagar con las tres formas de formateo.


Producto: Laptop
Precio unitario: 750.50
Cantidad: 2
Total a pagar: 1501.00
"""

######################
# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
######################
producto = input("1. Nombre del producto: ")
precio = float(input("2. Precio: "))
cantidad = int(input("3. Escriba la cantidad que sea comprar: "))
total_pagar = precio * cantidad
cadena = ""

# VARIABLES CONSTANTES
COLOR_ROJO = "\033[31m"
COLOR_VERDE = "\033[32m"
COLOR_CYAN = "\u001b[36m"
RESET = "\033[0m"

######################
# FORMATEO DE CADENAS
######################
# Para limitar la cantidad de decimales a 2 utilizaré el siguiente formateo: '.nf' donde n corresponde a 2

# Uso de %
cadena = COLOR_ROJO+"""
     Operador porcentaje
_____________________________
    [Detalles de la compra]
        1. Producto - %s
        2. Precio - $%.2f
        3. Cantidad - %d
        
        Total a pagar: $%.2f
_____________________________
""" % (producto, precio, cantidad, total_pagar)
print(cadena)

# Uso de str.format()
cadena = COLOR_VERDE+"""
     str.format()
_____________________________
    [Detalles de la compra]
        1. Producto - {}
        2. Precio - ${:.2f}
        3. Cantidad - {}
        
        Total a pagar: ${:.2f}
_____________________________
""".format(producto, precio, cantidad, total_pagar)
print(cadena)

# Uso de f-string
cadena = COLOR_CYAN+f"""
     f-string
__________________________________
    [Detalles de la compra] 
        1. Producto - {producto} 
        2. Precio - ${precio:.2f}
        3. Cantidad - {cantidad}
        
        Total a pagar: ${total_pagar:.2f}
__________________________________
"""
print(cadena)

