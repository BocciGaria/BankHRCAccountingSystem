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


class TextButtonCommandItem(CommandItem):
    """テキストボタンコマンドアイテムクラス"""

    def __init__(self, text: str, command: Callable[[None], None]):
        self.text = text
        self.process = command

    def _primitive_operation(self):
        self.process()

    def get_widget(
        self, parent: base_widget.ITclComposite
    ) -> base_widget.WrappedTButton:
        return base_widget.WrappedTButton(
            parent, text=self.text, command=self._execute_command
        )


class ImageButtonCommandItem(CommandItem):
    """イメージボタンコマンドアイテムクラス"""

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
            image=self.img,
            command=self._execute_command,
            compound="image",
        )


class TextImageButtonCommandItem(CommandItem):
    """テキストイメージボタンコマンドアイテムクラス"""

    def __init__(
        self,
        text: str,
        image_url: Path,
        command: Callable[[None], None],
    ):
        self.text = text
        self.img = tk.PhotoImage(file=image_url)
        self.process = command

    def _primitive_operation(self):
        self.process()

    def get_widget(
        self, parent: base_widget.ITclComposite
    ) -> base_widget.WrappedTButton:
        return base_widget.WrappedTButton(
            parent,
            text=self.text,
            image=self.img,
            command=self._execute_command,
            compound=tk.LEFT,
        )


class TextEntryCommandItem(CommandItem):
    """エントリーコマンドアイテムクラス"""

    def __init__(self, command: Callable[[tk.StringVar], None]):
        self.input = tk.StringVar()
        self.process = command

    def _primitive_operation(self):
        self.process(self.input)

    def get_widget(self, parent: base_widget.ITclComposite) -> base_widget.WrappedTEntry:
        return base_widget.WrappedTEntry(
            parent, textvariable=self.input, command=self._execute_command
        )


class TextEntryAndButtonCommandItem(CommandItem):
    """エントリー＆ボタンコマンドアイテムクラス"""

    def __init__(
        self,
        command: Callable[[tk.StringVar], None],
        button_text: str = None,
        button_image_url: Path = None,
    ):
        if button_text is None and button_image_url is None:
            raise ValueError("button_text or button_image_url must be specified.")
        self.input = tk.StringVar()
        self.process = command
        self.button_text = button_text
        self.button_image = tk.PhotoImage(file=button_image_url)

    def _primitive_operation(self):
        self.process(self.input)

    def get_widget(self, parent: base_widget.ITclComposite) -> base_widget.WrappedTEntry:
        frame = base_widget.WrappedTFrame(parent)
        base_widget.WrappedTEntry(
            frame, textvariable=self.input, command=self._execute_command
        ).grid(row=0, column=0, sticky=NSEW)
        base_widget.WrappedTButton(
            frame,
            text=self.button_text,
            image=self.button_image,
            command=self._execute_command,
            compound=tk.LEFT,
        ).grid(row=0, column=1, sticky=NSEW)
        return frame


class TextComboboxCommandItem(CommandItem):
    """テキストコンボボックスコマンドアイテムクラス"""

    def __init__(
        self,
        values: Tuple[str],
        command: Callable[[tk.StringVar], None],
    ):
        self.selection = tk.StringVar()
        self.process = command
        self.values = values

    def _primitive_operation(self):
        self.process(self.selection)

    def get_widget(
        self, parent: base_widget.ITclComposite
    ) -> base_widget.WrappedTCombobox:
        return base_widget.WrappedTCombobox(
            parent,
            textvariable=self.selection,
            command=self._execute_command,
            values=self.values,
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
