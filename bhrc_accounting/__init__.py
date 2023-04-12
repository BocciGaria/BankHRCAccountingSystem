from bhrc_accounting.data.model import ClubMember
from bhrc_accounting.widget import base_widget, menu


def main():
    root = base_widget.WrappedTk()

    menu.Menu(root).grid()

    root.mainloop()


if __name__ == "__main__":
    main()
