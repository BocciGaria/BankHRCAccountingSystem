import abc
import re
import tkinter as tk
from tkinter.constants import *
from typing import Any, Type

from bhrc_accounting.const import *
from bhrc_accounting.typing import (
    CommandSignature,
    Index,
    InputAction,
    ValidateCmdOption,
    WidgetName,
)
from bhrc_accounting.controller.base import IController
from bhrc_accounting.view.widget import base_widget as bw


class ICommand(metaclass=abc.ABCMeta):
    """コマンドインターフェース

    Tclオブジェクトからの要求される処理を実装するCommandオブジェクトのインターフェースを定義します。
    """

    @abc.abstractmethod
    def __init__(self, client: bw.ITclComposite = None, receiver: Any = None) -> None:
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

    def __init__(self, client: bw.ITclComposite = None, receiver: Any = None) -> None:
        self.root = client.get_root()
        self.cmd_str = self.root.register(self.execute)

    def get_signature(self) -> CommandSignature:
        return (self.cmd_str, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")

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
        self.widget = self.root.nametowidget(w)


class DigitValidateCommand(ValidateCommand):
    """数値入力バリデーションコマンドクラス"""

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
        return P.isdigit()


class DateValidateCommand(ValidateCommand):
    """日付入力バリデーションコマンドクラス"""

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
        super().execute(d, i, P, s, S, v, V, w)
        result = bool(re.match(r"^\d{4}-\d{2}-\d{2}$", P))
        if result:
            self.widget.config(foreground="black")
        else:
            self.widget.config(foreground="red")
        return result


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
        return S.isdigit() and not P.startswith("0")


class CreateWindowCommand(Command):
    """ウィンドウ生成コマンドクラス"""

    def __init__(
        self,
        client: bw.ITclComposite = None,
        receiver: Type[IController] = None,
    ) -> None:
        if client is None:
            raise ValueError("client is None")
        if receiver is None:
            raise ValueError("receiver is None")
        self.__root_window: bw.WrappedTk = client.get_root()
        self.__controller_type: Type[IController] = receiver

    def execute(self, *args, **kwargs) -> Any:
        self.__controller_type(self.__root_window).run()
