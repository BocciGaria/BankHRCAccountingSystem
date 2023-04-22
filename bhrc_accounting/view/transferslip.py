from datetime import date
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from typing import *

from bhrc_accounting import config
from bhrc_accounting.controller.command import command
from bhrc_accounting.view.widget import (
    base_widget,
    commandbar,
)


class TransferSlipView(base_widget.WrappedToplevel):
    """振替伝票ウィンドウクラス

    Attributes:
        DETAIL_HEADER_ROW_COUNT (int): 振替伝票明細のヘッダー行数
        var_member (tk.StringVar): 会員名の変数
        var_sum_debit (tk.StringVar): 借方合計の変数
        var_sum_credit (tk.StringVar): 貸方合計の変数
        details (List[TransferSlipDetail]): 振替伝票明細のリスト
    """

    DETAIL_HEADER_ROW_COUNT = 1

    def __init__(self, parent: base_widget.ITclComposite, **kwargs):
        super().__init__(parent, **kwargs)
        # ========== メンバー変数の初期化 ==========
        self.var_member = tk.StringVar()
        self.var_sum_debit = tk.StringVar()
        self.var_sum_credit = tk.StringVar()

        ttk.Style().configure("TEntry", font="System 24", borderwidth=1, relief="solid")
        ttk.Style().configure("TLabel", font="System 24", borderwidth=1, relief="solid")
        ttk.Style().configure(
            "TCombobox", font="System 24", borderwidth=1, relief="solid"
        )

        # ========== コンテンツの生成 ==========
        # *****外枠*****
        frame_outer = base_widget.WrappedTFrame(self)
        frame_outer.grid(column=0, row=0)
        frame_outer.columnconfigure(0, weight=1)
        frame_outer.rowconfigure(0, weight=1)
        # *****コマンドバー*****
        cmd_bar = commandbar.CommandBar(frame_outer)
        cmd_bar.add_command(
            commandbar.ImageButtonCommandItem(
                config.get_image_path("hard-drive-solid.png"),
                self._register,
            )
        )
        cmd_bar.add_command(
            commandbar.ImageButtonCommandItem(
                config.get_image_path("insert.png"),
                self._insert_row,
            )
        )
        cmd_bar.grid(column=0, row=0, sticky=NSEW)
        cmd_bar.rowconfigure(0, weight=1)
        # *****ヘッダー部*****
        frame_header = base_widget.WrappedTFrame(frame_outer)
        frame_header.grid(column=0, row=1, sticky=NSEW)
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        base_widget.WrappedTLabel(
            frame_header,
            text="振替伝票",
            font=("System", 32, "underline"),
            anchor=CENTER,
        ).grid(column=0, row=0, rowspan=2, sticky=NSEW)
        base_widget.WrappedTLabel(
            frame_header,
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 24),
            anchor=CENTER,
        ).grid(column=1, row=0, rowspan=2, sticky=NSEW)
        base_widget.WrappedTLabel(
            frame_header,
            text="記入者",
            font=("System", 16),
            anchor=CENTER,
        ).grid(column=2, row=0, sticky=NSEW)
        base_widget.WrappedTEntry(
            frame_header,
            textvariable=self.var_member,
            width=10,
            font=("System", 20),
        ).grid(column=2, row=1, sticky=NSEW)
        # *****明細部*****
        frame_detail = base_widget.WrappedTFrame(frame_outer)
        frame_detail.grid(column=0, row=2, sticky=NSEW)
        frame_detail.columnconfigure(0, weight=1)
        # 明細部ヘッダー
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        for i in range(0, len(detail_labels)):
            frame_detail.columnconfigure(i, weight=TransferSlipDetailRow.WIDTHS[i])
            base_widget.WrappedTLabel(
                frame_detail,
                text=detail_labels[i],
                anchor=CENTER,
            ).grid(column=i, row=0, sticky=NSEW)
        # 明細部ボディ
        self.details: List[TransferSlipDetailRow] = list()
        for i in range(0, 7):
            self.details.append(TransferSlipDetailRow(frame_detail))
            self.details[i].grid_items(i + self.DETAIL_HEADER_ROW_COUNT)
        # 明細部フッター
        base_widget.WrappedTEntry(
            frame_detail,
            textvariable=self.var_sum_debit,
            width=-1,
            font=("System", 18),
            state="readonly",
        ).grid(column=0, row=1000, sticky=NSEW)
        base_widget.WrappedTLabel(
            frame_detail, text="合計", font=("System", 24, "bold"), anchor=CENTER
        ).grid(column=1, row=1000, columnspan=3, sticky=NSEW)
        base_widget.WrappedTEntry(
            frame_detail,
            textvariable=self.var_sum_credit,
            width=-1,
            font=("System", 18),
            state="readonly",
        ).grid(column=4, row=1000, sticky=NSEW)

    def _register(self, *args):
        """登録処理"""
        pass

    def _insert_row(self, *args):
        """行挿入処理"""
        master = self.details[0].parent
        new_detail = TransferSlipDetailRow(master)
        self.details.append(new_detail)
        row_index = self.details.index(new_detail) + self.DETAIL_HEADER_ROW_COUNT
        self.details[-1].grid_items(row_index)


