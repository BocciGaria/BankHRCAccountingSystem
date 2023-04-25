from .base import BaseController
from .command.command import CreateWindowCommand
from .transferslip import TransferSlipController
from .journal import JournalController
from .ledger import LedgerController
from bhrc_accounting.view.widget import base_widget as bw
from bhrc_accounting.view.menu import MenuView


class MenuController(BaseController):
    """Controller class for the menu window"""

    def __init__(self, master: bw.ITclComposite):
        super().__init__(master)
        self.view = MenuView(master)
        self.view.create_widgets()
        self.view.set_btn_transferslip_command(
            CreateWindowCommand(self.view.master, TransferSlipController).get_signature()
        )
        self.view.set_btn_journal_command(
            CreateWindowCommand(self.view.master, JournalController).get_signature()
        )
        self.view.set_btn_ledger_command(
            CreateWindowCommand(self.view.master, LedgerController).get_signature()
        )

    def run(self):
        self.view.grid_widgets()

    def stop(self):
        self.view.destroy_widgets
