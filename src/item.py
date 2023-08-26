import csv

from settings import CSV_PATH


class InstantiateCSVError(Exception):
    """Класс-исключение для проверки целостности файла"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"InstantiateCSVError: {self.message}"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    csv_path = CSV_PATH

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}{(self.__name, self.price, self.quantity)}"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(self, Item) and issubclass(other.__class__, Item):
            return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls):
        if not cls.csv_path.exists():
            raise FileNotFoundError("Отсутствует файл")
        with open(cls.csv_path, newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for x in reader:
                print(x)
                if None in x.values():
                    raise InstantiateCSVError("Файл поврежден")
            Item.all.append(Item(x["name"], x["price"], x["quantity"]))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("Длина превышает 10 символов")
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(string):
        """
        Из переданной строки возвращает первый символ-цифру.
        @param string: Строка для поиска символа.
        @return: Возвращает цифру.
        """
        for x in range(len(string)):
            if string[x].isdigit():
                return int(string[x])


print(Item.instantiate_from_csv())
