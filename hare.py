import random
from collections import Counter
import matplotlib.pyplot as plt

"""
    Assume a large number o hares that can either jump left or right.
    Result is that the distribution is normal. The mean matches the
    expected value.
"""


class Hare:
    def __init__(self, hop_size, hop_prob):
        self.pos = 0
        self.hop_size = hop_size
        self.hop_prob = hop_prob

    def next_hop(self):
        if random.random() < self.hop_prob[0]:
            return self.hop_size[0]
        else:
            return self.hop_size[1]

    def hop(self):
        self.pos += self.next_hop()


if __name__ == "__main__":
    num_hares = 10**6
    total_hops = 1000

    hares = []
    for _ in range(num_hares):
        hares.append(Hare((-1, 1), (0.01, 0.99)))

    for i in range(total_hops):
        for j in range(len(hares)):
            hares[j].hop()

    pos_lst = []
    for i in range(len(hares)):
        pos_lst.append(hares[i].pos)

    freq_cnt = Counter(pos_lst)
    table = freq_cnt.most_common()
    x_values = []
    y_values = []
    for cnt in table:
        x_values.append(cnt[0])
        y_values.append(cnt[1])

    plt.bar(x_values, y_values, align='center', label="PositionOfHares")
    plt.show()
