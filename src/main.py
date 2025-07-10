from classes import Client, Flight, city
from typing import Dict, List
from uuid import UUID
from random import randint

flights: Dict[UUID, Flight] = {}
cities: List[str] = ["Maceio", "Recife", "Rio de Janeiro"]


def main():
    for i in range(3):
        flight = Flight(
            cities[randint(0, len(cities))], cities[randint(0, len(cities))]
        )
        flights[flight.id] = flight

    name = input("insert username:")
    client = Client(name)
    options: List[UUID] = []
    while True:
        for i, v in flights.items():
            print("")

        choice = int(input("Which Flight do you want to board? 1-3"))
