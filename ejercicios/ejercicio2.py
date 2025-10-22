"""
Generar código Python que permita imprimir la siguiente frase

Hola, mi nombre es 
Juan y 
tengo un promedio 
de 6.3 en mi libreta.


Debe usar las 3 formas estudiadas

Uso de operador % (porcentaje)
Uso de la función format
Uso de f-string

Deben existir tres print
"""

######################
# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
######################
nombre_persona = "Juan"
nota1 = 8
nota2 = 4
nota3 = 7
nota_promedio = (nota1+nota2+nota3)/3

# VARIABLES CONSTANTES
COLOR_ROJO = "\033[31m"
COLOR_VERDE = "\033[32m"
COLOR_CYAN = "\u001b[36m"

######################
# FORMATEO DE CADENAS
######################
# Para limitar la cantidad de decimales a 1 utilizaré el siguiente formateo: '.nf' donde n corresponde a 1

# Uso de %
cadena = COLOR_ROJO+"Hola, mi nombre es %s y tengo un promedio de %.1f en mi libreta" % (nombre_persona, nota_promedio)
print(cadena)

# Uso de str.format()
cadena = COLOR_VERDE+"Hola, mi nombre es {} y tengo un promedio de {:.1f} en mi libreta".format(nombre_persona, nota_promedio)
print(cadena)

# Uso de f-string
cadena = COLOR_CYAN+f"Hola, mi nombre es {nombre_persona} y tengo un promedio de {nota_promedio:.1f} en mi libreta"
print(cadena)

