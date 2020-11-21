from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            left = 0
            right = len(i) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if mid == 0 and i[mid] < 0 or i[mid] < 0 and i[mid - 1] >= 0:
                    count += len(i) - mid
                    break
                elif i[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
        return count