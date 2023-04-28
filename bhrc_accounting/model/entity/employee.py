from . import base
from ..db.factory import FieldFactory


class Employee(base.BaseTableEntity):
    """Model class for employee table

    Attributes:
        id (TextField): ID
        name (TextField): Name
        is_active (BooleanField): Active flag
    """

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_text_field()
        self.name = field_factory.get_text_field()
        self.is_active = field_factory.get_boolean_field()
        self.fields = dict(
            id=self.id,
            name=self.name,
            is_active=self.is_active,
        )
