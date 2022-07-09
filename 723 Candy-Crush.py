# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def candyCrush(arr):
    m = len(arr)
    n = len(arr[0])
    
    flag = True
    
    while flag:
        flag = False
        # check candies
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0: continue
                if i+1 < m and i+2 < m:
                    if abs(arr[i][j])== abs(arr[i+1][j]) and abs(arr[i][j])==abs(arr[i+2][j]):
                        flag = True
                        v = abs(arr[i][j])
                        arr[i][j] = -v
                        arr[i+1][j] = -v
                        arr[i+2][j] = -v
                if j+1 < n and j+2 < n:
                    #print(j+2)
                    if abs(arr[i][j])== abs(arr[i][j+1]) and abs(arr[i][j+2])==abs(arr[i][j]):
                        flag = True
                        v = abs(arr[i][j])
                        arr[i][j] = -v
                        arr[i][j+1] = -v
                        arr[i][j+2] = -v
        #print(arr)
        
        
        # crush candies
        if flag:
            for j in range(n):
                idx = m-1
                for i in range(m-1,-1,-1):
                    if arr[i][j]>0:
                        arr[idx][j] = arr[i][j]
                        idx -= 1
                for x in range(idx,-1,-1):
                    arr[x][j] = 0
            print(arr)
        
        
    return arr
            

                    
    
array = [[1,2,1,0],[1,3,3,3],[1,3,2,0],[2,3,2,3],[1,2,2,3],[3,2,1,3]]

print(candyCrush(array))
