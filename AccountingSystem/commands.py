import abc
import tkinter as tk
from tkinter.constants import *
from typing import Type, TypeVar

from const import *
from widgets import ITclComposite, WrappedTk, WrappedToplevel


class ICommand(metaclass=abc.ABCMeta):
    """コマンドインターフェース

    Tclオブジェクトからの要求される処理を実装するCommandオブジェクトのインターフェースを定義します。
    """

    @abc.abstractmethod
    def __init__(self, root_window: WrappedTk = None) -> None:
        raise NotImplementedError()


class ValidateCommand(ICommand):
    """入力チェッククラス"""

    check_input_amount: str
    is_digit: str

    def __init__(self, root_window: WrappedTk = None) -> None:
        self.is_digit = root_window.register(self.__is_digit)
        self.check_input_amount = root_window.register(self.__check_input_amount)

    def __is_digit(self, input: str) -> bool:
        """数値入力チェック"""
        return input.isdigit()

    def __check_input_amount(self, input: str, new_val: str) -> bool:
        """金額入力チェック"""
        return (
            input.isdigit()
            and len(new_val) <= MAX_LENGTH_INPUT_AMOUNT
            and not new_val.startswith("0")
        )


class WidgetLifecycleCommand(ICommand):
    """ウィジェットのライフサイクルコマンドクラス"""

    __root_window: WrappedTk

    def __init__(self, root_window: WrappedTk = None) -> None:
        self.__root_window = root_window

    def new_window(self, window_type: Type[WrappedToplevel]):
        """トップレベルオブジェクト生成"""
        window_type(self.__root_window)
