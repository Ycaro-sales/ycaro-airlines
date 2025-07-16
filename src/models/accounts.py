from base.model import Model
from enum import Enum
from typing import Dict, List
from models.airlines import Flight


class Roles(Enum):
    Customer = "Customer"
    Admin = "Admin"
    Default = ""


class Account(Model):
    permissions = []
    accounts: Dict[str, "Account"] = {}

    def __init__(self, username: str, name: str):
        super().__init__()
        self.username: str = username
        self.name = name
        self.role: Roles = Roles.Default


class AdminAccount(Account):
    pass


class Customer(Account):
    def __init__(self, name: str, username: str):
        super().__init__(name, username)
        super().accounts["username"] = self
        self.role: Roles = Roles.Customer
        self.booked_flights: List[Flight] = []
