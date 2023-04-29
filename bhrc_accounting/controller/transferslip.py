from .base import BaseController
from bhrc_accounting.model.transferslip import TransferSlipModel
from bhrc_accounting.view.widget import base_widget as bw
from bhrc_accounting.view.transferslip import TransferSlipView, TransferSlipDetailRow


class TransferSlipController(BaseController):
    """Controller class for the transfer slip window"""

    def __init__(self, master: bw.ITclComposite):
        super().__init__(master)
        self.model = TransferSlipModel()
        self.view = TransferSlipView(master, self.model.get_account_titles())

    def run(self):
        self.view.create_widgets()
        self.view.command_bar.command_items["save"].set_command(
            self.register_transfer_slip
        )
        self.view.command_bar.command_items["insert_row"].set_command(self._insert_row)
        self.view.grid_widgets()

    def stop(self):
        self.view.destroy_widgets()

    def register_transfer_slip(self, *args):
        """Save the transfer slip"""
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

    def _insert_row(self, *args):
        """Insert a new row to the detail section"""
        master = self.view.details[0].parent
        new_detail = TransferSlipDetailRow(master, self.view.account_titles)
        self.view.details.append(new_detail)
        row_index = (
            self.view.details.index(new_detail) + self.view.DETAIL_HEADER_ROW_COUNT
        )
        self.view.details[-1].create_widgets()
        self.view.details[-1].grid_widgets(row_index)
