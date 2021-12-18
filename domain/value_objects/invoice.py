import random
import string


class InvoiceID:
    __value: str

    __LENGTH = 12
    __SEQUENCE = string.ascii_letters + string.digits

    def __hash__(self):
        return hash(self.__value)

    def __repr__(self):
        return self.__value

    def __str__(self):
        return self.__value

    def __eq__(self, other):
        if not isinstance(other, InvoiceID):
            return False
        return self.__value == other.__value

    def __init__(self):
        v = ""
        for x in range(0, self.__LENGTH):
            if x == round(self.__LENGTH / 2):
                v += "-"
                continue
            v += random.choice(self.__SEQUENCE)
        self.__value = v
