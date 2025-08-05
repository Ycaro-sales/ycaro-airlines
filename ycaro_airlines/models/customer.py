from itertools import count
from typing import Self
from ycaro_airlines.models import Booking


class Customer:
    customer_counter = count()
    customers: dict[int, Self] = {}

    def __init__(self, username: str) -> None:
        self.username: str = username
        self.id: int = next(self.customer_counter)
        self.customers[self.id] = self

    @property
    def bookings(self):
        return {k: v for k, v in Booking.bookings.items() if v.owner == self}
