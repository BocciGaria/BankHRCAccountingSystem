from bhrc_accounting.commands import CreateWindowCommand
from bhrc_accounting.widgets import WrappedTButton, WrappedTFrame, WrappedTk
from bhrc_accounting.windows import TransferSlip


class App(WrappedTk):
    """アプリケーションルートオブジェクトクラス"""


class Menu(WrappedTFrame):
    """メインメニューフレームクラス"""

    def __init__(self, parent: App, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        WrappedTButton(
            self,
            text="振替伝票",
            command=CreateWindowCommand(self, TransferSlip).get_signature(),
        ).grid(column=0, row=0, padx=100, pady=50)


root = App()

Menu(root).grid()

root.mainloop()
