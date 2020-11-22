from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        if root is None:
            return arr
        elif len(root.children) == 0:
            return [root.val]
        else:
            for child in root.children:
                val = self.postorder(child)
                arr += val
            arr += [root.val]
        return arr