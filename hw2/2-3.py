seasons_list = ['зима', 'весна', 'лето', 'осень', 'зима']
seasons_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}

while True:
    user_month = input('Введите номер месяца: ')
    if user_month.isdigit() and 1 <= int(user_month) <= 12:
        user_month = int(user_month)
        print(f'{user_month}-й месяц года - {seasons_list[user_month // 3]}')
        print(f'{user_month}-й месяц года - {seasons_dict[user_month // 3]}')
        break
    else:
        print('Необходимо ввести число от 1 до 12!')
