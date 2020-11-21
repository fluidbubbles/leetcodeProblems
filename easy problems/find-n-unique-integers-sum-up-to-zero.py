from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        i = 1
        while i <= n // 2:
            arr += [i, i * -1]
            i += 1
        if n % 2 != 0:
            arr.append(0)

        return arr

