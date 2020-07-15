import random 
import logging
import curses
import curses.ascii
from curses import wrapper

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Environment:
    def __init__(self, name):
        self.name = name

class Room:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

Alien = Enemy("Alien", 10)
Terminal = Enemy("Terminal", 5)
Roomba = Enemy("Roomba", 2)

Wall = Environment("|")
Ceiling = Environment("--")
Floor = Environment(".")
Gold = Environment("*")

X = random.randint(0,40)
Y = random.randint(0,40)
B = Room(X, Y)

def main (screen):
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, filemode="w")
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    screen.clear()

    logging.debug("This message should go to the log file")

    screen.getkey()
wrapper (main)
