class Node:
    

    def __init__(self,k):
        self.key=k
        self.next=None
        
        
        
def insert_at_end(head,x):
    
    if head==None:
        return x
    
    curr=head
    
    temp=Node(x)
    while curr.next!=None:
        
        curr=curr.next
        
    curr.next=temp   
        
    return head
        
        
           
    
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

head=insert_at_end(head,50)


printList(head)