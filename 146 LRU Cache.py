class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.len = capacity
        self.dic = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        
        v = self.dic.pop(key)
        self.dic[key] = v
        return v


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        
        if key not in self.dic:
            if len(self.dic) < self.len:
                self.dic[key]= value
                return
            self.dic.popitem(last =False)
            self.dic[key]= value
            return
        
        
        self.dic.pop(key)
        self.dic[key] = value
        return
    
    
  #############################################################
class DLinkedNode:
    def __init__(self, key = 0, value= 0):
        self.pre = None
        self.next = None
        self.key = key
        self.value = value
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.len = capacity
        self.size = 0
        self.dic = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        
        v = self.dic[key].value
        self.move_to_head(self.dic[key])
        return v


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if key in self.dic:
            self.dic[key].value = value
            self.move_to_head(self.dic[key])
 
            return
        if self.size < self.len:
            node = DLinkedNode(key,value)
            self.dic[key]=node
            self.add_to_head(node)
            self.size += 1
            return
        self.dic.pop(self.remove_tail().key)
        node = DLinkedNode(key, value)
        self.dic[key]=node
        self.add_to_head(node)
        #print(self.dic)
        return
        
        
    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
 
        
    def move_to_head(self,node):
        self.remove_node(node)
        self.add_to_head(node)
        
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
