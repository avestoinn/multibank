class ParentException(Exception):
    txt = "This is a parental exception"

    def __init__(self):
        super().__init__(self.txt)


class MoneyError:
    class NotMoneyType(ParentException):
        txt = "Should be <Money> type"

    class DifferentCurrencies(ParentException):
        txt = "Can't compare and make any operations between two different currencies"


class BankError:
    class BankAlreadyExist(ParentException):
        txt = "Bank with the provided name already exists"

    class NotAccountIdType(ParentException):
        txt: str = "Should be <AccountID> type"


class AccountError:
    class NotEnoughBalance(ParentException):
        txt: str = "Not enough balance for executing this command"


class CardError:
    class NotCardType(ParentException):
        txt: str = "Should be <Card> type"

    class InvalidPAN(ParentException):
        txt: str = "Invalid PAN value or length"

    class InvalidCV2(ParentException):
        txt: str = "Invalid CV2 value or length"

    class InvalidExpirationDate(ParentException):
        txt: str = "Invalid expiration date"

    class NotExpirationDateType(ParentException):
        txt: str = "Should be <ExpirationDate> type"
