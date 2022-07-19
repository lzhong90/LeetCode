"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cur = root
        head = None
        mov = None
        
        if not root or(not root.left and not root.right): return root
        
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        mov = cur.left
                    else:
                        mov.next = cur.left
                        mov = mov.next
                
                if cur.right:
                    if not head:
                        head = cur.right
                        mov = cur.right
                    else:
                        mov.next = cur.right
                        mov = cur.right                       
                        
                
                
                cur = cur.next
            
            cur = head
            head = None
            mov = None
        
        return root
