import enum

from domain.value_objects.money import Money, Currency, TJS
from domain.value_objects.bank import AccountID, AccountType
from . import Model

from pydantic.fields import Field

from ..exceptions import AccountError


class Bank(Model):
    """Bank entity"""
    name: str


class Account(Model):
    """Bank account entity"""

    id: AccountID = Field(default_factory=AccountID)
    type: AccountType = AccountType.DEBIT
    bank: Bank
    balance: Money = Money(0, TJS)

    @property
    def currency(self) -> Currency:
        return self.balance.currency

    def deposit(self, money: Money):
        self.balance += money

    def withdraw(self, money: Money):
        if money > self.balance:
            raise AccountError.NotEnoughBalance()
        self.balance -= money
