Solution 1: Iterative Method

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            tmp = head
            head = head.next
            tmp.next = prev
            prev = tmp
        return prev

 Solution 2: Recursive Method
 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head  or not head.next:
            return head
        else:
            reverse= self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return reverse 
