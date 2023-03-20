import abc

import db_type


class IField(metaclass=abc.ABCMeta):
    """フィールドインターフェース

    データベーステーブルフィールドオブジェクトが提供するインターフェースを定義します。
    """

    @property
    @abc.abstractproperty
    def type(self) -> db_type.IDbType:
        """データ型"""
        raise NotImplementedError()


class BaseField(IField):
    """フィールド抽象クラス

    フィールド具象クラスの要求に対する標準処理、その他のインターフェースを定義します。"""

    __type: db_type.IDbType

    @property
    def type(self) -> db_type.IDbType:
        return self.__type


class TextField(BaseField):
    """テキスト型フィールド

    データ型が文字列のカラムに対応するフィールドオブジェクトを表現します。
    """

    def __init__(self) -> None:
        super().__init__()
        self.__type = db_type.Text()


class FloatField(BaseField):
    """8バイト浮動小数点数型フィールド"""

    def __init__(self) -> None:
        super().__init__()
        self.__type = db_type.Float()


class RealField(FloatField):
    """SQLiteの8バイト浮動小数点数型フィールド"""

    def __init__(self) -> None:
        super().__init__()
        self.__type = db_type.Real()


if __name__ == "__main__":
    pass
