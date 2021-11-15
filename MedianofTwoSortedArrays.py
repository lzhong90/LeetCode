#Initial Method:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        s = []
        if m is 0:
            if n is 0:
                return Null
            else:
                if n % 2 is 0:
                    return (nums2[n//2 - 1] + nums2[n//2])/2.0
                else:
                    return nums2[n//2]
                
        else:
            if n is 0:
                if m % 2 is 0:
                    return (nums1[m//2 -1] + nums1[m//2])/2.0
                else:
                    return nums1[m//2]
            else:
                #print(sum(nums1) + sum(nums2))
                #print(len(nums1) + len(nums2))
                l = m+n
                x = 0
                y = 0
                t = 0
                while x+y <= l//2:
                    if x > m-1:
                        t = nums2[y]
                        y +=1
                        s.append(t)
                        continue
                    if y > n-1:
                        t = nums1[x]
                        x += 1
                        s.append(t)
                        continue
                    if nums1[x] < nums2[y]:
                        if x <= m-1:
                            t = nums1[x]
                            x += 1
                        else:
                            t = nums2[y]
                            y += 1
                    else:
                        if y <= n-1:
                            t = nums2[y]
                            y += 1
                        else:
                            t = nums1[x]
                            x += 1
                    print(t)
                    s.append(t)   
                
                if l%2 is 1:
                    return t
                else:
                    return (s[-1] + s[-2])/2.0
                        
