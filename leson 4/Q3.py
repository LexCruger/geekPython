if __name__ == '__main__':
    result = (i for i in range(20, 241) if not i % 20 or not i % 21)

    print(f"Is generator object: {result.__class__.__name__ == 'generator'}")
    print(list(result))
