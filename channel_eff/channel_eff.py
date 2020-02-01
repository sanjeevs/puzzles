# Assume that there are 2 transmitters. One transmitter randomly
# sends packet which is one tick wide. The other transmitter sends
# randomly a packet that is 4 ticks wide.
# If there is a collision on any slot, the transmitters have to repeat
# the entire packet.
# What is the channel efficiency? Ie the ratio of slots with data and the
# slots that were wasted.
import random
from transmitter1 import *
from transmitter2 import *

if __name__ == "__main__":
    p = 0.5
    n = 10
    tx1 = Transmitter1(p)
    tx2 = Transmitter2(1)
    samples = []
    for _ in range(n):
        tx1.eval()
        tx2.eval()
        pkt1_valid = tx1.is_pkt_valid
        if tx2.is_idle() and pkt1_valid:
            samples.append(1)
        elif tx2.is_pkt_valid(pkt1_valid):
            samples.append([1, 1, 1, 1])
        tx1.update()
        tx2.update()
    print(samples)
