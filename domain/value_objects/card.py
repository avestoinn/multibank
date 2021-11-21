import datetime
import random


from domain.exceptions import CardError


class ExpirationDate:
    _month: int
    _year: int
    _until_date: datetime.datetime

    @classmethod
    def generate_three_years(cls):
        until = datetime.datetime.now() + datetime.timedelta(days=365*3)
        return cls(until.month, until.year)

    def date(self) -> datetime.datetime:
        return self._until_date

    def __init__(self, month: int, year: int):
        now = datetime.datetime.now()
        if month not in range(1, 13) or not 1900 < year < 2100:
            raise CardError.InvalidExpirationDate()
        if month < now.month or year < now.year:
            raise CardError.InvalidExpirationDate()

        self._month = month
        self._year = year
        self._until_date = datetime.datetime(year, month, 1)

    def __eq__(self, other):
        if isinstance(other, ExpirationDate):
            return self._until_date == other._until_date
        elif isinstance(other, datetime.datetime):
            return self._until_date == other
        raise CardError.NotExpirationDateType()

    def __gt__(self, other):
        if isinstance(other, ExpirationDate):
            return self._until_date > other._until_date
        elif isinstance(other, datetime.datetime):
            return self._until_date > other
        raise CardError.NotExpirationDateType()

    def __lt__(self, other):
        if isinstance(other, ExpirationDate):
            return self._until_date < other._until_date
        elif isinstance(other, datetime.datetime):
            return self._until_date < other
        raise CardError.NotExpirationDateType()

    def __ge__(self, other):
        if isinstance(other, ExpirationDate):
            return self._until_date >= other._until_date
        elif isinstance(other, datetime.datetime):
            return self._until_date >= other
        raise CardError.NotExpirationDateType()

    def __le__(self, other):
        if isinstance(other, ExpirationDate):
            return self._until_date <= other._until_date
        elif isinstance(other, datetime.datetime):
            return self._until_date <= other
        raise CardError.NotExpirationDateType()

    def __repr__(self):
        return f"{self._month}/{self._year.__str__()[2:4]}"

    def __str__(self):
        return f"{self._month}/{self._year.__str__()[2:4]}"


class PAN(str):
    """PAN значение карты"""
    __value: str

    LENGTH: int = 16

    @classmethod
    def generate(cls):
        v = ""
        for x in range(0, 16):
            v = v + str(random.randint(0, 9))
        return PAN(v)

    def __init__(self, code: str):
        code = code.replace(" ", "")
        if len(code) != self.LENGTH:
            raise CardError.InvalidPAN()
        self.__value = code

    def __repr__(self):
        return self.__value

    def __str__(self):
        return self.__value


class CV2(int):
    """3-значное CV2 значение карты"""
    __value: int

    @classmethod
    def generate(cls):
        return CV2(random.randint(100, 999))

    def __init__(self, value: int):
        if 100 <= value <= 999:
            self.__value = value
        else:
            raise CardError.InvalidCV2()

    def __repr__(self):
        return f"{self.__value}"

    def __str__(self):
        return f"{self.__value}"
