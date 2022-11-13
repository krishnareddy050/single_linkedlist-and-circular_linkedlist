class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def reverse_linkedlist(head):
    
    
    curr=head
    prev=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        
        prev=curr
        curr=next
        
        
    return prev
    

    
    
    
    
    
    
   
    


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

head=reverse_linkedlist(head)

print("After reversing  the linkedlist the new linkedlist is  : ")

printList(head)