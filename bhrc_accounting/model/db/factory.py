from typing import *

from .field import IField, FieldName
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
            sqlite3=lambda x: sqlite3field.IntegerField(x),
            mysql=lambda x: mysqlfield.BigIntField(x),
        )
        self.__text_fields = dict(
            sqlite3=lambda x: sqlite3field.TextField(x),
            mysqlfield=lambda x: mysqlfield.TextField(x),
        )
        self.__date_fields = dict(
            sqlite3=lambda x: sqlite3field.DateField(x),
            mysql=lambda x: mysqlfield.DateField(x),
        )
        self.__boolean_fields = dict(
            sqlite3=lambda x: sqlite3field.BooleanField(x),
            mysql=lambda x: mysqlfield.TinyIntField(x),
        )

    def get_8bits_integer_field(self, field_name: FieldName) -> IField:
        """Get 8bits integer field"""
        return self.__8bits_integer_fields[DB](field_name)

    def get_text_field(self, field_name: FieldName) -> IField:
        """Get text field"""
        return self.__text_fields[DB](field_name)

    def get_date_field(self, field_name: FieldName) -> IField:
        """Get date field"""
        return self.__date_fields[DB](field_name)

    def get_boolean_field(self, field_name: FieldName) -> IField:
        """Get boolean field"""
        return self.__boolean_fields[DB](field_name)


class OperatorFactory:
    """Factory for creating database operators"""

    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls) -> Self:
        return cls()

    def get_operator(self, connection_string: str) -> IOperator:
        """Get operator instance"""
        if DB == "sqlite3":
            return sqlite3operator.Sqlite3Operator(connection_string)
        elif DB == "mysql":
            raise NotImplementedError()
        else:
            raise NotImplementedError()
