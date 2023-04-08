import abc
import tkinter as tk
from tkinter import ttk


class ITclComponent(tk.Widget, metaclass=abc.ABCMeta):
    """Tcl グラフィックComponentインターフェース

    すべてのグラフィックオブジェクトに共通のインターフェースを定義します。
    """

    @abc.abstractmethod
    def get_root(self) -> tk.Tk:
        """アプリケーションルートオブジェクトを取得する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_master(self) -> tk.Widget:
        """インスタンスの直属の親要素を取得する"""
        raise NotImplementedError()


class ITclComposite(ITclComponent, metaclass=abc.ABCMeta):
    """Tcl グラフィックCompositeインターフェース

    Componentオブジェクトを内包したComponentオブジェクト
    のインターフェースを定義します。
    """


class ITclLeaf(ITclComponent, metaclass=abc.ABCMeta):
    """Tcl グラフィックLeafインターフェース

    TclグラフィックオブジェクトのCompositeパターンにおける
    終端要素のインターフェースを定義します。
    """


# class TclComponent(ITclComponent):
#     """TclグラフィックComponent具象クラス"""

#     def get_root(self) -> tk.Tk:
#         return self.get_master().get_root()

#     def get_master(self) -> tk.Widget:
#         return self.master


class TclComposite(ITclComposite):
    """Tcl グラフィックComposite具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()

    def get_master(self) -> tk.Widget:
        return self.master


class TclLeaf(ITclLeaf):
    """Tcl グラフィックLeaf具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()

    def get_master(self) -> tk.Widget:
        return self.master


class WrappedTk(tk.Tk, TclComposite):
    """TclグラフィックCompositeでラップしたTkクラス"""

    def get_root(self) -> tk.Tk:
        return self


class WrappedToplevel(tk.Toplevel, TclComposite):
    """TclグラフィックCompositeでラップしたトップレベルクラス"""


class WrappedTFrame(ttk.Frame, TclComposite):
    """TclグラフィックCompositeでラップしたTフレームクラス"""


class WrappedTLabel(ttk.Label, TclComposite):
    """TclグラフィックCompositeでラップしたTラベルクラス"""


class WrappedTButton(ttk.Button, TclLeaf):
    """TclグラフィックLeafでラップしたTボタンクラス"""


class WrappedTEntry(ttk.Entry, TclLeaf):
    """TclグラフィックLeafでラップしたTエントリークラス"""


class WrappedTCombobox(ttk.Combobox, TclLeaf):
    """TclグラフィックLeafでラップしたTコンボボックスクラス"""
