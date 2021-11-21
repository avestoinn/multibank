import enum

from domain.value_objects.money import Money, Currency, TJS
from domain.value_objects.bank import AccountID, AccountType
from . import Model

from pydantic.fields import Field


class Bank(Model):
    name: str


class Account(Model):
    """Bank account"""

    id: AccountID = Field(default_factory=AccountID)
    type: AccountType = AccountType.DEBIT
    bank: Bank
    balance: Money = Money(0, TJS)

    @property
    def currency(self) -> Currency:
        return self.balance.currency
