class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        
        if l == 0 or s[0] == '0':
            return 0
        if l == 1:
            return 1
        
        arr = [0]*l
        
        arr[0] = 1
        if s[1] == '0':
            if int(s[0]) >= 3: 
                return 0
            else:
                arr[1] = 1
        else:
            if int(s[0:2]) > 26:
                arr[1] = 1
            else:
                arr[1] = 2
    
        
        for i in range(2, l):
            if s[i] == '0':
                if int(s[i-1:i+1]) > 0 and int(s[i-1:i+1]) < 26:
                    arr[i] = arr[i-2]
                else: 
                    return 0
            else:
                if s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                    arr[i] = arr[i-1]
                else:
                    arr[i] = arr[i-1] + arr[i-2]
        
        return arr[l-1]
