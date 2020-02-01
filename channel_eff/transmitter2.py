#
# Transmitter 2: Randomly send data for 4 consecutive slots.
#
import random


class Transmitter2:
    def __init__(self, p):
        self.p = p
        self.pkt_valid = 0
        self.pkt_len = 4
        self.num_bytes = 0
        self.state = "IDLE"

    def eval(self):
        """At start of tick."""
        print("BEG:tx2 state=", self.state, "num_bytes=", self.num_bytes, "valid=", self.pkt_valid)
        if self.state == "IDLE":
            if random.random() < self.p:
                self.state = "TX"
                self.pkt_valid = 1
                self.num_bytes = 0
        else:
            self.num_bytes += 1
            if self.num_bytes == self.pkt_len:
                self.state = "DONE"
        print("END:tx2 state=", self.state, "num_bytes=", self.num_bytes, "valid=", self.pkt_valid)

    def is_pkt_valid(self, pkt1_valid):
        """Return 1 if the packet successfully transmitted else 0."""
        if pkt1_valid:
            self.pkt_valid = 0
        if self.state == "DONE":
            return self.pkt_valid
        else:
            return 0

    def update(self):
        """At end of tick."""
        if self.state == "DONE":
            self.state = "IDLE"

    def is_idle(self):
        """Return 1 if the transmitter is silent."""
        if self.state == "IDLE":
            return 1
        else:
            return 0
