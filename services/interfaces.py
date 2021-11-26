from abc import ABC, abstractmethod

from repository.interfaces import RepositoryManager
from domain.entities.bank import Bank
from domain.commands.bank import CreateBankCommand
from domain.events.bank import NewBankCreateFailedEvent, NewBankCreatedEvent, BankCreateResult
from domain.value_objects.bank import AccountID, AccountType


class IBankService(ABC):
    """Service for bank"""
    _repo: RepositoryManager

    @abstractmethod
    def create_bank(self, command: CreateBankCommand) -> BankCreateResult: ...


class ServiceManager:
    """Менеджер объединяющий все service приложения"""
    _repo: RepositoryManager
    bank: IBankService

    def __init__(self, repo_manager: RepositoryManager, bank_s: IBankService):
        self._repo = repo_manager
        self.bank = bank_s
