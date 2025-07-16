from datetime import date, timedelta
from base.model import Model
from uuid import UUID
from enum import Enum
from typing import List, Dict
from models.accounts import Customer


class cities(Enum):
    Maceio = "Maceio"
    Recife = "Recife"
    Aracaju = "Aracaju"
    Joao_pessoa = "Joao Pessoa"

    @classmethod
    def distance(cls, city1: "cities", city2: "cities"):
        distances: Dict[cities, Dict[cities, timedelta]] = {
            cities.Maceio: {
                cities.Aracaju: timedelta(hours=1),
                cities.Recife: timedelta(hours=1),
                cities.Joao_pessoa: timedelta(hours=2),
            },
            cities.Aracaju: {
                cities.Maceio: timedelta(hours=1),
                cities.Recife: timedelta(hours=2),
                cities.Joao_pessoa: timedelta(hours=3),
            },
            cities.Recife: {
                cities.Maceio: timedelta(hours=1),
                cities.Joao_pessoa: timedelta(hours=1),
                cities.Aracaju: timedelta(hours=2),
            },
            cities.Joao_pessoa: {
                cities.Aracaju: timedelta(hours=3),
                cities.Maceio: timedelta(hours=2),
                cities.Recife: timedelta(hours=1),
            },
        }
        return distances[city1][city2]


class PlaneModels(Enum):
    pass


class Airplane(Model):
    planes: Dict[UUID, "Airplane"] = {}

    def __init__(
        self,
        model: int,
        capacity: int = 255,
        identification: str = "",
        current_city: cities = cities.Maceio,
    ):
        super().__init__()
        self.capacity: int = capacity
        self.identification: str = identification
        self.current_city: cities = current_city
        self.current_flight: Flight | None = None

        self.planes[self.id] = self

    @classmethod
    def list_airplanes(cls):
        planes = list(cls.planes.values())
        return planes


class Flight(Model):
    flights: Dict[UUID, "Flight"] = {}

    def __init__(
        self,
        plane: Airplane,
        departure: date,
        From: cities = cities.Maceio,
        To: cities = cities.Recife,
        price: float = 200.00,
    ):
        super().__init__()
        self.plane: Airplane = plane
        self.passengers: List[Customer] = []
        self.From: cities = From
        self.To: cities = To
        self.departure: date = departure
        self.arrival: date = departure + cities.distance(From, To)
        self.price = price
        self.flights[self.id] = self

    def is_full(self) -> bool:
        if len(self.passengers) >= self.plane.capacity:
            return True
        return False

    # TODO: implement filters
    @classmethod
    def list_flights(cls):
        flights = list(cls.flights.values())
        return flights


class Airport(Model):
    pass


class Airline(Model):
    pass
