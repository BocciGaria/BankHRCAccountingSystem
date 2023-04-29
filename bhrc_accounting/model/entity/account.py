from .base import BaseTableEntity, TableName
from ..db.factory import FieldFactory


class Account(BaseTableEntity):
    """Model class for accounting table

    Attributes:
        table_name (TableName): Table name
        id (IntegerField): ID
        date (DateField): Date
        debit_title (IntegerField): Debit title id
        credit_title (IntegerField): Credit title id
        ammount (IntegerField): Ammount
        description (TextField): Description
        slip (IntegerField): Slip number
    """

    table_name = TableName("account")

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_8bits_integer_field("id")
        self.date = field_factory.get_date_field("date")
        self.debit_title = field_factory.get_8bits_integer_field("debit_title")
        self.credit_title = field_factory.get_8bits_integer_field("credit_title")
        self.ammount = field_factory.get_8bits_integer_field("ammount")
        self.description = field_factory.get_text_field("description")
        self.slip = field_factory.get_8bits_integer_field("slip")
        self.fields = {
            self.id.field_name: self.id,
            self.date.field_name: self.date,
            self.debit_title.field_name: self.debit_title,
            self.credit_title.field_name: self.credit_title,
            self.ammount.field_name: self.ammount,
            self.description.field_name: self.description,
            self.slip.field_name: self.slip,
        }
