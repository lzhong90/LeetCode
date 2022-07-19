# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# DFS 
# time: O(N)
# space: O(H), H is the height of the binary tree


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return None
        
        stck = []       

        stck.append((root,0))
        dic = {}
        max_dep = 0
        #print(stck)
        
        while stck:
            tmp, dep = stck.pop()
            max_dep = max(max_dep, dep)
            if dep not in dic:
                dic[dep] = tmp.val
 
            if tmp.left:
                stck.append((tmp.left, dep+1))
            if tmp.right:
                stck.append((tmp.right, dep+1))
            
        
        return [dic[i] for i in range(max_dep+1)]
