import tkinter as tk
from tkinter import ttk

from windows import TransferSlip


class Menu(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        ttk.Button(self, text="振替伝票", command=self.show_transfer_slip).grid(
            column=0, row=0, padx=100, pady=50
        )

    def show_transfer_slip(self):
        TransferSlip(self.master, self.master).grid()


if __name__ == "__main__":
    root = tk.Tk()

    Menu(root).grid()

    root.mainloop()
