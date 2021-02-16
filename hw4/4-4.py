from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Исходный список:\n{my_list}\nСписок без повторений:\n{new_list}")
