from .base import BaseTableEntity, TableName
from ..db.factory import FieldFactory


class Employee(BaseTableEntity):
    """Model class for employee table

    Attributes:
        table_name (TableName): Table name
        id (TextField): ID
        name (TextField): Name
        is_active (BooleanField): Active flag
    """

    table_name = TableName("employee")

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_text_field("id")
        self.name = field_factory.get_text_field("name")
        self.is_active = field_factory.get_boolean_field("is_active")
        self.fields = {
            self.id.field_name: self.id,
            self.name.field_name: self.name,
            self.is_active.field_name: self.is_active,
        }
