from dataclasses import dataclass
from pydantic.fields import Field
import datetime


@dataclass(kw_only=True)
class Command:
    """Command base (abstract) class to be inherited by children"""

    invoked_on: datetime.datetime = Field(default_factory=datetime.datetime.now)