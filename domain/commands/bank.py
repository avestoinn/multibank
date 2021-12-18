from dataclasses import dataclass
from domain.commands.interfaces import Command, Config
from domain.entities.bank import AccountID
from domain.value_objects.money import Currency, Money


@dataclass
class CreateBankCommand(Command):
    """Command for creating a new bank"""
    name: str


@dataclass
class IssueAccountCommand(Command):
    """Command for issuing a new card"""
    bank_name: str
    currency: Currency


@dataclass
class TransferFundsCommand(Command):
    from_account_id: AccountID
    to_account_id: AccountID
    amount: Money
