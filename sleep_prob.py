# Consider a coin toss. If it is head, I sleep for 1 hr. If it is tail, I
# watch a movie for 4 hrs.
# What is the expected amount of time that I would sleep?
# Answer: 0.2
# python3 sleep_prob.py
# Mean number of sleeping hours=0.20003780107903807

import random


def trial(p):
    """Return 1 for favorable event."""
    if random.random() > p:
        return 1
    else:
        return 0


def experiment(n, p):
    """Run the experiment n times with trial prob p."""
    samples = []
    for _ in range(n):
        if trial(p):
            # Sleep for 1 hr
            samples.append(1)
        else:
            # Watch a movie for 4hrs
            samples.extend([0] * 4)
    return samples


if __name__ == "__main__":
    num_of_tosses = 10**8
    prob_of_success = 0.5
    samples = experiment(num_of_tosses, prob_of_success)
    mean = sum(samples) / len(samples)
    print("Mean number of sleeping hours={}".format(mean))
