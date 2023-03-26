import abc

from model import fields


class IDbType(metaclass=abc.ABCMeta):
    """データベースデータ型インターフェース

    データベースのデータ型が提供するインターフェースを定義します。
    """

    @property
    @abc.abstractproperty
    def name(self) -> str:
        """データ型名"""
        raise NotImplementedError()

    @abc.abstractclassmethod
    def validate(self, value: fields.IField) -> bool:
        """データ型による値チェック(True:正常、False:不正)"""
        raise NotImplementedError()


class Text(IDbType):
    """文字列型"""

    @property
    def name(self) -> str:
        return "text"

    def validate(self, value: fields.IField) -> bool:
        return True


class Float(IDbType):
    """8バイト浮動小数型"""

    @property
    def name(self) -> str:
        return "float"


class Real(Float):
    """SQLiteの8バイト浮動小数型"""

    def name(self) -> str:
        return "real"


if __name__ == "__main__":
    pass
