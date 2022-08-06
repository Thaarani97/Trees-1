#TC O(n)
#SC O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.prev = float("-inf")
        self.inorder(root)
        return self.flag
        
    
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        if root.val <= self.prev:
            self.flag = False
        self.prev = root.val
        self.inorder(root.right)