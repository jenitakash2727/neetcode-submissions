class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:#Treenode already-val.root/left,root.right irrukum 

        if root is None:
            return None

        root.left, root.right = root.right, root.left #step1 : root.rught ,root/left mathuna pothum invert akirom leftla irukurathu right node right node left node pokum 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root