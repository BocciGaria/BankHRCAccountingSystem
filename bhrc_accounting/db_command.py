import abc

from singleton import Singleton

from db_connection import IDatabaseConnection
from models import IModel


class ISqlCommand(Singleton, metaclass=abc.ABCMeta):
    """SQLコマンドクラスインターフェース"""

    @abc.abstractmethod
    def __init__(self, connection: IDatabaseConnection):
        """コンストラクタ

        Args:
            connection (IDatabaseConnection): データベース接続オブジェクト
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def select(self, model: IModel) -> None:
        """SELECTメソッド

        Args:
            model (IModel): モデルオブジェクト
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def insert(self, model: IModel) -> None:
        """INSERTメソッド

        Args:
            model (IModel): モデルオブジェクト
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, model: IModel) -> None:
        """UPDATEメソッド

        Args:
            model (IModel): モデルオブジェクト
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, model: IModel) -> None:
        """DELETEメソッド

        Args:
            model (IModel): モデルオブジェクト
        """
        raise NotImplementedError()


class Sqlite3Command(ISqlCommand):
    """SQLite3コマンドクラス"""

    __connection: IDatabaseConnection

    def __init__(self, connection: IDatabaseConnection):
        self.__connection = connection
