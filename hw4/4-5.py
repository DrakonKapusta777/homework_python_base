from functools import reduce


def func_1(el1, el2):
    return el1 * el2


my_list = [el for el in range(100, 1001, 2)]
print(f"Список:\n{my_list}\nПроизведение всех элементов списка:\n{reduce(func_1, my_list)}")
