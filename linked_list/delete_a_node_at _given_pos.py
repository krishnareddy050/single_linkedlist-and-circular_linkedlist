class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def delete_node(head,x):
    
    if head==None:
        return None
    
    if head.next==None:
        return None
    
    curr=head
    while  curr.next.key!=x:     
        curr=curr.next
        
    curr.next=curr.next.next
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
head.next.next.next.next = Node(25)


printList(head)

head =delete_node(head,25)      

printList(head)