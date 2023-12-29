import pytest
import sys
sys.path.append('/Users/tsunanory/Desktop/Python/OOP/electronics-shop_project/homework-1')
from src.item import Item

@pytest.fixture
def test_obj():
    return Item('name', 100, 30)

def test_calculate_total_price(test_obj):
    """func total_price works correctly - returns price * qty"""
    assert test_obj.calculate_total_price() == 3000

def test_apply_discount(test_obj):
    """func sell returns price with sell coefficient accounted"""
    assert test_obj.apply_discount() == 100