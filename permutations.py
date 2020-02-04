def swap(a,i):
    if(i==0):
        return a
    x = a[i] + a[1:i] + a[0] + a[i+1:]
    return x
    
def permu(a1):
    ans = []
    if(len(a1)==2):
        x = []
        b = a1[1] + a1[0]
        x.append(b)
        return x
    else:
        for i in range(len(a1)):
            a = swap(a1,i)
            x = a[:1-len(a1)]
            y = a[1-len(a1):]
            b = x + y
            ans.append(b)
            y = permu(y)
            for j in y:
                b = x + j
                if b not in ans:
                    ans.append(b)
            
        return ans
        
a = permu("abcdef")
print(a)
print(len(a))
        

