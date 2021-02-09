def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_2 > arg_1 and arg_3 > arg_1:
        return arg_2 + arg_3
    else:
        return arg_1 + arg_3


print(my_func(1, 2, 3))
print(my_func(22, 1, 33))
print(my_func(220, 330, 1))
