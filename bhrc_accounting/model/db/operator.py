import abc
from typing import *

from ..entity.base import ITableEntity


class IOperator(metaclass=abc.ABCMeta):
    """Interface for database operators"""

    @abc.abstractmethod
    def __init__(self, connection_string: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_all(self, entity_type: Type[ITableEntity]) -> Iterable[ITableEntity]:
        """Get all records

        Args:
            model_type: The model type

        Returns:
            The records
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_for_primary_key(self, entity_type: Type[ITableEntity]) -> ITableEntity:
        """Get a record for primary key

        Args:
            model_type: The model type

        Returns:
            The record
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, entity: ITableEntity) -> None:
        """Save models

        Args:
            models: The models
        """
        raise NotImplementedError()


class BaseOperator(IOperator):
    """Base class for database operators"""

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
