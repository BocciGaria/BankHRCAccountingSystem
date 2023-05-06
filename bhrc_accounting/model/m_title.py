from . import base
from .db.sqlite3 import field


class MTitleModel(base.BaseModel):
    """Model class for accounting titles master table

    Attributes:
        id (IntegerField): ID
        name (TextField): Title name
        is_active (BooleanField): Active flag"""

    def __init__(self) -> None:
        super().__init__()
        self.id = self.field_factory.get_8bytes_integer_field()
        self.name = self.field_factory.get_text_field()
        self.is_active = self.field_factory.get_boolean_field()
        self.fields = dict(
            id=self.id,
            name=self.name,
            is_active=self.is_active,
        )
