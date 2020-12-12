import collections
from itertools import combinations


class CombinationIterator:

    # def __init__(self, characters: str, combinationLength: int):
    #     self.allCombinations = list(combinations(characters, combinationLength))
    #     self.count = 0
    #
    # def next(self) -> str:
    #     self.count += 1
    #     return "".join(self.allCombinations[self.count - 1])
    #
    # def hasNext(self) -> bool:
    #     return self.count < len(self.allCombinations)

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = collections.deque(list(combinations(characters, combinationLength)))

    def next(self) -> str:
        return "".join(self.combinations.popleft())

    def hasNext(self) -> bool:
        if self.combinations:
            return True
        return False

obj = CombinationIterator("gksou", 3)
print(obj.next())
print(obj.next())

print(obj.next())

print(obj.next())

print(obj.hasNext())