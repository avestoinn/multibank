class MoneyError:
    class NotMoneyType(Exception):
        def __init__(self, txt: str = "Should be <Money> type"):
            super().__init__(txt)

    class DifferentCurrencies(Exception):
        def __init__(self, txt: str = "Can't compare and make any operations between two different currencies"):
            super().__init__(txt)


class BankError:
    class NotAccountIdType(Exception):
        def __init__(self, txt: str = "Should be <AccountID> type"):
            super().__init__(txt)


class CardError:
    class NotCardType(Exception):
        def __init__(self, txt: str = "Should be <Card> type"):
            super().__init__(txt)

    class InvalidPAN(Exception):
        def __init__(self, txt: str = "Invalid PAN value or length"):
            super().__init__(txt)

    class InvalidCV2(Exception):
        def __init__(self, txt: str = "Invalid CV2 value or length"):
            super().__init__(txt)

    class InvalidExpirationDate(Exception):
        def __init__(self, txt: str = "Invalid expiration date"):
            super().__init__(txt)

    class NotExpirationDateType(Exception):
        def __init__(self, txt: str = "Should be <ExpirationDate> type"):
            super().__init__(txt)