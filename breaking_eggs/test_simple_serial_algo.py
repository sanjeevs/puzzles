#
# Tests for checking boundary conditions.
#

from simple_serial_algo import run as algo
from experiment import *
import pytest

def test_level_0():
    """Test for level 0 with 128 stories."""
    num_stories = 128
    secret_level = 0
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 1

def test_level_1():
    """Test for level 1 with 128 stories."""
    num_stories = 128
    secret_level = 1
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 2

def test_level_13():
    """Test for random level with 128 stories."""
    num_stories = 128
    secret_level = 13
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 14

def test_level_127():
    """Test for the highest level."""
    num_stories = 128
    secret_level = 127 
    experiment = Experiment(secret_level)
    assert algo(num_stories, 1, experiment) == secret_level 
    assert experiment.num_attempts == 128

def test_invalid_level():
    """Test if the solution is not possible"""
    num_stories = 128
    secret_level = num_stories
    experiment = Experiment(secret_level)
    with pytest.raises(ValueError):
        algo(num_stories, 1, experiment)
    assert experiment.num_attempts == 0

