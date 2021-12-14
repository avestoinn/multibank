import datetime

from domain.value_objects.money import Money, Currency, TJS
from domain.value_objects.invoice import InvoiceID
from domain.entities.bank import Account
from . import Model

from pydantic.fields import Field


class Invoice(Model):
    id: InvoiceID = Field(default_factory=InvoiceID)
    from_account: Account
    to_account: Account
    amount: Money
    issued: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def to_dict(self):
        return self.dict(include={'id': ..., 'from_account': {'id', 'bank'}, 'to_account': {'id', 'bank'}, 'amount': ...,
                                  'issued': ...})