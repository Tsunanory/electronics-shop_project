import os

import pytest
import csv

from config import ROOT_DIR
from src.item import Item, InstantiateCSVError


@pytest.fixture
def test_item():
    return Item('name', 100, 30)

@pytest.fixture
def csv_data():
    rows = []
    test_file_path = os.path.join(ROOT_DIR, 'src', 'items.csv')
    with open(test_file_path, 'r', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append([row['name'], int(row['price']), int(row['quantity'])])
        return rows


def test_calculate_total_price(test_item):
    """func works correctly - returns price * qty"""
    assert test_item.calculate_total_price() == 3000

def test_apply_discount(test_item):
    """returns price with sell coefficient accounted"""
    old_price = test_item.price
    test_item.pay_rate = 0.85
    test_item.apply_discount()
    assert test_item.price == 85

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name(test_item):
    old_name = test_item.name
    test_item.name = 'new_name'
    assert old_name != 'new_name'

def test_instantiate_from_csv():
    test_file_path = os.path.join(ROOT_DIR, 'src', 'items.csv')
    Item.instantiate_from_csv(test_file_path)
    assert len(Item.all) == 4
    # objects = []
    # q = [csv_data[0][2], csv_data[1][2], csv_data[2][2], csv_data[3][2], csv_data[4][2]]
    # for row in csv_data:
    #     objects.append(Item(row[0], row[1], row[2]))
    # f = 0
    # for obj in objects:
    #     assert obj.quantity == q[f]
    #     f += 1

def test_repr(test_item):
    assert repr(test_item) == "Item('name', 100, 30)"

def test_str(test_item):
    assert str(test_item) == 'name'

def test_add(test_item):
    assert test_item + test_item == 60

def test_file_is_absent(test_item):
    with pytest.raises(FileNotFoundError):
        test_item.instantiate_from_csv('some_path')


def test_instantianion_error(test_item):
    test_file_path = os.path.join(ROOT_DIR, 'tests', 'test_file_for_instantiate_broken.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(test_file_path)
