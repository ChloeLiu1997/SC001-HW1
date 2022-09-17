"""
File: CollectNewspaperKarel.py
Name: Chloe
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the North-West of the house, facing East
    post-condition: Karel is back to the North-West of the house with beeper, facing East
    """
    move_and_pick_beeper()
    go_back_and_put_beeper()


def move_and_pick_beeper():
    # Move karel to the beeper and pick it up
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def go_back_and_put_beeper():
    # Move Karel back to the house and put beeper
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
