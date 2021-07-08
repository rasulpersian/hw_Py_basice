


def exe_6(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


def exe_6_use():
    print(exe_6(input('Input text: ').split()))


def sep():
    print('+' * 30)


def refresh():
    print('Выберите задание и его решение')
    sep()
    print('Задание 1. Введите: 1')
    sep()
    print('Задание 2. Введите: 2')
    sep()
    print('Задание 3. Введите: 3')
    sep()
    print('Задание 4. Введите: 4 или 41 (2 решения)')
    sep()
    print('Задание 5. Введите: 5')
    sep()
    print('Задание 6. Введите: 6\n')


# Начало


menu = {1: exe_1_use,
        2: exe_2_use,
        3: exe_3_use,
        4: exe_4_use,
        41: exe_41_use,
        5: exe_5,
        6: exe_6_use,
        }

number_user = 1

while number_user != 0:
    refresh()
    number_user = int(input('Выберите задание или введите "0", чтобы выйти: '))
    if number_user == 0:
        break
    if number_user in menu:
        x = menu[number_user]
        x()
        input('Нажмите Enter, чтобы продолжить ')