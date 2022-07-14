class Solution:
    def firstUniqChar(self, s: str) -> int:
        ll = len(s)
        if ll < 1: return None
        if ll == 1: return 0
        dic = {}
        dic2 = OrderedDict()
        
        for i in range(ll):
            if s[i] not in dic:
                dic[s[i]] = i
                dic2[s[i]] = i
            else:
                #print(res)
                if dic[s[i]] in dic2:
                    dic2.pop(dic[s[i]])
        
        if len(dic2)>0:
            return dic2.popitem(last= False)[1]
        else:
            return -1
      
 ####################################################
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ll = len(s)
        if ll < 1: return None
        if ll == 1: return 0
        
        cnt = Counter(s)
        
        for i, chr in enumerate(s):
          if cnt[chr] == 1:
            return i
        return -1
      
      
