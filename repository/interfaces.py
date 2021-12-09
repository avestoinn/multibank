import typing
from abc import ABC, abstractmethod
from domain.entities.card import Card
from domain.entities.bank import Bank, Account

from domain.value_objects.card import PAN
from domain.value_objects.bank import AccountID


class ICardRepository(ABC):
    """Repository interface for cards"""

    @abstractmethod
    def get_cards(self): pass

    @abstractmethod
    def get_card_by_pan(self, pan: PAN): pass

    @abstractmethod
    def insert_card(self, card: Card): pass

    @abstractmethod
    def remove_card_by_pan(self, pan: PAN): pass


class IBankRepository(ABC):
    """Repository interface for banks"""

    @abstractmethod
    def get_banks(self): pass

    @abstractmethod
    def get_bank_by_name(self, name: str): pass

    @abstractmethod
    def remove_bank_by_name(self, name: str): pass

    @abstractmethod
    def insert_bank(self, bank: Bank): pass


class IAccountRepository(ABC):
    """Repository interface for accounts"""

    @abstractmethod
    def get_accounts(self): pass

    @abstractmethod
    def get_account_by_id(self, account_id: AccountID): pass

    @abstractmethod
    def remove_account_by_id(self, account_id: AccountID): pass

    @abstractmethod
    def insert_account(self, account: Account): pass


class IMemoryStorage(ABC):
    """Memory-based storage interface"""
    __storage: typing.Dict

    def __init__(self):
        self.__storage = {}

    def _get_all(self):
        return [i for i in self.__storage.values()]

    def _get(self, key: typing.Any) -> typing.Union[typing.Any, None]:
        if key.__str__() not in self.__storage.keys():
            return None
        return self.__storage[key]

    def _put(self, key: typing.Any, value) -> bool:
        if key not in self.__storage.keys():
            self.__storage[key] = value
            return True
        return False

    def _remove(self, key: typing.Any = None) -> bool:
        if key not in self.__storage.keys():
            return False
        self.__storage.pop(key)
        return True


class RepositoryManager:
    """Менеджер, объединяющий все repo"""
    bank: IBankRepository
    account: IAccountRepository
    card: ICardRepository

    def __init__(self, bank_r: IBankRepository, account_r: IAccountRepository,
                 card_r: ICardRepository):
        self.bank = bank_r
        self.account = account_r
        self.card = card_r
