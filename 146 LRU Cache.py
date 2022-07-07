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
