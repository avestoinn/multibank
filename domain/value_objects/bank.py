import enum
import random
import string


class AccountID:
    __value: str

    __LENGTH = 20
    __SEQUENCE = string.digits

    def __hash__(self):
        return hash(self.__value)

    def __repr__(self):
        return self.__value

    def __str__(self):
        return self.__value

    def __eq__(self, other):
        if not isinstance(other, AccountID) or not isinstance(other, str):
            return False
        return self.__value == other.__value if isinstance(other, AccountID) else self.__value == other

    def __init__(self):
        v = ""
        for x in range(0, self.__LENGTH):
            v += random.choice(self.__SEQUENCE)
        self.__value = v


class AccountType(enum.Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"
