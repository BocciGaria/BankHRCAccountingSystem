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
        self.validate_slip()
        for detail in self.view.details:
            if self.is_blanc(detail):
                continue
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
                    credit_amount=detail.var_credit_amount.get(),
                    debit_amount=detail.var_debit_amount.get(),
                    description=detail.var_summary.get(),
                    slip=self.view.var_slip_number.get(),
                )
            )
        # TODO: ここでDBに登録する

    def validate_slip(self) -> bool:
        """Validate the slip header

        Raises:
            ValueError: When the slip header is invalid
        """
        if self.view.var_date.get() == "":
            self.popup_error("日付が空欄です。")
            return False
        if self.view.var_slip_number.get() == "":
            self.popup_error("伝票番号が空欄です。")
            return False
        return True

    def is_blanc(self, detail: TransferSlipDetailRow) -> bool:
        """Check if the detail row is blanc"""

        return (
            detail.var_debit_title.get() == ""
            and detail.var_debit_amount.get() == ""
            and detail.var_credit_title.get() == ""
            and detail.var_credit_amount.get() == ""
            and detail.var_summary.get() == ""
        )

    def validate_detail(self, detail: TransferSlipDetailRow) -> bool:
        """Validate the detail row

        Args:
            detail (TransferSlipDetailRow): The detail row to validate
        """
        if detail.var_debit_title.get() == "":
            self.popup_error("借方科目が空欄です。")
            return False
        if detail.var_debit_amount.get() == "":
            self.popup_error("借方金額が空欄です。")
            return False
        if detail.var_credit_title.get() == "":
            self.popup_error("貸方科目が空欄です。")
            return False
        if detail.var_credit_amount.get() == "":
            self.popup_error("貸方金額が空欄です。")
            return False
        if detail.var_summary.get() == "":
            self.popup_error("摘要が空欄です。")
            return False
        return True

    def popup_error(self, message: str):
        """Popup an error message

        Args:
            message (str): The error message to popup
        """
        self.view.popup_error(message)
