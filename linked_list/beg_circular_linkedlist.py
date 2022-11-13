class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def circular(head,x):
    temp = Node(x)
    curr=head
    temp.next=curr.next
    
    head.next=temp
    
    head.data,temp.data=temp.data,head.data
    
    return head
    
    




def printCircular(head):
    if head == None:
        return
    print(head.data, end="->")
    curr = head.next
    while curr != head:
        print(curr.data, end="->")
        curr = curr.next

    print("None") 


    
    
    
    
    
    

   
    





head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


printCircular(head)   


head=circular(head,25)   

printCircular(head)   


