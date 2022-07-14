# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return root.val
        
        
        mx_root, mx = self.maxSum(root)
        
        return max(mx_root, mx)
    
    def maxSum(self, root):
        if not root: return None, None
        if not root.left and not root.right: return root.val, root.val
        
        lroot, l = self.maxSum(root.left)
        rroot, r = self.maxSum(root.right)
        
        print(lroot)
        print(l)
        
        if not root.left: 
            return max(root.val,root.val+rroot), max(rroot, r)
        if not root.right: 
            return max(root.val, root.val+lroot), max(lroot, l)
        
        mx = max(l,r, lroot, rroot, lroot+rroot+root.val)
        mx_root = max(lroot+root.val, rroot+root.val, root.val)
        
        return mx_root, mx
