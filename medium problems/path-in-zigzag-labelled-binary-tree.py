from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        length_of_tree = 1
        length_arr = 0
        while not label < length_of_tree:
            length_of_tree *= 2
            length_arr += 1
        rng_upper = length_of_tree - 1
        rng_lower = length_of_tree // 2
        arr = [0] * length_arr
        length_arr -= 1
        arr[length_arr] = label
        while label != 1:
            next_label = (rng_upper - label) // 2
            rng_upper = rng_lower - 1
            rng_lower //= 2
            label = rng_lower + next_label
            length_arr -= 1
            arr[length_arr] = label
        return arr

