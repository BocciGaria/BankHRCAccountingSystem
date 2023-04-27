from typing import *

from .field import IField
from .operator import IOperator
from .mysql import field as mysqlfield
from .sqlite3 import (
    field as sqlite3field,
    operator as sqlite3operator,
)
from bhrc_accounting.config import DB


class FieldFactory:
    """Factory for creating database fields"""

    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls) -> Self:
        return cls()

    def __init__(self) -> None:
        self.__8bits_integer_fields = dict(
            sqlite3=lambda: sqlite3field.IntegerField(),
            mysql=lambda: mysqlfield.BigIntField(),
        )
        self.__text_fields = dict(
            sqlite3=lambda: sqlite3field.TextField(),
            mysqlfield=lambda: mysqlfield.TextField(),
        )
        self.__date_fields = dict(
            sqlite3=lambda: sqlite3field.DateField(),
            mysql=lambda: mysqlfield.DateField(),
        )
        self.__boolean_fields = dict(
            sqlite3=lambda: sqlite3field.BooleanField(),
            mysql=lambda: mysqlfield.TinyIntField(),
        )

    def get_8bits_integer_field(self) -> IField:
        """Get 8bits integer field"""
        return self.__8bits_integer_fields[DB]()

    def get_text_field(self) -> IField:
        """Get text field"""
        return self.__text_fields[DB]()

    def get_date_field(self) -> IField:
        """Get date field"""
        return self.__date_fields[DB]()

    def get_boolean_field(self) -> IField:
        """Get boolean field"""
        return self.__boolean_fields[DB]()


class OperatorFactory:
    """Factory for creating database operators"""

    @classmethod
    def get_operator(cls, connection_string: str) -> IOperator:
        """Get operator instance"""
        if DB == "sqlite3":
            return sqlite3operator.Sqlite3Operator(connection_string)
        elif DB == "mysql":
            raise NotImplementedError()
        else:
            raise NotImplementedError()
