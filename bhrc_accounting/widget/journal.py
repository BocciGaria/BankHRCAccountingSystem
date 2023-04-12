from bhrc_accounting.widget.base_widget import WrappedToplevel, WrappedTLabel
from bhrc_accounting.const import FONT_FIXED_24


class Journal(WrappedToplevel):
    """仕訳帳ウィンドウ"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("仕訳帳原簿")

        # >>>>>DEBUG>>>>>
        WrappedTLabel(
            self, text="JournalEntry(仕訳帳ウィンドウ)", padding=40, font=FONT_FIXED_24
        ).grid()
        # <<<<<DEBUG<<<<<
