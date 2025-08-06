from typing import Callable, Tuple
from ycaro_airlines.menus import menu_factory


def login_action():
    pass


def signup_action():
    pass


def user_menu():
    options: list[Tuple[str, Callable]] = [
        ("Login", login_action),
        ("Sign up", signup_action),
    ]
    menu_factory("User menu", options=options)()
