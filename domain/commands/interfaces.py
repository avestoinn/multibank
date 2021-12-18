from dataclasses import dataclass
from pydantic.fields import Field
from pydantic import BaseModel
import datetime


class Config:
    arbitrary_types_allowed = True


@dataclass(kw_only=True)
class Command:
    """Command base (abstract) class to be inherited by children"""

    def __post_init__(self):
        self.invoked_on = datetime.datetime.now()