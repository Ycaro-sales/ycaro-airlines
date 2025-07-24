from collections import Counter
from datetime import datetime, timedelta
from enum import Enum, auto
from functools import reduce
from itertools import count
from typing import Dict, Optional
from random import randint, sample

cities = ["Maceio", "Recife", "Aracaju", "Joao Pessoa"]


def stringify_date(date: datetime):
    return f"{str(date.hour).zfill(2)}:{str(date.minute).zfill(2)} {str(date.day).zfill(2)}/{str(date.month).zfill(2)}"


class Flight:
    flight_counter = count()

    def __init__(
        self,
        From: str,
        To: str,
        capacity: int = 255,
        departure: datetime = datetime.now() + timedelta(hours=1),
        arrival: datetime = datetime.now() + timedelta(hours=3),
        price: float = 200.00,
    ) -> None:
        self.From: str = From
        self.To: str = To
        self.id: int = next(self.flight_counter)
        self.departure: datetime = departure
        self.arrival: datetime = arrival
        self.price: float = price

    def __str__(self):
        return f"{self.id} - {self.From} -> {self.To}\n{stringify_date(self.departure)} -> {stringify_date(self.arrival)} | R${self.price} "


class BookingStatus(Enum):
    booked = 1
    checked_in = auto()
    cancelled = auto()


class Booking:
    booking_counter = count()

    def __init__(self, flight: Flight):
        self.flight = flight
        self.id = next(self.booking_counter)
        self.status = BookingStatus
        self.seat = self.select_seat()

    def cancel_booking(self):
        pass

    def check_in(self):
        pass

    def select_seat(self):
        pass


class Customer:
    customer_counter = count()

    def __init__(self, username: str) -> None:
        self.username: str = username
        self.id: int = next(self.customer_counter)
        self.fligths: list[Booking] = []


flights: Dict[int, Flight] = {}


def mock_flight():
    """Creates mocked flights to fill flights global dictionary"""
    timedelta_arrival = timedelta(hours=randint(1, 5))
    city1, city2 = sample(cities, k=2)
    price = randint(100, 400)
    mock: Flight = Flight(
        From=city1,
        To=city2,
        departure=datetime.now() + timedelta_arrival,
        arrival=datetime.now() + timedelta_arrival + timedelta(hours=randint(1, 5)),
        price=price,
    )
    flights[mock.id] = mock


def filter_by_city(
    flights: Dict[int, Flight], From: Optional[str] = None, To: Optional[str] = None
):
    filtered_list = flights.values()

    if From is not None:
        filtered_list = [x for x in filtered_list if x.From == From]

    if To is not None:
        filtered_list = [x for x in filtered_list if x.To == To]

    return filtered_list


def filter_by_date(
    flights: Dict[int, Flight],
    arrival_date: Optional[datetime] = None,
    departure_date: Optional[datetime] = None,
):
    filtered_list = flights.values()

    if arrival_date is not None:
        filtered_list = [x for x in filtered_list if x.arrival == arrival_date]

    if departure_date is not None:
        filtered_list = [x for x in filtered_list if x.departure == departure_date]

    return filtered_list


def filter_by_price(
    flights: Dict[int, Flight],
    price_lte: Optional[float] = None,
    price_gte: Optional[float] = None,
):
    filtered_list = flights.values()

    if price_lte is not None:
        filtered_list = [x for x in filtered_list if x.price <= price_lte]

    if price_gte is not None:
        filtered_list = [x for x in filtered_list if x.price >= price_gte]

    return filtered_list


def price_key(flight: Flight):
    return flight.price


def arrival_key(flight: Flight):
    return flight.arrival


def departure_key(flight: Flight):
    return flight.departure


def from_key(flight: Flight):
    return flight.From[0]


def to_key(flight: Flight):
    return flight.To[0]


def box(text_lines: list[str]):
    longest_text_len = len(reduce(lambda x, y: y if len(y) > len(x) else x, text_lines))

    print("".join(("┏", "━" * longest_text_len, "┓")))
    for i in text_lines:
        print("".join(("┃", i, " " * (longest_text_len - len(i)), "┃")))

    print("".join(("┗", "━" * longest_text_len, "┛")))


def menu(title: str, question: str, options: dict):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
