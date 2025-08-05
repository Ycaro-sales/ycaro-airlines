import questionary
from ycaro_airlines.models import Flight, Booking, Customer
from ycaro_airlines.menus import console
from rich.table import Table
from rich.console import Console


def create_booking_action(user: Customer):
    flight_id = questionary.autocomplete(
        "Insira o id do voo que voce quer comprar a passagem:",
        choices=[str(k) for k, _ in Flight.flights.items()],
        validate=lambda x: True
        if x in {str(k) for k, _ in Flight.flights.items()}
        else False,
    ).ask()

    flight = Flight.flights[int(flight_id)]
    flight.print_flight_table(console)

    wants_to_book = questionary.confirm("Voce quer comprar essa passagem?").ask()
    if not wants_to_book:
        return

    # voce quer comprar essa passagem
    booking = Booking(flight, user)

    wants_to_select_seat = questionary.confirm("Voce quer escolher um assento?").ask()

    if wants_to_select_seat:
        select_seat_action(booking)

    # TODO: show flight id
    print("Flight booked")

    # see departure and arrival


def show_baggage_information(booking: Booking, console: Console):
    _ = booking
    table = Table(title="Bagagem")
    table.add_column("Tipo")
    table.add_column("Descrição")
    table.add_column("Preço")

    table.add_row(
        "Peça Adicional", "Bagagem Extra Transportada", "R$149.99/Bagagem adicional"
    )
    table.add_row(
        "Excesso de peso",
        "Bagagem de mão acima de 13 kg e Bagagem despachada acima de 23 kg",
        "R$19.99/por kg acima do limite",
    )
    table.add_row(
        "Sobredimensão",
        "Bagagem com dimensões superiores a 300 cm lineares(altura+comprimento+largura)",
        "R$10.00/Centimetro acima do limite",
    )
    console.print(table)


def select_seat_action(booking: Booking):
    seat = int(
        questionary.autocomplete(
            "Qual assento voce deseja?",
            choices=[str(i) for i, v in enumerate(booking.flight.seats) if v is None],
            validate=lambda x: True
            if x in {str(i) for i, v in enumerate(booking.flight.seats) if v is None}
            else False,
        ).ask()
    )
    booking.select_seat(seat)


def cancel_booking_action(user: Customer, booking: Booking):
    confirmation = questionary.confirm(
        "Voce tem certeza que voce quer cancelar essa passagem?"
    ).ask()

    if not confirmation or booking.owner.id != user.id:
        return

    booking.cancel_booking()


def check_in_action(booking: Booking):
    name_confirmation = questionary.text("Confirme o seu nome:").ask()
    if name_confirmation != booking.owner.username:
        print("Nome Incorreto!")

    confirm_check_in = questionary.confirm(
        "Voce tem certeza que quer fazer o check-in?"
    )

    if not confirm_check_in:
        return

    booking.check_in()

    if booking.seat is None:
        select_seat_action(booking)

    see_baggage_information: bool = questionary.confirm(
        "Voce quer ver informacoes sobre bagagens e taxas?"
    ).ask()

    if see_baggage_information:
        show_baggage_information(booking, console)
        questionary.press_any_key_to_continue()
