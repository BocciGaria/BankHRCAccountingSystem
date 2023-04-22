from bhrc_accounting.controller.command import command
from . import journal, ledger, transferslip
from .widget import base_widget as bw


class MenuView(bw.WrappedTFrame):
    """メインメニューフレームクラス"""

    def __init__(self, parent: bw.WrappedTk, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        # 振替伝票ウィンドウ表示ボタン
        bw.WrappedTButton(
            self,
            text="振替伝票",
            command=command.CreateWindowCommand(
                self, transferslip.TransferSlipView
            ).get_signature(),
        ).grid(column=0, row=0, padx=100, pady=50)
        # 仕訳帳ウィンドウ表示ボタン
        bw.WrappedTButton(
            self,
            text="仕訳帳",
            command=command.CreateWindowCommand(self, journal.JournalView),
        ).grid(column=0, row=1, padx=100, pady=50)
        # 元帳ウィンドウ表示ボタン
        bw.WrappedTButton(
            self,
            text="元帳",
            command=command.CreateWindowCommand(self, ledger.LedgerView),
        ).grid(column=0, row=2, padx=100, pady=50)
