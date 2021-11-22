from abc import ABC, abstractmethod

from repository.interfaces import IBankRepository
from domain.entities.bank import Bank
from domain.commands.bank import CreateBankCommand
from domain.events.bank import NewBankCreateFailedEvent, NewBankCreatedEvent, BankCreateResult
from domain.value_objects.bank import AccountID, AccountType


class BankService(ABC):
    """Service for bank"""
    _repo: IBankRepository

    @abstractmethod
    def create_bank(self, command: CreateBankCommand) -> BankCreateResult: ...