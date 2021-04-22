from typing import Iterable, Callable
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


def my_sorted(iterable: Iterable, key: Callable = None, reverse: bool = False, ) -> list:
    # выбор направления сортировки
    cmp: Callable = (
        lambda x, y: x > y,  # по возрастанию
        lambda x, y: x < y,  # по убыванию
    )[reverse]

    # функция извлечения - если отсутствует - берем как есть
    key: Callable = key if isinstance(key, Callable) else lambda k: k
    # извлекаем сортируемые данные
    result: list = [key(item) for item in iterable]

    for idx in range(1, len(result)):
        current: [int, float, str] = result[idx]
        position: int = idx

        # ищем позицию вставки с учетом направления и конца списка
        while cmp(result[position - 1], current) and position > 0:
            result[position] = result[position - 1]
            position -= 1

        result[position] = current

    return result


def my_func(a, b, c):
    try:
        sorted_list: list = my_sorted((a, b, c), reverse=True)
        return my_sum(sorted_list[:2])
    except TypeError as e:
        print(f'Вай!!! как не хорошо: {e}')


if __name__ == '__main__':
    unsorted_list = [20, 167, 67.3];
    print(my_func(*unsorted_list))
