from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        i = 0
        while i < len(nums):
            decompressed += [nums[i + 1] for j in range(nums[i])]
            i += 2
        return decompressed
