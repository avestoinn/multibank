import enum
import random
import string


class AccountID:
    __value: str

    __LENGTH = 20
    __SEQUENCE = string.digits

    def __repr__(self):
        return self.__value

    def __str__(self):
        return self.__value

    def __eq__(self, other):
        if not isinstance(other, AccountID):
            return False
        return self.__value == other.__value

    def __init__(self):
        v = ""
        for x in range(0, 20):
            v += random.choice(self.__SEQUENCE)
        self.__value = v


class AccountType(enum.Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"
