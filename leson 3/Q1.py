number_types = (int, float, complex)
def my_div(x: number_types, y: number_types) -> number_types:
    if not (isinstance(x, number_types) and isinstance(y, number_types)):
        raise TypeError(f"unsupported operand type(s) for my_div: "
                        f"'{x.__class__.__name__}' and '{y.__class__.__name__}'")

    return x / y

input_patterns = (
    ('Пожалуйста введите делимое: ', float,),
    ('Пожалуйста введите делитель: ', float,),
)

if __name__ == '__main__':
    div_data = []

    while not div_data:
        for item_title, item_type in input_patterns:
            try:
                div_data.append(item_type(input(item_title)))
            except ValueError:
                print("Вводимые данные должны быть числом")
                div_data.clear()

    try:
        quotient = my_div(*div_data)
        print(f'Результа: {quotient}')
    except ZeroDivisionError:
        print('Попытка деления на ноль')
