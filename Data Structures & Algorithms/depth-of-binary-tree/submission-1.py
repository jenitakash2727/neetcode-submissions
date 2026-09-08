class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right) #right sidel maximum irrukum depth so ethu maximum  athaan kandupidikanum so maximum 3 node left right paatha 

        return max(left, right) + 1 