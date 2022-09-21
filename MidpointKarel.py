"""
File: MidpointKarel.py
Name: Chloe
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel wil find the midpoint of the world and put one beeper on it.
    """
    fill_the_line()
    back_to_the_most_left()

    while not facing_north():
        if front_is_clear():
            # if on_beeper():
            move_to_the_right_most_beeper()
            if on_beeper():
                pick_beeper()
                move()
        if front_is_clear():
            # if on_beeper():
            move_to_the_left_most_beeper()
            if on_beeper():
                pick_beeper()
                move()
        else:
            turn_right()
        if not on_beeper():
            if facing_west():
                turn_right()
            if facing_east():
                turn_left()
            put_beeper()
        # else:
        #     if facing_west():
        #         turn_right()
        #     if facing_east():
        #         turn_left()
    pick_beeper()
    put_beeper()

    # move_to_the_right_most_beeper()
    # pick_beeper()
    # move()
    # move_to_the_left_most_beeper()
    # pick_beeper()
    # move()
    # move_to_the_right_most_beeper()
    # pick_beeper()
    # move()
    # move_to_the_left_most_beeper()
    # pick_beeper()
    # move()



def fill_the_line():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel wil fill the line, facing East.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def back_to_the_most_left():
    """
    Pre-condition: karel is on the most right, facing East.
    Post-condition: karel is on the most left, facing East.
    """
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()


def move_to_the_right_most_beeper():
    """
    Pre-condition: karel is on the left most beeper, facing East.
    Post-condition: karel is on the right most beeper, facing West.
    """
    while not facing_south():
        if on_beeper():
            if front_is_clear():
                move()
            else:
                turn_right()
        else:   #不在beeper上的話要跳出這個迴圈的方法
            turn_right()
    if not on_beeper(): #   in case Karel is on the right of the right most beeper
        turn_right()
        move()
    if facing_south():
        turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_to_the_left_most_beeper():
    """
    Pre-condition: karel is on the right most beeper, facing west.
    Post-condition: karel is on the left most beeper, facing east.
    """
    while not facing_south():
        if on_beeper():
            if front_is_clear():
                move()
            else:
                turn_left()
        else:
            turn_left()
    if not on_beeper(): #   in case Karel is on the left of the left most beeper
        turn_left()
        move()
    if facing_south():
        turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
