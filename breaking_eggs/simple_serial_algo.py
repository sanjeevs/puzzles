from experiment import *
import pytest

def run(num_stories, num_eggs, experiment):
    """
    Return the minm level at which the egg will break.
    Simply start at the lowest level and count up till the egg breaks.

    Keyword arguments:
    num_stories -- number of levels in the building
    num_eggs -- initial number of eggs provided
    experiment -- function to conduct the trial. Records the number of attempts.

    """
    if num_eggs == 0:
        raise ValueError("Number of eggs cannot be 0")

    if not experiment.is_solution_possible(num_stories):
        raise ValueError("No possible solution. Check configuration")

    # Count from lowest level
    return __run_helper(0, num_stories -1, num_eggs, experiment)

def __run_helper(start_level, end_level, num_eggs, experiment):
    if experiment.trial(start_level) == ResultTrial.egg_break:
        return start_level
    else:
        return __run_helper(start_level + 1, end_level, num_eggs, experiment)
