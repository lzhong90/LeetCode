class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            raise ValueError('ss')
        if l == 1:
            return True
        mx = nums[0]
        
        for i in range(1,l):
            if i > mx:
                return False
            mx = max(nums[i]+i,mx)
            
        if mx >= l-1:
            return True
        else:
            return False
