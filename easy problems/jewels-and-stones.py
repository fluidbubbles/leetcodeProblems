class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        seen = {}
        for i in J:
            seen[i] = "seen"
        my_jewels = 0
        for i in S:
            if seen.get(i) is not None:
                my_jewels += 1
        return my_jewels