import typing

from pydantic.dataclasses import dataclass

from domain.events.interfaces import Event


@dataclass
class NewBankCreatedEvent(Event):
    """Event when a new bank created"""
    bank_id: str
    name: str


@dataclass
class NewBankCreateFailedEvent(Event):
    """Event when a new bank creation failed"""
    msg: str


BankCreateResult = typing.Union[NewBankCreatedEvent, NewBankCreateFailedEvent]