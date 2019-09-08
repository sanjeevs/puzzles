from enum import Enum
import random


class ResultTrial(Enum):
    """Possible result of dropping an egg from a level."""
    egg_break = 0
    egg_ok = 1


class Experiment:
    """Experiment to find if the egg breaks when dropped.

    Keyword arguments:
    num_stories -- the number of stories in the building.
    A building cannot have 0 stories.
    if level of egg was 0 and we drop from 0, then it breaks.
    """

    def __init__(self, secret_level):
        self.secret_level = secret_level
        self.num_attempts = 0

    def trial(self, try_level):
        """Return the result of dropping the egg from the given level."""
        self.num_attempts += 1
        if try_level >= self.secret_level:
            print("experiment", "try_level", try_level, "result", "break")
            return ResultTrial.egg_break
        else:
            print("experiment", "try_level", try_level, "result", "ok")
            return ResultTrial.egg_ok

    def is_solution_possible(self, num_stories):
        if self.secret_level >= num_stories:
            raise ValueError("The answer is not in legal range")
        return True
