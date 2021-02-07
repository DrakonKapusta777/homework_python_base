user_list = list(input("Укажите элементы для списка через пробел: ").split())
print(f'Ваш список: {" ".join(user_list)}')
for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
print(f'Список с переставленными элементами: {" ".join([i for i in user_list])}')
