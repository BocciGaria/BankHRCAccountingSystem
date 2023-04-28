from . import base
from ..db.factory import FieldFactory


class MTitle(base.BaseTableEntity):
    """Model class for accounting titles master table

    Attributes:
        id (IntegerField): ID
        name (TextField): Title name
        is_active (BooleanField): Active flag"""

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_8bits_integer_field()
        self.name = field_factory.get_text_field()
        self.is_active = field_factory.get_boolean_field()
        self.fields = dict(
            id=self.id,
            name=self.name,
            is_active=self.is_active,
        )
