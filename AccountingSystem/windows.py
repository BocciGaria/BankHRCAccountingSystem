from datetime import date
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from typing import *

from commands import ValidateCommand
from const import *
from widgets import ITclComposite, TclComposite


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


class TransferSlip(tk.Toplevel, TclComposite):
    """振替伝票ウィンドウ
    Attributes:

    """

    valid_cmd: ValidateCommand
    var_member: tk.StringVar
    var_debit_amount: list[tk.IntVar]
    var_debit_item: list[tk.IntVar]
    var_summary: list[tk.StringVar]
    var_credit_item: list[tk.IntVar]
    var_credit_amount: list[tk.IntVar]

    def __init__(self, parent: TclComposite, **kwargs):
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
        frame_external = ttk.Frame(self, style="debug0.TFrame")
        # ヘッダー部
        frame_header = ttk.Frame(frame_external, style="debug1.TFrame")
        frame_title = ttk.Frame(
            frame_header, style="debug2.TFrame", width=630, height=105
        )
        label_title = ttk.Label(
            frame_title,
            style="debug0.TLabel",
            text="振替伝票",
            font=("System", 18, "underline"),
        )
        frame_date = ttk.Frame(
            frame_header, style="debug2.TFrame", width=500, height=105
        )
        label_date = ttk.Label(
            frame_date,
            style="debug0.TLabel",
            text=date.today().strftime("%Y/%m/%d"),
            font=("System", 16),
        )
        frame_member_header = ttk.Frame(
            frame_header, style="debug2.TFrame", width=150, height=40
        )
        label_member_header = ttk.Label(
            frame_member_header,
            style="debug0.TLabel",
            text="記入者",
            font=("System", 11),
        )
        frame_member_input = ttk.Frame(
            frame_header, style="debug2.TFrame", width=150, height=65
        )
        entry_member = ttk.Entry(
            frame_member_input,
            textvariable=self.var_member,
            style="debug0.TEntry",
            width=8,
        )
        # 明細部
        frame_detail = ttk.Frame(frame_external, style="debug1.TFrame")
        detail_labels = ("金額", "借方科目", "摘要", "貸方科目", "金額")
        for i in range(0, len(detail_labels)):
            ttk.Label(frame_detail, text=detail_labels[i], style="debug0.TLabel").grid(
                column=i, row=0
            )
        for i in range(0, 7):
            ttk.Entry(
                frame_detail,
                textvariable=self.var_debit_amount[i],
                validate="key",
                validatecommand=(self.valid_cmd.check_input_amount, "%S", "%P"),
            ).grid(column=0, row=i + 1)
            ttk.Combobox(
                frame_detail,
                textvariable=self.var_debit_item[i],
            ).grid(column=1, row=i + 1)
            ttk.Entry(frame_detail, textvariable=self.var_summary).grid(
                column=2, row=i + 1
            )
            ttk.Combobox(frame_detail, textvariable=self.var_credit_item[i]).grid(
                column=3, row=i + 1
            )
            ttk.Entry(
                frame_detail,
                textvariable=self.var_credit_amount[i],
                validate="key",
                validatecommand=(self.valid_cmd.check_input_amount, "%S", "%P"),
            ).grid(column=4, row=i + 1)

        # ========== ジオメトリー設定 ==========
        self.geometry("1280x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=105)
        self.rowconfigure(1, weight=426)
        frame_external.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_external.columnconfigure(0, weight=1)
        frame_external.rowconfigure(0, weight=1)
        frame_header.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_header.columnconfigure(0, weight=630)
        frame_header.columnconfigure(1, weight=500)
        frame_header.columnconfigure(2, weight=150)
        frame_header.rowconfigure(0, weight=40)
        frame_header.rowconfigure(1, weight=65)
        frame_title.grid(column=0, row=0, rowspan=2, sticky=(N, E, S, W))
        label_title.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_date.grid(column=1, row=0, rowspan=2, sticky=(N, E, S, W))
        label_date.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_member_header.grid(column=2, row=0, sticky=(N, E, S, W))
        label_member_header.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_member_input.grid(column=2, row=1, sticky=(N, E, S, W))
        frame_member_input.columnconfigure(0, weight=1)
        frame_member_input.rowconfigure(0, weight=1)
        entry_member.grid(column=0, row=0, sticky=(N, E, S, W))
        frame_detail.grid(column=0, row=1, sticky=(N, E, S, W))
        frame_detail.columnconfigure(0, weight=1)
        frame_detail.rowconfigure(0, weight=1)

    def get_master(self) -> ITclComposite:
        return self.master
