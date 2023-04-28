import abc

from .db.factory import OperatorFactory
from bhrc_accounting.config import DB_CONNECTION_STRING


class IModel(metaclass=abc.ABCMeta):
    """Interface for models

    Describe the interface for models in Tkinter/MVC
    """

    @abc.abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()


class BaseModel(IModel):
    """Base class for models"""

    table_name: str = None

    def __init__(self, **kwargs) -> None:
        self.operator = OperatorFactory.get_instance().get_operator(DB_CONNECTION_STRING)
