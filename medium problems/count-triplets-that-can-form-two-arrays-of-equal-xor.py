from typing import List

ans = 2 ^ 3 ^ 1
ans1 = 3 ^ 1 ^ 1
ans2 = 1 ^ 6 ^ 7
ans3 = 1 ^ 7 ^ 7
print(ans, ans1)


def countTriplets(arr: List[int]) -> int:
    res = 0
    for i in range(len(arr) - 1):
        xor = 0
        for j in range(i, len(arr)):
            x = arr[j]
            xor ^= arr[j]
            if xor == 0:
                res += j - i  # len-1
    return res


countTriplets([1,1,1,1,1])