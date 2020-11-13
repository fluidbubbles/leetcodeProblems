from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        i = 0
        k = n
        while i < n:
            arr.append(nums[i])
            arr.append(nums[k])
            i += 1
            k += 1
        return arr