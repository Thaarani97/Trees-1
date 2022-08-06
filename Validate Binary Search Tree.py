#TC O(n)
#SC O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        self.inorder(root)
        for i in range(1,len(self.res)):
            if self.res[i-1] < self.res[i]:
                continue
            else:
                return False
        return True
    
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)