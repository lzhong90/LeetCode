class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stck = []
        for i in s:
            if len(stck) == 0:
                stck.append(i)
                continue
            if i == stck[-1]:
                stck.pop()
            else:
                stck.append(i)
                
        return ''.join(stck)
