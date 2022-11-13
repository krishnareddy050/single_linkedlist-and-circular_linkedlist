class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def remove_duplicates(head):
    
    
    curr=head
    
    while curr!=None and curr.next!=None:
        
        if curr.key==curr.next.key:
            
            curr.next=curr.next.next
            
            
        else:
            curr=curr.next
            
            
            
    return head
    
    
    
    
    
    
   
    


def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end="->")
        curr = curr.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(40)
head.next.next.next.next = Node(40)



printList(head)

head=remove_duplicates(head)

print("After sorted the linked list is: ")

printList(head)