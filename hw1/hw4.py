user_number = int(input("Введите число: "))

result = -1
while user_number > 10:
    n = user_number % 10
    user_number = user_number // 10
    if n > result:
        result = n
print("Самая большая цифра в числе:", result)
