import tkinter as tk

from bhrc_accounting.view.widget import base_widget
from bhrc_accounting.view import menu
from bhrc_accounting import config


class App(base_widget.WrappedTk):
    def __init__(self):
        super().__init__()
        self.iconphoto(
            False, tk.PhotoImage(file=config.get_image_path("horse-head-lines.png"))
        )
        menu.MenuView(self).grid()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
