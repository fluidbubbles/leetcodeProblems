from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.current = 1
        self.n = n
        self.mapping = {i: None for i in range(1, n + 1)}

    def insert(self, id: int, value: str) -> List[str]:
        self.mapping[id] = value

        res = []

        for id in range(self.current, self.n + 1):
            if not self.mapping[id]: break

            res.append(self.mapping[id])
            self.current += 1

        return res