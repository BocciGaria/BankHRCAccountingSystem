from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from typing import *

from bhrc_accounting import config
from bhrc_accounting.controller.command import command
from .base import BaseView
from .widget import base_widget as bw
from .widget.commandbar import CommandBar, ImageButtonCommandItem


class TransferSlipView(BaseView):
    """View class for the transfer slip window

    Attributes:
        var_slip_number (tk.StringVar): Slip number
        var_member (tk.StringVar): Member name
        var_sum_debit (tk.StringVar): Total debit amount
        var_sum_credit (tk.StringVar): Total credit amount
        window (bw.WrappedToplevel): Window
        details (List[TransferSlipDetailRow]): Details
        register (Callable): Callback
    """

    DETAIL_HEADER_ROW_COUNT = 1

    def __init__(self, master):
        super().__init__(master)
        # Variables
        self.var_slip_number = tk.StringVar()
        self.var_date = tk.StringVar()
        self.var_member = tk.StringVar()
        self.var_sum_debit = tk.StringVar()
        self.var_sum_credit = tk.StringVar()
        # Window
        self.window: bw.WrappedToplevel
        # Details
        self.details: List[TransferSlipDetailRow]
        # Callback
        self.register: Callable = None

    def create_widgets(self):
        # ブロック節
        if self.register is None:
            raise ValueError("register is not set")

        # *****ウィンドウ*****
        self.window = bw.WrappedToplevel(self.master)

        # *****外枠*****
        frame_outer = bw.WrappedTFrame(self.window)
        frame_outer.grid(column=0, row=0)
        frame_outer.columnconfigure(0, weight=1)
        frame_outer.rowconfigure(0, weight=1)
        # *****コマンドバー*****
        cmd_bar = CommandBar(frame_outer)
        cmd_bar.add_command(
            ImageButtonCommandItem(
                config.get_image_path("hard-drive-solid.png"),
                self.register,
            )
        )
        cmd_bar.add_command(
            ImageButtonCommandItem(
                config.get_image_path("insert.png"),
                self._insert_row,
            )
        )
        cmd_bar.grid(column=0, row=0, sticky=NSEW)
        cmd_bar.rowconfigure(0, weight=1)
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
        frame_slip_number = bw.WrappedTFrame(frame_header)
        frame_slip_number.grid(column=1, row=0, sticky=NSEW)
        bw.WrappedTLabel(
            frame_slip_number,
            text="No.",
        ).grid(column=0, row=0, sticky=NSEW)
        bw.WrappedTEntry(
            frame_slip_number,
            textvariable=self.var_slip_number,
            validate="key",
            validatecommand=command.UDigitValidateCommand(self.master).get_signature(),
        ).grid(column=1, row=0, sticky=NSEW)
        frame_date = bw.WrappedTFrame(frame_header)
        frame_date.grid(column=1, row=1, sticky=NSEW)
        bw.WrappedTLabel(
            frame_date,
            text="日付 : ",
            font=("System", 16),
            anchor=CENTER,
        ).grid(column=0, row=0, sticky=NSEW)
        bw.WrappedTEntry(
            frame_date,
            textvariable=self.var_date,
            validate="focusout",
            validatecommand=command.DateValidateCommand(self.master).get_signature(),
            font=("System", 24),
        ).grid(column=1, row=0, sticky=NSEW)
        self.var_date.set(date.today().strftime("%Y-%m-%d"))
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
            self.details.append(TransferSlipDetailRow(frame_detail))
            self.details[i].grid_items(i + self.DETAIL_HEADER_ROW_COUNT)
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

    def _insert_row(self, *args):
        """行挿入処理"""
        master = self.details[0].parent
        new_detail = TransferSlipDetailRow(master)
        self.details.append(new_detail)
        row_index = self.details.index(new_detail) + self.DETAIL_HEADER_ROW_COUNT
        self.details[-1].grid_items(row_index)

    def set_register_command(self, callback: Callable):
        """登録ボタンのコマンドを設定する

        Args:
            callback (Callable): 登録ボタンのコマンド
        """
        self.register = callback


class TransferSlipDetailRow:
    """振替伝票明細行クラス

    Attributes:
        WIDTHS (Tuple[int, int, int, int, int]): 各列の幅
        parent (bw.ITclComposite): 明細行の各ウィジェットを直接配置する親ウィジェット
        cmd_valid_ammount (UDigitValidateCommand): 金額入力時の検証コマンド
        var_date (tk.StringVar): 日付変数
        var_debit_amount (tk.StringVar): 借方金額変数
        var_debit_item (tk.StringVar): 借方科目変数
        var_summary (tk.StringVar): 摘要変数
        var_credit_item (tk.StringVar): 貸方科目変数
        var_credit_amount (tk.StringVar): 貸方金額変数
    """

    WIDTHS = (12, 10, 40, 10, 12)

    def __init__(self, parent: bw.ITclComposite):
        """コンストラクタ

        Args:
            parent (tk.Widget): 明細行の各ウィジェットを直接配置する親ウィジェット
        """
        self.parent = parent
        self.cmd_valid_ammount = command.UDigitValidateCommand(parent)
        self.var_debit_amount = tk.StringVar()
        self.var_debit_title = tk.StringVar()
        self.var_summary = tk.StringVar()
        self.var_credit_title = tk.StringVar()
        self.var_credit_amount = tk.StringVar()

    def grid_items(self, row):
        """明細行の各ウィジェットを配置する

        Args:
            row (int): 親ウィジェット内の各ウィジェットを配置する行番号
        """
        ttk.Style().configure(
            "TCombobox", font="System 24", borderwidth=1, relief="solid"
        )
        bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_debit_amount,
            width=self.WIDTHS[0],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
        ).grid(column=0, row=row, sticky=NSEW)
        bw.WrappedTCombobox(
            self.parent,
            textvariable=self.var_debit_title,
            width=self.WIDTHS[1],
            font=("System", 18),
        ).grid(column=1, row=row, sticky=NSEW)
        bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_summary,
            width=self.WIDTHS[2],
            font=("System", 18),
        ).grid(column=2, row=row, sticky=NSEW)
        bw.WrappedTCombobox(
            self.parent,
            textvariable=self.var_credit_title,
            width=self.WIDTHS[3],
            font=("System", 18),
        ).grid(column=3, row=row, sticky=NSEW)
        bw.WrappedTEntry(
            self.parent,
            textvariable=self.var_credit_amount,
            width=self.WIDTHS[4],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
        ).grid(column=4, row=row, sticky=NSEW)
