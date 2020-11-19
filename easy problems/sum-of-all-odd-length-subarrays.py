from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = 1
        i, j, x = 0, 0, True
        sum_all = 0
        while length <= len(arr):
            if length == 1 or x:
                x = False
                sum_arr = sum(arr[j:length+j])
            else:
                sum_arr = sum_arr - arr[j-1] + arr[length+j-1]
            sum_all += sum_arr
            j += 1
            if length + j <= len(arr):
                i += 1
                j = i
            else:
                x = True
                i, j = 0, 0
                length += 2
        return sum_all