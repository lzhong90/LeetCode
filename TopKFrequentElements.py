class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [word for word, word_count in Counter(nums).most_common(k)]
    
    ###Method 2###
       dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        return sorted(dic, key = dic.get, reverse = True)[:k]
