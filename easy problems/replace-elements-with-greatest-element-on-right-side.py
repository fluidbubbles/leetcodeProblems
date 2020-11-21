from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        k = 0
        for i in range(len(arr)-1):
            if i == k:
                next_max = 0
                for j in range(i+1, len(arr)):
                    if arr[j] > next_max:
                        next_max, k = arr[j], j
            arr[i] = next_max
        arr[-1] = -1
        return arr