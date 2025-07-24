import curses as c
import curses.textpad as ct
from curses import wrapper

stdscr = c.initscr()


def main(stdscr):
    # Clear screen
    stdscr.clear()

    for i in range(0, 11):
        v = i - 10
        stdscr.addstr(i, 0, "10 divided by {} is {}".format(v, 10 / v))

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
