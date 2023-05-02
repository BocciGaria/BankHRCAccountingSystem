import abc
from typing import *

from . import dbtype


class IField(metaclass=abc.ABCMeta):
    """フィールドインターフェース

    データベーステーブルフィールドオブジェクトが提供するインターフェースを定義します。
    """

    @abc.abstractmethod
    def __init__(self, initial_value: Any = None) -> None:
        """コンストラクタ

        Args:
            initial_value (Any): 初期値
        """
        raise NotImplementedError()

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

    _type: Type[dbtype.IDbType]

    def __init__(self, initial_value: Any = None) -> None:
        self._value = None
        if initial_value is not None:
            self.set_value(initial_value)

    @property
    def type(self) -> Type[dbtype.IDbType]:
        return self._type

    def get_value(self) -> dbtype.IDbType:
        if self._value is None:
            raise ValueError("値が設定されていません。")
        return self._value

    def set_value(self, value: Any) -> None:
        self._value = self._type(value)
