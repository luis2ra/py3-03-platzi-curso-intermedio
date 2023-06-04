# class 11: High order functions: filter

def run():
    print('class 11: high order functions (part 2 - filter)')

    # de una lista de numeros, imprimir los numeros impares, usando 'list comprehensions'
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = [i for i in my_list if i % 2 != 0]
    print(odd)

    # de una lista de numeros, imprimir los numeros impares, usando la función "filter"
    # filter(function, iterable)
    odd2 = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd2)

if __name__ == '__main__':
    run()
