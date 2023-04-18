import tkinter as tk

from bhrc_accounting.data.model import ClubMember
from bhrc_accounting.widget import base_widget, menu
from bhrc_accounting import config


class App(base_widget.WrappedTk):
    def __init__(self):
        super().__init__()
        self.iconphoto(
            False, tk.PhotoImage(file=config.get_image_path("horse-head-lines.png"))
        )
        menu.Menu(self).grid()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
