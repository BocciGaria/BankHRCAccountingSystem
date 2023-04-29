from typing import *

from .base import BaseModel
from .entity.account import Account
from .entity.m_title import MTitle


class TransferSlipModel(BaseModel):
    """Model class for the transfer slip window"""

    def get_account_titles(self) -> Dict[int, str]:
        m_titles: Iterable[MTitle] = self.operator.get_all(MTitle)
        return {m_title.id.get_value(): m_title for m_title in m_titles}
