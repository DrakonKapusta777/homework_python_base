with open("text1.txt", "w", encoding="utf-8") as text1:
    line = " "
    while line != "":
        line = input("Введите строку: ")
        text1.write(f'{line}\n')
