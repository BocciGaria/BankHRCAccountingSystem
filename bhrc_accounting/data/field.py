import abc

from . import dbtype


class IField(metaclass=abc.ABCMeta):
    """フィールドインターフェース

    データベーステーブルフィールドオブジェクトが提供するインターフェースを定義します。
    """

    @property
    @abc.abstractproperty
    def type(self) -> dbtype.IDbType:
        """データ型"""
        raise NotImplementedError()


class BaseField(IField):
    """フィールド抽象クラス

    フィールド具象クラスの要求に対する標準処理、その他のインターフェースを定義します。
    """

    __type: dbtype.IDbType

    @property
    def type(self) -> dbtype.IDbType:
        return self.__type


class TextField(BaseField):
    """テキスト型フィールド

    データ型が文字列のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self) -> None:
        super().__init__()
        self.__type = dbtype.Text()


class FloatField(BaseField):
    """8バイト浮動小数点数型フィールド"""

    def __init__(self) -> None:
        super().__init__()
        self.__type = dbtype.Float()


class RealField(FloatField):
    """SQLiteの8バイト浮動小数点数型フィールド"""

    def __init__(self) -> None:
        super().__init__()
        self.__type = dbtype.Real()


if __name__ == "__main__":
    pass
