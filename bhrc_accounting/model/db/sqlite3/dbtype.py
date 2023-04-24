import datetime
from typing import *

from ..dbtype import BaseDbType


class Text(BaseDbType):
    """Sqlite3の文字列型"""

    __type = str

    @property
    def name(self) -> str:
        return "text"


class Real(BaseDbType):
    """Sqlite3の8バイト浮動小数型"""

    __type = float

    def name(self) -> str:
        return "real"


class Integer(BaseDbType):
    """Sqlite3の整数型"""

    __type = int

    def name(self) -> str:
        return "integer"


class Blob(BaseDbType):
    """Sqlite3のバイナリ型"""

    __type = bytes

    def name(self) -> str:
        return "blob"


class Boolean(BaseDbType):
    """Sqlite3の真偽型"""

    __type = bool

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        if self.__value:
            self.__value = 1
        else:
            self.__value = 0

    def name(self) -> str:
        return "boolean"


class Date(BaseDbType):
    """Sqlite3の日付型"""

    __type = datetime.date

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        self.__value = str(self.__value)

    def name(self) -> str:
        return "date"
