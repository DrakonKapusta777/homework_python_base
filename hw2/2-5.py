my_list = [7, 5, 3, 3, 2]

while True:
    user_num = int(input("Введи натуральное число (для выхода введите 111): "))
    flag = False
    if user_num != 111:
        for j in range(len(my_list)):
            if my_list[j] < user_num:
                my_list.insert(j, user_num)
                flag = True
                break
        if not flag:
            my_list.append(user_num)
        print(my_list)
    else:
        break


