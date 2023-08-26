from src.item import Item


class Mixinlang:
    def __init__(self, lang="EN"):
        self.lang = lang

    @property
    def language(self):
        return self.lang

    def change_lang(self):
        if self.language == "EN":
            self.lang = "RU"
        else:
            self.lang = "EN"
        return self


class Keyboard(Item, Mixinlang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.language})"

    def __str__(self):
        return f'{self.name}'
