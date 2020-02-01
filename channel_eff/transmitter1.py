#
# Randomly send data every tick.
#
import random


class Transmitter1:
    def __init__(self, p):
        self.p = p
        self.state = "IDLE"

    def eval(self):
        """At start of tick."""
        if self.state == "IDLE":
            if random.random() < self.p:
                self.state = "TX"

    def is_pkt_valid(self, pkt1_valid):
        """Return 1 if the packet successfully transmitted else 0."""
        return 0
        if self.state == "TX":
            return 1
        else:
            return 0

    def update(self):
        """At end of tick."""
        self.state = "IDLE"
