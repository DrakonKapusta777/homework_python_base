user_sec = int(input("Введите количество секунд: "))

hours = user_sec // 3600
minutes = (user_sec - hours * 3600) // 60
seconds = user_sec - hours * 3600 - minutes * 60

print(hours, minutes, seconds, sep=":")
