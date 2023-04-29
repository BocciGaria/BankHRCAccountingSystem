import abc
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

    _type: Type[Any] = None

    def __init__(self, value: Any) -> None:
        if self.validate(value):
            raise ValueError("引数 value の値または型が不正です。")
        self._value = self._type(value)

    def __str__(self) -> str:
        return str(self._value)

    @property
    def value(self) -> Any:
        return self._value

    def validate(self, value: Any) -> bool:
        try:
            self._type(value)
        except ValueError:
            return True
        except TypeError:
            return True
        return False
