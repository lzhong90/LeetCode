class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return 0
        cnt = {'a':0, 'b':0, 'c':0}
        res = 0
        x = 0
        j = 0
        for i in range(len(s)):
            cnt[s[i]] += 1

            while all(cnt.values()):
                x += 1
                cnt[s[j]] -= 1
                j += 1
            res += x
        return res
