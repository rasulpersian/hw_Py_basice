"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_number(first_arg, second_arg):
    return first_arg / second_arg


while True:
    first_arg, second_arg = list(map(int, input('Введите пару чисел: ').split()))
    # Валидация данных
    if first_arg == 0 or first_arg == 0:
        print('Деление на 0 (ноль)!!!')
    else:
        print(f'Результать деления {first_arg} / {second_arg} = {division_number(first_arg, second_arg)}')
        break
