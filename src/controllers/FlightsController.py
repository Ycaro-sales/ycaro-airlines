from models.accounts import Customer
from models.airlines import Flight, Airplane, cities
from datetime import date


class FlightsController:
    @staticmethod
    def create_flight(
        plane: Airplane,
        departure: date,
        From: cities = cities.Maceio,
        To: cities = cities.Recife,
        price: float = 200.00,
    ):
        return Flight(plane, departure, From, To, price)
