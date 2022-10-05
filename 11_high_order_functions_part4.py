import functools

def run():
    print('class 11: high order functions (part 4)')

    # de una lista de numeros, obtener la multiplicacion de todos, usando for
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = 1
    for i in my_list:
        all_multiplied *= i
    print(all_multiplied)

    # de una lista de numeros, obtener la multiplicacion de todos, usando la función "reduce"
    # functools.reduce(function, iterable[, initializer])
    all_multiplied2 = functools.reduce(lambda a, b: a * b, my_list)
    print(all_multiplied2)


if __name__ == '__main__':
    run()