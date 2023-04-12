from bhrc_accounting.widget.base_widget import WrappedToplevel, WrappedTLabel
from bhrc_accounting.const import FONT_FIXED_24


class Ledger(WrappedToplevel):
    """元帳ウィンドウ"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("元帳")

        # >>>>>DEBUG>>>>>
        WrappedTLabel(
            self, text="Ledger(元帳ウィンドウ)", padding=40, font=FONT_FIXED_24
        ).grid()
        # <<<<<DEBUG<<<<<
