# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from idlelib.tree import TreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        self.dic = set()
        self.build_tree(root, 0)

    def build_tree(self, root, x):
        if root:
            self.dic.add(x)
            self.build_tree(root.left, 2 * x + 1)
            self.build_tree(root.right, 2 * x + 2)

    def find(self, target: int) -> bool:
        return target in self.dic


class FindElements2:

    def __init__(self, root: TreeNode):
        self.A = A = set()
        if not root:
            return
        #
        queue = collections.deque([[root,0]])
        while queue:
            n,x = queue.popleft()
            A.add(x)
            if n.left:
                queue.append( [n.left  , 2*x+1] )
            if n.right:
                queue.append( [n.right , 2*x+2] )

    def find(self, target: int) -> bool:
        return target in self.A

