class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pair = 0
        for i in nums:
            if seen.get(i) is not None:
                seen[i] += 1
                pair += seen.get(i)
            else:
                seen[i] = 0
        return pair
