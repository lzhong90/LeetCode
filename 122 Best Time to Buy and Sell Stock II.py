class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        
        if l <= 1:
            return 0
        s = 0
        for i in range(1,l):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                s+= tmp
        
        return s
######################################



