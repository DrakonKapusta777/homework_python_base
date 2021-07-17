def my_f(x, y):
    return x ** y


def my_f2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(f'Ответ: {my_f(float(input("Введите число возводимое в степень: ")), int(input("Введите степень: ")))}')
print(f'Ответ: {my_f2(float(input("Введите число возводимое в степень: ")), int(input("Введите степень: ")))}')
