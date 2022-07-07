def subs(strs):
    stck = []
    cnt = []
    i = 0
    for i in range(len(strs)): 
        if len(stck) == 0:
            stck.append(strs[i])
            cnt.append(1)
            continue
        else:
            if strs[i] == stck[-1]:
                cnt[-1] += 1
            else:
                if cnt[-1] > 2:
                    stck.pop()
                    cnt.pop()
                    if len(stck) > 0 and strs[i] == stck[-1]:
                        cnt[-1] += 1
                        continue
                stck.append(strs[i])
                cnt.append(1)

    s = ''
    for i in range(len(stck)):
        if cnt[i] <3:
            s = s+stck[i]*cnt[i]
            
    return s
a = "aabbccddeeedcba"
b= "aabbbacd"
c= 'aaaaaaaaaaaaa'
d= "aaabbbacd"
e = 'ABCCCBB'
print(subs(e))
