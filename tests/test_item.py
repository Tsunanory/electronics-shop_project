import pytest
import csv
from src.item import Item


@pytest.fixture
def test_obj():
    return Item('name', 100, 30)


@pytest.fixture
def csv_data():
    rows = []
    with open('src/items.csv', 'r', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append([row['name'], int(row['price']), int(row['quantity'])])
        return rows


def test_calculate_total_price(test_obj):
    """func works correctly - returns price * qty"""
    assert test_obj.calculate_total_price() == 3000


def test_apply_discount(test_obj):
    """returns price with sell coefficient accounted"""
    old_price = test_obj.price
    test_obj.pay_rate = 0.85
    test_obj.apply_discount()
    assert test_obj.price == 85


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name(test_obj):
    old_name = test_obj.name
    test_obj.name = 'new_name'
    assert old_name != 'new_name'

def test_instantiate_from_csv(csv_data):
    objects = []
    q = [csv_data[0][2], csv_data[1][2], csv_data[2][2], csv_data[3][2], csv_data[4][2]]
    for row in csv_data:
        objects.append(Item(row[0], row[1], row[2]))
        f = 0
    for obj in objects:
        assert obj.quantity == q[f]
        f += 1

def test_repr(test_obj):
    assert repr(test_obj) == "Item('name', 100, 30)"

def test_str(test_obj):
    assert str(test_obj) == 'name'