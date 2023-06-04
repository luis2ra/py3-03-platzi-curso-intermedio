# class 09: Dictionary comprehensions

import math

def run():
    print('hola mundo!')
    
    # crear un diccionario, llave 1 al 100, valores los cubos respectivos
    cubes = {}

    for i in range(1, 101):
        cubes[i] = i ** 3
    # print(cubes)

    '''
    Esquema de un dictionary comprehensions:
    
    {key:value for key in iterable if condition}
    '''
    challenge = {i: i ** 3 for i in range (1, 101) if i % 3 != 0}
    # print(challenge)

    # crear un diccionario, llave 1 al 1000, donde los valores son las raices cuadradas
    challenge2 = {i: math.sqrt(i) for i in range (1, 1001)}
    print(challenge2)

if __name__ == '__main__':
    run()
