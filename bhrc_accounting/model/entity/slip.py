from . import base
from ..db.factory import FieldFactory


class slip(base.BaseTableEntity):
    """Model class for slip table

    Attributes:
        id (IntegerField): ID
        first_date (DateField): First date
        last_date (DateField): Last date
        employee (TextField): Employee id
    """

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_8bits_integer_field()
        self.first_date = field_factory.get_date_field()
        self.last_date = field_factory.get_date_field()
        self.employee = field_factory.get_text_field()
        self.fields = dict(
            id=self.id,
            first_date=self.first_date,
            last_date=self.last_date,
            employee=self.employee,
        )
