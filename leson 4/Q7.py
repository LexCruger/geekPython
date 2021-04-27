from math import factorial


def fact(n: int):

    for i in range(1, n + 1):
        yield factorial(i)


if __name__ == '__main__':
    input_data = input('Пожалуйста введите количество вычисленных факториалов: ')

    try:
        value = int(input_data)
    except ValueError as e:
        print(e)
        exit(1)

    for el in fact(value):
        print(el)
