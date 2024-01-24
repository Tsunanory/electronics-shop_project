import csv

class InstantiateCSVError(Exception):
    def __init__(self, message):
        print(message)

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
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other) -> int:
        if isinstance(other, Item) or issubclass(other.__class__, Item):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        Item.all.clear()
        cnt = 0
        try:
            with open(path, 'r',
                  encoding='cp1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Item(row['name'], float(row['price']), int(row['quantity']))
                    cnt += 1
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')
        if cnt != 5:
           raise InstantiateCSVError('Файл поврежден')


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


