#### TLE Method#####

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        if l == 0:
            return None
        if l == 1:
            return nums[0]
        
        mx = float('-inf')
        
        arr = [[0 for i in range(l)] for i in range(l)]
        arr[0][0] = nums[0]
        
 
        for i in range(l):
            for j in range(i,l):
                arr[i][j] = arr[i][j-1] + nums[j]
                mx = max(arr[i][j], mx)
        return mx
   
 #######DP Method############

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        
        if l == 0:
            return None
        if l == 1:
            return nums[0]
        
        arr = [0]*l
        
        arr[0] = nums[0]
        
        mx = arr[0]
        
        for i in range(1, l):
            if arr[i-1] > 0:
                arr[i] = arr[i-1] + nums[i]
            else:
                arr[i] = nums[i]
            mx = max(mx, arr[i])
        
        return mx
