from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from typing import *

from bhrc_accounting.command import UDigitValidateCommand
from bhrc_accounting.widget.base_widget import (
    ITclComposite,
    WrappedTCombobox,
    WrappedTEntry,
    WrappedTLabel,
    WrappedToplevel,
    WrappedTFrame,
)


class TransferSlip(WrappedToplevel):
    """振替伝票ウィンドウ

    Attributes:
        var_member (tk.StringVar): 会員名の変数
        var_sum_debit (tk.StringVar): 借方合計の変数
        var_sum_credit (tk.StringVar): 貸方合計の変数
        details (List[TransferSlipDetail]): 振替伝票明細のリスト
    """

    def __init__(self, parent: ITclComposite, **kwargs):
        super().__init__(parent, **kwargs)
        # ========== メンバー変数の初期化 ==========
        self.var_member = tk.StringVar()
        self.var_sum_debit = tk.StringVar()
        self.var_sum_credit = tk.StringVar()

        """>>>>>FOR DEBUG>>>>>"""
        ttk.Style().configure(
            "debug0.TFrame", background="green", borderwidth=2, relief="groove"
        )
        ttk.Style().configure(
            "debug1.TFrame", background="red", borderwidth=2, relief="groove"
        )
        ttk.Style().configure(
            "debug2.TFrame", background="yellow", borderwidth=2, relief="groove"
        )
        ttk.Style().configure(
            "debug0.TLabel", background="blue", borderwidth=2, relief="groove"
        )
        ttk.Style().configure(
            "debug0.TEntry", background="blue", borderwidth=2, relief="groove"
        )
        ttk.Style().configure(
            "debug0.Treeview", background="pale green", borderwidth=2, relief="groove"
        )
        """<<<<<FOR DEBUG<<<<<"""

        # ========== コンテンツの生成 ==========
        # *****外枠*****
        frame_outer = WrappedTFrame(self, style="debug0.TFrame")
        frame_outer.grid(column=0, row=0)
        frame_outer.columnconfigure(0, weight=1)
        frame_outer.rowconfigure(0, weight=1)
        # *****ヘッダー部*****
        frame_header = WrappedTFrame(frame_outer, style="debug1.TFrame")
        frame_header.grid(column=0, row=0, sticky=NSEW)
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        WrappedTLabel(
            frame_header,
            style="debug0.TLabel",
            text="振替伝票",
            font=("System", 18, "underline"),
            anchor=CENTER,
        ).grid(column=0, row=0, rowspan=2, sticky=NSEW)
        WrappedTLabel(
            frame_header,
            style="debug0.TLabel",
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 16),
            anchor=CENTER,
        ).grid(column=1, row=0, rowspan=2, sticky=NSEW)
        WrappedTLabel(
            frame_header,
            style="debug0.TLabel",
            text="記入者",
            font=("System", 11),
            anchor=CENTER,
        ).grid(column=2, row=0, sticky=NSEW)
        WrappedTEntry(
            frame_header,
            textvariable=self.var_member,
            style="debug0.TEntry",
            width=10,
        ).grid(column=2, row=1, sticky=NSEW)
        # *****明細部*****
        frame_detail = WrappedTFrame(frame_outer, style="debug1.TFrame")
        frame_detail.grid(column=0, row=1, sticky=NSEW)
        frame_detail.columnconfigure(0, weight=1)
        # 明細部ヘッダー
        frame_detail_header = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_detail_header.grid(column=0, row=0, sticky=NSEW)
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        for i in range(0, len(detail_labels)):
            frame_detail_header.columnconfigure(
                i, weight=TransferSlipDetailRow.WIDTHS[i]
            )
            WrappedTLabel(
                frame_detail_header,
                text=detail_labels[i],
                style="debug0.TLabel",
                anchor=CENTER,
            ).grid(column=i, row=0, sticky=NSEW)
        # 明細部ボディ
        frame_detail_details = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_detail_details.grid(column=0, row=1, sticky=NSEW)
        frame_detail_details.columnconfigure(0, weight=1)
        self.details: List[TransferSlipDetailRow] = list()
        for i in range(0, 7):
            self.details.append(TransferSlipDetailRow(frame_detail_details))
            self.details[i].grid(column=0, row=i, sticky=NSEW)
        # 明細部フッター
        frame_detail_footer = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_detail_footer.grid(column=0, row=2, sticky=NSEW)
        for i in range(0, len(TransferSlipDetailRow.WIDTHS)):
            frame_detail_footer.columnconfigure(
                i, weight=TransferSlipDetailRow.WIDTHS[i]
            )
        WrappedTLabel(
            frame_detail_footer, textvariable=self.var_sum_debit, style="debug0.TLabel"
        ).grid(column=0, row=0, sticky=NSEW)
        WrappedTLabel(
            frame_detail_footer, text="合計", font=("System", 18, "bold"), anchor=CENTER
        ).grid(column=1, row=0, columnspan=3, sticky=NSEW)
        WrappedTLabel(
            frame_detail_footer, textvariable=self.var_sum_credit, style="debug0.TLabel"
        ).grid(column=4, row=0, sticky=NSEW)


class TransferSlipDetailRow(WrappedTFrame):
    """振替伝票明細行クラス

    Constants:
        WIDTHS (Tuple[int, int, int, int, int]): 各列の幅

    Attributes:
        cmd_valid_ammount (UDigitValidateCommand): 金額入力時の検証コマンド
        var_debit_amount (tk.StringVar): 借方金額変数
        var_debit_item (tk.StringVar): 借方科目変数
        var_summary (tk.StringVar): 摘要変数
        var_credit_item (tk.StringVar): 貸方科目変数
        var_credit_amount (tk.StringVar): 貸方金額変数
    """

    WIDTHS = (12, 8, 40, 8, 12)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd_valid_ammount = UDigitValidateCommand(self)
        self.var_debit_amount = tk.StringVar()
        self.var_debit_item = tk.StringVar()
        self.var_summary = tk.StringVar()
        self.var_credit_item = tk.StringVar()
        self.var_credit_amount = tk.StringVar()
        for i in range(0, len(self.WIDTHS)):
            self.columnconfigure(i, weight=self.WIDTHS[i])
        WrappedTEntry(
            self,
            textvariable=self.var_debit_amount,
            width=self.WIDTHS[0],
            validate="key",
            validatecommand=self.cmd_valid_ammount.get_signature(),
        ).grid(column=0, row=0, sticky=NSEW)
        WrappedTCombobox(
            self, textvariable=self.var_debit_item, width=self.WIDTHS[1]
        ).grid(column=1, row=0, sticky=NSEW)
        WrappedTEntry(self, textvariable=self.var_summary, width=self.WIDTHS[2]).grid(
            column=2, row=0, sticky=NSEW
        )
        WrappedTCombobox(
            self, textvariable=self.var_credit_item, width=self.WIDTHS[3]
        ).grid(column=3, row=0, sticky=NSEW)
        WrappedTEntry(
            self, textvariable=self.var_credit_amount, width=self.WIDTHS[4]
        ).grid(column=4, row=0, sticky=NSEW)
