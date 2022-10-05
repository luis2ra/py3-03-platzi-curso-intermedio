def run():
    print('class 07: Listas y diccionarios anidados')
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Luis", "lastname": "Altuve"}

    super_list = [
        {"firstname": "Dayana", "lastname": "Campos"},
        {"firstname": "Mariela", "lastname": "Suarez"},
        {"firstname": "Yajaira", "lastname": "Erazo"},
        {"firstname": "Rosalinda", "lastname": "Rivas"},
        {"firstname": "Lucia", "lastname": "Cuevas"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "float_nums": [-0.5, 0.5, 1.2, 2.3, 3.3],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for index, item in enumerate(super_list):
        print(index, "-", item)

if __name__ == '__main__':
    run()
