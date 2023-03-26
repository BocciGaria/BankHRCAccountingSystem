import abc
from typing import Iterable, Union

from . import fields


class IModel(metaclass=abc.ABCMeta):
    """モデルインターフェース

    データベースの各テーブルオブジェクトが提供するインターフェースを定義します。
    """

    # @property
    # @abc.abstractproperty
    # def columns(self) -> Iterable[IField]:
    #     """カラム"""
    #     raise NotImplementedError()

    # @property
    # @abc.abstractproperty
    # def primarykey(self) -> Iterable[IField]:
    #     """主キー"""
    #     raise NotImplementedError()

    @abc.abstractmethod
    def insert(self):
        """INSERTメソッド"""
        raise NotImplementedError()

    @abc.abstractmethod
    def select(self):
        """SELECTメソッド"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self):
        """UPDATEメソッド"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self):
        """DELETEメソッド"""
        raise NotImplementedError()


class BaseModel(IModel):
    """モデル抽象クラス

    モデル具象クラスの要求に対する標準処理、その他のインターフェースを定義します。
    """


class ClubMember(BaseModel):
    """クラブ会員クラス

    クラブに入会している利用者を実装します。

    Attributes:
        no (TextField): 会員番号
    """

    def __init__(self) -> None:
        super().__init__()
        self.no = fields.RealField()


def sample_function():
    return lambda: 1 + 2 * 3 / 4


if __name__ == "__main__":
    pass
    print("Hello World!")
    print("Hello", "World", "!", sep=" ")

    if True:
        pass

    print("Hello World!")


if __name__ == "__main__":
    print(__package__)
    print(__path__)
