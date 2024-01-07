import csv
import sys

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item."""
        self.__name = name
        self.price = price
        self.quantity = quantity
        #self.all.append(self) #Для homework-2 этa команда перенесена в функцию instantiate_from_csv

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, 'r',
                  encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Item.all.append(Item(row['name'], int(row['price']), int(row['quantity'])))

    @staticmethod
    def string_to_number(string):
        if '.' in string:
            string = string[:string.index('.')]
        return int(string)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name