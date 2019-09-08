"""
Run a simulation with 128 stories and 4 eggs. Compare the
performance of a bin search vs fixed interval algo.
"""
import mit_algo
import mit_algo
import bin_search_algo
import random
from experiment import Experiment


def main():
    num_stories = 128
    num_eggs = 2
    num_trials = 100

    algos = ["bin_search", "mit"]
    results = {}
    for a in algos:
        results[a] = []

    for t in range(num_trials):
        secret_level = random.randint(1, num_stories - 1)
        results["bin_search"].append(run_bin_trial(num_stories, num_eggs, secret_level))
        results["mit"].append(run_mit_trial(num_stories, num_eggs, secret_level))

    draw_plot(num_trials, results)


def run_bin_trial(num_stories, num_eggs, secret_level):
    """Return the number of attempts taken by the bin algo."""
    experiment = Experiment(secret_level)
    answer = bin_search_algo.run(num_stories, num_eggs, experiment)
    assert answer == secret_level
    return experiment.num_attempts


def run_mit_trial(num_stories, num_eggs, secret_level):
    """Return the number of attempts taken by the fixed interval algo."""
    experiment = Experiment(secret_level)
    answer = mit_algo.run(num_stories, num_eggs, experiment)
    assert answer == secret_level
    return experiment.num_attempts


import matplotlib.pyplot as plt


def draw_plot(num_trials, results):
    x_values = range(1, num_trials + 1)
    for k in results:
        plt.plot(x_values, results[k], marker='o')
    plt.legend(results.keys())
    plt.title("Experimenal comparsion of algos")
    plt.xlabel("Trial Run")
    plt.ylabel("Number of attempts")
    plt.show()


if __name__ == "__main__":
    main()
