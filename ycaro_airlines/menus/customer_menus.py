from ycaro_airlines.menus import menu_factory, console
from ycaro_airlines.actions.booking_actions import (
    select_seat_action,
    check_in_action,
    cancel_booking_action,
    create_booking_action,
)

from ycaro_airlines.actions.flight_actions import search_flight_action
import questionary
from ycaro_airlines.models import Customer, Booking, Flight, BookingStatus
from typing import Callable, Tuple
from functools import partial


def customer_menu(user: Customer):
    options: list[Tuple[str, Callable]] = [
        ("Ver Voos", partial(flights_menu, user=user)),
        ("Ver bilhetes", partial(bookings_menu, user=user)),
    ]

    menu_factory("Customer Menu", options)()


def bookings_menu(user: Customer):
    Booking.print_bookings_table(user, console)

    booking_id = questionary.autocomplete(
        "Insira o id da passagem que voce deseja gerenciar: ",
        choices=[str(i.id) for i in Booking.list_bookings(user)],
        validate=lambda x: True
        if x in {str(i.id) for i in Booking.list_bookings(user)}
        else False,
    ).ask()

    booking = Booking.bookings[int(booking_id)]
    booking.print_booking_table(console)

    options: list[Tuple[str, Callable]] = [
        (
            "Cancelar Passagem",
            partial(cancel_booking_action, user=user, booking=booking),
        ),
        ("Modificar Assento", partial(select_seat_action, booking=booking)),
        ("Check-in Online", partial(check_in_action, booking=booking)),
    ]

    if booking.status != BookingStatus.booked:
        options = [
            (
                "Ver passagem",
                partial(booking.print_booking_table, console=console),
            )
        ]

    menu_factory("Booking management", options)()


def flights_menu(user: Customer):
    options: list[Tuple[str, Callable]] = [
        ("Book flight", partial(create_booking_action, user=user)),
        ("Search/filter flights", search_flight_action),
    ]

    Flight.print_flights_table(console)

    menu_factory("Flights", options)()
