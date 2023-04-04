import abc
import tkinter as tk


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


class TclComponent(tk.BaseWidget, ITclComponent):
    """TclグラフィックComponent具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()

    def get_master(self) -> ITclComposite:
        return self.master


class TclComposite(tk.BaseWidget, ITclComposite):
    """Tcl グラフィックComposite具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()

    def get_master(self) -> ITclComposite:
        return self.master


class TclLeaf(tk.BaseWidget, ITclLeaf):
    """Tcl グラフィックLeaf具象クラス"""

    def get_root(self) -> tk.Tk:
        return self.get_master().get_root()

    def get_master(self) -> ITclComposite:
        return self.master
