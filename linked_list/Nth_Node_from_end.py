class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def nth_node_fromend(head,n):
    
    if head==None:
        return 
    first=head
    
    for i in range(n):
        if first==None:
            return
        
        first=first.next
        
        
    second=head
    
    while first!=None:
        first=first.next
        
        second=second.next
        
        
    print(second.key)
    
    
    
    
   
    


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
head.next.next.next.next = Node(50)



printList(head)

head=nth_node_fromend(head,4)