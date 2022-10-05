def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:  # se detecto con el Debug de VSCode que el valor correcto era 0, y no 1
            # import pdb; pdb.set_trace()
            # breakpoint() => es una funcion nativa que usa pdb a partir de python 3.7
            divisors.append(i)
    return divisors


def run():
    print('class 14: debugging')
    num = int(input("ingresa un numero: "))
    print(divisors(num))
    print('fin del programa')


if __name__ == '__main__':
    run()