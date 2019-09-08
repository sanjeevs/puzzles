"""
This is the adapted version of the solution by Prof Srini.
A better representation using radix.
"""

from experiment import *


def run(num_stories, num_eggs, experiment):

    # First determine the radix r
    r = 1
    while (r**num_eggs <= num_stories):
        r = r + 1
    print('Radix chosen is', r)

    floorNoBreak = [0] * num_eggs
    for i in range(num_eggs):
        # Begin phase i
        for j in range(r - 1):
            # increment ith digit of representation
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r, num_eggs, floorNoBreak)
            # Make sure you aren't higher than the highest floor
            if Floor > num_stories:
                floorNoBreak[i] -= 1
                break
            curr_result = experiment.trial(Floor - 1)
            if curr_result == ResultTrial.egg_break:
                floorNoBreak[i] -= 1
                break

    hardness = convertToDecimal(r, num_eggs, floorNoBreak)
    return hardness


def convertToDecimal(r, d, rep):
    """Return the decimal number given a the base and the representation.
     >>> convertToDecimal(4, 4, [3,3,3,3])
     255
     >>> convertToDecimal(4, 4, [1,2,3,3])
     111
     >>> convertToDecimal(4, 4, [1,0,0,0])
     64
     >>> convertToDecimal(4, 4, [2,0,0,0])
     128
     >>> convertToDecimal(4, 4, [1,1,0,0])
     80
     >>> convertToDecimal(4, 4, [1,2,0,0])
     96
     param r -- r-ary representation of number
     param d -- number of balls
     param rep -- representation of the number

"""
    number = 0
    for i in range(d - 1):
        number = (number + rep[i]) * r
    number += rep[d - 1]

    return number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
