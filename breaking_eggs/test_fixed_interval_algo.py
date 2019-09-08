#
# Tests for checking boundary conditions.
#

from fixed_interval_algo import run as algo
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


def test_16_stories_2_eggs():
    """Directed test for 10 stories with 2 eggs"""
    num_stories = 16
    num_eggs = 2
    secret_level = 7
    experiment = Experiment(secret_level)
    assert algo(num_stories, num_eggs, experiment) == secret_level
    assert experiment.num_attempts == 9


def test_16_stories_2_eggs_l_0():
    """Directed test for 16 stories, 4 eggs, level=15"""
    num_stories = 16
    num_eggs = 4
    secret_level = 0
    experiment = Experiment(secret_level)
    assert algo(num_stories, num_eggs, experiment) == secret_level
    assert experiment.num_attempts == 4


def test_16_stories_4_eggs_l_7():
    """Directed test for 16 stories, 4 eggs, level=15"""
    num_stories = 16
    num_eggs = 4
    secret_level = 7
    experiment = Experiment(secret_level)
    assert algo(num_stories, num_eggs, experiment) == secret_level
    assert experiment.num_attempts == 11


def test_16_stories_4_eggs_l15():
    """Directed test for 16 stories, 4 eggs, level=15"""
    num_stories = 16
    num_eggs = 4
    secret_level = 15
    experiment = Experiment(secret_level)
    assert algo(num_stories, num_eggs, experiment) == secret_level
    assert experiment.num_attempts == 3


def test_algo_sanity():
    """Test sanity that the algo generates the correct result. """
    for _ in range(100):
        num_stories = random.randint(128, 1024)
        num_eggs = random.randint(1, num_stories)
        secret_level = random.randint(0, num_stories - 1)
        experiment = Experiment(secret_level)
        assert algo(num_stories, num_eggs, experiment) == secret_level


def test_algo_sanity_4_eggs():
    """Test sanity that the algo with always 4 eggs """
    for _ in range(100):
        num_stories = random.randint(128, 1024)
        num_eggs = 4
        secret_level = random.randint(0, num_stories - 1)
        experiment = Experiment(secret_level)
        assert algo(num_stories, num_eggs, experiment) == secret_level
