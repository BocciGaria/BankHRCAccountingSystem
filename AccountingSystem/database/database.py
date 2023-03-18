from pathlib import Path
import sqlite3
from sqlite3 import *


class Database:
    """データベースクラス

    データベース接続情報を保持し、接続を管理する

    Attributes:
    """

    def __init__(self, name, base_dir):
        self.__path = Path.joinpath(base_dir, name)

    @property
    def path(self) -> Path:
        return self.__path

    def connect(self) -> Connection:
        self.__connection = sqlite3.connect(self.path)
        return self.__connection

    # def close(self) -> None:
    #     if self.__connection is None:
    #         raise ValueError("接続がありません。")
    #     self.__connection.close()
