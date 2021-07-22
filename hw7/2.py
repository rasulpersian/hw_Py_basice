"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды  в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и
 рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothing(ABC):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        return self.v / 6.6 + 0.5

    @property
    def suit(self):
        return self.h * 2 + 0.3

    @abstractmethod
    def get_square(self):
        return str('Общий расход ткани {:.2f}'.format(self.coat + self.suit))


class Coat(Clothing):

    # def __str__(self):
    #     return f'Площадь, требуемая для пальто {self.coat}'

    def get_square(self):
        return 'Площадь, требуемая для пальто {:.2f}'.format(self.coat)


class Suit(Clothing):
    # def __str__(self):
    #     return f'Площадь, требуемая на костюм {self.suit}'

    def get_square(self):
        return 'Площадь, требуемая на костюм {:.2f}'.format(self.suit)


coat = Coat(3, 4)
suit = Suit(3, 4)
print(coat.get_square())
print(suit.get_square())
