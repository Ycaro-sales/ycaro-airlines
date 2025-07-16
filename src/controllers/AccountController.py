from models.accounts import Customer
from models.airlines import Flight, Airplane


class AccountController:
    @staticmethod
    def book_flight(customer: Customer, flight: Flight) -> bool:
        if flight.is_full():
            return False

        flight.passengers.append(customer)
        customer.booked_flights.append(flight)

        return True

    @staticmethod
    def cancel_booking(customer: Customer, flight: Flight) -> bool:
        if flight not in customer.booked_flights:
            print("Flight not booked")
            return False

        customer.booked_flights.remove(flight)
        flight.passengers.remove(customer)

        return True
