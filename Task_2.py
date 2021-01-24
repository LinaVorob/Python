from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_size(self):
        pass


class Coat(Clothes):
    @property
    def calc_size(self):
        return round(self.param / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def calc_size(self):
        return round(self.param * 2 + 0.3)


suit = Suit(180)
coat = Coat(69)
print(f'на костюм необходимо {suit.calc_size} м ткани, для пальто - {coat.calc_size} м. Суммарно - '
      f'{coat.calc_size + suit.calc_size}')
