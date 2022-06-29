class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        ls = len(s)
        if lp > ls:
            return []
        r = []
        cnt_p = Counter(p)
        cnt_s = Counter(s[0:lp])
        l_cnt_p = sorted(cnt_p.items())
        ll = len(l_cnt_p)
        for i in range(0, ls - lp + 1):
            if i == 25 or i == 26:
                print(cnt_s.most_common(lp))
            if cnt_s == cnt_p or l_cnt_p == sorted(cnt_s.most_common(ll)):
                r.append(i)
            cnt_s[s[i]] -= 1
            
            if i + lp < ls:
                cnt_s[s[i+lp]] += 1
            else:
                return r
        return r  
