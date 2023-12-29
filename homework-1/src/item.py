class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty

    def apply_discount(self):
        return self.price * self.pay_rate

