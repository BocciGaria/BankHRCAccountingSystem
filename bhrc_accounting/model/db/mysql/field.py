from typing import *

from . import dbtype
from ..field import BaseField


class CharField(BaseField):
    """固定長文字型フィールド

    データ型が固定長文字のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Char


class VarCharField(BaseField):
    """可変長文字型フィールド

    データ型が可変長文字型のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.VarChar


class IntField(BaseField):
    """符号付き整数型フィールド

    データ型が符号付き整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Int


class TinyIntField(BaseField):
    """符号付き1バイト整数型フィールド

    データ型が符号付き1バイト整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.TinyInt


class SmallIntField(BaseField):
    """符号付き2バイト整数型フィールド

    データ型が符号付き2バイト整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.SmallInt


class MediumIntField(BaseField):
    """符号付き3バイト整数型フィールド

    データ型が符号付き3バイト整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.MediumInt


class BigIntField(BaseField):
    """符号付き8バイト整数型フィールド

    データ型が符号付き8バイト整数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.BigInt


class FloatField(BaseField):
    """4バイト浮動小数点数型フィールド

    データ型が4バイト浮動小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Float


class DoubleField(BaseField):
    """8バイト浮動小数点数型フィールド

    データ型が8バイト浮動小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Double


class DecimalField(BaseField):
    """固定小数点数型フィールド

    データ型が固定小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Decimal


class NumericField(BaseField):
    """固定小数点数型フィールド

    データ型が固定小数点数のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Numeric


class BitField(BaseField):
    """ビットフィールド

    データ型がビットフィールドのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Bit


class DateField(BaseField):
    """日付型フィールド

    データ型が日付のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Date


class DateTimeField(BaseField):
    """日時型フィールド

    データ型が日時のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.DateTime


class TimeField(BaseField):
    """時刻型フィールド

    データ型が時刻のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Time


class TimeStampField(BaseField):
    """タイムスタンプ型フィールド

    データ型がタイムスタンプのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.TimeStamp


class YearField(BaseField):
    """年型フィールド

    データ型が年のカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Year


class BinaryField(BaseField):
    """バイナリ型フィールド

    データ型がバイナリのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Binary


class VarBinaryField(BaseField):
    """可変長バイナリ型フィールド

    データ型が可変長バイナリのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.VarBinary


class TextField(BaseField):
    """テキスト型フィールド

    データ型がテキストのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Text


class BlobField(BaseField):
    """BLOB型フィールド

    データ型がBLOBのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Blob


class EnumField(BaseField):
    """ENUM型フィールド

    データ型がENUMのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Enum


class SetField(BaseField):
    """SET型フィールド

    データ型がSETのカラムに対応するフィールドオブジェクトを表現します。
    """

    # __type = dbtype.Set
