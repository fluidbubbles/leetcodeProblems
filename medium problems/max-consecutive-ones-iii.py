from typing import List


def longestOnes(A: List[int], K: int) -> int:
    i = 0
    for j in range(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1

longestOnes([1,1,1,0,0], 2)