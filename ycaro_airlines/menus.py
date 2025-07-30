from functools import partial
from typing import (
    Any,
    Callable,
    Tuple,
)
from questionary import select, confirm, text, autocomplete, Choice
import questionary
from rich.table import Table
from rich.console import Console
from ycaro_airlines.models import Flight, Customer, Booking


# ╭─ hello ─────────╮
# │ <1> - oi        │
# │ <2> - tchau     │
# ╰─────────────────╯

console = Console()


def main_menu(user: Customer):
    pass


def menu_factory(title: str, options: list[Tuple[str, Callable]]):
    choices: list[Choice] = [Choice(c[0], c[1]) for c in options]
    choices.append(Choice("Go Back", value=""))

    def menu() -> Any:
        while True:
            selection = questionary.select(title, choices=choices).ask()
            match selection:
                case "":
                    break
                case _:
                    selection()

    return menu


def customer_menu(user: Customer):
    options: list[Tuple[str, Callable]] = [
        ("Ver Voos", partial(flights_menu, user=user)),
        ("Ver bilhetes", partial(booking_menu, user=user)),
    ]

    menu_factory("Customer Menu", options)()


def manage_booking(user: Customer, booking: Booking):
    pass


def booking_menu(user: Customer):
    options: list[Tuple[str, Callable]] = [
        ("Comprar Passagem", partial(flights_menu, user=user)),
        ("Ver bilhetes", partial(booking_menu, user=user)),
    ]

    menu_factory("Customer Menu", options)()


def select_seat_action(user: Customer, booking: Booking):
    seat = int(
        questionary.autocomplete(
            "Qual assento voce deseja?",
            choices=[str(i) for i, v in enumerate(booking.flight.seats) if v is None],
        ).ask()
    )
    booking.select_seat(seat)


def create_booking_action(user: Customer):
    flight_id = questionary.autocomplete(
        "Insira o id do voo que voce quer comprar a passagem:",
        choices=[str(k) for k, _ in Flight.flights.items()],
    ).ask()

    flight = Flight.flights[int(flight_id)]
    flight.print_flight_table(console)

    wants_to_book = questionary.confirm("Voce quer comprar essa passagem?").ask()
    if not wants_to_book:
        return

    # voce quer comprar essa passagem
    booking = Booking(flight, user)

    # wants_to_select_seat = questionary.confirm("Voce quer escolher um assento?").ask()
    #
    # if wants_to_select_seat:
    #     select_seat_action(user, booking)

    # TODO: show flight id
    print("Flight booked")

    # see departure and arrival


def bookings_menu(user: Customer):
    Booking.print_bookings_table(user, console)

    booking_id = questionary.autocomplete(
        "Insira o id da passagem que voce deseja gerenciar: ",
        choices=[str(i.id) for i in Booking.list_bookings(user)],
    ).ask()

    booking = Booking.bookings[booking_id]
    booking.print_booking_table(console)

    options: list[Tuple[str, Callable]] = [
        ("Cancelar Passagem", booking.cancel_booking),
        ("Modificar Passagem", print),
    ]

    menu_factory("Booking management", options)()

    print("Flight booked")


def flights_menu(user: Customer):
    options: list[Tuple[str, Callable]] = [
        ("Comprar Passagem", partial(create_booking_action, user=user)),
    ]

    Flight.print_flights_table(console)

    menu_factory("Flights", options)()
