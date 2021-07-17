"""
6.	Реализовать два небольших скрипта:
●	итератор, генерирующий целые числа, начиная с указанного;
●	итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

"""
from itertools import count
from itertools import cycle

# итератор, генерирующий целые числа, начиная с указанного;
from sys import argv
begin_el, sec_el = argv
# список для второго часть заднии получаем из первой чать заднии
list_for_sec_less = []
counter = 0
print('итератор, генерирующий целые числа, начиная с указанного:')
for el in count(int(sec_el)):
    if counter > 7:
        break
    else:
        counter += 1
        print(el)
        list_for_sec_less.append(el)
# итератор, повторяющий элементы некоторого списка, определённого заранее.
print("итератор, повторяющий элементы некоторого списка, определённого заранее")
counter = 0
for el in cycle(list_for_sec_less):
    if counter >= len(list_for_sec_less):
        break
    else:
        counter += 1
        print(el)