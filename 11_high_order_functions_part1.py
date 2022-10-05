def saludo(func):
    func()

def hola():
    print('hola!')

def adios():
    print('adios!')

def run():
    print('class 11: high order functions (part 1)')
    saludo(hola)
    saludo(adios)

if __name__ == '__main__':
    run()
