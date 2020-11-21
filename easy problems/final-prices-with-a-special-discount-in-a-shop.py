from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) == 1:
            return prices
        j = 0
        i = 1
        while i <= len(prices) - 1 > j:
            while i < len(prices) - 1 and prices[j] < prices[i]:
                i += 1
            if prices[j] >= prices[i]:
                prices[j] = prices[j] - prices[i]
            j += 1
            i = j + 1
        return prices


