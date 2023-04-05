import tkinter as tk
from tkinter import ttk

from commands import WidgetLifecycleCommand
from widgets import ITclComposite, WrappedTk, WrappedTFrame
from windows import TransferSlip


class App(WrappedTk):
    """アプリケーションルートオブジェクトクラス"""


class Menu(WrappedTFrame):
    """メインメニューフレームクラス"""

    widget_lc_cmd: WidgetLifecycleCommand
    # window_transfer_slip: TransferSlip

    def __init__(self, parent: tk.Tk, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.widget_lc_cmd = WidgetLifecycleCommand(self.get_root())
        # self.window_transfer_slip = TransferSlip(parent)
        ttk.Button(
            self,
            text="振替伝票",
            command=lambda: self.widget_lc_cmd.new_window(TransferSlip),
        ).grid(column=0, row=0, padx=100, pady=50)


if __name__ == "__main__":
    root = App()

    Menu(root).grid()

    root.mainloop()
