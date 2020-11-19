from typing import List


def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
    mat = [[0]*m for i in range(n)]
    odd = 0
    i = 0
    while i < len(indices):
        k, m = indices[i][0], indices[i][1]
        j = 0
        while True:
            if j < len(mat[k]):
                mat[k][j] += 1
                if mat[k][j] % 2 == 1:
                    odd += 1
                else:
                    odd -= 1
            if j < len(mat):
                mat[j][m] += 1
                if mat[j][m] % 2 == 1:
                    odd += 1
                else:
                    odd -= 1
            j += 1
            if j >= len(mat) and j >= len(mat[k]):
                break
        i += 1
    return odd

