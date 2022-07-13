class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        
        if l1 > l2:
            return False
        
        if l2 < 1 and l1 <1:
            return True
        
        cnt = collections.Counter(s1)
        
        for i in range(0, l1):
            if s2[i] in cnt:
                cnt[s2[i]] -= 1
            
        
        for i in range(l2):
            if all(value == 0 for value in cnt.values()):
                return True
            
            if s2[i] in cnt:
                cnt[s2[i]] += 1
            if i+l1 < l2:
                if s2[i+l1] in cnt:
                    cnt[s2[i+l1]] -= 1
            else:
                return False
