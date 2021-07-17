with open("text5.txt", "w", encoding="utf-8") as text5:
    text5.write(f"{' '.join([str(i) for i in range(1, 51)])}")
with open("text5.txt", "r", encoding="utf-8") as text5:
    numbers = [int(i) for i in text5.read().split()]
    print(f'Сумма чисел: {sum(numbers)}')
