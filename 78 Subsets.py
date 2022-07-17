# cascading method
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for i in nums:
            for x in output:
                output = output + [x + [i]]
        
        return output
 
# bit manipulation

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nth_bit = 1<<n
        #print(bin(nth_bit))
        output = []
        for i in range(2**n):
            bitmask = bin(i | nth_bit)[3:]
            output.append([nums[j] for  j in range(n) if bitmask[j] == '1'])
        return output
