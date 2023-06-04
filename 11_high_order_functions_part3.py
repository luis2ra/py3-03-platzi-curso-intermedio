# class 11: High order functions: map

def run():
    print('class 11: high order functions (part 3 - map)')

    # de una lista de numeros, obtener los cuadrados, usando 'list comprehensions'
    my_list = [1, 2, 3, 4, 5]
    squares = [i ** 2 for i in my_list]
    print(squares)

    # de una lista de numeros, obtener los cuadrados, usando la función "map"
    # map(function, iterable, ...)
    squares2 = list(map(lambda x: x ** 2, my_list))
    print(squares2)


if __name__ == '__main__':
    run()
