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


class TextField(BaseField):
    """テキスト型フィールド

    データ型が文字列のカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Text


class IntegerField(BaseField):
    """符号付き整数型フィールド

    データ型が符号付き整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Integer


class RealField(BaseField):
    """8バイト浮動小数点数型フィールド

    データ型が8バイト浮動小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Real


class BlobField(BaseField):
    """バイナリデータ型フィールド

    データ型がバイナリデータのカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Blob


class BooleanField(BaseField):
    """真偽値型フィールド

    データ型が真偽値のカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Boolean


class DateField(BaseField):
    """日付型フィールド

    データ型が日付のカラムに対応するフィールドオブジェクトを表現します。
    """

    __type = dbtype.Date
