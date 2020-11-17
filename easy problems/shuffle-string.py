from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle_dict = {}
        for i in range(len(indices)):
            shuffle_dict[indices[i]] = s[i]
        i = 0
        result = ""
        while i < len(indices):
            result += shuffle_dict.get(i)
            i += 1
        return result