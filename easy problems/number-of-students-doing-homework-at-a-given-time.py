from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        i = 0
        count = 0
        while i < len(startTime):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
            i += 1
        return count
