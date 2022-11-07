def mergesort(arr,l,mid,r):
    left=arr[l:mid+1]
    right=arr[mid+1:r+1]
    
    i=0
    j=0
    res=0
    
    k=l
    
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            
            
            i+=1
            
            k+=1
            
            
            
        else:
            arr[k]=right[j]
            j+=1
            k+=1
            res+=(len(left)-i)
            
            
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
        
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
        
        
    return res
        
        
    








def merge(arr,l,r):
    res=0
    if l<r:
        
        mid=(l+r)//2
        res+=merge(arr,l,mid)                           #this function first divide left ,divide right and mergeleft  mergeright
        
        res+=merge(arr,mid+1,r)
        
        res+=mergesort(arr,l,mid,r)
        
    return res
        
        
arr=[1, 20, 6, 4, 5]    
print(merge(arr,0,4))

