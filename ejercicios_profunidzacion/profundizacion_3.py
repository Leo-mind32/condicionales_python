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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# 1- ¿Cuáles de ellas es la máxima temperatura ingresada?

temp_1 = float(input("Ingrese la primer temperatura: "))
temp_2 = float(input("Ingrese la segunda temperatura: "))
temp_3 = float(input("Ingrese la tercer temperatura: "))

if temp_1 > temp_2 and temp_1 > temp_3:
    print("La maxima temperatura ingresada es: ", temp_1,'°C')
elif temp_2 > temp_1 and temp_2 > temp_3:
    print("La maxima temperatura ingresada es: ", temp_2,'°C')
else:
    print("La maxima temperatura ingresada es: ", temp_3,'°C')

# 2 - ¿Cuáles de ellas es la mínima temperatura ingresada?

if temp_1 < temp_2 and temp_1 < temp_3:
    print("La minima temperatura ingresada es: ", temp_1,'°C')
elif temp_2 < temp_1 and temp_2 < temp_3:
    print("La minima temperatura ingresada es: ", temp_2,'°C')
else:
    print("La minima temperatura ingresada es: ", temp_3,'°C')

# 3 - ¿Cuál es el promedio de las temperaturas ingresadas?

promedio = (temp_1 + temp_2 + temp_3) / 3
print("El promedio de las temperaturas ingresadas es: ", promedio)