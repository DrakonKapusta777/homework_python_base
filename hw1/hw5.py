proceeds = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
profit = proceeds - costs

if proceeds > costs:
    print("Фирма работает в прибыль!")
    print(f'Рентабельность составляет: {profit / proceeds * 100:.2f} %')
    staff = int(input("Укажите численность персонала: "))
    print(f'Прибыль в расчете на одного сотрудника составляет: {profit / staff:.2f} руб.')
elif proceeds == costs:
    print("Фирма работает в ноль!")
else:
    print("Фирма работает в убыток!")
