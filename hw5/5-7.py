import json

my_dict = {}
aver_profit = 0
num = 0
with open("text7.txt", encoding="utf-8") as text7:
    for line in text7:
        name, _, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            aver_profit += profit
            num += 1
        my_dict[name] = profit
aver_profit /= num
with open("json7.json", "w", encoding="utf-8") as f:
    json.dump([my_dict, {"Средняя прибыль: ": aver_profit}], f, ensure_ascii=False)
