class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def delete_last_node(head):
    
    if head==None:                      #this corner cases will handle if head is none or it contains only one node
        return None

    if head.next==None:
        return None
    
    curr=head
    while curr.next.next!=None:
        curr=curr.next
        
    curr.next=None
    
    
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

head = delete_last_node(head)

printList(head)