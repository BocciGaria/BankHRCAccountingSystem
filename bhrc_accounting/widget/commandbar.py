import abc
from pathlib import Path
import tkinter as tk
from tkinter.constants import *
from typing import *

from . import base_widget


class ICommandItem(metaclass=abc.ABCMeta):
    """コマンドアイテムインターフェース

    コマンドバーに配置されるコマンドアイテムオブジェクトき期待されるインターフェースを定義します。
    """

    @abc.abstractmethod
    def _execute_command(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def _primitive_operation(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_widget(self, parent: base_widget.ITclComposite) -> base_widget.ITclComponent:
        raise NotImplementedError()


class CommandItem(ICommandItem):
    """コマンドアイテム抽象クラス

    コマンドアイテムオブジェクトが共通して提供する機能を定義します。
    """

    def _execute_command(self):
        self._primitive_operation()


class ImageButtonCommandItem(CommandItem):
    """ボタンコマンドアイテムクラス"""

    def __init__(self, image_url: Path, command: Callable[[None], None]):
        self.img = tk.PhotoImage(file=image_url)
        self.process = command

    def _primitive_operation(self):
        self.process()

    def get_widget(
        self, parent: base_widget.ITclComposite
    ) -> base_widget.WrappedTButton:
        return base_widget.WrappedTButton(
            parent,
            text="登録",
            width=1,
            image=self.img,
            command=self._execute_command,
            compound="image",
        )


class CommandBar(base_widget.WrappedTFrame):
    """コマンドバークラス"""

    def __init__(self, parent: base_widget.ITclComposite, **kwargs):
        super().__init__(parent, **kwargs)
        self.item_count = 0
        self.configure(style="debug1.TFrame")

    def add_command(self, command_item: ICommandItem):
        """コマンドアイテムを追加します。"""
        self.item_count += 1
        command_item.get_widget(self).grid(
            row=0, column=self.item_count, padx=5, pady=5, sticky=NSEW
        )
