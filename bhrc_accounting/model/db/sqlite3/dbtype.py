import abc
from typing import *


class IDbType(metaclass=abc.ABCMeta):
    """データベースデータ型インターフェース

    データベースのデータ型が提供するインターフェースを定義します。
    """

    @property
    @abc.abstractproperty
    def name(self) -> str:
        """データ型名"""
        raise NotImplementedError()

    @abc.abstractclassmethod
    def validate(self, value: Any) -> bool:
        """データ型による値チェック(True:正常、False:不正)"""
        raise NotImplementedError()


class BaseDbType(IDbType):
    """データベースデータ型基底クラス"""


class Text(IDbType):
    """文字列型"""

    @property
    def name(self) -> str:
        return "text"

    def validate(self, value: str) -> bool:
        return True


class Real(IDbType):
    """8バイト浮動小数型"""

    def name(self) -> str:
        return "real"


class Integer(IDbType):
    """整数型"""

    def name(self) -> str:
        return "integer"


class Blob(IDbType):
    """バイナリ型"""

    def name(self) -> str:
        return "blob"


class Boolean(IDbType):
    """真偽型"""

    def name(self) -> str:
        return "boolean"


class Date(IDbType):
    """日付型"""

    def name(self) -> str:
        return "date"
