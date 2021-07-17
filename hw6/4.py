"""
    4.	Реализуйте базовый класс Car.

    ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Вызовите методы и покажите результат.
    """


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name}, цвет: {self.color}, едит'

    def stop(self):
        return f'\nАвтомобиль {self.name}, цвет: {self.color}, остановилась'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name}, цвет: {self.color}, повернула {direction}'

    def show_speed(self):
        return f' скрость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nАвтомобиль {self.name}, цвет {self.color}, едит превышеннной скростью {self.speed}'
        else:
            return f'Автомобиль {self.name}, цвет {self.color}, едит со скростью {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Автомобиль {self.name}, цвет {self.color}, едит превышеннной скростью {self.speed}'
        else:
            return f'Автомобиль {self.name}, цвет {self.color}, едит со скростью {self.speed}'


class PoliceCar(Car):
    pass


tw_car = TownCar(speed=240, name='Mercedes', color='красный')
print(tw_car.go(), tw_car.turn('внекуда'), tw_car.show_speed(), tw_car.stop())
