import abc
from typing import *

from ..db.field import IField


class ITableEntity(metaclass=abc.ABCMeta):
    """Interface for table entities

    Describe the interface for table entities
    """

    table_name: str = None
    fields: Iterable[IField] = None


class BaseTableEntity(ITableEntity):
    """Base class for table entities"""
