import random
from collections import Counter
import matplotlib.pyplot as plt

"""
    Given a population of hits/misses, estimate the number of hits.
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


def num_hits_sub_sampling(samples, sample_size):
    """Return the number of hits in small sample size."""
    lst = []
    num_hits = 0
    for i in range(len(samples)):
        num_hits += samples[i]
        if (i + 1) % sample_size == 0:
            lst.append(num_hits)
            num_hits = 0
    return lst


def test_num_hits_sub_sampling():
    lst = num_hits_sub_sampling([0, 1, 1, 1, 0, 0, 1], 3)
    assert lst == [2, 1]


def prob_hit(samples):
    num_hits = sum(samples)
    return num_hits / len(samples)


def plot_hit_freq(hit_freq):
    x_values = []
    y_values = []
    for i in hit_freq:
        x_values.append(i[0])
        y_values.append(i[1])
    plt.bar(x_values, y_values, label="sample hits", align='center')
    plt.show()


if __name__ == "__main__":
    samples = experiment(10**7)
    print("Prob of hit=", prob_hit(samples))
    lst = num_hits_sub_sampling(samples, 100)
    table = Counter(lst)
    hit_freq = table.most_common()
    plot_hit_freq(hit_freq)
