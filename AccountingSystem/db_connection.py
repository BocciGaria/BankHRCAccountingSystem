import abc
from pathlib import Path
import sqlite3
from typing import *

from db_command import ISqlCommand


class IDatabaseConnection(metaclass=abc.ABCMeta):
    """データベース接続インターフェース

    データベース接続情報を保持し、接続を管理する

    Properties:
        command (ISqlCommand): データベースコマンドオブジェクト
    """

    @abc.abstractmethod
    def __init__(self, con_str: str) -> None:
        """コンストラクタ

        Args:
            con_str (str): 接続文字列
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def command(self) -> ISqlCommand:
        """SQLコマンドクラスのインスタンスを取得する

        Returns:
            ISqlCommand: _description_
        """
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
    """SQLite3のデータベース接続クラス

    Properties:
        command (ISqlCommand): SQLite3のコマンドクラスインスタンス
    """

    __path: Path
    __connection: sqlite3.Connection
    __cursor: sqlite3.Cursor

    def __init__(self, path: Path):
        self.__path = path

    @property
    def command(self) -> ISqlCommand:
        return

    def connect(self) -> None:
        self.__connection = sqlite3.connect(self.__path)

    def open(self) -> None:
        self.__cursor = self.__connection.cursor()

    def close(self) -> None:
        self.__connection.close()

    def commit(self) -> None:
        self.__connection.commit()

    def rollback(self) -> None:
        self.__connection.rollback()
