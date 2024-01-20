import pytest
from src.keyboard import Keyboard

@pytest.fixture
def test_keyb():
    return Keyboard('Cool kB', 800, 10)

def test_str(test_keyb):
    assert test_keyb.__str__() == 'Cool kB'

def test_change_lang(test_keyb):
    test_keyb.change_lang()
    assert test_keyb.language == "RU"