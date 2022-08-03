class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500, 'M':1000}
        
        if not s:
            return None
        
        l = len(s)
        res = 0
        
        for i in range(l-1):
            if dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        res += dic[s[l-1]]
        return res