class TransferSlipDetailRow:
    """振替伝票明細行クラス

    Attributes:
        WIDTHS (Tuple[int, int, int, int, int]): 各列の幅
        parent (base_widget.ITclComposite): 明細行の各ウィジェットを直接配置する親ウィジェット
        cmd_valid_ammount (UDigitValidateCommand): 金額入力時の検証コマンド
        var_debit_amount (tk.StringVar): 借方金額変数
        var_debit_item (tk.StringVar): 借方科目変数
        var_summary (tk.StringVar): 摘要変数
        var_credit_item (tk.StringVar): 貸方科目変数
        var_credit_amount (tk.StringVar): 貸方金額変数
    """

    WIDTHS = (12, 10, 40, 10, 12)

    def __init__(self, parent: base_widget.ITclComposite):
        """コンストラクタ

        Args:
            parent (tk.Widget): 明細行の各ウィジェットを直接配置する親ウィジェット
        """
        self.parent = parent
        self.cmd_valid_ammount = command.UDigitValidateCommand(parent)
        self.var_debit_amount = tk.StringVar()
        self.var_debit_item = tk.StringVar()
        self.var_summary = tk.StringVar()
        self.var_credit_item = tk.StringVar()
        self.var_credit_amount = tk.StringVar()

    def grid_items(self, row):
        """明細行の各ウィジェットを配置する

        Args:
            row (int): 親ウィジェット内の各ウィジェットを配置する行番号
        """
        ttk.Style().configure(
            "TCombobox", font="System 24", borderwidth=1, relief="solid"
        )
        base_widget.WrappedTEntry(
            self.parent,
            textvariable=self.var_debit_amount,
            width=self.WIDTHS[0],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
            # style="transferslip_detail.TEntry",
        ).grid(column=0, row=row, sticky=NSEW)
        base_widget.WrappedTCombobox(
            self.parent,
            textvariable=self.var_debit_item,
            width=self.WIDTHS[1],
            font=("System", 18),
        ).grid(column=1, row=row, sticky=NSEW)
        base_widget.WrappedTEntry(
            self.parent,
            textvariable=self.var_summary,
            width=self.WIDTHS[2],
            font=("System", 18),
        ).grid(column=2, row=row, sticky=NSEW)
        base_widget.WrappedTCombobox(
            self.parent,
            textvariable=self.var_credit_item,
            width=self.WIDTHS[3],
            font=("System", 18),
        ).grid(column=3, row=row, sticky=NSEW)
        base_widget.WrappedTEntry(
            self.parent,
            textvariable=self.var_credit_amount,
            width=self.WIDTHS[4],
            font=("System", 18),
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
            # style="transferslip_detail.TEntry",
        ).grid(column=4, row=row, sticky=NSEW)

        # >>>>>DEBUG>>>>>

        # <<<<<DEBUG<<<<<
