import random
import sys
from collections import defaultdict
import matplotlib.pyplot as plt


def trial():
    return random.randint(1, 6)


def experiment(ntimes):
    score = 0.0
    for _ in range(ntimes):
        score += trial()
    return round(score / ntimes, 1)


def test(mtimes, ntimes):
    pdf = defaultdict(lambda: 0)
    for i in range(mtimes):
        avg = experiment(ntimes)
        pdf[avg] += 1
    return pdf


def main(argv):
    if(len(argv) == 3):
        mtimes = int(argv[1])
        ntimes = int(argv[2])
    elif(len(argv) == 2):
        mtimes = int(argv[1])
        ntimes = 1024
    else:
        mtimes = 1024
        ntimes = 1024

    print("Running experiment ", mtimes, " with num trials ", ntimes)
    pdf = test(mtimes, ntimes)
    print(pdf)
    plt.bar(range(len(pdf)), list(pdf.values()), align='center')
    plt.xticks(range(len(pdf)), sorted(list(pdf.keys())))
    plt.show()


if __name__ == "__main__":
    main(sys.argv)
