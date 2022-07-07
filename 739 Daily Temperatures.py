####Brute force#######

class Solution(object):
    def dailyTemperatures(self, input):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(input)
    
        if l == 1:
            return [0]
        if l == 0:
            return None
    
        out = [0]*l
    
        for i in range(l-1):
            j = i+1
            while j < l:
                if input[j] > input[i]:
                    out[i] = j-i
                    break
                else:
                    j += 1
        return out
      
      
######################

class Solution(object):
    def dailyTemperatures(self, input):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(input)
    
        if l == 1:
            return [0]
        if l == 0:
            return None
    
        out = [0]*l
        x = [input[0]]

        stck = [input[0]]
        idx = [0]        
        
        for i in range(1, len(input)):
            if input[i] > x[-1]:
 
                while len(x) != 0:
                    if input[i] > x[-1]:
                        out[idx[-1]] = i-idx[-1]
                        x.pop()
                        idx.pop()
                    else:
                        break

            x.append(input[i])
            idx.append(i)
           
          
###############################################################


class Solution(object):
    def dailyTemperatures(self, input):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(input)
    
        if l == 1:
            return [0]
        if l == 0:
            return None
    
        out = [0]*l
        mx = input[-1]
        
        for j in range(l-2,-1,-1):
            v = j + 1
            
            if input[j] > mx:
                continue
            while v < l:
                if input[v] <= input[j]:
                    if out[v] == 0:
                        break
                    if v == l-1:
                        break
                    else:
                        v=v+out[v]
                else:
                    out[j] = v-j
                    break 
