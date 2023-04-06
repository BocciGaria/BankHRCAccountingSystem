from datetime import date
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from typing import *

from commands import ValidateCommand
from const import *
from widgets import ITclComposite, WrappedToplevel, WrappedTFrame, WrappedTLabel


class Ledger(tk.Toplevel):
    """元帳
    Attributes:

    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("元帳")

        # >>>>>DEBUG>>>>>
        ttk.Label(self, text="Ledger(元帳ウィンドウ)", padding=40, font=FONT_FIXED_24).grid()
        # <<<<<DEBUG<<<<<


class JournalEntry(tk.Toplevel):
    """仕訳帳ウィンドウ
    Attributes:

    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("仕訳帳原簿")

        # >>>>>DEBUG>>>>>
        ttk.Label(
            self, text="JournalEntry(仕訳帳ウィンドウ)", padding=40, font=FONT_FIXED_24
        ).grid()
        # <<<<<DEBUG<<<<<


class TransferSlip(WrappedToplevel):
    """振替伝票ウィンドウ
    Attributes:

    """

    valid_cmd: ValidateCommand
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
        self.valid_cmd = ValidateCommand(self.get_root())
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
        frame_external = ttk.Frame(self, style="debug0.TFrame", width=1280, height=600)
        frame_external.grid(column=0, row=0)
        # ヘッダー部
        frame_header = ttk.Frame(frame_external, style="debug1.TFrame")
        frame_header.grid(column=0, row=0, sticky=NSEW)
        frame_title = ttk.Frame(
            frame_header, style="debug2.TFrame", width=630, height=105
        )
        frame_title.grid(column=0, row=0, rowspan=2, sticky=NSEW)
        label_title = ttk.Label(
            frame_title,
            style="debug0.TLabel",
            text="振替伝票",
            font=("System", 18, "underline"),
        )
        label_title.grid(column=0, row=0, sticky=NSEW)
        frame_date = ttk.Frame(
            frame_header, style="debug2.TFrame", width=500, height=105
        )
        frame_date.grid(column=1, row=0, rowspan=2, sticky=NSEW)
        label_date = ttk.Label(
            frame_date,
            style="debug0.TLabel",
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 16),
        )
        label_date.grid(column=0, row=0, sticky=NSEW)
        frame_member_header = ttk.Frame(
            frame_header, style="debug2.TFrame", width=150, height=40
        )
        frame_member_header.grid(column=2, row=0, sticky=NSEW)
        label_member_header = ttk.Label(
            frame_member_header,
            style="debug0.TLabel",
            text="記入者",
            font=("System", 11),
        )
        label_member_header.grid(column=0, row=0, sticky=NSEW)
        frame_member_input = ttk.Frame(
            frame_header, style="debug2.TFrame", width=150, height=65
        )
        frame_member_input.grid(column=2, row=1, sticky=NSEW)
        entry_member = ttk.Entry(
            frame_member_input,
            textvariable=self.var_member,
            style="debug0.TEntry",
            width=8,
        )
        entry_member.grid(column=0, row=0, sticky=NSEW)
        # 明細部
        frame_detail = ttk.Frame(
            frame_external, style="debug1.TFrame", width=1280, height=426
        )
        frame_detail.grid(column=0, row=1)
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        for i in range(0, len(detail_labels)):
            ttk.Label(frame_detail, text=detail_labels[i], style="debug0.TLabel").grid(
                column=i, row=0, sticky=NSEW
            )
        for i in range(0, 7):
            ttk.Entry(
                frame_detail,
                textvariable=self.var_debit_amount[i],
                validate="key",
                validatecommand=(self.valid_cmd.check_input_amount, "%S", "%P"),
            ).grid(column=0, row=i + 1, sticky=NSEW)
            ttk.Combobox(
                frame_detail,
                textvariable=self.var_debit_item[i],
            ).grid(column=1, row=i + 1, sticky=NSEW)
            ttk.Entry(frame_detail, textvariable=self.var_summary).grid(
                column=2, row=i + 1, sticky=NSEW
            )
            ttk.Combobox(frame_detail, textvariable=self.var_credit_item[i]).grid(
                column=3, row=i + 1, sticky=NSEW
            )
            ttk.Entry(
                frame_detail,
                textvariable=self.var_credit_amount[i],
                validate="key",
                validatecommand=(self.valid_cmd.check_input_amount, "%S", "%P"),
            ).grid(column=4, row=i + 1, sticky=NSEW)
        # 合計部
        frame_sum = WrappedTFrame(
            frame_external, style="debug1.TFrame", width=1280, height=69
        )
        frame_sum.grid(column=0, row=2)
        label_sum_debit = WrappedTLabel(
            frame_sum, textvariable=self.var_sum_debit, style="debug0.TLabel"
        )
        label_sum_debit.grid(column=0, row=0, sticky=NSEW)
        label_sum_title = WrappedTLabel(
            frame_sum, text="合計", font=("System", 18, "bold"), style="debug0.TLabel"
        )
        label_sum_title.grid(column=1, row=0, sticky=NSEW)
        label_sum_credit = WrappedTLabel(
            frame_sum, textvariable=self.var_sum_credit, style="debug0.TLabel"
        )
        label_sum_credit.grid(columns=2, row=0, sticky=NSEW)

        # ========== ジオメトリー設定 ==========
        # self.geometry("1280x600")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=105)
        # self.rowconfigure(1, weight=426)
        # self.rowconfigure(2, weight=69)
        # self.rowconfigure(0, weight=1)
        # frame_external.columnconfigure(0, weight=1)
        # frame_external.rowconfigure(0, weight=105)
        # frame_external.rowconfigure(1, weight=426)
        # frame_external.rowconfigure(2, weight=1)
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        frame_header.rowconfigure(0, weight=40)
        frame_header.rowconfigure(1, weight=65)
        frame_member_input.columnconfigure(0, weight=1)
        frame_member_input.rowconfigure(0, weight=1)
        frame_detail.columnconfigure(0, weight=230)
        frame_detail.columnconfigure(1, weight=180)
        frame_detail.columnconfigure(2, weight=460)
        frame_detail.columnconfigure(3, weight=180)
        frame_detail.columnconfigure(4, weight=230)
        frame_detail.rowconfigure(0, weight=41)
        frame_detail.rowconfigure(1, weight=55)
        frame_detail.rowconfigure(2, weight=55)
        frame_detail.rowconfigure(3, weight=55)
        frame_detail.rowconfigure(4, weight=55)
        frame_detail.rowconfigure(5, weight=55)
        frame_detail.rowconfigure(6, weight=55)
        frame_detail.rowconfigure(7, weight=55)
        frame_sum.columnconfigure(0, weight=230)
        frame_sum.columnconfigure(1, weight=820)
        frame_sum.columnconfigure(2, weight=230)
