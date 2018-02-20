#!/bin/python3

import sys

if __name__ == "__main__":

    house_left_side, house_right_side = input().strip().split(' ')
    house_left_side, house_right_side = [int(house_left_side), int(house_right_side)]
    larry_position, bob_position = input().strip().split(' ')
    larry_position, bob_position = [int(larry_position), int(bob_position)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]

    apple = map(int, input().strip().split(' '))
    orange = map(int, input().strip().split(' '))

    acount = 0
    for move in apple:
        if house_left_side <= larry_position + move <= house_right_side:
            acount += 1

    ocount = 0
    for move in orange:
        if house_left_side <= bob_position + move <= house_right_side:
            ocount += 1

    print(acount)
    print(ocount)
