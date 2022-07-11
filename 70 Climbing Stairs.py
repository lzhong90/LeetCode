class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        a = [0]*n
        a[0] = 1
        a[1] = 2
        
        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]
        
        return a[n-1]
