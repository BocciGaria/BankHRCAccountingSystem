from . import base
from .db.sqlite3 import field


class Account(base.BaseModel):
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

    def __init__(self) -> None:
        super().__init__()
        self.id = field.IntegerField()
        self.date = field.DateField()
        self.debit_title = field.IntegerField()
        self.credit_title = field.IntegerField()
        self.ammount = field.IntegerField()
        self.description = field.TextField()
        self.slip = field.IntegerField()
        self.fields = dict(
            id=self.id,
            date=self.date,
            debit_title=self.debit_title,
            credit_title=self.credit_title,
            ammount=self.ammount,
            description=self.description,
            slip=self.slip,
        )
