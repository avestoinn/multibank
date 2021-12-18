from domain.entities.bank import Bank, Account
from domain.commands.bank import *
from domain.exceptions import BankError
from repository.interfaces import RepositoryManager
from services.interfaces import IBankService, IAccountService


class BankService(IBankService):
    _repo: RepositoryManager

    def create_bank(self, command: CreateBankCommand) -> Bank:
        if not self._repo.bank.get_bank_by_name(command.name):
            bank = Bank(name=command.name)
            self._repo.bank.save(bank)
            return bank
        else:
            raise BankError.BankAlreadyExist


class AccountService(IAccountService):
    _repo: RepositoryManager

    def issue_account(self, command: IssueAccountCommand) -> Account:
        bank = self._repo.bank.get_bank_by_name(command.bank_name)

        if not bank:
            raise BankError.BankNotExist

        new_account = Account(bank=bank, currency=command.currency)
        self._repo.account.save(new_account)
        return new_account

    def transfer_funds(self, command: TransferFundsCommand) -> bool:
        from_account = self._repo.account.get_account_by_id(command.from_account_id)
        to_account = self._repo.account.get_account_by_id(command.to_account_id)

        if from_account and to_account and from_account != to_account and from_account.bank == to_account.bank and \
                from_account.currency == to_account.currency and from_account.balance >= command.amount:
            from_account.withdraw(command.amount)
            to_account.deposit(command.amount)

            self._repo.account.save(from_account)
            self._repo.account.save(to_account)
            return True
        return False
