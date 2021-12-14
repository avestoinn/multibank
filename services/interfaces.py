from abc import ABC, abstractmethod

from repository.interfaces import RepositoryManager, IBankRepository
from domain.entities.bank import Bank
from domain.commands.bank import CreateBankCommand
from domain.events.bank import NewBankCreateFailedEvent, NewBankCreatedEvent, BankCreateResult
from domain.value_objects.bank import AccountID, AccountType


class IBankService(ABC):
    """Impl. helper for bank service"""
    _repo: IBankRepository

    def __init__(self, repo: IBankRepository):
        self._repo = repo

    @abstractmethod
    def create_bank(self, command: CreateBankCommand) -> Bank: ...


class ICardService(ABC):
    """Implementation helper for card service"""
    _repo: RepositoryManager


class ServiceManager:
    """Менеджер объединяющий все service приложения"""
    _repo: RepositoryManager
    bank: IBankService

    def __init__(self, repo_manager: RepositoryManager):
        from services.bank import BankService
        # Repo Manager
        self._repo = repo_manager

        # Services
        self.bank = BankService(self._repo.bank)
