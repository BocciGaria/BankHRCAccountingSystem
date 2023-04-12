from typing import Callable, Literal, NewType, Tuple, TypeVar

Index = NewType("Index", int)
InputAction = NewType("InputAction", int)
CommandSignature = TypeVar("CommandSignature", Callable, Tuple[Callable, ...])
ValidateCmdOption = NewType("ValidateCmdOption", Literal)
WidgetName = NewType("WidgetName", str)
