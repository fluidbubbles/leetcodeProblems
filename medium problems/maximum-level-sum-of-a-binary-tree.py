# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from idlelib.tree import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0
        max_level = 0
        max_sum = float('-inf')

        deque = collections.deque()
        deque.append(root)

        while deque:
            level += 1
            cur_sum = 0

            for i in range(len(deque)):
                root = deque.popleft()
                cur_sum += root.val

                if root.left:
                    deque.append(root.left)

                if root.right:
                    deque.append(root.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
        return max_level
