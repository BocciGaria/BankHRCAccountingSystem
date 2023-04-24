import abc
from typing import *

from . import dbtype


class IField(metaclass=abc.ABCMeta):
    """フィールドインターフェース

    データベーステーブルフィールドオブジェクトが提供するインターフェースを定義します。
    """

    @property
    @abc.abstractproperty
    def type(self) -> Type[dbtype.IDbType]:
        """データ型

        Returns:
            Type[IDbType]: フィールドのデータ型
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_value(self) -> dbtype.IDbType:
        """値取得

        Returns:
            IDbType: データベース値オブジェクト
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def set_value(self, value: Any) -> None:
        """値設定

        Args:
            value (IDbType): データベース値オブジェクト
        """
        raise NotImplementedError()


class BaseField(IField):
    """フィールド抽象クラス

    フィールド具象クラスの要求に対する標準処理、その他のインターフェースを定義します。
    """

    __type: Type[dbtype.IDbType]

    @property
    def type(self) -> Type[dbtype.IDbType]:
        return self.__type

    def get_value(self) -> dbtype.IDbType:
        if self.__value is None:
            raise ValueError("値が設定されていません。")
        return self.__value

    def set_value(self, value: Any) -> None:
        self.__value = self.__type(value)
