import abc


class ITableEntity(metaclass=abc.ABCMeta):
    """Interface for table entities

    Describe the interface for table entities
    """

    table_name: str = None


class BaseEntity(ITableEntity):
    """Base class for table entities"""
