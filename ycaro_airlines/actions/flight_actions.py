import re
import questionary
from ycaro_airlines.models import Flight, FlightQueryParams, cities
from math import inf
from datetime import datetime
from ycaro_airlines.menus.base_menu import console


def str_can_be_float(string: str) -> bool:
    if re.fullmatch(r"[0-9]*\.?[0-9]*", string):
        return True
    return False


def str_can_be_date(string: str) -> bool:
    if re.fullmatch(
        r"0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}", string
    ):
        return True
    return False


def search_flight_action():
    options: list[str] = [
        "price",
        "city",
        "departure date",
        "arrival date",
        "flight id",
    ]

    selected = questionary.checkbox(
        "How do you want to filter flights?", choices=options
    ).ask()

    query_params: FlightQueryParams = {}

    if "flight id" in selected:
        flight_id = questionary.autocomplete(
            "Type the id of the flight:",
            choices=[str(k) for k, _ in Flight.flights.items()],
            validate=lambda x: True
            if x in {str(k) for k, _ in Flight.flights.items()}
            else False,
        ).ask()

        query_params["flight_id"] = int(flight_id)

    if "price" in selected:
        price_lte = questionary.text(
            "Price <=:", default="inf", validate=str_can_be_float
        ).ask()

        if price_lte == "":
            price_lte = inf

        price_gte = questionary.text(
            "Price >=:",
            default="0",
            validate=str_can_be_float,
        ).ask()

        if price_lte == "inf":
            price_lte = inf

        query_params["price_lte"] = float(price_lte)
        query_params["price_gte"] = float(price_gte)

    if "city" in selected:
        city_from: str = questionary.autocomplete(
            "From:", choices=cities, validate=lambda x: x in cities
        ).ask()
        city_to: str = questionary.autocomplete(
            "To:", choices=cities, validate=lambda x: x in cities
        ).ask()

        if city_from != "":
            query_params["city_from"] = city_from

        if city_to != "":
            query_params["city_to"] = city_to

    if "arrival date" in selected:
        arrival_lte = questionary.text(
            "Arrival <=:(dd-mm-yyyy)", "", validate=str_can_be_date
        ).ask()

        arrival_gte = questionary.text(
            "Arrival >=:(dd-mm-yyyy)", "", validate=str_can_be_date
        ).ask()
        if arrival_lte != "":
            arrival_lte = list(map(lambda x: int(x), "/".split(arrival_lte)))
            query_params["date_arrival_lte"] = datetime(
                day=arrival_lte[0], month=arrival_lte[1], year=arrival_lte[2]
            )

        if arrival_gte != "":
            arrival_gte = list(map(lambda x: int(x), "/".split(arrival_gte)))
            query_params["date_arrival_gte"] = datetime(
                day=arrival_gte[0], month=arrival_gte[1], year=arrival_gte[2]
            )

    if "departure date" in selected:
        departure_lte = questionary.text(
            "Departure <=:(dd-mm-yyyy)", "", validate=str_can_be_date
        ).ask()

        departure_gte = questionary.text(
            "Departure >=:(dd-mm-yyyy)", "", validate=str_can_be_date
        ).ask()

        if departure_lte != "":
            departure_lte = list(map(lambda x: int(x), "/".split(departure_lte)))
            query_params["date_departure_lte"] = datetime(
                day=departure_lte[0], month=departure_lte[1], year=departure_lte[2]
            )

        if departure_gte != "":
            departure_gte = list(map(lambda x: int(x), "/".split(departure_gte)))
            query_params["date_departure_gte"] = datetime(
                day=departure_gte[0], month=departure_gte[1], year=departure_gte[2]
            )

    Flight.print_flights_table(console=console, **query_params)
