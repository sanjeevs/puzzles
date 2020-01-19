import random
from collections import Counter
import matplotlib.pyplot as plt

""" Demostrate binomial distribution by counting the number of misses
    before a hit.
"""


def roll_dice(num_sides=6):
    '''Return the face from [1,num_sides] of a dice roll.'''
    return random.randint(1, num_sides)


def test_roll_dice():
    events = []
    for _ in range(100):
        events.append(roll_dice())
    for i in range(6):
        assert((i + 1) in events)


def is_event_hit(event):
    '''Return True if the side is a 1.'''
    if event == 1:
        return True
    else:
        return False


def experiment(num_trials):
    samples = []
    for _ in range(num_trials):
        if is_event_hit(roll_dice()):
            samples.append(1)
        else:
            samples.append(0)
    return samples


def run_len_histogram(samples):
    '''
        Counts the different run length.
        Includes the hit also in the run length count.
    '''
    histogram = Counter()
    rl_cnt = 0

    for s in samples:
        rl_cnt += 1
        if s:
            histogram[rl_cnt] += 1
            rl_cnt = 0
    return histogram


def plot_histogram(histogram):
    print(histogram)
    x_values = []
    y_values = []
    for key in sorted(histogram.keys()):
        x_values.append(key)
        y_values.append(histogram[key])
    plt.bar(x_values, y_values, label="RunLength", align='center')
    plt.legend()
    plt.grid()
    plt.show()


def test_run_len_histogram():
    samples = [1, 0, 0, 1, 1]
    histogram = run_len_histogram(samples)
    assert(histogram[0] == 0)
    assert(histogram[1] == 2)
    assert(histogram[2] == 0)
    assert(histogram[3] == 1)


def prob_hit(samples):
    num_hits = sum(samples)
    return num_hits / len(samples)


if __name__ == "__main__":
    samples = experiment(10**6)
    print("Prob of hit=", prob_hit(samples))
    histogram = run_len_histogram(samples)
    plot_histogram(histogram)
