# class 10: lambad function

# lambda argumentos: expresion

# función palindrome aplicando una funcion lambda
palindrome = lambda string: string == string[::-1]

print('chequeo de palindrome: ', palindrome('ana'))

# función palindrome normal sin aplicar lambda
def palindrome2(string):
    return string == string[::-1]

print('chequeo de palindrome2: ', palindrome2('ana'))
