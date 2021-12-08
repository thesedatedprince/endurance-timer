import curses
import datetime
import time
import math

LENGTH = 5

CHAR_ZERO = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_ONE = (
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
)

CHAR_TWO = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2000",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_THREE = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_FOUR = (
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
)

CHAR_FIVE = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2000",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_SIX = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2000",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_SEVEN = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
)

CHAR_EIGHT = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
)

CHAR_NINE = (
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2588\u2000\u2000\u2000\u2588",
    "\u2588\u2588\u2588\u2588\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
    "\u2000\u2000\u2000\u2000\u2588",
)

CHAR_COLON = (
    "\u2000\u2000\u2000",
    "\u2000\u2588\u2000",
    "\u2000\u2000\u2000",
    "\u2000\u2588\u2000",
    "\u2000\u2000\u2000",
)

character_map = {
    "0": CHAR_ZERO,
    "1": CHAR_ONE,
    "2": CHAR_TWO,
    "3": CHAR_THREE,
    "4": CHAR_FOUR,
    "5": CHAR_FIVE,
    "6": CHAR_SIX,
    "7": CHAR_SEVEN,
    "8": CHAR_EIGHT,
    "9": CHAR_NINE,
    ":": CHAR_COLON
}

def format_time_digital(timestr):
    blocks = []
    for char in timestr:
        blocks.append(character_map[char])
    return blocks


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    timer = 0
    while True:
        stdscr.clear()

        blocks = format_time_digital(str(datetime.timedelta(seconds=timer)))
        i = 0
        line = math.floor(curses.LINES/2)
        while i < 5:
            result = ""
            for block in blocks:
                result += block[i]
                result += "\u2000"
            stdscr.addstr(line, math.floor(curses.COLS / 4), result, curses.color_pair(1))
            line += 1
            i += 1
        timer += 1
        time.sleep(1)
        stdscr.refresh()

    stdscr.getkey()


curses.wrapper(main)
