class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        root.left, root.right = root.right, root.left #step1 : root.rught

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root