from ycaro_airlines.models import Flight, Customer
from ycaro_airlines.menus import customer_menu


class App:
    def __init__(self) -> None:
        pass


def main():
    for i in range(0, 10):
        Flight.mock_flight()

    user = Customer(username="ycaro")
    customer_menu(user)

    pass


if __name__ == "__main__":
    main()
