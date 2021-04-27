def int_func(words):
    result = ""
    for word in words:
        word = word[0].upper() + word[1:]
        result += word + " "
    return result


string = input("Введите строку из слов, разделенных пробелом, где каждое слово состоит из латинских букв "
               "в нижнем регистре: ")
print(int_func(string.split()))