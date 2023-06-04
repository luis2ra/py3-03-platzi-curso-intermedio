# class 12: Proyecto de filtrado de datos

# definicion de la constante DATA
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    print('class 12: filtering data')

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print(all_python_devs)

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print(all_platzi_workers)

    all_adults_workers = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # print(all_adults_workers)
    adults_only_name = list(map(lambda worker: worker["name"], all_adults_workers))
    print(adults_only_name)

    # el caracter '|' une dos diccionarios (nuevo feature a partir de python 3.9)
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    print(old_people)

    challenge1 = list(map(lambda worker: worker["name"], list(filter(lambda worker: worker["language"] == "python", DATA))))
    print(challenge1)

    challenge2 = list(map(lambda worker: worker["name"], list(filter(lambda worker: worker["organization"] == "Platzi", DATA))))
    print(challenge2)

    # faltaria hacer el challenge3 (all_adults_workers) y challenge4 (old_people) as lists comprehensions


if __name__ == '__main__':
    run()
