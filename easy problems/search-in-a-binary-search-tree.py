from idlelib.tree import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root
        elif root.val > val:
            root = self.searchBST(root.left, val)
        else:
            root = self.searchBST(root.right, val)
        return root