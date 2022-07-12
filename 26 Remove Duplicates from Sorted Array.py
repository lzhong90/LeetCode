class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        if l < 1:
            return None
        if l == 1:
            return 
        
        idx = 1
        
        a = nums[0]
        
        for i in range(1, l):
            if nums[i] != a:
                nums[idx] = nums[i]
                idx += 1
                a = nums[i]
 
        while idx < l:
            nums.pop()
            idx += 1
