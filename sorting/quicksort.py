
#lomuto partition will puts the pivot element into correct position and  returns it index

def partition(arr,l,r):    
    pivot=arr[r]
    
    i=l-1
    
    for j in range(l,r):
        
        if arr[j]<=pivot:
            i=i+1
            
            arr[j],arr[i]=arr[i],arr[j]
            
            
    arr[i+1],arr[r]=arr[r],arr[i+1]
        
        
    return i+1
            










def quicksort(arr,l,r):
    if l<r:
        p=partition(arr,l,r)
        
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)
        
        
        
arr = [8, 4, 7, 9, 3, 10, 5]


l=0
r=6
quicksort(arr,l,r)
print(*arr)