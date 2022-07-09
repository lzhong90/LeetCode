#This is one of those magics of remainder theorem :)

#(a+(n*x))%x is same as (a%x)

#For e.g. in case of the array [23,2,6,4,7] the running sum is [23,25,31,35,42] and the remainders are [5,1,1,5,0]. We got remainder 5 at index 0 and at index 3. That means, in between these two indexes we must have added a number which is multiple of the k



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = len(nums)
        if m <= 1:
            return False
        sum_list = [0]*m
        dic = {}

        for i in range(0, m):
            if i == 0:
                sum_list[i] = nums[i]
            else:
                sum_list[i] = sum_list[i-1]+nums[i]
            if k != 0:
                xs = sum_list[i]%k

                if i != 0 and (sum_list[i] == 0 or xs == 0): return True
                if xs in dic and i-dic[xs]>1:
                    return True
                if xs not in dic:
                    dic[xs] = i
            print(dic)
        if k == 0:
            sum_set = set(sum_list)
            if len(sum_set) != len(sum_list):
                return True
