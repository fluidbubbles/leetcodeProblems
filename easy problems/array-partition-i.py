from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(len(nums) - 1, 0, -2):
            pair_sum += min(nums[i], nums[i-1])
        return pair_sum