import abc
from pathlib import Path
import sqlite3
from typing import *


class IDatabaseConnection(abc.ABCMeta):
    """データベース接続インターフェース

    データベース接続情報を保持し、接続を管理する
    """

    @abc.abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        raise NotImplementedError()

    @abc.abstractproperty
    @property
    def name(self) -> str:
        """データベース名"""
        raise NotImplementedError()

    @abc.abstractmethod
    def connect(self) -> None:
        """接続を開始する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def open(self) -> None:
        """接続を開く"""
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self) -> None:
        """接続を閉じる"""
        raise NotImplementedError()

    @abc.abstractmethod
    def begin_transaction(self) -> None:
        """トランザクションを開始する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def dispose_transaction(self) -> None:
        """トランザクションを破棄する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def commit(self) -> None:
        """トランザクションをコミットする"""
        raise NotImplementedError()

    @abc.abstractmethod
    def rollback(self) -> None:
        """トランザクションをロールバックする"""
        raise NotImplementedError()


class Sqlite3Connection(IDatabaseConnection):
    """SQLite3データベース接続クラス

    SQLite3のデータベース接続情報を保持し、接続を管理する

    Attributes:
        name(str): データベース名

    """

    def __init__(self, path: Path):
        self.__path = path

    @property
    def path(self) -> Path:
        return self.__path

    def connect(self) -> sqlite3.Connection:
        self.__connection = sqlite3.connect(self.path)
        return self.__connection

    # def close(self) -> None:
    #     if self.__connection is None:
    #         raise ValueError("接続がありません。")
    #     self.__connection.close()
