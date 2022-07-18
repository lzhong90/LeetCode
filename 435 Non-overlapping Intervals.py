########################
# Sort with begin number

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) == 1:
            return 0
        intervals.sort()
        cur = intervals[0][1]
        cnt = 0
        
        for i in range(1, len(intervals)):
            if cur > intervals[i][0]:
                cur = min(intervals[i][1], cur)
                cnt += 1
            else:
                cur = intervals[i][1]
        return cnt
     
    
    
    ##########################
    # Sort with end number
    
    class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) == 1:
            return 0
        intervals.sort(key = lambda x: x[1])
        cur = intervals[0][1]
        cnt = 0
        
        for i in range(1, len(intervals)):
            if cur > intervals[i][0]:
                #cur = min(intervals[i][1], cur)
                cnt += 1
            else:
                cur = intervals[i][1]
        return cnt
        
