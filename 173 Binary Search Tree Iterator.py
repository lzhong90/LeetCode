# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stck = []
        
        p = self.root
        while p != None:
            self.stck.append(p)
            p = p.left
        

    def next(self):
        """
        :rtype: int
        """
        a = self.stck.pop()
        p = a.right
        
        while p: 
            self.stck.append(p)
            p= p.left
        
        return a.val
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stck:
            return True
        else:
            return False
