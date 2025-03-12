"""
Generar código Python que permita imprimir la siguiente frase

Hola, mi nombre es Juan y tengo 25 años.


Debe usar las 3 formas estudiadas

Uso de operador % (porcentaje)
Uso de la función format
Uso de f-string

Deben existir tres print
"""

nombre_persona = "Juan"
anios = 25

cadena1 = "Hola, mi nombre es %s y tengo %d años." % (nombre_persona, anios)
cadena2 = "Hola, mi nombre es {} y tengo {} años.".format(nombre_persona, anios)
cadena3 = f"Hola, mi nombre es {nombre_persona} y tengo {anios} años."


print(cadena1)
print(cadena2)
print(cadena3)

