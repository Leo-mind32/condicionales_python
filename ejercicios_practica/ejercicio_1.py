# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las siguientes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print("El número {} es mayor que {}".format(numero_1, numero_2))
else:
    print("El número {} es mayor que {}".format(numero_2, numero_1))


# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 > 0:
    print("El número es positivo")
else:
    if numero_1 < 0:
        print("El número es negativo")
    else:
        print("El número es cero")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if numero_1 > 0 and numero_1 < 100:
    print("El número {} es mayor que 0 y menor a 100".format(numero_1))
else:
    print("No se cumple la condición.")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if numero_1 < 10 or numero_2 > -2:
    print("El número {} es menor a 10".format(numero_1))
    print("El número {} es mayor a -2".format(numero_2)) 
else:
    print("El número ingresado es incorrecto")




    
