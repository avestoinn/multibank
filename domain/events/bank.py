import typing
from pydantic.dataclasses import dataclass

from domain.entities.bank import Bank
from domain.events.interfaces import Event


@dataclass
class NewBankCreatedEvent(Event):
    """A new bank is created successfully"""
    bank: Bank

    def notify(self):
        pass


@dataclass
class NewBankCreateFailedEvent(Event):
    """A new bank creation failed"""
    msg: str = ""

    def notify(self):
        pass


BankCreateResult = typing.Union[NewBankCreatedEvent, NewBankCreateFailedEvent]