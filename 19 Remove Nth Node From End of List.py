# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x = head
        
        depth = 0
        while x != None:
            depth +=1
            x = x.next
        
        if n > depth:
            return head
        if n == 0:
            return head
        if depth == 1 and n== 1:
            return None
        if n == depth:
            head = head.next
            return head
            
        
        x = head
        for i in range(n):
            x= x.next
        y = head    
        while x!= None and x.next != None:
            y = y.next
            x= x.next
        
        y.next = y.next.next
        
        return head
