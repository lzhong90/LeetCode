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
        head = l3 = ListNode(0)       
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l3.val = carry % 10 
            carry = carry//10
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return head

    
#TODO: what if the linked numbers are not in reversed order?  

#Solution:

class Solution(object):
    def addTwoNumbers(self, l1, l2):
