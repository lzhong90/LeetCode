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
