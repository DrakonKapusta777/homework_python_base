with open("text2.txt", "r", encoding="utf-8") as text2:
    arr_name = []
    arr_inc = []
    my_list = text2.read().split("\n")
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            arr_name.append(i[0])
        arr_inc.append(i[1])
print(f'Сотрудники с окладом меньше 20000 RUR: {arr_name}\nСредний оклад: {sum(map(float, arr_inc)) / len(arr_inc):.2f}')
