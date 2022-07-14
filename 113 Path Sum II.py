# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, a, target, path):
            if not root: return None
            a += root.val
            path.append(root.val)
            if not root.left and not root.right:
                if a == target:
                    ans.append(path.copy())

            
            if root.left:
                dfs(root.left, a, target, path)
            if root.right:
                dfs(root.right, a, target, path)
            if len(path) >0:
                path.pop()
        
        ans = []
        a = 0
        dfs(root, a, targetSum, [])
        return ans   
