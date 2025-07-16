from src.lib.model import Model
from enum import Enum


class Permissions(Enum):
    pass


class Account(Model):
    permissions = []

    def __init__(self, username: str):
        super().__init__()
        self.username: str = username


class AdminAccount(Account):
    pass


class CustomerAccount(Account):
    pass
