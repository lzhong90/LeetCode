# Method 1:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return 0
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
       
# Method 2:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i]) + i + 1]
                  
# Method 3:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
          if nums[i] in hashmap:
            return [i, hashmap[nums[i]]]
          hashmap[target-nums[i]] = i
