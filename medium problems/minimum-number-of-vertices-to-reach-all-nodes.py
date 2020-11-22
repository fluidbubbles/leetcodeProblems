from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        for edge in edges:
            arr[edge[1]] = 1
        return [i for i in range(n) if arr[i] == 0]