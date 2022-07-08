class LFUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.len = capacity
        self.cache = OrderedDict(list())
        self.feq = OrderedDict(OrderedDict(list()))
        self.min_freq = float('inf')        
        

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        freq = self.cache[key][-1]
        self.feq[freq].pop(key)
        
        if len(self.feq[freq]) == 0:
                self.feq.pop(freq)
                if self.min_freq == freq:
                    self.min_freq += 1
        
        self.cache[key][-1] = freq+1
        if freq+1 not in self.feq:
            self.feq[freq+1] = OrderedDict({key:self.cache[key]})
        else:
            self.feq[freq+1][key] = self.cache[key]
        
        self.min_freq = min(self.min_freq, freq+1)
        return self.cache[key][-2]        

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.len == 0:
            return
        if key in self.cache:
            self.cache[key][-2] = value
            freq = self.cache[key][-1]
            self.cache[key][-1] = freq+1
            self.feq[freq].pop(key)
            #self.min_freq = min(self.min_freq, freq+1)
            
            if len(self.feq[freq]) == 0:
                self.feq.pop(freq)
                if self.min_freq == freq:
                    self.min_freq += 1
                    
            if freq+1 in self.feq:
                tmp = self.feq.pop(freq+1)
                tmp[key] = self.cache[key]
                self.feq[freq+1]=tmp
            else:
                self.feq[freq+1]=OrderedDict({key:self.cache[key]})
                #print(type(self.feq[freq+1]))
            return
        
        if len(self.cache) < self.len:
            self.cache[key] = [value, 1]
            #print(self.feq[1])
            if 1 not in self.feq:
                self.feq[1] = OrderedDict({key:[value,1]})
            else:
                self.feq[1][key] = [value, 1]
            
        else:
            print(type(self.feq[self.min_freq]))
            rm_key = self.feq[self.min_freq].popitem(last=False)[0]
            self.cache.pop(rm_key)
            self.cache[key] = [value,1]
            if 1 not in self.feq:
                self.feq[1] = OrderedDict({key:[value,1]})
            else:
                self.feq[1][key] = [value, 1]
        self.min_freq = 1
        return  
