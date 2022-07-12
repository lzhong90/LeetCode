class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lg = len(height)
        if lg < 2:
            return 0
        l = 0
        r = lg-1
        sx = 0
        while l<r:
            sx = max(min(height[r], height[l])*(r-l), sx)
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        
        return sx
