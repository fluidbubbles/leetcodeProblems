from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return A
        i = 0
        j = len(A) - 1
        while i <= j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while j > 0 and j > i and A[j] % 2 != 0:
                j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A