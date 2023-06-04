# class 10: lambda function

'''
Esquema de una lambda function:

lambda argumento(s): expresion

Recuerda que esta funcion es asignada a una variable (llamada identificador!!!)
'''

# función palindrome aplicando una funcion lambda
palindrome = lambda string: string == string[::-1]

print('chequeo de palindrome: ', palindrome('ana'))

# función palindrome normal sin aplicar lambda
def palindrome2(string):
    return string == string[::-1]

print('chequeo de palindrome2: ', palindrome2('ana'))

'''
la funcion anonima (lambda) es una forma simplificada de hacer una funcion, donde:

- en lugar de usar la palabra reservada "def", se usa la palabra reservada "lambda"
- en lugar de usar parentesis para los argumentos, estos no se usan
- el identificador es equivalente al nombre de la funcion
- se omite la palabra reservada "return"
'''
