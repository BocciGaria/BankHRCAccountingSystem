from .base import BaseView
from .widget import base_widget as bw
from bhrc_accounting.const import FONT_FIXED_24


# class JournalView(base_widget.WrappedToplevel):
#     """仕訳帳ウィンドウ"""

#     def __init__(self, parent, **kwargs):
#         super().__init__(parent, **kwargs)
#         # Set title of the window
#         self.title("仕訳帳原簿")

#         # >>>>>DEBUG>>>>>
#         base_widget.WrappedTLabel(
#             self, text="JournalEntry(仕訳帳ウィンドウ)", padding=40, font=FONT_FIXED_24
#         ).grid()
#         # <<<<<DEBUG<<<<<


class JournalView(BaseView):
    """View class for the journal window"""

    def __init__(self, master):
        super().__init__(master)
        # Window
        self.window: bw.WrappedToplevel

    def create_widgets(self):
        self.window = bw.WrappedToplevel(self.master)
        self.window.title("仕訳帳")

    def destroy_widgets(self):
        self.window.destroy()

    def grid_widgets(self):
        self.window.grid()

    def forget_widgets(self):
        self.window.forget()

    def remove_widgets(self):
        self.window.grid_remove()
