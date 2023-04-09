from datetime import date
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from typing import *

from bhrc_accounting.commands import UDigitValidateCommand
from bhrc_accounting.const import *
from bhrc_accounting.widgets import (
    ITclComposite,
    WrappedTCombobox,
    WrappedTEntry,
    WrappedTLabel,
    WrappedToplevel,
    WrappedTFrame,
)


class Ledger(tk.Toplevel):
    """元帳ウィンドウ"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("元帳")

        # >>>>>DEBUG>>>>>
        WrappedTLabel(
            self, text="Ledger(元帳ウィンドウ)", padding=40, font=FONT_FIXED_24
        ).grid()
        # <<<<<DEBUG<<<<<


class JournalEntry(tk.Toplevel):
    """仕訳帳ウィンドウ"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("仕訳帳原簿")

        # >>>>>DEBUG>>>>>
        WrappedTLabel(
            self, text="JournalEntry(仕訳帳ウィンドウ)", padding=40, font=FONT_FIXED_24
        ).grid()
        # <<<<<DEBUG<<<<<

