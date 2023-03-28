from typing import *


class Singleton:
    """シングルトンパターンデコレーター"""

    def __new__(cls, *args, **kwargs) -> Self:
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
