import collections
from typing import List


def numPairsDivisibleBy60(time: List[int]) -> int:
    remainders = collections.defaultdict(int)
    ret = 0
    for t in time:
        if t % 60 == 0:  # check if a%60==0 && b%60==0
            ret += remainders[0]
        else:  # check if a%60+b%60==60
            ret += remainders[60 - t % 60]
        remainders[t % 60] += 1  # remember to update the remainders
    return ret


numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18])