from domain.entities.bank import Bank
from domain.commands.bank import CreateBankCommand
from domain.exceptions import BankError
from repository.interfaces import IBankRepository
from services.interfaces import IBankService


class BankService(IBankService):
    _repo: IBankRepository

    def create_bank(self, command: CreateBankCommand) -> Bank:
        if not self._repo.get_bank_by_name(command.name):
            bank = Bank(name=command.name)
            self._repo.insert_bank(bank)
            return bank
        else:
            raise BankError.BankAlreadyExist
