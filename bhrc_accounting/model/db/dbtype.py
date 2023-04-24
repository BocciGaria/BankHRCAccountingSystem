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

    __type: Type[Any]

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