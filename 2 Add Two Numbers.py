# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode((l1.val + l2.val)%10)
        head = res

        
        c = (l1.val + l2.val)//10
        
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next
            x = l1.val+l2.val+c

            c= x//10
            
            res.next = ListNode(x%10)
            res = res.next
            print(res.val)
            
        
        
        while l1.next != None:
            l1 = l1.next
            x = l1.val+c
  
            c= x//10
            res.next = ListNode(x%10)
            res = res.next
            
        
        while l2.next != None:
            l2 = l2.next
            x = l2.val+c
       
            c= x//10
            res.next = ListNode(x%10)
            res = res.next
            
        
        if c >0:
            res.next = ListNode(c)

            
        return head
