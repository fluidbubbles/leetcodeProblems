from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candies = candies[0]
        for candy in candies:
            if candy > greatest_candies:
                greatest_candies = candy
        arr = []
        for candy in candies:
            arr.append(candy + extraCandies >= greatest_candies)
        return arr