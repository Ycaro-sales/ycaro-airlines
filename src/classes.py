from typing import List
from uuid import UUID, uuid4


class Client:
    def __init__(self, username: str) -> None:
        self.username: str = username
        self.id = uuid4()
        self.fligths: List[Flight] = []


class Flight:
    def __init__(self, From: str, To: str, capacity: int = 255) -> None:
        self.From: str = From
        self.To: str = To
        self.id: UUID = uuid4()
        self.capacity: int = capacity
        self.passengers: List[Client] = []
        self.seats_filled = 0

    def board(self, passenger: Client) -> UUID | None:
        if self.seats_filled == self.capacity:
            return None

        self.passengers.append(passenger)
        self.seats_filled += 1

        return self.id
