from pydantic.dataclasses import dataclass
from domain.commands.interfaces import Command


@dataclass
class CreateBankCommand(Command):
    """Command for creating a new bank"""
    name: str
