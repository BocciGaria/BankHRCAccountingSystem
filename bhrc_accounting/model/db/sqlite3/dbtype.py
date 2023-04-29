import datetime
from typing import *

from ..dbtype import BaseDbType


class Text(BaseDbType):
    """Sqlite3の文字列型"""

    _type = str

    @property
    def name(self) -> str:
        return "text"


class Real(BaseDbType):
    """Sqlite3の8バイト浮動小数型"""

    _type = float

    def name(self) -> str:
        return "real"


class Integer(BaseDbType):
    """Sqlite3の整数型"""

    _type = int

    def name(self) -> str:
        return "integer"


class Blob(BaseDbType):
    """Sqlite3のバイナリ型"""

    _type = bytes

    def name(self) -> str:
        return "blob"


class Boolean(BaseDbType):
    """Sqlite3の真偽型"""

    _type = bool

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        if self._value:
            self._value = 1
        else:
            self._value = 0

    def name(self) -> str:
        return "boolean"


class Date(BaseDbType):
    """Sqlite3の日付型"""

    _type = datetime.date

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        self._value = str(self._value)

    def name(self) -> str:
        return "date"
