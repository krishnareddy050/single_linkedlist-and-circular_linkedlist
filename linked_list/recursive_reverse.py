class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def recursive(head):
    
    if head==None:
        return head
    
    if head.next==None:
        return head
    
    rest_head=recursive(head.next)
    res_tail=head.next
    
    res_tail.next=head
    head.next=None
    
    return rest_head
    


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

head =recursive(head)      

printList(head)