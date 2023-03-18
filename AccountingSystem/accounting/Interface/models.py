import abc

from Interface.fields import IField


class IModel(metaclass=abc.ABCMeta):
    """モデル抽象クラス

    データベースの各テーブルオブジェクトのインターフェースを提供します。
    """

    @property
    @abc.abstractproperty
    def columns(self) -> tuple[IField]:
        """カラム"""
        raise NotImplementedError()

    @columns.setter
    def columns(self):
        """カラムセッター"""
        raise NotImplementedError()

    @property
    @abc.abstractproperty
    def primarykey(self) -> tuple[IField]:
        """主キー"""
        raise NotImplementedError()

    @primarykey.setter
    @abc.abstractmethod
    def primarykey(self):
        """主キーセッター"""
        raise NotImplementedError()

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
