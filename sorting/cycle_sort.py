# this sort is useful when the the array in the range [1,n]

#this sorting is useful for finding the duplicates etc .


def cyclesort(arr,k):
    
    i=1
    while i<len(arr):
        correct=arr[i]-1
        
        
        if arr[i]!=arr[correct]:
            
            arr[i],arr[correct]=arr[correct],arr[i]
            
        else:
            i+=1
            
            
arr=[2,1,4,3]

k=4
cyclesort(arr,k)

print(*arr)
            