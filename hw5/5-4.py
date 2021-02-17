rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text4-1.txt", "r", encoding="utf-8") as text4_1:
    with open("text4-2.txt", "w", encoding="utf-8") as text4_2:
        for line in text4_1:
            line = line.split()
            text4_2.write(rus[line[0]] + " - " + line[2] + "\n")
