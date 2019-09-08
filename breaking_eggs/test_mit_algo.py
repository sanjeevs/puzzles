#
# Tests for checking boundary conditions.
#

from mit_algo import run as algo
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
    assert experiment.num_attempts == 10 


def test_level_127_2_eggs():
    """Test for level 127 with 128 stories and 2 egg."""
    num_stories = 128
    secret_level = 127
    experiment = Experiment(secret_level)
    assert algo(num_stories, 2, experiment) == secret_level
    assert experiment.num_attempts == 18


def test_algo_sanity():
    """Test sanity that the algo generates the correct result. """
    for _ in range(100):
        num_stories = random.randint(128, 1024)
        num_eggs = random.randint(1, num_stories)
        secret_level = random.randint(0, num_stories - 1)
        experiment = Experiment(secret_level)
        assert algo(num_stories, num_eggs, experiment) == secret_level


def xx_test_algo_sanity_buckets_4():
    """Test sanity that the algo works with 4 buckets. """
    for _ in range(100):
        num_stories = random.randint(128, 1024)
        num_eggs = 4
        secret_level = random.randint(0, num_stories - 1)
        experiment = Experiment(secret_level)
        assert algo(num_stories, num_eggs, experiment) == secret_level
