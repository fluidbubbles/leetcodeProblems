from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        i, j = 0, len(mat[0]) - 1
        for nlist in mat:
            res += nlist[i] + nlist[j] if i != j else nlist[i]
            i += 1
            j -= 1
        return res
