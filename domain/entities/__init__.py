import datetime

from pydantic import BaseModel

from domain.value_objects.bank import AccountID
from domain.value_objects.invoice import InvoiceID
from domain.value_objects.money import Money


class Model(BaseModel):
    def dict(self, **kwargs):
        hidden_fields = set(
            attribute_name
            for attribute_name, model_field in self.__fields__.items()
            if model_field.field_info.extra.get("hidden") is True
        )
        kwargs.setdefault("exclude", hidden_fields)
        return super().dict(**kwargs)

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True
        json_encoders = {
            AccountID: lambda a_id: a_id.__str__(),
            InvoiceID: lambda i_id: i_id.__str__(),
            Money: lambda m: m.__str__(),
            datetime.datetime: lambda d: d.strftime("%d.%m.%Y  %H:%M:%S")
        }