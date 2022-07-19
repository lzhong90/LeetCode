# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return None
        
        head = root
        
        stck = [head]
        
        while stck:
            tmp = stck.pop()
            if tmp.right:
                stck.append(tmp.right)
            if tmp.left:
                stck.append(tmp.left)
            if stck:
                tmp.right = stck[-1]
                tmp.left = None
            
        return head
