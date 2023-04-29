from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from typing import *

from bhrc_accounting import config
from bhrc_accounting.controller.command import command
from .base import BaseView
from .widget import base_widget as bw
from .widget.commandbar import CommandItemName, CommandBar, ImageButtonCommandItem


class TransferSlipView(BaseView):
    """View class for the transfer slip window

    Attributes:
        window (WrappedToplevel): The window
        var_member (StringVar): The variable for the member name
        var_sum_debit (StringVar): The variable for the sum of debit
        var_sum_credit (StringVar): The variable for the sum of credit
        command_bar (CommandBar): The command bar
        details (List[TransferSlipDetailRow]): The detail rows
        register (Callable): The callback for the register button
        account_titles (Dict[int, str]): The account titles for the combobox
    """

    DETAIL_HEADER_ROW_COUNT = 1

    def __init__(self, master: bw.ITclComposite, account_titles: Dict[int, str]):
        """Constructor

        Args:
            master: The master widget for the view
            account_titles: The account titles for the combobox
        """
        super().__init__(master)
        # Variables
        self.var_member = tk.StringVar()
        self.var_sum_debit = tk.StringVar()
        self.var_sum_credit = tk.StringVar()
        self.details: List[TransferSlipDetailRow]
        self.account_titles = account_titles

    def create_widgets(self):
        # *****ウィンドウ*****
        self.window = bw.WrappedToplevel(self.master)
        # *****外枠*****
        frame_outer = bw.WrappedTFrame(self.master)
        frame_outer.grid(column=0, row=0)
        frame_outer.columnconfigure(0, weight=1)
        frame_outer.rowconfigure(0, weight=1)
        # *****コマンドバー*****
        self.command_bar = CommandBar(frame_outer)
        self.command_bar.add_command_item(
            ImageButtonCommandItem(
                CommandItemName("save"),
                config.get_image_path("hard-drive-solid.png"),
            )
        )
        self.command_bar.add_command_item(
            ImageButtonCommandItem(
                CommandItemName("insert_row"),
                config.get_image_path("insert.png"),
            )
        )
        self.command_bar.grid(column=0, row=0, sticky=NSEW)
        self.command_bar.rowconfigure(0, weight=1)
        # *****ヘッダー部*****
        frame_header = bw.WrappedTFrame(frame_outer)
        frame_header.grid(column=0, row=1, sticky=NSEW)
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        bw.WrappedTLabel(
            frame_header,
            text="振替伝票",
            font=("System", 32, "underline"),
            anchor=CENTER,
        ).grid(column=0, row=0, rowspan=2, sticky=NSEW)
        bw.WrappedTLabel(
            frame_header,
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 24),
            anchor=CENTER,
        ).grid(column=1, row=0, rowspan=2, sticky=NSEW)
        bw.WrappedTLabel(
            frame_header,
            text="記入者",
            font=("System", 16),
            anchor=CENTER,
        ).grid(column=2, row=0, sticky=NSEW)
        bw.WrappedTEntry(
            frame_header,
            textvariable=self.var_member,
            width=10,
            font=("System", 20),
        ).grid(column=2, row=1, sticky=NSEW)
        # *****明細部*****
        frame_detail = bw.WrappedTFrame(frame_outer)
        frame_detail.grid(column=0, row=2, sticky=NSEW)
        frame_detail.columnconfigure(0, weight=1)
        # 明細部ヘッダー
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        for i in range(0, len(detail_labels)):
            frame_detail.columnconfigure(i, weight=TransferSlipDetailRow.WIDTHS[i])
            bw.WrappedTLabel(
                frame_detail,
                text=detail_labels[i],
                anchor=CENTER,
            ).grid(column=i, row=0, sticky=NSEW)
        # 明細部ボディ
        self.details = list()
        for i in range(0, 7):
            self.details.append(TransferSlipDetailRow(frame_detail, self.account_titles))
            self.details[i].create_widgets()
            self.details[i].grid_widgets(i + self.DETAIL_HEADER_ROW_COUNT)
        # 明細部フッター
        bw.WrappedTEntry(
            frame_detail,
            textvariable=self.var_sum_debit,
            width=-1,
            font=("System", 18),
            state="readonly",
        ).grid(column=0, row=1000, sticky=NSEW)
        bw.WrappedTLabel(
            frame_detail, text="合計", font=("System", 24, "bold"), anchor=CENTER
        ).grid(column=1, row=1000, columnspan=3, sticky=NSEW)
        bw.WrappedTEntry(
            frame_detail,
            textvariable=self.var_sum_credit,
            width=-1,
            font=("System", 18),
            state="readonly",
        ).grid(column=4, row=1000, sticky=NSEW)

    def destroy_widgets(self):
        self.window.destroy()

    def grid_widgets(self):
        self.window.grid()

    def forget_widgets(self):
        self.window.forget()

    def remove_widgets(self):
        self.window.grid_remove()

    # def _insert_row(self, *args):
    #     """行挿入処理"""
    #     master = self.details[0].parent
    #     new_detail = TransferSlipDetailRow(master)
    #     self.details.append(new_detail)
    #     row_index = self.details.index(new_detail) + self.DETAIL_HEADER_ROW_COUNT
    #     self.details[-1].create_widgets()
    #     self.details[-1].grid_widgets(row_index)

    # def set_register_command(self, callback: Callable):
    #     """登録ボタンのコマンドを設定する

    #     Args:
    #         callback (Callable): 登録ボタンのコマンド
    #     """
    #     self.register = callback


