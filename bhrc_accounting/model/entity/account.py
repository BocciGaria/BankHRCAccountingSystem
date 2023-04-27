from . import base


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
        self.id = self.field_factory.get_8bits_integer_field()
        self.date = self.field_factory.get_date_field()
        self.debit_title = self.field_factory.get_8bits_integer_field()
        self.credit_title = self.field_factory.get_8bits_integer_field()
        self.ammount = self.field_factory.get_8bits_integer_field()
        self.description = self.field_factory.get_text_field()
        self.slip = self.field_factory.get_8bits_integer_field()
        self.fields = dict(
            id=self.id,
            date=self.date,
            debit_title=self.debit_title,
            credit_title=self.credit_title,
            ammount=self.ammount,
            description=self.description,
            slip=self.slip,
        )
