# assert condicion, mensaje de error

def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]


def run():
    print("class 17: assert statements")
    print(palindrome(""))  # aca se coloca un error inducido


if __name__ == '__main__':
    run()