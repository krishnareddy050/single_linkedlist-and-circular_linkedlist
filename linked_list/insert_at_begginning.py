class Node:
    

    def __init__(self,k):
        self.key=k
        self.next=None
        
        
        
def insert_at_beg(head,x):
    
    
    if head==None:
        return x
    
    
    temp=Node(x)
    temp.next=head
    
    return temp
    
    
    
def printList(head):
    curr=head
    while curr!=None:
        print(curr.key,end="->")
        
        curr=curr.next
        
    print("None")
        
        
        
        
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

head=insert_at_beg(head,5)


printList(head)



