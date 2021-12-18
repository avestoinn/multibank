from domain.entities.card import Card
from domain.entities.bank import Bank, Account

from domain.value_objects.card import PAN
from domain.value_objects.bank import AccountID

from repository.interfaces import IMemoryStorage, IAccountRepository, IBankRepository


class MemoryAccountRepository(IAccountRepository, IMemoryStorage):
    def get_accounts(self):
        return self._get_all()

    def get_account_by_id(self, account_id: AccountID) -> Account:
        return self._get(account_id)

    def remove_account_by_id(self, account_id: AccountID):
        return self._remove(account_id)

    def insert_account(self, account: Account):
        return self._put(account.id, account)

    def save(self, account: Account):
        return self._put(account.id, account, force=True)


class MemoryBankRepository(IBankRepository, IMemoryStorage):
    def insert_bank(self, bank: Bank):
        return self._put(bank.name, bank)

    def remove_bank_by_name(self, name: str):
        return self._remove(name)

    def get_banks(self):
        return self._get_all()

    def get_bank_by_name(self, name: str):
        return self._get(name)

    def save(self, bank: Bank):
        return self._put(bank.name, bank, force=True)