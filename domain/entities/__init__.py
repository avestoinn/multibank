from pydantic import BaseModel


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
