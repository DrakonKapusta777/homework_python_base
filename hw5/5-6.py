my_dict = {}
with open("text6.txt", encoding="utf-8") as text6:
    for line in text6:
        subj, ex = line.split(':')
        ex = ex.split()
        num = 0
        for i in ex:
            if "-" in i:
                continue
            nums, _ = i.split('(')
            num += int(nums)
        my_dict[subj] = num
print(my_dict)
