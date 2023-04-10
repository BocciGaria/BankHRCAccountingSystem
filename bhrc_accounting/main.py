# import tkinter as tk
# from tkinter import ttk

# from commands import CreateWindowCommand
# from widgets import WrappedTk, WrappedTFrame
# from windows import TransferSlip


# class App(WrappedTk):
#     """アプリケーションルートオブジェクトクラス"""


# class Menu(WrappedTFrame):
#     """メインメニューフレームクラス"""

#     def __init__(self, parent: tk.Tk, **kwargs) -> None:
#         super().__init__(parent, **kwargs)
#         ttk.Button(
#             self,
#             text="振替伝票",
#             command=CreateWindowCommand(self, TransferSlip).get_signature(),
#         ).grid(column=0, row=0, padx=100, pady=50)


# if __name__ == "__main__":
#     root = App()

#     Menu(root).grid()

#     root.mainloop()
