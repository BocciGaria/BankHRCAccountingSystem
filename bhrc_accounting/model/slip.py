from . import base
from .db.sqlite3 import field


class slip(base.BaseModel):
    """Model class for slip table

    Attributes:
        id (IntegerField): ID
        first_date (DateField): First date
        last_date (DateField): Last date
        employee (TextField): Employee id
    """

    def __init__(self) -> None:
        super().__init__()
        self.id = field.IntegerField()
        self.first_date = field.DateField()
        self.last_date = field.DateField()
        self.employee = field.TextField()
        self.fields = dict(
            id=self.id,
            first_date=self.first_date,
            last_date=self.last_date,
            employee=self.employee,
        )
