"""
File: CheckerboardKarel.py
Name: Chloe
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel finishes the task, facing South.
    """
    # while front_is_clear():
    #     fill_one_line()
    #     if facing_east():
    #         turn_left()
    #
    #         move()
    #         turn_left()
    #         fill_one_line()
    #     if facing_west:
    #         turn_right()
    #         move()
    #         turn_right()
    fill_one_line()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def fill_one_line():
    while not facing_south():
        put_beeper()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
            else: #wall
                if facing_west():
                    turn_right()
                    if front_is_clear():
                        move()
                        turn_right()
                    else:   #放了逼ㄆ走了一格面向西邊右轉：變成面向北邊，左邊是牆（終點）
                        turn_left()
                        turn_left()
                else:
                    turn_left()
                    if front_is_clear():
                        move()
                        turn_left()
                    else:
                        turn_left()
                        turn_left()
        else:   #   put beeper but front is not clear!
            if facing_west():
                turn_right()
                if front_is_clear():
                    move()
                    turn_right()
                    if front_is_clear():
                        move()
                    else:
                        turn_left()
                        if front_is_clear():
                            move()
                        else:
                            turn_left()
                            turn_left()
            else:
                turn_left()
                if front_is_clear():
                    move()
                    turn_left()
                    if front_is_clear():
                        move()
                    else:
                        turn_right()
                        if front_is_clear():
                            move()
                        else:
                            turn_left()
                            turn_left()










# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
