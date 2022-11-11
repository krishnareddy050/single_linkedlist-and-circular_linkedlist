
class Node:
    

    def __init__(self,key):
        self.data=key
        self.next=None
    
    
def search(head,ele):
    size=1
    curr=head
    if head==None:
        return -1
    while curr!=None:
        
        if curr.data==ele:
            return size
        
        size+=1
        
        curr=curr.next
        
    return -1
        
           
        
        
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)


print(search(head,5))