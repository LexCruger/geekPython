def print_user_data(**user_data) -> None:
    print(f'Имя: {user_data.get("name")}, фамилия: {user_data.get("surname")},'
          f' год рождения: {user_data.get("birth_year")}, город проживания: {user_data.get("city")},'
          f' email: {user_data.get("email")}, телефон: {user_data.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Lex',
        'surname': 'Cruger',
        'birth_year': '1970',
        'city': 'NY',
        'email': 'LexCruger@NY.ru',
        'phone': '+100000',
    }

    print_user_data(**user)
