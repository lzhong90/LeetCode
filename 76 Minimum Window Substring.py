class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        
        if ls == 0 or ls < lt:
            return ''
        if lt == 0:
            return ''
        
        cnt_t = collections.Counter(t)
        window = {}
        
        right = 0
        left  = 0
        
        mn = float('inf')
        res = ''
        
        
        while right < ls:
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            
            if all(key in window for key in cnt_t.keys()):
                while all(window[key] >= cnt_t[key] for key in cnt_t.keys()):                
                    if mn > right -left:
                        mn = right-left
                        res = s[left:right+1]
                    
                    window[s[left]] -= 1
                    left += 1
            
            right += 1
        
        return res
