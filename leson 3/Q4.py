from typing import Iterable
number_types = (int, float, complex)

def my_pow(base: number_types, exp: number_types, mod: number_types = None) -> number_types:

    if not isinstance(base, number_types) or not isinstance(exp, number_types):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, number_types):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    if mod is not None and exp < 0:
        raise ValueError('base is not invertible for the given modulus')

    result = 1

    for _ in my_range(my_abs(exp)):
        result *= base

    result = 1 / result if exp < 0 else result

    if mod is None:
        return result
    else:
        return result % mod

def my_range(start: int, stop: int = None, step: int = 1) -> Iterable:
    # базовые проверки
    if (
            not isinstance(start, int)
            or not (stop is None or isinstance(stop, int))
            or not (step is None or isinstance(step, int))
    ):
        raise TypeError(f"'{start.__class__.__name__}' "
                        f"object cannot be interpreted as an integer")

    if stop is None:
        stop = start
        start = 0

    while start < stop:
        yield start
        start += step

def my_abs(x: number_types) -> number_types:

    if isinstance(x, complex):
        return sqrt(x.real ** 2 + x.imag ** 2)

    return -x if x < 0 else x

def my_func(x, y):
    if x < 0:
        raise ValueError('Неверный аргумент x')

    if int(y) != float(y) or y >= 0:
        raise ValueError('Неверный аргумент y')

    return my_pow(x, y)


if __name__ == '__main__':
    try:
        print(my_func(2, -4))
    except (ValueError, TypeError) as e:
        print(e)
