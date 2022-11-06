def  bubble(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        

l=[5,6,8,2,4,3]
bubble(l)
print("Sorted array is:")
for i in range(len(l)):
    print("% d" % l[i], end=",")