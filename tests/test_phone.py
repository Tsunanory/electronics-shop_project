import pytest
from src.phone import Phone

@pytest.fixture
def test_phone():
    return Phone('iPhone', 1000, 10, 1)

def test_pepr(test_phone):
    assert repr(test_phone) == "Phone('iPhone', 1000, 10, 1)"

def test_add(test_phone):
    assert test_phone + test_phone == 20
