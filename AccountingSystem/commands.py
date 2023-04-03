import tkinter as tk
class ValidateCommand:
    """入力チェッククラス"""

    is_digit: str

    def __init__(self, root: tk.Tk):
        self.is_digit = root.register(self.__is_digit)

    def __is_digit(self, input: str):
        """数値チェック"""
        return input.isdigit()
