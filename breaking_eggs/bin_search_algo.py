from experiment import *


def run(num_stories, num_eggs, experiment):
    """
    Return the minm level at which the egg will break.
    Divide the interval around the mean value till single egg is left.
    """
    if num_eggs == 0:
        raise ValueError("Number of eggs cannot be 0")

    if not experiment.is_solution_possible(num_stories):
        raise ValueError("No possible solution. Check configuration")

    guess = int((num_stories - 1) / 2)
    return __run_helper(guess, 0, num_stories - 1, num_eggs, experiment)


def __run_helper(guess, start_level, end_level, num_eggs, experiment):
    if num_eggs == 1:
        return __linear_search(start_level, end_level, experiment)
    elif (start_level == end_level):
        return start_level
    elif ((start_level + 1) == end_level):
        return __linear_search(start_level, end_level, experiment)
    else:
        # Be more aggressive.
        if experiment.trial(guess) == ResultTrial.egg_ok:
            # Lucky, Egg did NOT break
            new_guess = int((guess + end_level) / 2)
            return __run_helper(new_guess, guess + 1,
                                end_level, num_eggs, experiment)
        else:
            # Egg break means that focos on the lower half.
            new_guess = int((start_level + guess) / 2)
            return __run_helper(new_guess, start_level,
                                guess, num_eggs - 1, experiment)


def __linear_search(start_level, end_level, experiment):
    for i in range(start_level, end_level + 1):
        if experiment.trial(i) == ResultTrial.egg_break:
            return i
    raise RuntimeError("Could not break the egg. Finished all levels.")
