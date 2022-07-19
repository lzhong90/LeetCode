# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# The idea is to use preorder traversal, because in preorder traversal, the value of node from the same layer always comes from left to right, from upside down

# For post order traversal, he value of node from the same layer always comes from left to right, from downside up
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    
        
        def dfs(root, lev):
            if not root: return
            
            if lev < len(res):
                if lev % 2 == 1:
                    res[lev].appendleft(root.val)
                else:
                    res[lev].append(root.val)
            else:
                res.append(deque([root.val]))
            
            if root.left:
                dfs(root.left, lev+1)
            if root.right:
                dfs(root.right, lev+1)
        
        
        
        
        res = []
        dfs(root, 0)
        return res
