import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        seen = collections.Counter(moves)
        if seen["U"] == seen["D"] and seen["L"] == seen["R"]:
            return True
        return False
