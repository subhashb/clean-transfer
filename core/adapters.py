from typing import NamedTuple

from core.entities import Transfer
from core.usecase import TransferUseCase
from db.repository import TransferRepository


class AccountData(NamedTuple):
    name: str
    balance: float


class TransferData(NamedTuple):
    from_account: AccountData
    to_account: AccountData
    amount: float
    transaction_date: str


class TransferAdapter:

    def __init__(self, repository: TransferRepository):
        self.usecase = TransferUseCase(repository)

    def create(self, transfer_data: TransferData) -> TransferData:
        transfer = self._data_to_transfer(transfer_data)
        transfer = self.usecase.create(transfer)
        return self._transfer_to_data(transfer)

    @classmethod
    def _transfer_to_data(cls, transfer: Transfer) -> TransferData:
        pass

    @classmethod
    def _data_to_invoice(cls, transfer_data: TransferData) -> Transfer:
        pass