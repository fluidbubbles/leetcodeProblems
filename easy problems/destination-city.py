from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = {}
        for path in paths:
            for i in range(len(path)):
                if seen.get(path[i]) is None:
                    seen[path[i]] = 1 if i != 0 else 2
                else:
                    seen[path[i]] += 1
        print(seen)
        for key in seen:
            if seen[key] == 1:
                return key
