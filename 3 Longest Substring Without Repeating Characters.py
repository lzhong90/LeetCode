Solution 1:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = []
        j = 0
        max = 0
        if len(s) is 0:
            return 0
        for i in range(len(s)):
            if s[i] not in r:
                j += 1
                r.append(s[i])
            else:
                r =r[r.index(s[i]) + 1 :]
                r.append(s[i])
                j = len(r)
            if j > max:
                max = j

        return max
    
    #################################
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ll = len(s)
        if len(s) <= 1:return len(s)
        
        right = 0
        left = 0
        cnt = 0
        
        while right < ll:
            if s[right] not in dic:
                dic[s[right]] = right
                cnt = max(cnt, right-left+1)
            else:
                left = max(left, dic[s[right]]+1)

                cnt = max(cnt, right-left+1)
                dic[s[right]] = right
            right += 1
        return cnt
    
    ####################################
    
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        if len(s) ==1:return 1
        cnt = 0
        mx = 0
        for i, e in enumerate(s):
            if e not in dic:
                dic[e]= i
                cnt +=1
            else:
                cnt+= 1
                cnt = min(cnt, i-dic[e])                
                dic[e] = i
            mx = max(cnt, mx)
        return mx
