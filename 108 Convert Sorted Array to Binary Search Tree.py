# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        length = len(nums)
        
        if length == 1:
            return TreeNode(nums[0])
        
        left = 0
        right = length-1
        
        def build(l, r):
            if l > r:
                return
            m = (l+r)//2
            
            root = TreeNode(nums[m])
            
            root.left = build(l,m-1)
            root.right = build(m+1, r)
            
            return root
        
        return build(left, right)
