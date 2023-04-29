import abc
from typing import *

from . import dbtype


class FieldName(str):
    """Field name value object"""


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

    @property
    @abc.abstractproperty
    def field_name(self) -> FieldName:
        """フィールド名

        Returns:
            FieldName: フィールド名
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

    def __init__(self, field_name: FieldName) -> None:
        self._type: Type[dbtype.IDbType] = None
        self._field_name = field_name
        self._value: dbtype.IDbType = None

    @property
    def type(self) -> Type[dbtype.IDbType]:
        if self._type is None:
            raise ValueError("The db type of this field is not set.")
        return self._type

    @property
    def field_name(self) -> FieldName:
        if self._field_name is None:
            raise ValueError("The field name of this field is not set.")
        return self._field_name

    def get_value(self) -> dbtype.IDbType:
        if self._value is None:
            raise ValueError("The value of this field is not set.")
        return self._value

    def set_value(self, value: Any) -> None:
        if type(value) is self._type:
            self._value = value
        self._value = self._type(value)
