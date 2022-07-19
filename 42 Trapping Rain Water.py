class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        length = len(height)
        
        if length <= 1:
            return 0
        
        l = 0
        r = length-1
        
        lmax = height[l]
        rmax = height[r]
        
        res = 0
        while l <= r:
            if lmax < rmax:
                lmax = max(height[l], lmax)
                res += lmax-height[l]
                l+=1
            else:
                rmax = max(height[r], rmax)
                res += rmax-height[r]
                r-=1
        return res
