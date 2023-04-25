from .base import BaseController
from bhrc_accounting.view.widget import base_widget as bw
from bhrc_accounting.view.transferslip import TransferSlipView


class TransferSlipController(BaseController):
    """Controller class for the transfer slip window"""

    def __init__(self, master: bw.ITclComposite):
        super().__init__(master)
        self.view = TransferSlipView(master)
        self.view.set_register_command(lambda: print("Register button is clicked."))
        self.view.create_widgets()

    def run(self):
        self.view.grid_widgets()

    def stop(self):
        self.view.destroy_widgets()
