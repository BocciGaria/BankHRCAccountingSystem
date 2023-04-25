from bhrc_accounting.controller.command import command
from . import journal, ledger, transferslip
from .base import BaseView
from .widget import base_widget as bw


# class MenuView(bw.WrappedTFrame):
#     """メインメニューフレームクラス"""

#     def __init__(self, parent: bw.WrappedTk, **kwargs) -> None:
#         super().__init__(parent, **kwargs)
#         # 振替伝票ウィンドウ表示ボタン
#         bw.WrappedTButton(
#             self,
#             text="振替伝票",
#             command=command.CreateWindowCommand(
#                 self, transferslip.TransferSlipView
#             ).get_signature(),
#         ).grid(column=0, row=0, padx=100, pady=50)
#         # 仕訳帳ウィンドウ表示ボタン
#         bw.WrappedTButton(
#             self,
#             text="仕訳帳",
#             command=command.CreateWindowCommand(self, journal.JournalView),
#         ).grid(column=0, row=1, padx=100, pady=50)
#         # 元帳ウィンドウ表示ボタン
#         bw.WrappedTButton(
#             self,
#             text="元帳",
#             command=command.CreateWindowCommand(self, ledger.LedgerView),
#         ).grid(column=0, row=2, padx=100, pady=50)


class MenuView(BaseView):
    """View for the main menu"""

    def __init__(self, master):
        super().__init__(master)
        self.frame_outer: bw.WrappedTFrame
        self.btn_transferslip: bw.WrappedTButton
        self.btn_journal: bw.WrappedTButton
        self.btn_ledger: bw.WrappedTButton

    def create_widgets(self):
        self.frame_outer = bw.WrappedTFrame(self.master)
        self.btn_transferslip = bw.WrappedTButton(
            self.frame_outer,
            text="振替伝票",
            command=command.CreateWindowCommand(
                self.master, transferslip.TransferSlipView
            ).get_signature(),
        )
        self.btn_journal = bw.WrappedTButton(
            self.frame_outer,
            text="仕訳帳",
            command=command.CreateWindowCommand(
                self.master, journal.JournalView
            ).get_signature(),
        )
        self.btn_ledger = bw.WrappedTButton(
            self.frame_outer,
            text="元帳",
            command=command.CreateWindowCommand(
                self.master, ledger.LedgerView
            ).get_signature(),
        )

    def destroy_widgets(self):
        self.frame_outer.destroy()

    def grid_widgets(self):
        self.frame_outer.grid()
        self.btn_transferslip.grid(column=0, row=0, padx=100, pady=50)
        self.btn_journal.grid(column=0, row=1, padx=100, pady=50)
        self.btn_ledger.grid(column=0, row=2, padx=100, pady=50)

    def forget_widgets(self):
        self.frame_outer.forget()

    def remove_widgets(self):
        self.frame_outer.grid_remove()
