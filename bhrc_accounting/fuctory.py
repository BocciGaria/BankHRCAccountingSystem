from typing import Callable, Dict, Type


class WrappedTclFactory:
    """Tclオブジェクトのファクトリークラス

    CompositeパターンでラップされたTclオブジェクトの生成処理を実装します
    """

    __widget_dictionary: Dict[Type, Callable]

    def __init__(self) -> None:
        self.__widget_dictionary = {}


class CommandFactory:
    """コマンドオブジェクトのファクトリークラス"""

    __command_dictionary: Dict[Type, Callable]

    def __init__(self) -> None:
        self.__command_dictionary = {}
