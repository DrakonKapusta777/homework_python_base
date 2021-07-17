def div():
    try:
        arg_1 = int(input("Введите делимое: "))
        arg_2 = int(input("Введите делитель: "))
        result = arg_1 / arg_2
    except ValueError:
        return 'Неверное значение!'
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"
    return result


print(f'Ответ: {div()}')
