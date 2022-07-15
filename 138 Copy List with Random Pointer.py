"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        dic = {}
        
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
            
        return dic[head]
       
 ###############################################################################
 
 """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val)
            cur = cur.next
            cur.next = nxt
            cur = cur.next
        
        cur = head
        
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = cur.random
            cur = cur.next.next
            
            
        cur = head.next
        second = cur
        
        while cur and head:
            head.next = cur.next
            head = head.next
            if head:
                cur.next = head.next
                cur = cur.next
        
        return second
