class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums)/k
        mx = sum(nums[0:k])
        su = mx
        for i in range(1, len(nums)-k+1):
            su = su+nums[i+k-1]-nums[i-1]
            mx = max(su,mx)
        return mx/k
