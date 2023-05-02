from datetime import date

from . import base
from .db.sqlite3 import field


class Account(base.BaseModel):
    """Model class for accounting table

    Attributes:
        id (IntegerField): ID
        date (DateField): Date
        debit_title (IntegerField): Debit title id
        credit_title (IntegerField): Credit title id
        amount (IntegerField): Ammount
        description (TextField): Description
        slip (IntegerField): Slip number
    """

    def __init__(
        self,
        id: int = None,
        date: date = None,
        debit_title: int = None,
        debit_amount: int = None,
        credit_title: int = None,
        credit_amount: int = None,
        amount: int = None,
        description: str = None,
        slip: int = None,
    ) -> None:
        super().__init__()
        self.id = self.field_factory.get_8bytes_integer_field(id)
        self.date = self.field_factory.get_date_field(date)
        self.debit_title = self.field_factory.get_8bytes_integer_field(debit_title)
        self.credit_title = self.field_factory.get_8bytes_integer_field(credit_title)
        self.amount = self.field_factory.get_8bytes_integer_field(amount)
        self.description = self.field_factory.get_text_field(description)
        self.slip = self.field_factory.get_8bytes_integer_field(slip)
        self.fields = dict(
            id=self.id,
            date=self.date,
            debit_title=self.debit_title,
            credit_title=self.credit_title,
            amount=self.amount,
            description=self.description,
            slip=self.slip,
        )

    def get_all(self):
        raise NotImplementedError()

    def get_for_primary_key(self, **primary_keys):
        raise NotImplementedError()

    def save(self):
        raise
