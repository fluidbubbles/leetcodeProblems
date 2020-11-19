from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        if len(points) < 2:
            return seconds
        x1, y1 = points[0][0], points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        i = 1
        while True:
            x3 = abs(x1 - x2)
            y3 = abs(y1 - y2)
            seconds += y3 if x3 < y3 else x3
            i += 1
            if i == len(points):
                break
            x1, y1 = x2, y2
            x2 = points[i][0]
            y2 = points[i][1]
        return seconds
