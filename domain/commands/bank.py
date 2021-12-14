from pydantic.dataclasses import dataclass
from domain.commands.interfaces import Command


@dataclass(frozen=True)
class CreateBankCommand(Command):
    """Command for creating a new bank"""
    name: str
