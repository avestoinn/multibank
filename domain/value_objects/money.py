import typing
from domain.exceptions import MoneyError


class Currency(str):
    __code: str

    def __init__(self, code: str):
        self.__code = code

    def __str__(self):
        return f"{self.__code}"

    def __repr__(self):
        return f"(Currency, {self.__code})"

    def __eq__(self, other):
        if not isinstance(other, Currency):
            raise MoneyError.DifferentCurrencies()
        return self.__code == other.__code


# Constants
TJS = Currency("TJS")
RUB = Currency("RUB")
USD = Currency("USD")


class Money:
    __value: float
    __currency: Currency

    @property
    def currency(self):
        return self.__currency

    @staticmethod
    def __check_is_money(other):
        if not isinstance(other, Money):
            raise MoneyError.NotMoneyType()
        other.__value = round(other.__value, 2)  # Округляем до сотых, копейки, дирамы

    def __check_currencies(self, other):
        if not self.__currency == other.__currency:
            raise MoneyError.DifferentCurrencies()

    def __init__(self, value: float, currency: Currency = TJS):
        if not isinstance(currency, Currency):
            raise TypeError('currency should be a Currency type')
        self.__value = 0 if value < 0 else value
        self.__currency = currency

    def __str__(self):
        return f"{self.__value} {self.__currency.__str__()}"

    def __repr__(self):
        return f"{self.__value} {self.__currency}"

    def __eq__(self, other):
        self.__check_is_money(other)
        return self.__value == other.__value and self.__currency == other.__currency

    def __lt__(self, other):
        self.__check_is_money(other)
        return self.__value < other.__value and self.__currency == other.__currency

    def __gt__(self, other):
        self.__check_is_money(other)
        return self.__value > other.__value and self.__currency == other.__currency

    def __le__(self, other):
        self.__check_is_money(other)
        return self.__value <= other.__value and self.__currency == other.__currency

    def __ge__(self, other):
        self.__check_is_money(other)
        return self.__value >= other.__value and self.__currency == other.__currency

    def __add__(self, other):
        self.__check_is_money(other)
        self.__check_currencies(other)
        self.__value += other.__value
        return self

    def __sub__(self, other):
        self.__check_is_money(other)
        self.__check_currencies(other)
        self.__value -= other.__value
        return self
