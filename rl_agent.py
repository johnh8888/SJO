import random

class RLAgent:

    def __init__(self):
        self.q = {"BET": 0, "SKIP": 0}

    def state(self, edge):

        return "GOOD" if max(edge.values()) > 0.03 else "BAD"

    def act(self, state):

        if state == "GOOD":
            return "BET"
        return "SKIP"

    def reward(self, pnl):

        self.q["BET"] += pnl
