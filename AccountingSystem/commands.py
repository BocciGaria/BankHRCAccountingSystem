import abc
import tkinter as tk
from tkinter.constants import *
from typing import Any, Type

from const import *
from mytyping import CommandSignature, Index, InputAction, ValidateCmdOption, WidgetName
from widgets import ITclComposite, WrappedTk, WrappedToplevel


class ICommand(metaclass=abc.ABCMeta):
    """コマンドインターフェース

    Tclオブジェクトからの要求される処理を実装するCommandオブジェクトのインターフェースを定義します。
    """

    @abc.abstractmethod
    def __init__(self, client: ITclComposite = None, receiver: Any = None) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_signature(self) -> CommandSignature:
        """コマンドのシグネチャを取得する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """コマンドの実行

        コマンド具象クラスの要求に対する処理を実装する
        """
        raise NotImplementedError()


class Command(ICommand):
    """コマンド抽象クラス"""

    def get_signature(self) -> CommandSignature:
        return self.execute


class ValidateCommand(ICommand):
    """入力チェック抽象クラス"""

    cmd_str: str

    def __init__(self, client: ITclComposite = None, receiver: Any = None) -> None:
        self.cmd_str = client.get_root().register(self.execute)

    def get_signature(self) -> CommandSignature:
        return (self.execute, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")

    def execute(
        self,
        d: InputAction,
        i: Index,
        P: str,
        s: str,
        S: str,
        v: ValidateCmdOption,
        V: ValidateCmdOption,
        w: WidgetName,
    ) -> bool:
        super().__execute()


class DigitValidateCommand(ValidateCommand):
    """数値入力コマンドクラス"""

    def execute(
        self,
        d: InputAction,
        i: Index,
        P: str,
        s: str,
        S: str,
        v: ValidateCmdOption,
        V: ValidateCmdOption,
        w: WidgetName,
    ) -> bool:
        if d != "1":
            return True
        return S.isdigit()


class UDigitValidateCommand(ValidateCommand):
    """正の数値入力コマンドクラス"""

    def execute(
        self,
        d: InputAction,
        i: Index,
        P: str,
        s: str,
        S: str,
        v: ValidateCmdOption,
        V: ValidateCmdOption,
        w: WidgetName,
    ) -> bool:
        if d != "1":
            return True
        return S.isdigit() and not P.startswith("0")


class CreateWindowCommand(Command):
    """ウィンドウ生成コマンドクラス"""

    __root_window: WrappedTk
    __window_type: Type[WrappedToplevel]

    def __init__(
        self, client: ITclComposite = None, receiver: Type[WrappedToplevel] = None
    ) -> None:
        if client is None:
            raise ValueError("client is None")
        if receiver is None:
            raise ValueError("receiver is None")
        self.__root_window = client.get_root()
        self.__window_type = receiver

    def execute(self, *args, **kwargs) -> Any:
        self.__window_type(self.__root_window)
