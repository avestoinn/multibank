from abc import ABC, abstractmethod

from repository.interfaces import RepositoryManager, IBankRepository, IAccountRepository, ICardRepository
from domain.entities.bank import Bank, Account
from domain.commands.bank import CreateBankCommand, IssueAccountCommand
from domain.events.bank import NewBankCreateFailedEvent, NewBankCreatedEvent, BankCreateResult
from domain.value_objects.bank import AccountID, AccountType


class IService(ABC):
    """Parent for all services in order to avoid duplicating code"""
    _repo: RepositoryManager

    def __init__(self, repo: RepositoryManager):
        self._repo = repo


class IBankService(IService):
    """Impl. helper for bank service"""

    @abstractmethod
    def create_bank(self, command: CreateBankCommand) -> Bank: ...


class IAccountService(IService):
    """Implementation helper for account service"""

    @abstractmethod
    def issue_account(self, command: IssueAccountCommand) -> Account: ...


class ICardService(ABC):
    """Implementation helper for card service"""


class ServiceManager:
    """Менеджер объединяющий все service приложения"""
    _repo: RepositoryManager
    bank: IBankService
    account: IAccountService

    def __init__(self, repo_manager: RepositoryManager):
        from services.bank import BankService, AccountService
        # Repo Manager
        self._repo = repo_manager

        # Services
        self.bank = BankService(self._repo)
        self.account = AccountService(self._repo)
