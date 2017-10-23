from typing import ContextManager

from core.entities import Transfer


class TransferRepository:

    def record_transfer(self, Transfer):
        raise NotImplementedError()

    def save(self, transfer: Transfer) -> Transfer:
        raise NotImplementedError()

    def atomic(self) -> ContextManager:
        raise NotImplementedError()