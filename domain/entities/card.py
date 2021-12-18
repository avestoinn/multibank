from pydantic.dataclasses import dataclass
from pydantic import validator
from pydantic.fields import Field

from domain.value_objects.card import PIN, PAN, CV2, ExpirationDate
from domain.entities.bank import Account
from domain.entities import Model
from domain.exceptions import CardError
from domain.value_objects.money import Money


class Card(Model):
    expiration_date: ExpirationDate = ExpirationDate.generate_three_years()
    pan: PAN = Field(default_factory=PAN.generate)
    cv2: CV2 = Field(default_factory=CV2.generate)
    pin: PIN = Field(default_factory=PIN.generate)
    account: Account

    @classmethod
    def issue(cls, account: Account):
        return Card(
            account=account
        )

    @property
    def balance(self):
        return self.account.balance

    @property
    def currency(self):
        return self.account.currency

    def deposit(self, money: Money):
        self.account.deposit(money)

    def withdraw(self, money: Money):
        self.account.withdraw(money)

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise CardError.NotCardType()
        return self.pan == other.pan and self.expiration_date == other.expiration_date \
            and self.cv2 == other.cv2 and self.pin == other.pin
