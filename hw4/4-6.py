from itertools import count, cycle


for i in count(int(input('Введите целое число для начала генерации последовательности из чисел. Для выхода введите "q" '))):
    print(i, end='')
    leave = input()
    if leave == 'q':
        break


my_list = input('Введите элементы списка через пробел, для выхода - "q": ').split()
func_list = cycle(my_list)
leave = None

while leave != 'q':
    print(next(func_list), end='')
    leave = input()
