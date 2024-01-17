from .item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim=1):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, (self.__class__, Item.__class__)):
            return self.quantity + other.quantity

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, val):
        if not isinstance(val, int) or val < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
