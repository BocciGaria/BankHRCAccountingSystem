import abc
from typing import *

from ..db.field import IField, FieldName


class TableName(str):
    """Table name value object"""


class ITableEntity(metaclass=abc.ABCMeta):
    """Interface for table entities

    Describe the interface for table entities
    """

    table_name: TableName
    fields: Dict[FieldName, IField]


class BaseTableEntity(ITableEntity):
    """Base class for table entities"""

    def __init__(self) -> None:
        self.table_name = None
        self.fields = None
