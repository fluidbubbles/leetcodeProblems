from idlelib.tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.get_count(root, root.val)

    def get_count(self, root, big):
        c = 0
        if root:
            if root.val >= big:
                c += 1
                big = root.val
            left = self.get_count(root.left, big)
            right = self.get_count(root.right, big)
            c += left
            c += right
        return c