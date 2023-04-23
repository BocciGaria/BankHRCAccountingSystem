import abc
import datetime
from typing import *


class IDbType(metaclass=abc.ABCMeta):
    """データベースデータ型インターフェース

    データベースのデータ型が提供するインターフェースを定義します。
    """

    @abc.abstractproperty
    def name(self) -> str:
        """データ型名"""
        raise NotImplementedError()

    @abc.abstractclassmethod
    def validate(self, value: Any) -> bool:
        """データ型による値チェック(True:正常、False:不正)"""
        raise NotImplementedError()

    @abc.abstractproperty
    def value(self) -> Any:
        """データ"""
        raise NotImplementedError()


class BaseDbType(IDbType):
    """データベースデータ型基底クラス"""

    __type: Type

    def __init__(self, value: Any) -> None:
        if self.validate(value):
            raise ValueError("引数 value の値または型が不正です。")
        self.__value = self.__type(value)

    @property
    def value(self) -> Any:
        return self.__value

    def validate(self, value: Any) -> bool:
        try:
            self.__type(value)
        except ValueError:
            return False
        except TypeError:
            return False
        return True


class Text(IDbType):
    """文字列型"""

    __type = str

    @property
    def name(self) -> str:
        return "text"


class Real(IDbType):
    """8バイト浮動小数型"""

    __type = float

    def name(self) -> str:
        return "real"


class Integer(IDbType):
    """整数型"""

    __type = int

    def name(self) -> str:
        return "integer"


class Blob(IDbType):
    """バイナリ型"""

    __type = bytes

    def name(self) -> str:
        return "blob"


class Boolean(IDbType):
    """真偽型"""

    __type = bool

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        if self.__value:
            self.__value = 1
        else:
            self.__value = 0

    def name(self) -> str:
        return "boolean"


class Date(IDbType):
    """日付型"""

    __type = datetime.date

    def __init__(self, value: Any) -> None:
        super().__init__(value)
        self.__value = str(self.__value)

    def name(self) -> str:
        return "date"
