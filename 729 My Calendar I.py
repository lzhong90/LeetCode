### Solution: BST
#Time Complexity (Python): O(N2)O(N^2)O(N2) worst case, with O(Nlog⁡N)O(N \log N)O(NlogN) on random data. 
#For each new event, we insert the event into our binary tree. As this tree may not be balanced, it may take a linear number of steps to add each event.

class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    def insert(self, node):
        
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        return False
            

class MyCalendar(object):

    def __init__(self):
        self.root = None
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
      
      
    ####Brute Force 
    O(n^2)
            
