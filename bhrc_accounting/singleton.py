from typing import *


# class Singleton:
#     """シングルトンクラス"""

#     __instance = None

#     def __new__(cls) -> Self:
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance

#     @classmethod
#     def get_instance(cls) -> Self:
#         if cls.__instance is None:
#             cls.__instance = cls()
#         return cls.__instance
