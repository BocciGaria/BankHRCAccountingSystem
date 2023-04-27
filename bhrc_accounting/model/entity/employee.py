from . import base
from .db.sqlite3 import field


class Employee(base.BaseModel):
    """Model class for employee table

    Attributes:
        id (TextField): ID
        name (TextField): Name
        is_active (BooleanField): Active flag
    """

    def __init__(self) -> None:
        super().__init__()
        self.id = self.field_factory.get_text_field()
        self.name = self.field_factory.get_text_field()
        self.is_active = self.field_factory.get_boolean_field()
        self.fields = dict(
            id=self.id,
            name=self.name,
            is_active=self.is_active,
        )
