class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        x = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[x] = nums[i]
                x+=1
        while x <len(nums):
            nums[x]= 0
            x+= 1
        
        return nums
