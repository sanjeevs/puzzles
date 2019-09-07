#
# Tests for checking boundary conditions.
#

from bin_search_algo import run as algo
from experiment import *
import pytest

def test_level_0():
    """Test for level 0 with 128 stories and 1 egg."""
    num_stories = 128
    secret_level = 0
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 1

def test_level_13():
    """Test for random level with 128 stories and 1 egg."""
    num_stories = 128
    secret_level = 13
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 14

def test_level_63_2_eggs():
    """Test for level 0 with 128 stories and 2 egg."""
    num_stories = 128
    secret_level = 63 
    experiment = Experiment(secret_level)
    assert algo(num_stories, 2, experiment) == secret_level 
    assert experiment.num_attempts == 65


def test_level_127_2_eggs():
    """Test for level 127 with 128 stories and 2 egg."""
    num_stories = 128
    secret_level = 127 
    experiment = Experiment(secret_level)
    assert algo(num_stories, 2, experiment) == secret_level 
    assert experiment.num_attempts == 8

def test_level_rand_x_eggs():
    """Test for level 127 with 128 stories and 2 egg."""
    num_stories = 128
    for _ in range(100):
        num_eggs = random.randint(1, num_stories)
        secret_level = random.randint(0, num_stories-1) 
        experiment = Experiment(secret_level)
        assert algo(num_stories, num_eggs, experiment) == secret_level 
