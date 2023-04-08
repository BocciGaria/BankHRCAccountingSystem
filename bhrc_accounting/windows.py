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


class TransferSlip(WrappedToplevel):
    """振替伝票ウィンドウ
    Attributes:

    """

    valid_ammount: UDigitValidateCommand
    var_member: tk.StringVar
    var_debit_amount: list[tk.StringVar]
    var_debit_item: list[tk.StringVar]
    var_summary: list[tk.StringVar]
    var_credit_item: list[tk.StringVar]
    var_credit_amount: list[tk.StringVar]
    var_sum_debit: tk.StringVar
    var_sum_credit: tk.StringVar

    def __init__(self, parent: ITclComposite, **kwargs):
        super().__init__(parent, **kwargs)
        # ========== メンバー変数の初期化 ==========
        self.valid_ammount = UDigitValidateCommand(self)
        self.var_member = tk.StringVar()
        self.var_debit_amount = list()
        self.var_debit_item = list()
        self.var_summary = list()
        self.var_credit_item = list()
        self.var_credit_amount = list()
        for i in range(0, 7):
            self.var_debit_amount.append(tk.StringVar())
            self.var_debit_item.append(tk.StringVar())
            self.var_summary.append(tk.StringVar())
            self.var_credit_item.append(tk.StringVar())
            self.var_credit_amount.append(tk.StringVar())
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
        # 外枠
        frame_outer = WrappedTFrame(self, style="debug0.TFrame")
        frame_outer.grid(column=0, row=0)
        frame_outer.columnconfigure(0, weight=1)
        frame_outer.rowconfigure(0, weight=1)
        # ヘッダー部
        frame_header = WrappedTFrame(frame_outer, style="debug1.TFrame")
        frame_header.grid(column=0, row=0, sticky=NSEW)
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        frame_title = WrappedTFrame(frame_header, style="debug2.TFrame")
        frame_title.grid(column=0, row=0, rowspan=2, sticky=NSEW)
        frame_title.columnconfigure(0, weight=1)
        frame_title.rowconfigure(0, weight=1)
        WrappedTLabel(
            frame_title,
            style="debug0.TLabel",
            text="振替伝票",
            font=("System", 18, "underline"),
            anchor=CENTER,
        ).grid(column=0, row=0, sticky=NSEW)
        frame_date = WrappedTFrame(frame_header, style="debug2.TFrame")
        frame_date.columnconfigure(0, weight=1)
        frame_date.rowconfigure(0, weight=1)
        frame_date.grid(column=1, row=0, rowspan=2, sticky=NSEW)
        label_date = WrappedTLabel(
            frame_date,
            style="debug0.TLabel",
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 16),
            anchor=CENTER,
        )
        label_date.grid(column=0, row=0, sticky=NSEW)
        frame_member_header = WrappedTFrame(frame_header, style="debug2.TFrame")
        frame_member_header.grid(column=2, row=0, sticky=NSEW)
        frame_member_header.columnconfigure(0, weight=1)
        frame_member_header.rowconfigure(0, weight=1)
        label_member_header = WrappedTLabel(
            frame_member_header,
            style="debug0.TLabel",
            text="記入者",
            font=("System", 11),
            anchor=CENTER,
        )
        label_member_header.grid(column=0, row=0, sticky=NSEW)
        frame_member_input = WrappedTFrame(frame_header, style="debug2.TFrame")
        frame_member_input.grid(column=2, row=1, sticky=NSEW)
        frame_member_input.columnconfigure(0, weight=1)
        frame_member_input.rowconfigure(0, weight=1)
        entry_member = WrappedTEntry(
            frame_member_input,
            textvariable=self.var_member,
            style="debug0.TEntry",
            width=10,
        )
        entry_member.grid(column=0, row=0, sticky=NSEW)
        # 明細部
        frame_detail = WrappedTFrame(frame_outer, style="debug1.TFrame")
        frame_detail.grid(column=0, row=1, sticky=NSEW)
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        frames_detail_header = list(
            [
                WrappedTFrame(frame_detail, style="debug2.TFrame")
                for i in range(0, len(detail_labels))
            ]
        )
        for i in range(0, len(detail_labels)):
            frames_detail_header[i].grid(column=i, row=0, sticky=NSEW)
            frames_detail_header[i].columnconfigure(0, weight=1)
            WrappedTLabel(
                frames_detail_header[i],
                text=detail_labels[i],
                style="debug0.TLabel",
                anchor=CENTER,
            ).grid(column=0, row=0, sticky=NSEW)
        frames_detail_cell: List[List[WrappedTFrame]] = list()
        for i in range(0, 7):
            frames_detail_cell.append(
                list(
                    [
                        WrappedTFrame(frame_detail, style="debug2.TFrame")
                        for j in range(0, len(detail_labels))
                    ]
                )
            )
        for i in range(0, 7):
            frames_detail_cell[i][0].grid(column=0, row=i + 1, sticky=NSEW)
            WrappedTEntry(
                frames_detail_cell[i][0],
                textvariable=self.var_debit_amount[i],
                width=12,
                validate="key",
                validatecommand=self.valid_ammount.get_signature(),
            ).grid(column=0, row=i + 1, sticky=NSEW)
            frames_detail_cell[i][1].grid(column=1, row=i + 1, sticky=NSEW)
            WrappedTCombobox(
                frames_detail_cell[i][1],
                width=8,
                textvariable=self.var_debit_item[i],
            ).grid(column=1, row=i + 1, sticky=NSEW)
            frames_detail_cell[i][2].grid(column=2, row=i + 1, sticky=NSEW)
            WrappedTEntry(
                frames_detail_cell[i][2], width=40, textvariable=self.var_summary
            ).grid(column=2, row=i + 1, sticky=NSEW)
            frames_detail_cell[i][3].grid(column=3, row=i + 1, sticky=NSEW)
            WrappedTCombobox(
                frames_detail_cell[i][3],
                width=8,
                textvariable=self.var_credit_item[i],
            ).grid(column=3, row=i + 1, sticky=NSEW)
            frames_detail_cell[i][4].grid(column=4, row=i + 1, sticky=NSEW)
            WrappedTEntry(
                frames_detail_cell[i][4],
                textvariable=self.var_credit_amount[i],
                width=12,
                validate="key",
                validatecommand=self.valid_ammount.get_signature(),
            ).grid(column=4, row=i + 1, sticky=NSEW)
        # 合計部
        frame_sum_debit = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_sum_debit.grid(column=0, row=8, sticky=NSEW)
        frame_sum_debit.columnconfigure(0, weight=1)
        WrappedTLabel(frame_sum_debit, textvariable=self.var_sum_debit).grid(
            column=0, row=0, sticky=NSEW
        )
        frame_sum_title = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_sum_title.grid(column=1, row=8, columnspan=3, sticky=NSEW)
        frame_sum_title.columnconfigure(0, weight=1)
        WrappedTLabel(
            frame_sum_title, text="合計", font=("System", 18, "bold"), anchor=CENTER
        ).grid(column=0, row=0, sticky=NSEW)
        frame_sum_credit = WrappedTFrame(frame_detail, style="debug2.TFrame")
        frame_sum_credit.grid(column=4, row=8, sticky=NSEW)
        frame_sum_credit.columnconfigure(0, weight=1)
        WrappedTLabel(frame_sum_credit, textvariable=self.var_sum_credit).grid(
            column=0, row=0, sticky=NSEW
        )
