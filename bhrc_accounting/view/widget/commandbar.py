import abc
from pathlib import Path
import tkinter as tk
from tkinter.constants import *
from typing import *

from . import base_widget


class CommandItemName(str):
    """The command item name value object"""


class ICommandItem(metaclass=abc.ABCMeta):
    """コマンドアイテムインターフェース

    コマンドバーに配置されるコマンドアイテムオブジェクトき期待されるインターフェースを定義します。
    """

    @abc.abstractmethod
    def __init__(
        self,
        id: CommandItemName,
        *args,
        process: Callable[[None], None] = None,
        **kwargs
    ) -> None:
        """コンストラクタ"""
        raise NotImplementedError()

    @property
    @abc.abstractproperty
    def id(self) -> CommandItemName:
        """コマンドアイテム名を取得します"""
        raise NotImplementedError()

    @abc.abstractmethod
    def _execute_command(self):
        """コマンドを実行します"""
        raise NotImplementedError()

    @abc.abstractmethod
    def _primitive_operation(self):
        """コマンドのプリミティブな処理を実行します"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_widget(self, parent: base_widget.ITclComposite) -> base_widget.ITclComponent:
        """コマンドアイテムのウィジェットを取得します"""
        raise NotImplementedError()

    @abc.abstractmethod
    def set_command(self, process: Callable[[None], None]):
        """コマンドを設定します

        Args:
            process (Callable[[None], None]): The command process
        """
        raise NotImplementedError()


class CommandItem(ICommandItem):
    """コマンドアイテム抽象クラス

    コマンドアイテムオブジェクトが共通して提供する機能を定義します。

    Attributes:
        _id (CommandItemName): The command item name
        process (Callable[[None], None]): The command process
    """

    def __init__(
        self,
        id: CommandItemName,
        *args,
        process: Callable[[None], None] = None,
        **kwargs
    ) -> None:
        self._id = id
        self.process = process

    @property
    def id(self) -> CommandItemName:
        return self._id

    def _execute_command(self):
        self._primitive_operation()

    def set_command(self, process: Callable[[None], None]):
        self.process = process


class TextButtonCommandItem(CommandItem):
    """テキストボタンコマンドアイテムクラス"""

    def __init__(
        self, id: CommandItemName, text, process: Callable[[None], None] = None
    ) -> None:
        super().__init__(id, process=process)
        self.text = text

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

    def __init__(
        self,
        id: CommandItemName,
        image_url: Path,
        process: Callable[[None], None] = None,
    ):
        super().__init__(id, process=process)
        self.img = tk.PhotoImage(file=image_url)

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
        id: CommandItemName,
        text: str,
        image_url: Path,
        process: Callable[[None], None] = None,
    ):
        super().__init__(id, process=process)
        self.text = text
        self.img = tk.PhotoImage(file=image_url)

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

    def __init__(
        self, id: CommandItemName, process: Callable[[tk.StringVar], None] = None
    ):
        super().__init__(id, process=process)
        self.input = tk.StringVar()

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
        id: CommandItemName,
        button_text: str,
        button_image_url: Path,
        process: Callable[[tk.StringVar], None] = None,
    ):
        super().__init__(id, process=process)
        if button_text is None and button_image_url is None:
            raise ValueError("button_text or button_image_url must be specified.")
        self.input = tk.StringVar()
        self.button_text = button_text
        self.button_image = tk.PhotoImage(file=button_image_url)

    def _primitive_operation(self):
        self.process(self.input)

    def get_widget(self, parent: base_widget.ITclComposite) -> base_widget.WrappedTEntry:
        frame = base_widget.WrappedTFrame(parent)
        base_widget.WrappedTEntry(frame, textvariable=self.input).grid(
            row=0, column=0, sticky=NSEW
        )
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
        id: CommandItemName,
        values: Tuple[str],
        process: Callable[[tk.StringVar], None] = None,
    ):
        super().__init__(id, process=process)
        self.selection = tk.StringVar()
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
        self.command_items: Dict[CommandItemName, CommandItem] = {}
        self.configure(style="debug1.TFrame")

    def add_command_item(self, command_item: ICommandItem):
        """コマンドアイテムを追加します。"""
        command_item.get_widget(self).grid(
            row=0, column=len(self.command_items), padx=5, pady=5, sticky=NSEW
        )
        self.command_items[command_item.id] = command_item
