class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s
        
        stck = []
        
        
        for i in s:
            tmp = []
            cnt = ''
            if i != ']':
                stck.append(i)
            else:
                #x = stck.pop()
                while len(stck) > 0:
                    x = stck.pop()
                    if x != '[':
                        tmp.append(x)
                    else:
                        tmp = tmp[::-1]
                        while len(stck) >0:
                            if stck[-1] <= '9' and stck[-1] >= '0':
                                cnt = stck.pop()+cnt
                            else:
                                break
                        #cnt = cnt[::-1]    
                        tmp = tmp*int(cnt)
                        stck.extend(tmp)
                        break
        return ''.join(stck)
