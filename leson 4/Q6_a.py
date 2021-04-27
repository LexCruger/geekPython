from typing import Callable
from itertools import count, takewhile

number_types = (int, float, complex)


def my_count(start: number_types = 0, step: number_types = 1):

    while True:
        yield start
        start += step


def get_count_list1(func: Callable, start: int = 0, stop: int = 10) -> list:

    items = []

    iterable = func(start, 1)

    while True:
        item = next(iterable)
        if item >= stop:
            break

        items.append(item)

    return items


def get_count_list2(func: Callable, start: int = 0, stop: int = 10) -> list:

    items = []

    for item in func(start, 1):
        if item >= stop:
            break

        items.append(item)

    return items


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа от 0 до 10: ')

    try:
        value = int(input_data)
        if not 0 < value <= 10:
            raise ValueError("Number can't be less than 0 or more than 10")
    except ValueError as e:
        print(e)
        exit(1)

    stop = 10

    itertools_count_list1 = get_count_list1(count, value, stop)
    print(f"get_count_list1(itertools.count)", itertools_count_list1)

    custom_my_count_list1 = get_count_list1(my_count, value, stop)
    print('get_count_list1(custom my_count)', custom_my_count_list1)

    itertools_count_list2 = get_count_list2(count, value, stop)
    print(f"get_count_list2(itertools.count)", itertools_count_list2)

    custom_my_count_list2 = get_count_list2(my_count, value, stop)
    print('get_count_list2(custom my_count)', custom_my_count_list2)

    exotic_count_list = list(takewhile(int(stop).__gt__, count(value, 1)))
    print('exotic_count_list', exotic_count_list)
