class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insert_node(head,x):
    
    temp=Node(x)
    
    if head==None:
        return temp
    
    if head.next==None:
        temp.next=head
        
    return temp
    
    
            
    curr=head
        
    while  curr.next!=None and curr.next.key<x:     
        curr=curr.next
        
    temp.next=curr.next
    curr.next=temp
    return head
    


def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end="->")
        curr = curr.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)



printList(head)

head =insert_node(head,35)      

printList(head)