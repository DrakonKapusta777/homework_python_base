user_str = input('Введите строку разделяя элементы пробелами: ').split()

for i, word in enumerate(user_str, 1):
    print(f'{i}) {word[:10]}')
