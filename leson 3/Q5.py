from typing import Iterable

number_types = (int, float, complex)


def my_sum(iterable: Iterable, start: number_types = 0) -> [int, float]:

    # базовые проверки
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{iterable.__class__.__name__}' object is not iterable")

    if not isinstance(start, number_types):
        raise TypeError(f"my_sum() can't sum strings [use ''.join(seq) instead]")

    result = start

    for item in iterable:
        # падаем, если типы не совместимы
        if not isinstance(item, number_types):
            raise TypeError(f"unsupported operand type(s) for +:"
                            f" 'int' and '{item.__class__.__name__}'")

        result += item

    return result

stop_index = None
result = 0


def convert_item(item: str) -> (int, float):

    try:
        float_item = float(item)
        int_item = int(item.split('.')[0])
    except ValueError:
        raise

    if float_item == int_item:
        return int_item
    else:
        return float_item


if __name__ == '__main__':
    while stop_index is None:
        data = input('Пожалуйста введите числа разделённые\n'
                     'пробелами (допускаются int, float): ').split()

        try:
            stop_index = data.index('q')
            data = data[:stop_index]
        except ValueError:
            pass

        try:
            data = [convert_item(i) for i in data]
        except ValueError:
            print("Введенные данные содержат неверный тип")
            continue

        result += my_sum(data)

        print(result)

