def my_function():
    print(" Задать длинну списка  ")
    a = int(input())
    print(" Задать максимальное значение в списке ")
    b = int(input())
    from random import randint
    list = [randint(1, b) for i in range(a)]
    print(list)

my_function()