import pytest
import os
from src.item import Item


@pytest.fixture
def test_obj():
    return Item('name', 100, 30)


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
