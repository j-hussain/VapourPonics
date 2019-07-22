# Dummy GPIO library
import random
OUT = 1
IN = 2
LOW = 0
HIGH = 1
BOARD = 5
def setup(p, m):
    pass
def output(p, v):
    pass
def setmode(m):
    pass
def setwarnings(w):
    pass
def cleanup():
    pass
def input(p):
    return random.choice((True, False))
