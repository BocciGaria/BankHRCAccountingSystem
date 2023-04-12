from bhrc_accounting import command
from . import base_widget, journal, ledger, transferslip


class Menu(base_widget.WrappedTFrame):
    """メインメニューフレームクラス"""

    def __init__(self, parent: base_widget.WrappedTk, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        # 振替伝票ウィンドウ表示ボタン
        base_widget.WrappedTButton(
            self,
            text="振替伝票",
            command=command.CreateWindowCommand(
                self, transferslip.TransferSlip
            ).get_signature(),
        ).grid(column=0, row=0, padx=100, pady=50)
        # 仕訳帳ウィンドウ表示ボタン
        base_widget.WrappedTButton(
            self,
            text="仕訳帳",
            command=command.CreateWindowCommand(self, journal.Journal),
        ).grid(column=0, row=1, padx=100, pady=50)
        # 元帳ウィンドウ表示ボタン
        base_widget.WrappedTButton(
            self,
            text="元帳",
            command=command.CreateWindowCommand(self, ledger.Ledger),
        ).grid(column=0, row=2, padx=100, pady=50)
