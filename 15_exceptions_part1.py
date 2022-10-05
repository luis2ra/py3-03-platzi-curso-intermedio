# ejemplo inicial donde no se usa manejo de excepciones

def palindrome(string):
    return string == string[::-1]


def run():
    print("class 15: exceptions handling")
    print(palindrome(1))  # aca se coloca un error inducido


if __name__ == '__main__':
    run()
