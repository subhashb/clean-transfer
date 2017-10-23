from core.entities import Transfer
from db.repository import TransferRepository


class TransferUseCase:

    def __init__(self, repository: TransferRepository):
        self.repository = repository

    def create(self, transfer: Transfer):

        transfer = None

        if transfer.from_account.validate() \
                and transfer.to_account.validate() \
                and transfer.from_account.has_sufficient_balance(transfer.amount)\
                and self._validate_transfer_request(transfer):
            with self.repository.atomic():
                self.from_account.debit(transfer.amount)
                self.to_account.credit(transfer.amount)
                transfer = self.repository.save(transfer)

        return transfer

    def _validate_transfer_request(self, transfer: Transfer):
        pass