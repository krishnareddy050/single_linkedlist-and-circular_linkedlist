def merge(a,b):
    i=0
    j=0
    m=len(a)
    n=len(b)
    res=[]

    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1

        else:
            res.append(b[j])
            j+=1
    while i<m :
        res.append(a[i])
        i=i+1
    while j<n:
        res.append(b[j])
        j=j+1
    return res
    
b=[2,5]
a=[6,8,9]
merge(a,b)
 
print(merge(a,b))