class TransferSlipDetailRow:
    """振替伝票明細行クラス

    Attributes:
        WIDTHS (Tuple[int, int, int, int, int]): 各列の幅
        parent (bw.ITclComposite): 明細行の各ウィジェットを直接配置する親ウィジェット
        cmd_valid_ammount (UDigitValidateCommand): 金額入力時の検証コマンド
        var_debit_amount (tk.StringVar): 借方金額変数
        var_debit_title (tk.StringVar): 借方科目変数
        var_summary (tk.StringVar): 摘要変数
        var_credit_title (tk.StringVar): 貸方科目変数
        var_credit_amount (tk.StringVar): 貸方金額変数
    """

    WIDTHS = (12, 10, 40, 10, 12)

    def __init__(self, parent: bw.ITclComposite, account_titles: Dict[int, str]):
        """コンストラクタ

        Args:
            parent (tk.Widget): 明細行の各ウィジェットを直接配置する親ウィジェット
            account_titles (Dict[int, str]): 科目IDと科目名の辞書
        """
        self.parent = parent
        self.account_titles = account_titles
        self.cmd_valid_ammount = command.UDigitValidateCommand(parent)
        self.var_debit_amount = tk.StringVar()
        self.var_debit_title = tk.StringVar()
        self.var_summary = tk.StringVar()
        self.var_credit_title = tk.StringVar()
        self.var_credit_amount = tk.StringVar()

    def create_widgets(self):
        """明細行の各ウィジェットを配置する

        Args:
            row (int): 親ウィジェット内の各ウィジェットを配置する行番号
        """
        ttk.Style().configure(
            "TCombobox", font="System 24", borderwidth=1, relief="solid"
        )
        self.debit_amount = bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_debit_amount,
            width=self.WIDTHS[0],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
            # style="transferslip_detail.TEntry",
        )
        self.debit_item = bw.WrappedTCombobox(
            self.parent,
            textvariable=self.var_debit_title,
            values=list(self.account_titles.values()),
            width=self.WIDTHS[1],
            font=("System", 18),
        )
        self.summary = bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_summary,
            width=self.WIDTHS[2],
            font=("System", 18),
        )
        self.credit_title = bw.WrappedTCombobox(
            self.parent,
            textvariable=self.var_credit_title,
            values=list(self.account_titles.values()),
            width=self.WIDTHS[3],
            font=("System", 18),
        )
        self.credit_amount = bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_credit_amount,
            width=self.WIDTHS[4],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
            # style="transferslip_detail.TEntry",
        )

    def grid_widgets(self, row: int):
        self.debit_amount.grid(column=0, row=row, sticky=NSEW)
        self.debit_item.grid(column=1, row=row, sticky=NSEW)
        self.summary.grid(column=2, row=row, sticky=NSEW)
        self.credit_title.grid(column=3, row=row, sticky=NSEW)
        self.credit_amount.grid(column=4, row=row, sticky=NSEW)
