"""
1.	Создать класс TrafficLight (светофор).

●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from datetime import datetime
import time


class TrafficLight:
    _color = 'red'

    def running(self):
        if self._color is None or '':
            print('Нарушена пордок переключение светофора')
        elif self._color == 'красный':
            print(f'\033[41m горит {self._color} Время:', datetime.now().strftime('%H:%M:%S'))
            time.sleep(7)
        elif self._color == 'жёлтый':
            print(f'\033[43m горит {self._color} Время:', datetime.now().strftime('%H:%M:%S'))
            time.sleep(2)
        elif self._color == 'зелёный':
            print(f'\033[42m горит {self._color} Время:', datetime.now().strftime('%H:%M:%S'))
            time.sleep(7)


t_l = TrafficLight()
t_l._color = 'красный'
t_l.running()
t_l._color = 'жёлтый'
t_l.running()
t_l._color = 'зелёный'
t_l.running()
t_l._color = ''
t_l.running()
