from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        order = {}
        for i in range(len(arr)):
            order[arr[i]] = i
        for piece in pieces:

            if len(piece) > 1:
                for i in range(len(piece) - 1):
                    if order.get(piece[i]) is None or order.get(piece[i + 1]) is None or order.get(
                            piece[i + 1]) - order.get(piece[i]) != 1:
                        return False
            elif order.get(piece[0]) is None:
                return False
        return True
