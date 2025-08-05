from enum import Enum, auto
from itertools import count
from typing import Self
from ycaro_airlines.customer import Customer
from ycaro_airlines.flight import Flight


class BookingStatus(Enum):
    booked = 1
    checked_in = auto()
    cancelled = auto()


class Booking:
    booking_counter = count()
    bookings: dict[int, Self] = {}

    def __init__(self, flight: Flight, customer: Customer):
        self.flight = flight
        self.id = next(self.booking_counter)
        self.owner = customer
        self.status = BookingStatus.booked
        self.seat = None
        self.bookings[self.id] = self

    def cancel_booking(self):
        self.status = BookingStatus.cancelled
        if self.seat:
            self.flight.seats[self.seat] = None

    @classmethod
    def list_bookings(cls, customer: Customer):
        return list(
            filter(
                lambda x: True if x.owner.id == customer.id else False,
                cls.bookings.values(),
            )
        )

    def check_in(self, seat: Optional[int] = None):
        self.status = BookingStatus.checked_in
        if self.seat is None and seat is not None:
            self.select_seat(seat)

    def select_seat(self, seat: int):
        self.seat = seat
        self.flight.check_in_booking(self)

    @classmethod
    def print_bookings_table(cls, customer: Customer, console: Console):
        table = Table(title="Bookings")
        table.add_column("Booking")
        table.add_column("Flight")
        table.add_column("From", justify="right", no_wrap=True)
        table.add_column("Departure", justify="right", no_wrap=True)
        table.add_column("Destination")
        table.add_column("Arrival", justify="right", no_wrap=True)
        table.add_column("Status", justify="right", no_wrap=True)

        for i in cls.list_bookings(customer):
            table.add_row(
                f"{i.id}",
                f"{i.flight.id}",
                f"{i.flight.From}",
                f"{stringify_date(i.flight.departure)}",
                f"{i.flight.To}",
                f"{stringify_date(i.flight.arrival)}",
                f"{i.status.name}",
            )

        console.print(table)

    def print_booking_table(self, console: Console):
        pass
