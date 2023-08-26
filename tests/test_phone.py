def test_phone(phone_1):
    assert phone_1.name == "iPhone 14"
    assert phone_1.price == 120_000
    assert phone_1.quantity == 5
    assert phone_1.number_of_sim == 2


def test_repr(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(item_1, phone_1):
    assert item_1 + phone_1 == 25


def test_number_of_sim(phone_2):
    assert phone_2.number_of_sim == 0

