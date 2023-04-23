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
        self.id = field.IntegerField()
        self.name = field.TextField()
        self.is_active = field.BooleanField()
        self.fields = dict(
            id=self.id,
            name=self.name,
            is_active=self.is_active,
        )
