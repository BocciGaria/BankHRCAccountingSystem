from .base import BaseController
from bhrc_accounting.model.account import Account
from bhrc_accounting.view.widget import base_widget as bw
from bhrc_accounting.view.transferslip import TransferSlipView, TransferSlipDetailRow


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
        accounts = []
        for detail in self.view.details:
            self.validate_detail(detail)
            count += 1
            print(f"======= Detail {count} =======")
            print(f"Debit title   : {detail.var_debit_title}")
            print(f"Debit amount  : {detail.var_debit_amount}")
            print(f"Credit title  : {detail.var_credit_title}")
            print(f"Credit amount : {detail.var_credit_amount}")
            print(f"Summary       : {detail.var_summary}")
            print()
            accounts.append(
                Account(
                    date=self.view.var_date.get(),
                    debit_title=detail.var_debit_title.get(),
                    credit_title=detail.var_credit_title.get(),
                    credit_amount=detail.var_credit_amount,
                    debit_amount=detail.var_debit_amount.get(),
                    description=detail.var_summary.get(),
                    slip=self.view.var_slip_number.get(),
                )
            )
        # TODO: ここでDBに登録する

    def validate_detail(self, detail: TransferSlipDetailRow) -> bool:
        """Validate the detail row

        Args:
            detail (TransferSlipDetailRow): The detail row to validate
        """
        if self.view.var_date.get() == "":
            raise ValueError("Date is empty")
        if detail.var_debit_title.get() == "":
            raise ValueError("Debit title is empty")
        if detail.var_debit_amount.get() == "":
            raise ValueError("Debit amount is empty")
        if detail.var_credit_title.get() == "":
            raise ValueError("Credit title is empty")
        if detail.var_credit_amount.get() == "":
            raise ValueError("Credit amount is empty")
        if self.view.var_slip_number.get() == "":
            raise ValueError("Slip number is empty")
        return True
