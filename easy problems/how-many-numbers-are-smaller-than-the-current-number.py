from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [num for num in nums]
        res.sort()
        counts = {}
        for pos, val in enumerate(res):
            counts.setdefault(val, pos)
        for pos in range(len(nums)):
            nums[pos] = counts[nums[pos]]
        return nums
