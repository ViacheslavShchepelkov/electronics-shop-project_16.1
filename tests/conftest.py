import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture()
def item_1():
    return Item('Смартфон', 10000, 20)


@pytest.fixture()
def phone_1():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture()
def phone_2():
    return Phone("iPhone 13", 90000, 10, 0)


@pytest.fixture()
def keyboard_1():
    return Keyboard('Defender', 3000, 5)


@pytest.fixture()
def damage_file():
    test_ex = InstantiateCSVError("Файл поврежден")
    return test_ex
