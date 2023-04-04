import tkinter as tk
from tkinter.constants import *

from const import *


class ValidateCommand:
    """入力チェッククラス"""

    check_input_amount: str
    is_digit: str

    def __init__(self, root: tk.Tk) -> None:
        self.is_digit = root.register(self.__is_digit)
        self.check_input_amount = root.register(self.__check_input_amount)

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


class WidgetLifecycleCommand:
    def new_window(self, win: tk.Toplevel):
        win.grid()
