from .base import BaseController
from bhrc_accounting.view.widget import base_widget as bw
from bhrc_accounting.view.transferslip import TransferSlipView


class TransferSlipController(BaseController):
    """Controller class for the transfer slip window"""

    def __init__(self, master: bw.ITclComposite):
        super().__init__(master)
        self.view = TransferSlipView(master)
        self.view.set_register_command(self.register_transfer_slip)
        self.view.create_widgets()

    def run(self):
        self.view.grid_widgets()

    def stop(self):
        self.view.destroy_widgets()

    def register_transfer_slip(self):
        count = 0
        for detail in self.view.details:
            count += 1
            print(f"========== Detail {count} ==========")
            print(f"Debit item      : {detail.var_debit_item}")
            print(f"Debit ammount : {detail.var_credit_amount}")
            print(f"Credit item     : {detail.var_debit_item}")
            print(f"Credit ammount: {detail.var_credit_amount}")
            print(f"Summary       : {detail.var_summary}")
            print()
