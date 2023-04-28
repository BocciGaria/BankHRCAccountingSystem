from . import base
from ..db.factory import FieldFactory


class Account(base.BaseTableEntity):
    """Model class for accounting table

    Attributes:
        id (IntegerField): ID
        date (DateField): Date
        debit_title (IntegerField): Debit title id
        credit_title (IntegerField): Credit title id
        ammount (IntegerField): Ammount
        description (TextField): Description
        slip (IntegerField): Slip number
    """

    table_name = "account"

    def __init__(self) -> None:
        super().__init__()
        field_factory = FieldFactory.get_instance()
        self.id = field_factory.get_8bits_integer_field()
        self.date = field_factory.get_date_field()
        self.debit_title = field_factory.get_8bits_integer_field()
        self.credit_title = field_factory.get_8bits_integer_field()
        self.ammount = field_factory.get_8bits_integer_field()
        self.description = field_factory.get_text_field()
        self.slip = field_factory.get_8bits_integer_field()
        self.fields = dict(
            id=self.id,
            date=self.date,
            debit_title=self.debit_title,
            credit_title=self.credit_title,
            ammount=self.ammount,
            description=self.description,
            slip=self.slip,
        )
