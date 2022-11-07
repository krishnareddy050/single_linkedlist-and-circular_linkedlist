def selection(l):
    n=len(l)
    for i in range(n-1):
        min_indx=i
        for j in range(i+1,n):
            if l[j]<l[min_indx]:
                min_indx=j
        l[min_indx],l[i]=l[i],l[min_indx]   


l=[5,4,3,10,9]
selection(l)
print("Sorted array is:")
for i in range(len(l)):
    print("% d" % l[i], end=" ")