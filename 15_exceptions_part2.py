# ejemplo modificado donde se usa try/except para el manejo de errores

def palindrome(string):
    return string == string[::-1]


def run():
    try:
        print("class 15: exceptions handling")
        print(palindrome(1))  # aca se coloca un error inducido
        print("esta linea no se muestra...")
    except TypeError:
        print("Solo se puede ingresar strings")


if __name__ == '__main__':
    run()
