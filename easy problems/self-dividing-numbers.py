from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        while left <= right:
            x = left
            while x != 0 and x % 10 != 0:
                y = x
                x = x % 10
                if left % x != 0:
                    break
                x = y // 10
            if x == 0:
                arr.append(left)
            left += 1
        return arr