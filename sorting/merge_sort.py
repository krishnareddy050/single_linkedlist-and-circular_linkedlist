


def mergesort(arr,l,mid,r):
    left=arr[l:mid+1]
    right=arr[mid+1:r+1]
    
    i=0
    j=0
    
    k=l
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            
            k+=1
            
            
        else:
            arr[k]=right[j]
            j+=1
            k+=1
            
            
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
        
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
        
        
    








def merge(arr,l,r):
    if l<r:
        mid=(l+r)//2
        merge(arr,l,mid)                           #this function first divide left ,divide right and mergeleft  mergeright
        
        merge(arr,mid+1,r)
        
        mergesort(arr,l,mid,r)
        
        
arr=[10, 5, 30, 15, 7]      
merge(arr,0,4)

print(*arr)