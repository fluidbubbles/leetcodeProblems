from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1 = -1000
        num2 = -1000
        for i in nums:
            if i >= num1:
                num2 = num1
                num1 = i
            elif i >= num2:
                num2 = i
        return (num1 - 1) * (num2 - 1)
