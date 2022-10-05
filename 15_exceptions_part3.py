# ejemplo modificado donde se incluye el uso de la sentencia "raise" para el manejo de errores

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as e:
        print(e)
        return False


def run():
    try:
        print("class 15: exceptions handling")
        print(palindrome(""))  # aca se coloca un error inducido
    except TypeError:
        print("Solo se puede ingresar strings")


if __name__ == '__main__':
    run()
