# class 08: List comprehensions

def run():
    for x in range(1, 101):
        print('Para ', x, ', el cuadrado es:', x * x)

    '''
    Esquema de un list comprehensions:
    
    [element for element in iterable if condition]
    '''
    [print(x ** 2) for x in range(1,10)]

    squares = []
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    challenge = []
    challenge = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    # print(challenge)

if __name__ == '__main__':
        run()
