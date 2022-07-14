# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        
        
        l = self.minDepth(root.left) 
        r = self.minDepth(root.right)
        
        # if one of the subtree is empty, ignore it
        if l == 0: return r+1
        if r == 0: return l+1
        
        # return the minimum value when it is not 0
        return min(l,r)+1
