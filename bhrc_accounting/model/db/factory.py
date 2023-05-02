from typing import *

from .field import IField
from .mysql import field as mysqlfield
from .sqlite3 import field as sqlite3field
from bhrc_accounting.config import DB
from bhrc_accounting.const import SQLITE3, MYSQL


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
        self.__using_db = DB
        self.__8bits_integer_fields: Dict[str, Callable[[Any], IField]] = {
            SQLITE3: lambda x: sqlite3field.IntegerField(initial_value=x),
            MYSQL: lambda x: mysqlfield.BigIntField(initial_value=x),
        }
        self.__text_fields = {
            SQLITE3: lambda x: sqlite3field.TextField(initial_value=x),
            MYSQL: lambda x: mysqlfield.TextField(initial_value=x),
        }
        self.__date_fields = {
            SQLITE3: lambda x: sqlite3field.DateField(initial_value=x),
            MYSQL: lambda x: mysqlfield.DateField(initial_value=x),
        }
        self.__boolean_fields = {
            SQLITE3: lambda x: sqlite3field.BooleanField(initial_value=x),
            MYSQL: lambda x: mysqlfield.TinyIntField(initial_value=x),
        }

    def get_8bytes_integer_field(self, initial_value: Any = None) -> IField:
        """Get 8 bytes integer field"""
        return self.__8bits_integer_fields[self.__using_db](initial_value)

    def get_text_field(self, initial_value: Any = None) -> IField:
        """Get text field"""
        return self.__text_fields[self.__using_db](initial_value)

    def get_date_field(self, initial_value: Any = None) -> IField:
        """Get date field"""
        return self.__date_fields[self.__using_db](initial_value)

    def get_boolean_field(self, initial_value: Any = None) -> IField:
        """Get boolean field"""
        return self.__boolean_fields[self.__using_db](initial_value)
