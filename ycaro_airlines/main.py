from datetime import datetime
from typing import (
    Dict,
    Optional,
    TypeVar,
)
from ycaro_airlines.models import Flight, Customer
from ycaro_airlines.menus import customer_menu

cities = ["Maceio", "Recife", "Aracaju", "Joao Pessoa"]
T = TypeVar("T")


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


# ╭─ hello ─────────╮
# │ <1> - oi        │
# │ <2> - tchau     │
# ╰─────────────────╯


class App:
    def __init__(self) -> None:
        pass


def booking_menu(user: Customer):
    pass


# TODO: finish function


def main():
    Flight.mock_flight()
    Flight.mock_flight()
    Flight.mock_flight()
    Flight.mock_flight()
    Flight.mock_flight()

    user = Customer(username="ycaro")
    customer_menu(user)

    pass


if __name__ == "__main__":
    main()
