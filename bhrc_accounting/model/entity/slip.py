from .base import BaseTableEntity, TableName
from ..db.factory import FieldFactory


class Slip(BaseTableEntity):
    """Model class for slip table

    Attributes:
        table_name (TableName): Table name
        id (IntegerField): ID
        first_date (DateField): First date
        last_date (DateField): Last date
        employee (TextField): Employee id
    """

    table_name = TableName("slip")

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_8bits_integer_field("id")
        self.first_date = field_factory.get_date_field("first_date")
        self.last_date = field_factory.get_date_field("last_date")
        self.employee = field_factory.get_text_field("employee")
        self.fields = {
            self.id.field_name: self.id,
            self.first_date.field_name: self.first_date,
            self.last_date.field_name: self.last_date,
            self.employee.field_name: self.employee,
        }
