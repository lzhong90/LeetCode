# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return None   
        s = self.rootLeaf(root, 0)
        return s
    
    
    def rootLeaf(self, root, b):
        if not root: return None
        if not root.left and not root.right: 
            return root.val+10*b  
 
        x = root.val
        a = x+b*10
        s = 0    
        
        if root.left:
            s += self.rootLeaf(root.left, a)            
        
        if root.right:
            s += self.rootLeaf(root.right, a)
       
        return s
