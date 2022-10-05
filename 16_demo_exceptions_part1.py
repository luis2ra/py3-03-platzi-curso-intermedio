def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        print('class 16: poniendo a prueba manejo de excepciones')
        num = int(input("ingresa un número: "))
        print(divisors(num))
        print('fin del programa')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    run()