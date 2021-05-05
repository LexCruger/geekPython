FILENAME = "Q1.txt"


if __name__ == "__main__":
    while True:
        user_input = input('Введите произвольную строку: ')
        if not user_input:
            break

        try:
            with open(FILENAME, 'a', encoding='utf-8') as fh:
                fh.write(f'{user_input}\n')
        except IOError as e:
            print(e)
            break
