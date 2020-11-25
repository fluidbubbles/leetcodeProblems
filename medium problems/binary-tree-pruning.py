from idlelib.tree import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.val == 0 and not root.left and not root.right:
                return None
        return root