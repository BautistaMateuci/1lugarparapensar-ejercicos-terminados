"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

from ast import Lambda
from logging import exception


def funcionmax(n1 : int, n2 : int):
    if n1 > n2:
        return n1
    elif n1 == n2:
        return n1
    else:
        return n2
    
print(funcionmax(9,5))

"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def funcionmax3(n1: int, n2: int, n3: int):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n1 == n2 and n1 == n3:
        raise Exception('ERROR TODOS LOS VALORES SON IGUALES')
    else:
        return n3    
    
print(funcionmax3(1,2,3))

"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""
caracter = 'v'

def vocal(caracter):
    if caracter.upper() == 'A' or caracter.upper() == 'E' or caracter.upper() == 'I' or caracter.upper() == 'O' or caracter.upper() == 'U':
        return True
    else:
        return False

print(vocal(caracter))

"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
from functools import reduce

lista = [1,2,3,4]

def Suma(lista):
    resultado = reduce(lambda a, b : a + b, lista)
    return resultado

print(Suma(lista))

def multip(lista):
    resultado2 = reduce((lambda a, b: a * b), lista)
    return resultado2

print(multip(lista))

"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

cadena = 'estoy probando'

def inversa(cadena):
    return cadena[::-1]    

print(inversa(cadena))



"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
palabra = 'radar'

def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

print(es_palindromo(palabra))

"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
lista1 = [1,2,3,4]
lista2 = [1,5,6,7]
def superposicion(lista1, lista2):
    for item in lista1:
        for item2 in lista2:
            if item2 == item:
                return True
        
        return False

print(superposicion(lista1,lista2))

"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n):
    return '*' * n

print(generar_n_caracteres(100))

"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def procedimiento(lista):
    for i in lista:
        histograma = '*' * i
        print(histograma)

procedimiento([1,2,3,4])


# Estado en línea
# El objetivo de este reto es, dado un diccionario del estado online de las personas, contar el número de personas que están online.
# Escribe una función llamada online_count que toma un parámetro. El parámetro es un diccionario que mapea desde cadenas de nombres a la cadena "online" o "offline", como se ve arriba
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}




def online_count(statuses):
    genteonline = 0
    genteoffline = 0
    for valor in statuses:
        if statuses[valor] == 'online':
            genteonline += 1
        else:
            genteoffline += 1
    print(f'la cantidad de gente online es de {genteonline} ahora mismo y ofline estan {genteoffline} ahora mismo')


online_count(statuses)