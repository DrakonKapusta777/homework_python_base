with open("text1.txt", "r", encoding="utf-8") as text1:
    lines = -1
    words = 0
    for line in text1:
        lines += 1
        words += len(line.split())
print(f'Строк в файле: {lines}')
print(f'Слов в файле: {words}')
