"""
Implement the fixed interval algo for figuring out the min level
at which the ball will break.
"""
from experiment import *


def run(num_stories, num_eggs, experiment):
    """
    Return the minm level at which the egg will break.
    Divide the range into fixed intervals of size (n)**1/num_eggs.
    For example if there is 1 ball left, then interval size is 1.
    if there are 2 balls left then the interval size is sqrt(n
    if there are 3 balls left then the interval size is cube_root(n)
    """
    if num_eggs == 0:
        raise ValueError("Number of eggs cannot be 0")

    if not experiment.is_solution_possible(num_stories):
        raise ValueError("No possible solution. Check configuration")

    start_level = 0
    end_level = num_stories - 1

    return __run_helper(start_level, end_level, num_eggs, experiment)


def __run_helper(start_level, end_level, num_eggs, experiment):

    # Base case: Either we ran out of extra eggs or no more intervals.
    if num_eggs == 1 or (end_level - start_level <= 1):
        return __linear_search(start_level, end_level, experiment)

    intervals = create_intervals(start_level, end_level, num_eggs)

    # To have moved down the parent must have had an egg break.
    prev_result = ResultTrial.egg_break

    for (lsb, msb) in reversed(intervals):
        curr_result = experiment.trial(lsb)
        if curr_result == ResultTrial.egg_break:
            num_eggs -= 1
            if num_eggs == 1:
                return __linear_search(start_level, lsb, experiment)
            else:
                # Move down to the next interval
                pass
        else:
            # Egg did not break.
            if prev_result == ResultTrial.egg_break:
                # But last time it broke, hence scan up.
                # Need to check the lsb of the next interval if it exists.
                return __linear_search(lsb, msb + 1, experiment)
            else:
                # Ignore all the intervals below it. Focus on this
                print("ok: lsb =", lsb, "msb", msb, "num_eggs =", num_eggs)
                return __run_helper(lsb + 1, msb, num_eggs, experiment)
        prev_result = curr_result

    # If cycles through all the intervals, then the bottom most interval is the
    # correct interval.
    return __run_helper(intervals[0][0], intervals[0][1], num_eggs, experiment)


def __linear_search(start_level, end_level, experiment):
    """Return the level at which the egg breaks,
       by scanning from low to high.
    """
    for i in range(start_level, end_level + 1):
        if experiment.trial(i) == ResultTrial.egg_break:
            return i
    raise RuntimeError("Could not break the egg. Finished all levels.")


def create_intervals(start_level, end_level, num_eggs):
    """Return a list of intervals given the number of stories and eggs.
    Each interval is a tuple (a,b).
    The size of the interval is (num_stories)**1/num_eggs.

    :param start_level: Starting level
    :param end_level: Ending level
    :param num_eggs: Number of eggs

    >>> create_intervals(0, 0, 100)
    [(0, 0)]
    >>> create_intervals(0, 1, 2)
    [(0, 0), (1, 1)]
    >>> create_intervals(10, 11, 2)
    [(10, 10), (11, 11)]
    >>> create_intervals(0, 15, 2)
    [(0, 3), (4, 7), (8, 11), (12, 15)]
    >>> create_intervals(0, 14, 2)
    [(0, 2), (3, 5), (6, 8), (9, 11), (12, 14)]
    >>> create_intervals(10, 26, 2)
    [(10, 13), (14, 17), (18, 21), (22, 25), (26, 26)]
    >>> create_intervals(10, 20, 3)
    [(10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 20)]
    """
    num_stories = end_level - start_level + 1
    if num_stories <= 0 or num_eggs == 0:
        raise ValueError("Invalid configuration to create the intervals")

    if num_stories <= 1:
        return [(start_level, end_level)]

    lst = []
    if num_eggs == 1:
        for i in range(num_stories):
            lst.append((start_level + i, start_level + i))
        return lst

    interval_sz = int(num_stories**(1 / num_eggs))
    lsb = 0
    msb = 0
    while lsb < num_stories:
        msb = lsb + interval_sz - 1
        if msb >= num_stories:
            msb = num_stories - 1
        lst.append((start_level + lsb, start_level + msb))
        lsb = msb + 1
    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()
