# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkTrees(root.left, root.right)
        
    def checkTrees(self, leftT: TreeNode, rightT: TreeNode) -> bool:

        if leftT is None and rightT is None:
            return True
        if leftT is None or rightT is None:
            return False
        if leftT.val != rightT.val:
            return False
        else:
            outside = self.checkTrees(leftT.left, rightT.right)
            inside = self.checkTrees(leftT.right, rightT.left)

            return outside and inside
        
        
        