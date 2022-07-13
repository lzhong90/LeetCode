# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = self.reverse(l1)

        ll2 = self.reverse(l2)
        
        return self.reverse(self.addTwo(ll1,ll2))

    
    def reverse(self, l):
        if l.next == None:
            return l
        else: 
            c= l.next
        tmp = l
        tmp.next = None
        l= c
        c= l.next
        l.next = tmp
        
        while c != None:
            tmp = l
            l= c
            c = l.next
            l.next = tmp
        return l

    
    
    def addTwo(self, l1, l2):
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
      
      
########################################################
#Method without Reverse


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = self.countDepth(l1)
        len2 = self.countDepth(l2)
        
        l1 = self.zeroInterpolation(l1, len2-len1)
        l2 = self.zeroInterpolation(l2, len1-len2)
        #return l2
        
        c, ans = self.addList(l1,l2)
        
        if c > 0:
            tmp = ListNode(c)
            tmp.next = ans
            ans = tmp
        return ans
        
    def countDepth(self, l):
        cnt = 0
        while l != None:
            cnt+= 1
            l= l.next
        return cnt
    
    def zeroInterpolation(self, l, n):
        if n <= 0:
            return l
        for i in range(n):
            tmp = ListNode(0)
            tmp.next = l
            l= tmp
        return l
    
    def addList(self, l1, l2):
        if(not l1 and not l2):
            return 0, None
        
        c, ans = self.addList(l1.next, l2.next)
        
        x = l1.val + l2.val + c
        tmp = ListNode(x%10)
        c= x//10
        tmp.next = ans
        ans = tmp
        
        return c, ans
