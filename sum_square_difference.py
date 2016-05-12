import math

import time

def code_intro():
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------  Project Euler Problem 6  ----------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -- This project was done as part the https://projecteuler.net/ coding ----'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)

def main():
    code_intro()
    range_max = 100
    print square_of_sum(range_max) - sum_of_square(range_max)

def sum_of_square(range_max):
    sum = 0
    for number in range(1,range_max+1):
        sum += number ** 2
    return sum
def square_of_sum(range_max):
    sum = 0
    for number in range(1,range_max+1):
        sum += number
    return sum ** 2

main()
