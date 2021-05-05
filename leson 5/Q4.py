SRC_FILENAME = "Q4.txt"
DST_FILENAME = "Q4_dst.txt"
NUMERALS = ('Один', 'Два', 'Три', 'Четыре')

if __name__ == "__main__":
    try:
        with open(SRC_FILENAME, encoding='utf-8') as fhs:
            lines = fhs.readlines()

        numbers = [int(line[-2]) for line in lines if line != '\n']
        content = "\n".join(f'{NUMERALS[n - 1]} - {n}' for n in numbers)

        with open(DST_FILENAME, 'w', encoding='utf-8') as fhd:
            fhd.write(content)
    except IOError as e:
        print(e)
    except (ValueError, IndexError):
        print("Неконсистентные данные")
