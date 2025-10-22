"""

Pedir al usuario una temperatura en grados Celsius y convertirla a Fahrenheit usando la fórmula

F = (C × 9/5) + 32

Presentar la conversión con las tres formas de formateo.


Ejemplo de salida:

La temperatura de 25.0°C equivale a 77.0°F.

"""

######################
# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
######################
temperatura_grados_celsius = float(input("Temperatura grados Celsius: "))
formula = (temperatura_grados_celsius*(9/5)) + 32
temperatura_grados_fahrenheit = formula
cadena = ""


# VARIABLES CONSTANTES
COLOR_ROJO = "\033[31m"
COLOR_VERDE = "\033[32m"
COLOR_CYAN = "\u001b[36m"
RESET = "\033[0m"

######################
# FORMATEO DE CADENAS
######################
# Para limitar la cantidad de decimales a 1 utilizaré el siguiente formateo: '.nf' donde n corresponde a 1

# Uso de %
cadena = COLOR_ROJO+"""
_________ Porcentaje _________
  La temperatura de %.1fºC equivale a %.1fºF
""" % (temperatura_grados_celsius, temperatura_grados_fahrenheit)
print(cadena)

# Uso de str.format()
cadena = COLOR_VERDE+"""
________ str.format() ________
  La temperatura de {:.1f}ºC equivale a {:.1f}ºF
""".format(temperatura_grados_celsius, temperatura_grados_fahrenheit)
print(cadena)

# Uso de f-string
cadena = COLOR_CYAN+f"""
__________ f-string __________
  La temperatura de {temperatura_grados_celsius:.1f}ºC equivale a {temperatura_grados_fahrenheit:.1f}ºF
"""
print(cadena)

