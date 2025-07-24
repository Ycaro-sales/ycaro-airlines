from typing import List
from uuid import UUID, uuid4
from enum import Enum
from typing import Dict
from datetime import timedelta


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


class Customer:
    def __init__(self, username: str) -> None:
        self.username: str = username
        self.id = uuid4()
        self.fligths: List[Flight] = []


class Flight:
    def __init__(self, From: cities, To: cities, capacity: int = 255) -> None:
        self.From: cities = From
        self.To: cities = To
        self.id: UUID = uuid4()
        self.capacity: int = capacity
        self.passengers: List[Customer] = []
        self.seats_filled = 0

    def board(self, passenger: Customer) -> UUID | None:
        if self.seats_filled == self.capacity:
            return None

        self.passengers.append(passenger)
        self.seats_filled += 1

        return self.id
