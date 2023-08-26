
def test_keyboard(keyboard_1):
    assert keyboard_1.name == "Defender"
    assert keyboard_1.price == 3000
    assert keyboard_1.quantity == 5
    assert keyboard_1.language == "EN"


def test_change_lang(keyboard_1):
    keyboard_1.change_lang()
    assert keyboard_1.language == "RU"
    keyboard_1.change_lang()
    assert keyboard_1.language == "EN"
