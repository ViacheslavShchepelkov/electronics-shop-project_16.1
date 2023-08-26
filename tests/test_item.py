"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest
from src.item import InstantiateCSVError
from settings import ROOT_PATH
from src.item import Item


def test_item_name(item_1):
    assert item_1.name == 'Смартфон'
    assert item_1.price == 5000
    assert item_1.quantity == 5


def test_calc_total_price(item_1):
    assert item_1.calculate_total_price() == 25000.0


def test_apply_discount(item_1):
    Item.pay_rate = 0.8
    item_1.apply_discount()
    assert item_1.price == 4000.0


def test_string_to_number():
    assert Item.string_to_number('asdv5') == 5


def test_instance_from_csv():
    Item.instantiate_from_csv()
    first_instance_from_all = Item.all[0]
    assert first_instance_from_all.name == "Смартфон"


def test_repr(item_1):
    assert repr(item_1) == "Item('Смартфон', 5000, 5)"


def test_str(item_1):
    assert str(item_1) == "Смартфон"


def test_instantiate_from_csv_found_error():
    Item.csv_path = Path.joinpath(ROOT_PATH, 'src', 'wrong.csv')
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instance_from_csv_file_damaged():
    Item.csv_path = Path.joinpath(ROOT_PATH, 'src', 'test_csv.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_damaged_file(damage_file):
    result = InstantiateCSVError("Файл поврежден")
    assert result == damage_file


