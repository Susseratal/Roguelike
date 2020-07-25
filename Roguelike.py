import random 
import logging
import curses
from curses import wrapper
import curses.ascii

from things import *

Alien = Enemy("Alien", 10)
Terminal = Enemy("Terminal", 5)
Roomba = Enemy("Roomba", 2)

Wall = Environment("|")
Ceiling = Environment("--")
Floor = Environment(".")
Gold = Environment("*")


def main (screen):
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, filemode="w")
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    screen.clear()

    X = random.randint(15,90)
    Y = random.randint(0,18)
    width = random.randint(10,40)
    height = random.randint(10,18)
    B = (X + width)
    O = (Y + height)
    screen.vline(Y,X,curses.ACS_VLINE,height)
    screen.hline(Y,X,curses.ACS_HLINE,width)
    screen.vline(Y,B,curses.ACS_VLINE,height)
    screen.hline(O,X,curses.ACS_HLINE,width)
    screen.addch(Y,X,curses.ACS_ULCORNER)
    screen.addch(Y,B,curses.ACS_URCORNER)
    screen.addch(O,X,curses.ACS_LLCORNER)
    screen.addch(O,B,curses.ACS_LRCORNER)


    #logging
    logging.debug(screen.getmaxyx())
    logging.debug("This message should go to the log file")
    screen.getkey()


wrapper (main)
