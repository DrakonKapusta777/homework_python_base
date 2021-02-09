def my_f():
    sum_result = 0
    find_q = False
    while not find_q:
        user_numbers = input('Введите числа через пробел, для завершения введите "q": ').split()
        result = 0
        for el in range(len(user_numbers)):
            if user_numbers[el] == 'q':
                find_q = True
                break
            else:
                result = result + int(user_numbers[el])
        sum_result = sum_result + result
        print(f'Сумма чисел: {sum_result}, ')
    print(f'Окончательная сумма чисел: {sum_result}')


my_f()
