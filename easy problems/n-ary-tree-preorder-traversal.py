from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        if root is None:
            return arr
        arr += [root.val]
        for child in root.children:
            val = self.preorder(child)
            arr += val
        return arr
