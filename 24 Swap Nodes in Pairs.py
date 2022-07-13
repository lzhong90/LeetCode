# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        x = head
        if x== None:
            return x
        
        if x.next != None:
            tmp = x.next
            x.next = tmp.next
            tmp.next = x
            head = tmp
        
        while x.next != None and x.next.next != None:
            
            tmp= x.next
 
            x.next = tmp.next
 
            tmp.next = x.next.next
            x.next.next = tmp
            x= tmp

  
        return head
