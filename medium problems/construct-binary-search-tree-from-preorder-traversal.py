# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.insert(root, preorder[i])
        return root

    def insert(self, root, val):
        if root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)


obj = Solution()
obj.bstFromPreorder([8,5,1,7,10,12])