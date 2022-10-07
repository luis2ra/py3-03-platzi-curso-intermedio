import numbers


def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as read_file:
        for row in read_file:
            numbers.append(int(row))
    print(numbers)


def write_using_w():
    names = ["Luis", "Miguel", "Rosmy", "Richard", "Rosa", "Luisin", "Yolimar", "Rocío"]
    with open("./files/names.txt", "w", encoding="utf-8") as ww:
        for name in names:
            ww.write(name)
            ww.write("\n")


def write_using_a():
    names = ["Luis", "Miguel", "Rosmy", "Richard", "Rosa", "Luisin", "Yolimar", "Rocío"]
    with open("./files/names2.txt", "a", encoding="utf-8") as wa:
        for name in names:
            wa.write(name)
            wa.write("\n")


def run():
    print("class 19: files handling")
    read()
    write_using_w()
    write_using_a()


if __name__ == '__main__':
    run()
