import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()

    external_frame = ttk.Frame(root, width=1280, height=600)

    external_frame.grid()

    root.mainloop()
