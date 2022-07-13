class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ln = len(nums)
        
        if ln < 3:
            return []
        
        nums.sort()
        #print(nums)
        
        
        left = 0
        right = ln-1
        res = []
        
        for i in range(ln-2):
            left = i+1
            right = ln-1
            
            x= -nums[i]
            
            if i >= 1 and nums[i-1]==nums[i]:
                continue
          
            
            while left < right:
                
                s = nums[right] +nums[left]
                if s == x:
                    #if 
                    res.append([nums[i],nums[right],nums[left]])
                    left = left+1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right = right-1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                    
                if nums[right] +nums[left] < x:
                    left += 1
                elif nums[right] +nums[left] > x:
                    right -= 1
                

        return res
