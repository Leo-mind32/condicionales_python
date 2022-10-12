# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palab_1 = str(input("Ingrese la primer palabra: ").lower())
palab_2 = str(input("Ingrese la segunda palabra: ").lower())
palab_3 = str(input("Ingrese la tercer palabra: ").lower())


print("¿Como desea ordenar las palabras?")

opcion = int(input("SELECCIONE UNA OPCIÓN: 1- Ordenar alfabeticamente o 2- Por cantidad de letras: "))

if opcion == 1:
    if palab_1 > palab_2 and palab_1 > palab_3:
        mayor = palab_1
        if palab_2 > palab_3:
            intermedia = palab_2
            menor = palab_3
        else:
            intermedia = palab_3
            menor = palab_2
        print(f'{mayor}, {intermedia}, {menor}.')
    
    elif palab_2 > palab_3:
        mayor = palab_2
        if palab_1 > palab_3:
            intermedia = palab_1
            menor = palab_3
        else:
            intermedia = palab_3
            menor = palab_1
        print(f'{mayor}, {intermedia}, {menor}.')
    
    else:
        mayor = palab_3
        if palab_1 > palab_2:
            intermedia = palab_1
            menor = palab_2
        else:
            intermedia = palab_2
            menor = palab_1
        print(f'{mayor}, {intermedia}, {menor}.')        







