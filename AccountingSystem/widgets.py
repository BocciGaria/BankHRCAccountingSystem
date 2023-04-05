import abc
import tkinter as tk
from tkinter import ttk


class ITclComponent(metaclass=abc.ABCMeta):
    """Tcl グラフィックComponentインターフェース

    すべてのグラフィックオブジェクトに共通のインターフェースを定義します。
    """

    @abc.abstractmethod
    def get_root(self) -> tk.Tk:
        """アプリケーションルートオブジェクトを取得する"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_master(self):
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


class TclComponent(ITclComponent):
    """TclグラフィックComponent具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()


class TclComposite(ITclComposite):
    """Tcl グラフィックComposite具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()


class TclLeaf(ITclLeaf):
    """Tcl グラフィックLeaf具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()


class WrappedTk(tk.Tk, TclComposite):
    """TclグラフィックCompositeでラップしたTkクラス"""

    def get_root(self) -> tk.Tk:
        return self

    def get_master(self) -> tk.BaseWidget:
        return self.master


class WrappedToplevel(tk.Toplevel, TclComposite):
    """TclグラフィックCompositeでラップしたトップレベルクラス"""

    def get_master(self) -> tk.BaseWidget:
        return self.master


class WrappedTFrame(ttk.Frame, TclComposite):
    """TclグラフィックCompositeでラップしたTフレームクラス"""

    def get_master(self) -> tk.BaseWidget:
        return self.master
