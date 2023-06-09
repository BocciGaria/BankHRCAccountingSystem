from typing import *

from . import dbtype
from ..field import BaseField, FieldName


class TextField(BaseField):
    """テキスト型フィールド

    データ型が文字列のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Text


class IntegerField(BaseField):
    """符号付き整数型フィールド

    データ型が符号付き整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Integer


class RealField(BaseField):
    """8バイト浮動小数点数型フィールド

    データ型が8バイト浮動小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Real


class BlobField(BaseField):
    """バイナリデータ型フィールド

    データ型がバイナリデータのカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Blob


class BooleanField(BaseField):
    """真偽値型フィールド

    データ型が真偽値のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Boolean


class DateField(BaseField):
    """日付型フィールド

    データ型が日付のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self, field_name: FieldName) -> None:
        super().__init__(field_name)
        self._type = dbtype.Date
