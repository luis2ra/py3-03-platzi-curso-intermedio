# assert condicion, mensaje de error

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    print("class 17: assert statements")
    num = input("ingresa un número: ")
    assert num.isnumeric(), "Debe ingresar un valor numérico"
    print(divisors(int(num)))
    print('fin del programa')


if __name__ == '__main__':
    run()
