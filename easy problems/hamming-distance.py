class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x != 0 or y != 0:
            if x % 2 != y % 2:
                distance += 1
            x //= 2
            y //= 2
        return distance
