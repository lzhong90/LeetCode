class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while b!= 0:
            c = (a&b)&x
            a = (a^b)&x
            b = c<<1
        print(bin(a))
        print(bin(b))        
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^x)    
        
        return a
        
 # Explanation: https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python
