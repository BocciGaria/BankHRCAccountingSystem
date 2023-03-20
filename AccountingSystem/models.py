import abc
from typing import Iterable, Union

from database.fields import IField, RealField, TextField


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
        id (TextField): 会員番号
    """

    def __init__(self) -> None:
        super().__init__()
        self.id = TextField()


if __name__ == "__main__":
    pass
