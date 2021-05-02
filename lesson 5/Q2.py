import sys


FILENAME = "Q2.txt"


if __name__ == "__main__":
    try:
        with open(FILENAME, encoding='utf-8') as fh:
            lines = [line for line in fh.readlines() if line != '\n']
    except IOError as e:
        print(e)
        sys.exit(1)

    print(f"В файле непустых строк:", len(lines))

    for line in lines:
        print(f'Строка {line[:50]}... содержит {len(line.split())} слов')
