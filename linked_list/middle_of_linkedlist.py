class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def middle_linkedlist(head):
    
    
    if head==None:
        return
    
    
    count=0
    curr=head
    
    while curr:
        count+=1
        
        curr=curr.next
        
    curr=head   
    for i in range(count//2):
        curr=curr.next
        
    print(curr.key)
    
    
   
    


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

head=middle_linkedlist(head)






