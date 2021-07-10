"""
1.	Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

# выработка в часа
name_func, output, rate_per_hour, allowance = argv

print('Функция: ', name_func)
print('выработка в часах: ', output)
print('ставка в час: ', rate_per_hour)
print('премия: ', allowance)


def counter(output, rate_per_hour, allowance):
    return (int(output) * int(rate_per_hour)) + int(allowance)


print('Зп сотрудника: ', counter(output, rate_per_hour, allowance))
