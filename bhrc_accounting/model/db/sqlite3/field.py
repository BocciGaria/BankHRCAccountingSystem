from typing import *

from . import dbtype
from ..field import BaseField


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
