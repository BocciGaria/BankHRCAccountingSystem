from typing import Callable, Dict, Type, TypeVar


# 新しい型ヒントの定義
TypeName = TypeVar("TypeName", str)


class WrappedTclFactory:
    """Tclオブジェクトのファクトリークラス

    CompositeパターンでラップされたTclオブジェクトの生成処理を実装します
    """

    __widget_dictionary: Dict[TypeName, Callable]

    def __init__(self) -> None:
        self.__widget_dictionary = {
            
        }
